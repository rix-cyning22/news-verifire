from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import spacy
import re 

def scrape_text(link):
    nlp = spacy.load("en_core_web_lg")
    content = bs(urlopen(link), 'html.parser')
    title = content.find("h1").get_text()
    base = nlp(title)
    text = ""
    
    for para in content.find_all("p"):
        p = para.get_text()
        if nlp(p).similarity(base)>0.75:
            text += p
    text = title + text
    return text

def clean_text(txt):
  contractions = {
    "ain't": "am not", "aren't": "are not", "can't": "cannot",
    "you're": "you are",  "why's": "why is", "you'll've": "you will have",
    "can't've": "cannot have", "'cause": "because", "you'll": "you will",
    "could've": "could have", "i've": "i have", "what's": "what is",
    "couldn't": "could not", "couldn't've": "could not have",
    "didn't": "did not", "doesn't": "does not", "don't": "do not",
    "hadn't": "had not", "hadn't've": "had not have", "hasn't": "has not",
    "haven't": "have not", "he'd": "he would", "he'd've": "he would have",
    "he'll": "he will", "he'll've": "he will have", "he's": "he is",
    "how'd": "how did", "how'd'y": "how do you", "how'll": "how will",
    "how's": "how is", "i'd": "i would", "i'd've": "i would have",
    "i'll": "i will", "i'll've": "i will have", "i'm": "i am",
    "isn't": "is not", "it'd": "it had", "it'd've": "it would have",
    "it'll": "it will", "it'll've": "it will have", "it's": "it is",
    "let's": "let us", "ma'am": "madam", "mayn't": "may not",
    "when's": "when is", "we've": "we have", "we're": "we are",
    "might've": "might have", "mightn't": "might not", "we'll": "we will",
    "mightn't've": "might not have", "must've": "must have",
    "mustn't've": "must not have", "needn't": "need not",
    "needn't've":"need not have","o'clock":"of the clock",
    "oughtn't":"ought not", "that's": "that is", "she's": "she is",
    "oughtn't've": "ought not have","shan't": "shall not",
    "sha'n't": "shall not", "shouldn't": "should not",
    "shan't've": "shall not have", "she'd": "she would",
    "weren't": "were not", "there's": "there is", "where'd": "where did",
    "she'd've": "she would have","she'll": "she will",
    "she'll've":"she will have", "they'll": "they will",
    "should've": "should have", "they've": "they have",
    "shouldn't've": "should not have", "so've": "so have",
    "that'd": "that would", "that'd've": "that would have",
    "there'd": "there had","there'd've": "there would have",
    "they'd": "they would", "they'd've": "they would have",
    "they'll've": "they will have", "they're": "they are",
    "what're": "what are", "y'all": "you all", "you'd": "you had",
    "to've": "to have", "wasn't": "was not", "we'd": "we had",
    "we'd've": "we would have", "mustn't": "must not",
    "we'll've": "we will have", "you've": "you have",
    "what'll": "what will", "what'll've": "what will have",
    "what've": "what have", "when've": "when have", "so's": "so is",
    "where's": "where is", "where've": "where have", "who'll": "who will",
    "who'll've": "who will have", "who's": "who is", "won't": "will not",
    "who've": "who have", "why've": "why have", "will've": "will have",
    "won't've": "will not have", "would've": "would have",
    "wouldn't": "would not", "wouldn't've": "would not have",
    "y'alls": "you alls", "y'all'd": "you all would",
    "y'all'd've": "you all would have", "y'all're": "you all are",
    "y'all've": "you all have", "you'd've": "you would have",
    "u.s.": "united states", "u.k.": "united kingdom",
  }
  txt = txt.lower()
  txt = re.sub("([a-zA-Z0-9]+)([.?!/,;:])([a-z]+)", r"\1\2 \3", txt)
  txt = re.sub(r"[.]\d+", "@", txt)
  txt = re.sub(r"\d+([.][. ]+)", r"@\1", txt)
  txt = re.sub(r"\d[.][,0-9a-z]*", "@", txt)
  txt = re.sub(r"\d+", "@", txt)
  txt = re.sub(r"@[a-z]+", "@", txt)
  txt = re.sub(r"@@*", "@", txt)
  txt = txt.replace("\"", "")
  txt = txt.replace("'", "")
  return " ".join([contractions[t] if t in contractions.keys()
                                  else t
                  for t in txt.split()])