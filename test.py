
import requests
import json
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)





headers = {
    'x-session-id': '12345',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJidWxsc2hpdCI6ImJ1bGxzaGl0IiwiaWF0IjoxNTcxNDkxNDM2fQ.Nsj7D-QlOBrHfqX5jdbqeOzIUYzzuiyKZSSlTl57QEs',
    'Accept': 'application/json',
    'Content-Type': 'application/json'
}

# response = requests.get('https://koodihaaste-api.solidabis.com/bullshit', headers=headers)
# print(response.json)

# json_data = json.loads(response.text)
#json_data['bullshits']



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/SomeFunction')
def SomeFunction():
    response = requests.get('https://koodihaaste-api.solidabis.com/bullshit', headers=headers)
    data = json.loads(response.content)
    print(data)
    return render_template('content.html', data = data)



if __name__ == '__main__':
   app.run()