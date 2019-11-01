import requests
import json
import pandas as pd
import numpy as np
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


headers = {
    'x-session-id': '12345',
    'authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJidWxsc2hpdCI6ImJ1bGxzaGl0IiwiaWF0IjoxNTcxNDkxNDM2fQ.Nsj7D-QlOBrHfqX5jdbqeOzIUYzzuiyKZSSlTl57QEs',
    'Accept': 'application/json',
    'Content-Type': 'application/json',
}

response = requests.get(
    'https://koodihaaste-api.solidabis.com/bullshit', headers=headers)
json_data = json.loads(response.text)
json_data['bullshits']


words = [line.rstrip('\n').upper()
         for line in open('kaikkisanat.txt', encoding='utf-8')]
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ'
results = []
word_list = []
m = 0

for messages in json_data['bullshits']:
    m += 1
    message = messages['message'].upper().replace('.', '')
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in message:
            if symbol in LETTERS:
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
                translated_word_list = list(translated.split(' '))
            else:
                translated = translated + symbol
                translated_word_list = list(translated.split(' '))
        results.append([m, key, message, translated, *translated_word_list])
        word_list.append([m, key, *translated_word_list])

maxxx = max(len(l) for l in word_list)

columns = ['w' + str(i) for i in range(maxxx)]
df_words = pd.DataFrame(word_list, columns=columns)
df_words.fillna(value=0, inplace=True)
df_words['summa'] = df_words.iloc[:, 2:maxxx].isin(
    words).sum(axis=1, skipna=True)
# df_translated= df[df['summa']>=2].iloc[:,3].drop_duplicates()
# df_jibberish = df[df['summa']<2].iloc[:,2].drop_duplicates()
df_words.set_index(['w0', 'w1'], inplace=True)


print(df_words[df_words['summa'] > 2])
print(df_words)
print(max(len(l) for l in word_list))

df_words[df_words['summa'] > 2].to_csv("output.csv")


# with pd.option_context('display.max_rows', -1, 'display.max_columns', 5):


# @app.route('/')
# def index():
#     response = requests.get('https://koodihaaste-api.solidabis.com/bullshit', headers=headers)
#     data = json.loads(response.content)
#     return render_template('content.html', data = data)

# @app.route('/SomeFunction')
# def SomeFunction():
#     return render_template('index.html', data_t = df_translated, data_j = df_jibberish)


# if __name__ == '__main__':
#    app.run()
