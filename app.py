import requests
import json
import pandas as pd
import numpy as np
from flask import Flask, render_template, request
import xml.etree.ElementTree as ET


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
tree = ET.parse('kotus-sanalista_v1.xml')
root = tree.getroot()
words = [word.text.upper() for word in root.iter('s')]
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZÅÄÖ'
results = []
word_list = []
m = 1

for messages in json_data['bullshits']:
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
        word_list.append(
            [m, key, message + '.', translated + '.', *translated_word_list])
    m += 1

maxxx = max(len(l) for l in word_list)
columns = ['w' + str(i) for i in range(maxxx)]

df_words = pd.DataFrame(word_list, columns=columns)
df_words.fillna(value=0, inplace=True)
df_words['summa'] = df_words.iloc[:, 4:maxxx].isin(words).sum(axis=1, skipna=True)

df_all_originals = df_words.loc[:, ['w0', 'w2']].drop_duplicates()

df_words_no_bullshit = df_words[df_words['summa'] > 3].loc[:, ['w0', 'w3']]
df_words_no_bullshit.columns = ['#', 'No Bullshit']

df_words_bullshit = df_words[~df_words['w0'].isin(df_words_no_bullshit['#'])].loc[:, ['w0', 'w2']].drop_duplicates()
df_words_bullshit.columns = ['#', 'Bullshit']


@app.route('/')
def index():
    return render_template('index.html', tables=[df_all_originals.to_html(classes=["table table-striped", "th text-center", "thead thead-dark"], index=False, header=False)],
                           titles=['na', 'Originals'])


@app.route('/SomeFunction')
def SomeFunction():
    return render_template('testi.html', tables=[df_words_no_bullshit.to_html(classes=["table-info", "th text-center", "thead thead-dark"], index=False, header=False),
                                                 df_words_bullshit.to_html(classes=["table-danger", "th text-center", "thead thead-dark"],
                                                                            index=False, header=False)],
                           titles=['na', 'No Bullshit', 'Bullshit'])


if __name__ == '__main__':
    app.run()
