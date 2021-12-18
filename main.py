import json
import nltk
import plotly.express as px
import pandas as pd
import itertools
from datetime import date, datetime
from textblob import TextBlob
from tqdm import tqdm

nltk.download('words')
words = set(nltk.corpus.words.words())
file = open("result.json", encoding= "utf-8")
data = json.load(file)
allMessages = []
dictionary = dict()
englishMessagesDictionary = dict()
scores = []
messages = []
global dateset
dateset = set()

def set_up_dictionaries():
    global dateset
    for message in data["messages"]:
        dateset.add(message["date"][:10])

    dateset = list(sorted(dateset))

    for i in tqdm(dateset):
        dictionary[i] = []
        englishMessagesDictionary[i] = []


def extract_all_text():
    for message in tqdm(data["messages"]): 
        if len(message["text"]) > 0:
            s = ""
            for i in message["text"]:
                if isinstance(i, str):
                    s += i
                elif isinstance(i, dict):
                    s += i["text"]
            dictionary[message["date"][:10]].append(s)
        else:
            dictionary[message["date"][:10]].append(message["text"])


def extract_key_words():
    k1 = "shib"
    k2 = "doge"
    keys = list(map(''.join, itertools.product(*zip(k1.upper(), k1.lower()))))
    keys = keys + list(map(''.join, itertools.product(*zip(k2.upper(), k2.lower()))))

    for key in tqdm(dictionary.keys()):
        for value in dictionary[key]:
            english_words = " ".join(w for w in nltk.wordpunct_tokenize(value) if w.lower() in words or not w.isalpha())
            if len(english_words) > 0:
                for i in keys:
                    if i in english_words:
                        englishMessagesDictionary[key].append(value)


def calculate_scores():
    for key in tqdm(englishMessagesDictionary.keys()):
        s = 0
        l = len(englishMessagesDictionary[key])
        for value in englishMessagesDictionary[key]:
            sentiment_score = TextBlob(value).sentiment.polarity
            s += sentiment_score
        scores.append(round(s/l,4))
        messages.append(l)


def visualize():
    df = pd.DataFrame(list(zip(dateset, scores, messages)),
                columns =['Date', 'Sentiment_scores','Message_counts'])

    fig = px.line(df, x="Date", y="Sentiment_scores")
    fig.update_layout(
        title="Date vs Sentiment scores",
        xaxis_title="Date",
        yaxis_title="Value",
        font=dict(
            family="Courier New, monospace",
            size=14
        )
    )
    fig.show()

    fig = px.line(df, x="Date", y="Message_counts")
    fig.update_layout(
        title="Date vs Message counts",
        xaxis_title="Date",
        yaxis_title="Value",
        font=dict(
            family="Courier New, monospace",
            size=14
        )
    )
    fig.show()

    fig = px.line(df, x='Date', y=df.columns[1:])
    fig.update_layout(
        title="Date vs Sentiment scores and Message counts",
        xaxis_title="Date",
        yaxis_title="Value",
        font=dict(
            family="Courier New, monospace",
            size=14
        )
    )
    fig.show()


set_up_dictionaries()
extract_all_text()
extract_key_words()
calculate_scores()
visualize()

# @Language.factory("language_detector")
# def get_lang_detector(nlp, name):
#        return LanguageDetector()
# # nlp = spacy.load("en_core_web_sm")
# # nlp.add_pipe('language_detector', last=True)
# # print(nlp("Test")._.language)