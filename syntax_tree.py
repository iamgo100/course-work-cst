import nltk

sentense = '''My mom couldn't let me go to St.Petersburg.'''
tokens = nltk.word_tokenize(sentense)
tagged = nltk.pos_tag(tokens)

grammar = r'''
S: {<NP><VP>}
NP: {<PRP\$>?<NN.?>}
VP: {<AnV>?<VB.?><PRP>?<TO>?<NP>?}
AnV: {<MD><RB>?<VP>+?}
'''

parser = nltk.RegexpParser(grammar)
result = parser.parse(tagged)

result.draw()
