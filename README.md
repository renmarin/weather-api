# weather-api
Flask based Weather REST API

# Prerequisites
Встановити все з файлу requirements.txt виконавши команду:
`pip install -r requirements.txt`

# Як запустити та використовувати
0. До застосунку вже надано базу даних sqlite, та можливо наповнитит її даними самостійно на наступні 7 днів, використовуючи дані з сайту openweathermap.org. Для цього потрібно виконати команду `python populate_db.py`. Дана команда виконає ряд запитів до API openweathermap.org та з отриманих даних наповнить базу даних sqlite: **weather_seven_days**.
  Структура бази даних:
    - таблиція cities (id, cities)
    - таблиція data_for_7_days (id, name (ForeignKey - cities.name), date, tmp, pcp, clouds, pressure, humidity, wind_speed)
  
1. Запустити застосунок за допомогою команди `python app.py` в директорії проекту.
2. Підєднатись до api використовуючи одну з кінецівих точок:

  ```
  https://127.0.0.1/cities                                
  https://127.0.0.1/mean?value_type={}&city={}            
  https://127.0.0.1/records?city={}&start_dt={optional}&end_dt={optional} 
  https://127.0.0.1/moving_mean?value_type={}&city={}&wsize={optional}
  ```

  - /cities   - повертає список міст в базі даних в форматі json
  - /mean - повертає середнє значення вибраного параметру для вибраного міста в форматі json
      - value type    - одне з [temp, pcp, clouds, pressure, humidity, wind_speed]
      - city          - назва міста [Kyiv, Uzhhorod, Kharkiv, Odesa, Chernihiv]
  - /records - повертає значення всіх параметрів для вибраного міста впродовж вибраного терміну в форматі json
      - city          - назва міста [Kyiv, Uzhhorod, Kharkiv, Odesa, Chernihiv]
      - start_dt      - початкова дата для вибірки
      - end_dt        - кінцева дата для вибірки
  - /moving - повертає значення вибраного параметру перераховане за алгоритмом ковзного середнього (moving average) для вибраного міста для всіх дат в форматі json
      - value type    - одне з [temp, pcp, clouds, pressure, humidity, wind_speed]
      - city          - назва міста [Kyiv, Uzhhorod, Kharkiv, Odesa, Chernihiv]
      - wsize         - кількість періодів розрахунку (за замовчуванням = 3)
