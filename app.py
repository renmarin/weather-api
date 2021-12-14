from flask import Flask
from flask_restful import Resource, Api, request

from database import db_session
from models import Cities, CitiesSevenDays

from statistics import mean
import pandas


app = Flask(__name__)
api = Api(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.remove()


class CitiesView(Resource):
    def get(self):
        cities = Cities.query.all()
        return [Cities.serialize(city) for city in cities]


class Mean(Resource):
    """
    :return: середнє значення вибраного параметру для вибраного міста в форматі json
    
    :param city: назва міста
    :param value_type: одне з [temp, pcp, clouds, pressure, humidity, wind_speed]
    """
    def get(self):
        args = request.args
        city = args.get("city")
        value_type = args.get("value_type")
        datas = CitiesSevenDays.query.filter(CitiesSevenDays.name == city).all()
        serialize = [CitiesSevenDays.serialize(data) for data in datas]
        result = mean(day[value_type] for day in serialize)
        return {f"Mean of {value_type} for {city}": result}


class Records(Resource):
    """
    :return: значення всіх параметрів для вибраного	міста впродовж вибраного терміну в форматі json

    :param city: назва міста
    :param start_dt: початкова дата
    :param end_dt: кінцева дата
    """
    def get(self):
        args = request.args
        city = args.get("city")
        start_dt = args.get("start_dt", CitiesSevenDays.query.first().date)
        end_dt = args.get("end_dt", CitiesSevenDays.query.order_by(CitiesSevenDays.id.desc()).first().date)
        datas = CitiesSevenDays.query.filter(
            CitiesSevenDays.name == city,
            CitiesSevenDays.date >= start_dt,
            CitiesSevenDays.date <= end_dt,
        ).all()
        serialize = [CitiesSevenDays.serialize(data) for data in datas]
        return serialize


class MovingMean(Resource):
    """
    :return: значення вибраного параметру перераховане за алгоритмом ковзного середнього
             (moving average) для вибраного міста для всіх дат в форматі json

    :param city: назва міста
    :param value_type: одне з [temp, pcp, clouds, pressure, humidity, wind_speed]
    """
    def get(self):
        args = request.args
        city = args.get("city")
        value_type = args.get("value_type")
        wsize = int(args.get('wsize', 3))
        datas = CitiesSevenDays.query.filter(CitiesSevenDays.name == city).all()
        serialize = [CitiesSevenDays.serialize(data) for data in datas]

        values = [day[value_type] for day in serialize]
        window_size = wsize
        numbers_series = pandas.Series(values)
        windows = numbers_series.rolling(window_size)
        moving_averages = windows.mean()
        moving_averages_list = moving_averages.tolist()
        without_nans = moving_averages_list[window_size - 1:]

        return {f"Moving average of {value_type} for {city}": without_nans}


api.add_resource(CitiesView, '/cities')
api.add_resource(Mean, '/mean')
api.add_resource(Records, '/records')
api.add_resource(MovingMean, '/moving_mean')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
