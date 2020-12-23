import nltk
from urllib import request 
import string 
import random 


f=open("Mathematical_Jargon.txt",'r')
jargon_list=[]
for line in f:
    jargon_list.append(line.split())
f.close()

f2=open("Five of Maxwells Papers.txt","r")
maxwell_raw=f2.read()
maxwell_tokens=nltk.word_tokenize(maxwell_raw)
#maxwell_text=nltk.Text(maxwell_tokens)
f2.close()

f3=open("PartofScienceandHypothesis.txt","r")
science_raw=f3.read()

f4=open("DeclerationofIndependence.txt","r")
decleration_raw=f4.read()

f5=open("PartofMathematicalP.txt","r")
mathematicalp_raw=f5.read()

bigrams=nltk.bigrams(maxwell_raw)
cfd = nltk.ConditionalFreqDist(bigrams)

lem=nltk.stem.WordNetLemmatizer()

def LemmatizeWords(words):
    return [lem.lemmatize(word) for word in words]

remove_punctuation= dict((ord(punctuation),None) for punctuation in string.punctuation )

def Remove_Punctuations(text):
    return LemmatizeWords(nltk.word_tokenize(text.lower().translate(remove_punctuation)))

new_maxwell_raw=Remove_Punctuations(maxwell_raw)
new_science_raw=Remove_Punctuations(science_raw)
new_decleration_raw=Remove_Punctuations(decleration_raw)
new_mathematicalp_raw=Remove_Punctuations(mathematicalp_raw)

my_corpus=new_maxwell_raw+new_science_raw+new_decleration_raw+new_mathematicalp_raw

def generate_random_word(source = None, num = 1):
    result = []
    while source == None or not source[0].isalpha():
        source = random.choice(my_corpus)
    word = source
    result.append(word)
    while len(result) < num:
        if word in cfd:
            init_list = list(cfd[word].keys())
            choice_list = [x for x in init_list if x[0].isalpha()]
            if len(choice_list) > 0:
                newword = random.choice(choice_list)
                result.append(newword)
                word = newword
            else:
                word = None
                newword = None
        else:
            newword = None
            while newword == None or not newword[0].isalpha():
                newword = random.choice(my_corpus)
            result.append(newword)
            word = newword
    return result

def generate_random_statement():
    sentence=""
    prev_word=None
    for i in range(16):
        generated_word=generate_random_word(prev_word,2)[1]
        if(i==0):
            sentence+=generated_word.capitalize()+" "
        else:    
            if(generated_word=="i"):
                sentence+="I "
            else:    
                sentence+=generated_word+" "
    
    return sentence+random.choice(jargon_list)[0]

#print(generate_random_statement())