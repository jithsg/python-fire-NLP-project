from textblob import TextBlob
import wikipedia

def search_wikipedia(name):
    #write docstring
    """Searches Wikipedia for a given name 
    and returns the results"""
    print(f'Searching Wikipedia for {name}')
    return wikipedia.search(name)

def summarize_wikipedia(name):
    """Summarizes Wikipedia for a 
    given name and returns the results"""
    print(f'Summarizing Wikipedia for {name}')
    return wikipedia.summary(name)

def get_text_blob(text):
    """Returns a TextBlob object"""
    return TextBlob(text)

def get_phrases(name):
    """Returns a list of phrases"""
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases


