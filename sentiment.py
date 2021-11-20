import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def sentiment_analysis(text):
    data = pd.read_csv('../dataset.csv')
    x = data['text']
    y = data['category']
    vec = CountVectorizer(stop_words='english')
    x = vec.fit_transform(x).toarray()
    model = MultinomialNB()
    model.fit(x, y)
    ans = model.predict(vec.transform([text]))
    ans = list(ans)
    encoding = {'sadness':1, 'anger':2, 'love':3, 'surprise':4, 'fear':5, 'joy':6}
    emotion_list = list(encoding.keys())
    val_list = list(encoding.values())
    position = val_list.index(ans[0])
    return emotion_list[position]