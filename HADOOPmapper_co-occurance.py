import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
from nltk.stem import PorterStemmer  
import sys

nltk.download('stopwords')
nltk.download('punkt')
ps = PorterStemmer() 
sw = set(stopwords.words('english')) 

def concatenate_list_data(list):
    result= ''
    for element in list:
        element=element.encode('utf-8')
        result += str(" ")+ str(element)
    return result


# input comes from STDIN (standard input)

with open('nytimesData.txt') as f:
    lines = f.readlines()
    
for line in sys.stdin:
    examp=line
    examp=examp.decode("utf8")
    wt = word_tokenize(examp) 
    
    filtered_sentence = [w for w in wt if not w in sw] 
      
    examp = concatenate_list_data(filtered_sentence)
    
    examp = examp.decode("utf8")
    words = word_tokenize(examp)
    
    filtered_sentence = []
    for w in words: 
        filtered_sentence.append(ps.stem(w)) 
        
				
    examp = concatenate_list_data(filtered_sentence)
    line = examp
    
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()
    
    # increase counters
    for i in range(len(words)-1):
        for j in list(range(i+1,len(words))):
            print (words[i],words[j],1)

