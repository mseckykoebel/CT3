from nltk.corpus import wordnet

lion_synset = wordnet.synsets("Program")

# synset
print("Synset: ", lion_synset)

# the word
print("The word: ", lion_synset[0].name())

# definition
print("The definition: ", lion_synset[0].definition())

# some examples
print("Examples: ", lion_synset[0].examples())

synonyms = []
antonyms = []
word = "Got"

# find the synonyms and antonyms of the word variable
for syn in wordnet.synsets(word):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print("Synonyms: ", set(synonyms))
print("Antonyms: ", set(antonyms))
