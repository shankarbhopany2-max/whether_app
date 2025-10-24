# # import requests
# # url = ""
# # response = requests.get(url)
# # print(url)


# import requests

# def get_weather(city):
#     api_key = "your_api_key_here"  # Replace with your actual API key
#     url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#     response = requests.get(url)
#     data = response.json()
#     if data["cod"] == 200:
#         main = data["main"]
#         weather = data["weather"][0]
#         print(f"Weather in {city}:")
#         print(f"Temperature: {main['temp']}°C")
#         print(f"Condition: {weather['description'].title()}")
#     else:
#         print("City not found or API error.")
# city = input("Enter city name: ")
# get_weather(city)





import requests
while True:
    city = input("Enter city name: ")
    api_key = "0d73be152a34472fac0110919252410" 
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    try:
        response = requests.get(url)
        
        print("Requested URL:", url)
        print("Status Code:", response.status_code)
        
        if response.status_code == 200:
            data = response.json()
            print("\nWeather Data:")
            print(f"City: {data['location']['name']}")
            print(f"Temperature: {data['current']['temp_c']}°C")
            print(f"Condition: {data['current']['condition']['text']}")
            print(f"Humidity: {data['current']['humidity']}%")
        else:
            print(f"Error: {response.status_code}")
            print(response.text)
            
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except KeyError as e:
        print(f"Unexpected data format: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
