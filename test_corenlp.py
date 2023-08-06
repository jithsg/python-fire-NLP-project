from nlplogic.corenlp import get_phrases, get_text_blob, search_wikipedia, summarize_wikipedia

def test_get_phrases():
    """Tests get_phrases function"""
    phrases = get_phrases('Barack Obama')
    assert len(phrases) > 0
    assert 'obama' in phrases[0]
    
def test_get_text_blob():
    """Tests get_text_blob function"""
    text = 'This is a test'
    blob = get_text_blob(text)
    assert blob
    assert blob == text

def test_search_wikipedia():
    """Tests search_wikipedia function"""
    results = search_wikipedia('Barack Obama')
    assert len(results) > 0
    assert 'Obama' in results[0]

def test_summarize_wikipedia():
    results = summarize_wikipedia('Barack Obama')
    assert len(results) > 0
    assert 'Obama' in results
    