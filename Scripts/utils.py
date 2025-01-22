# Importing libraries
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import spacy
from LeIA import SentimentIntensityAnalyzer

# Loading Spacy's PT model
pt = spacy.load("pt_core_news_lg")

# Spacy portuguese stopwords, with some extra
pt_stopwords = pt.Defaults.stop_words
for word in ["há", "ano", "anos", "dia", "durante", "devido", "P"]:
    pt_stopwords.add(word)
    
# Sentiment analysis with an adaptation of nltk's VADER( Valence Aware Dictionary for Sentiment Reasoning) module
s = SentimentIntensityAnalyzer()

    
############################################################################################################################
##################################################>  Next Function  <#######################################################
############################################################################################################################

# Function to remove punctuation and lemmatize text
def lemmatizer(text):
    """Lemmatizes a given text"""
    
    # Disable components that are not needed for lemmatization
    doc = pt(text.lower(), disable=["morphologizer", "parser", "senter", "attribute_ruler", "ner"])
    
    # 1) Select only the lemma of each token that do not have punctuation
    # 2) Select only the lemmas that do not have their token text in portuguese stopwords
    lemmas = [token.lemma_ for token in doc if not token.is_punct and token.text not in pt_stopwords]
    return ' '.join(lemmas)


############################################################################################################################
##################################################>  Next Function  <#######################################################
############################################################################################################################

# Function to remove punctuation and lemmatize text
def tokenizer(text):
    """Tokenizes a given text"""
    
    # Disable components that are not needed for lemmatization
    doc = pt(text, disable=["morphologizer", "parser", "senter", "attribute_ruler", "ner"])
    
    # Removing punctuation and stopwords
    tokens = [token.text for token in doc if not token.is_punct and not token.is_digit and token.text not in pt_stopwords]
    return ' '.join(tokens)


############################################################################################################################
##################################################>  Next Function  <#######################################################
############################################################################################################################

# Function to vectorize text
def vectorizer(text):
    """Vectorizes a given text"""
    
    #Creating a document with all titles and descriptions
    doc = pt(text, disable=["morphologizer", "parser", "senter", "attribute_ruler", "ner"])
    
    return doc.vector 


############################################################################################################################
##################################################>  Next Function  <#######################################################
############################################################################################################################

# Function to find sentiment
def polarizer(sentence):
    """Finds sentiment compound through the use of LeIA library"""
    
    polarity = s.polarity_scores(sentence)
    return polarity["compound"]

############################################################################################################################
##################################################>  Next Function  <#######################################################
############################################################################################################################

from openai import OpenAI
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)
api_key = config["api_key"]
    
client_openai = OpenAI(api_key = api_key)

def get_embedding(text, model="text-embedding-ada-002"):
    response = client_openai.embeddings.create(
        input=text,
        model=model
    )
    return response.model_dump()["data"][0]["embedding"]


############################################################################################################################
##################################################>  Next Function  <#######################################################
############################################################################################################################

from scipy.spatial import distance
import numpy as np

def label_score(embedding, label_embeddings):
    cosine_similarities = [distance.cosine(embedding, label_embedding) for label_embedding in label_embeddings]
    return np.argmin(cosine_similarities)


############################################################################################################################
##################################################>  Next Function  <#######################################################
############################################################################################################################

# Applying "RdYlGn" directly on the plots was not working, the gradient needed will be applied manually to the data range through a function
def colormap_rdylgn(series, color_of_number = 0, vmin = -1, vmax = 1):
    """
    Returns a tuple:
    
    pos1[0]: colors -> a color mapping based on the values of a Series that vary between -1 and 1 (sentiment)
    pos2[1]: scalar_map -> a ScalarMappable object with the RdYlGn colormap to be used as a colorbar
    pos3[2]: color -> a specific color between the colormap, given a value between -1 and 1
    """
    # Create a colormap
    colormap = plt.cm.RdYlGn

    # Normalize the colormap based on data range
    norm = mcolors.Normalize(vmin, vmax)

    # Create a ScalarMappable object with the RdYlGn colormap
    scalar_map = plt.cm.ScalarMappable(cmap= colormap, norm= norm)

    # Create a color mapping based on normalized values 
    colors = [colormap(norm(value)) for value in series.values]
    scalar_map.set_array(series)
    
    color = colormap(norm(color_of_number))

    return colors, scalar_map, color