from nltk.probability import ConditionalFreqDist
import random

START_LINE = '<s>'
END_LINE = '</s>'

def startEndTag(corpus):
    ''' Tag beginning and end of line to sentences of a corpus '''
    corpus = list(corpus)
    for sentence in corpus:
        sentence.insert(0, START_LINE)
        sentence.append(END_LINE)
    return corpus

def makeBigram(corpus):
    ''' Use a conditional frequency distribution table
    to store bigram model
    @return: a bigram model '''
    corpus = startEndTag(corpus)
    bigram = ConditionalFreqDist()
    context = ''
    for sentence in corpus:
        for word in sentence:
            if word != START_LINE:
                bigram[context][word] += 1
            context = word
    return bigram

def makeTrigram(corpus):
    '''For trigram'''
    corpus = startEndTag(corpus)
    trigram = ConditionalFreqDist()
    context = END_LINE + '$%' + START_LINE
    for sentence in corpus:
        for word in sentence:
            if word != START_LINE:
                trigram[context][word] += 1
            context = context[context.find('$%') + 2:] + '$%' + word
    return trigram

def randomSentsFromBigram(bigram, num=25, common=5):
    '''Generate random sentences from bigram
    @param num: number of sentences to generate
    @param common: number of most common words following a context
    to randomize from
    @return: the list of sentences generated
    '''
    sentences = []
    for i in range(0, num):
        context = START_LINE
        sentence = []
        # First word is more random
        possibleFirstWord = bigram[context].most_common(num)
        randomAtMost = random.randint(0, len(possibleFirstWord) - 1)
        context = possibleFirstWord[randomAtMost][0]
        sentence.append(context)
        # From next word onward, pick $common most common words
        while 1:
            mostCommonWords = bigram[context].most_common(common)
            randomAtMost = random.randint(0, len(mostCommonWords) - 1)
            context = mostCommonWords[randomAtMost][0]
            if context == END_LINE:
                break
            sentence.append(context)
        sentences.append(sentence)
    return sentences

def randomSentsFromTrigram(trigram, num=25, common=5):
    '''Generate random sentences from trigram
    @param num: number of sentences to generate
    @param common: number of most common words following a context
    to randomize from
    @return: the list of sentences generated
    '''
    sentences = []
    for i in range(0, num):
        context = END_LINE + '$%' + START_LINE
        sentence = []
        # First word is more random
        possibleFirstWord = trigram[context].most_common(num)
        randomAtMost = random.randint(0, len(possibleFirstWord) - 1)
        firstWord = possibleFirstWord[randomAtMost][0]
        sentence.append(firstWord)
        context = context[context.find('$%') + 2:] + '$%' + firstWord
        # From next word onward, pick $common most common words
        while 1:
            mostCommonWords = trigram[context].most_common(common)
            randomAtMost = random.randint(0, len(mostCommonWords) - 1)
            commonWord = mostCommonWords[randomAtMost][0]
            if commonWord == END_LINE:
                break
            sentence.append(commonWord)
            context = context[context.find('$%') + 2:] + '$%' + commonWord
        sentences.append(sentence)
    return sentences

def writeToFile(writeFile, model, choice):
    ''' Write random generated sentences to file
    @param choice: either a bigram or trigram'''
    if choice == 'bigram':
        for sentence in randomSentsFromBigram(model):
            writeFile.write(' '.join(sentence))
            writeFile.write('\n')
    elif choice == 'trigram':
        for sentence in randomSentsFromTrigram(model):
            writeFile.write(' '.join(sentence))
            writeFile.write('\n')
    else:
        print "Error with input choice"
