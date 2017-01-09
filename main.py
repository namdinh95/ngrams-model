from nltk.corpus import gutenberg
from my_ngrams import *

# Use Jane Austen's "Emma" novel
emma = gutenberg.sents('austen-emma.txt')
# Use Bible
bible = gutenberg.sents('bible-kjv.txt')
# Make a weird corpus
emmabible = emma + bible

# Make a bigram for each
emmaBigram = makeBigram(emma)
bibleBigram = makeBigram(bible)
emmabibleBigram = makeBigram(emmabible)

# Open some files to write to
emmaFile = open('emma.txt', 'w')
bibleFile = open('bible.txt', 'w')
emmabibleFile = open('emmabible.txt', 'w')

# Write to files
writeToFile(emmaFile, emmaBigram, 'bigram')
writeToFile(bibleFile, bibleBigram, 'bigram')
writeToFile(emmabibleFile, emmabibleBigram, 'bigram')

# Now trigram
emmaTrigram = makeTrigram(emma)
bibleTrigram = makeTrigram(bible)
emmabibleTrigram = makeTrigram(emmabible)

# Open files to write to
emmaTFile = open('emmaT.txt', 'w')
bibleTFile = open('bibleT.txt', 'w')
emmabibleTFile = open('emmabibleT.txt', 'w')

# Write to files
writeToFile(emmaTFile, emmaTrigram, 'trigram')
writeToFile(bibleTFile, bibleTrigram, 'trigram')
writeToFile(emmabibleTFile, emmabibleTrigram, 'trigram')

# Close all files
emmaFile.close()
bibleFile.close()
emmabibleFile.close()
emmaTFile.close()
bibleTFile.close()
emmabibleTFile.close()
