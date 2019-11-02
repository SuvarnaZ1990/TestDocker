# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 11:52:52 2019

@author: Suvy
"""
import numpy as np
import re
import flask
import json
from flask import Flask, request
import nltk
from nltk.corpus import stopwords
from string import punctuation
nltk.download('stopwords')
nltk.download('punkt')
stop_words = stopwords.words('english')



app = Flask(__name__)



@app.route('/home')
def test_api():
    return 'Yay !! Its working'

@app.route('/topwords',methods=['POST'])
def find_top_words():
    
    data = json.loads(request.data.decode())
    text,num_words = data['text'], data['num']
    word_tokens = re.split(' |;|,|:',text)
    word_len = [len(word) for word in word_tokens]
    sorted_len = np.argsort(word_len)
    top_words = []
    for idx in sorted_len[-num_words:]:
        top_words.append(word_tokens[idx])
    return str(top_words)

@app.route('/lastwords',methods=['POST'])
def find_last_words():
    
    data = json.loads(request.data.decode())
    text,num_words = data['text'], data['num']
    word_tokens = re.split(' |;|,|:',text)
    word_len = [len(word) for word in word_tokens]
    sorted_len = np.argsort(word_len)
    last_words = []
    for idx in sorted_len[:num_words]:
        last_words.append(word_tokens[idx])
    return last_words

@app.route('/removestopwords',methods=['POST'])
def remove_stopwords():
    
    custom = stop_words+list(punctuation)
    data = json.loads(request.data.decode())
    text = data['text'].lower()
    tokens = nltk.tokenize.word_tokenize(text)
    tokens = [t for t in tokens if t not in customss] #remove stopwords and punctuation
    return str(tokens)
#top_words1 = find_top_words('my school is very far',4)
#last_words1 = find_last_words('my school is near to dom',2)
#print(top_words1)
#print(last_words1)

if __name__ =='__main__':
    app.run(host='localhost', port=5000, debug =True)