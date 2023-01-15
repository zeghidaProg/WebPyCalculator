from flask import Flask, request, jsonify
import json
import requests


app = Flask(__name__)

@app.route('/' , methods=['GET','POST'] )
def weather():
    if request.method == 'GET':
    
        return '''
            <form method="POST" action="/">
                <input type="text" name="city" placeholder="City">
                <br><br>
                <input type="submit" value="Get Weather">
            </form>
        '''
    else:

        city = request.form["city"]
        api_key = "6086f3f702d160e3b8f0c20f1b46b50e"
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}'
        r = requests.get(url)
        data = json.loads(r.text)
        weather = data['weather'][0]['main']
        temp = data['main']['temp']
        temp_min = data['main']['temp_min']
        temp_max = data['main']['temp_max']
        return f"Weather in {city} is {weather}. Temperature is {temp}°C. Minimum temperature is {temp_min}°C. Maximum temperature is {temp_max}°C"
        #return data



if __name__ == "__main__":
    app.run(debug=True)

