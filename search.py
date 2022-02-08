# Script generates a URL, and opens it in a given browser (msedge).
# The script needs adjustments depending on where your browser is installed,
# and which browser you want to use.
import webbrowser               # Opening url in local browser

# Setup browser location and type
browserLocation = "C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
webbrowser.register('edge',
	None,
	webbrowser.BackgroundBrowser(browserLocation))

def create_url():
    # Searchwords
    textToSearch = "&q="
    
    # Open file with searchphrases
    f = open('search_phrases.txt', 'rt', encoding='utf-8-sig')
    searchPhrases = f.read()
    searchPhrases = searchPhrases.split("\n")
    f.close()

    # Join all search phrases together with OR and put them in parenthesis.
    for phrase in searchPhrases:
        if phrase != "" and phrase != "#":
            if phrase == searchPhrases[0]:
                # First phrase
                phrase = "(" + phrase + ")"
                textToSearch = textToSearch + phrase
            else:
                # All consecutive phrases
                phrase = "(" + phrase + ")"
                textToSearch = textToSearch + " OR " + phrase
        elif phrase == "#":
            # Stop processing content here, for easier production of good search phrases
            break

    # Words that NEVER should be part of an ad
    f = open('no_no_words.txt', 'rt', encoding='utf-8-sig')
    noNoWords = f.read()
    noNoWords = noNoWords.split("\n") 
    f.close()

    # First line should 
    if noNoWords[0] != "":
        textToSearch = textToSearch + " NOT ("

        # Join NoNo words to the search phrase, with NOT
        for phrase in noNoWords:
            if phrase != "" and phrase != "#":
                if phrase == noNoWords[0]:
                    # First phrase
                    phrase = "(" + phrase + ")"
                    textToSearch = textToSearch + phrase
                else:
                    # All consecutive phrases
                    phrase = "(" + phrase + ")"
                    textToSearch = textToSearch + " NOT " + phrase
            elif phrase == "#":
                # Stop processing content here, for easier production of good anti-search phrases
                break

        textToSearch = textToSearch + ")"

    # Remove spaces and URLify
    textToSearch = textToSearch.replace(' ', '+')
    textToSearch = textToSearch.replace('(', '%28') # Not actually needed, just a precaution
    textToSearch = textToSearch.replace(')', '%29') # Not actually needed, just a precaution

    # Add location to search
    locOslo = "&location=1.20001.20061" # Not in use, only as an example
    location = ""

    # Other
    sortBy = "&sort=PUBLISHED_DESC"

    # Create URL from variables
    url = "https://www.finn.no/job/fulltime/search.html?abTestKey=rerank" + location + textToSearch + sortBy
    return url
 
 searchUrl = create_url()
 webbrowser.get('edge').open(searchUrl)
