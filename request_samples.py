import os

command = f"curl -H 'Content-Type:application/json' -X GET 'http://0.0.0.0:8000/cities'"
os.system(f"echo ===================================================")
os.system(f"echo http://0.0.0.0:8000/cities")
os.system(command)

command = f"curl -H 'Content-Type:application/json' -X GET 'http://0.0.0.0:8000/mean?value_type=clouds&city=Kyiv'"
os.system(f"echo ===================================================")
os.system(f"echo http://0.0.0.0:8000/mean?value_type=clouds&city=Kyiv")
os.system(command)

command = f"curl -H 'Content-Type:application/json' -X GET 'http://0.0.0.0:8000/mean?value_type=temp&city=Uzhhorod'"
os.system(f"echo ===================================================")
os.system(f"echo http://0.0.0.0:8000/mean?value_type=temp&city=Uzhhorod")
os.system(command)

command = f"curl -H 'Content-Type:application/json' -X GET 'http://0.0.0.0:8000/records?city=Kharkiv&start_dt=2021-12-15&end_dt=2021-12-17'"
os.system(f"echo ===================================================")
os.system(f"echo http://0.0.0.0:8000/records?city=Kharkiv&start_dt=2021-12-15&end_dt=2021-12-17")
os.system(command)

command = f"curl -H 'Content-Type:application/json' -X GET 'http://0.0.0.0:8000/records?city=Kharkiv'"
os.system(f"echo ===================================================")
os.system(f"echo http://0.0.0.0:8000/records?city=Kharkiv")
os.system(command)

command = f"curl -H 'Content-Type:application/json' -X GET 'http://0.0.0.0:8000/moving_mean?city=Odesa&value_type=clouds'"
os.system(f"echo ===================================================")
os.system(f"echo http://0.0.0.0:8000/moving_mean?city=Odesa&value_type=clouds")
os.system(command)

command = f"curl -H 'Content-Type:application/json' -X GET 'http://0.0.0.0:8000/moving_mean?city=Chernihiv&value_type=wind_speed&wsize=2'"
os.system(f"echo ===================================================")
os.system(f"echo http://0.0.0.0:8000/moving_mean?city=Chernihiv&value_type=wind_speed&wsize=2")
os.system(command)
