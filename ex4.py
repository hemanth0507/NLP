from collections import Counter
from nltk.util import ngrams

text="""I love ML.I love my mobile"""

tokens=text.lower().replace(".", "").split()
ug=Counter(tokens)
bg=Counter(ngrams(tokens,2))
tg=Counter(ngrams(tokens,3))

V=len(ug)
k=1
input_words=["I","love"]

nextwords=set(tokens)
scores={}
for word in nextwords:
    laplace=(bg[(input_words[1],word)]+1)/(ug[input_words[1]]+V)
    addk=(bg[(input_words[1],word)]+k)/(ug[input_words[1]]+k*V)
    
    if tg[(input_words[0],input_words[1],word)]>0:
        backoff=tg[(input_words[0],input_words[1],word)]/bg[(input_words[0],input_words[1])]
    elif bg[(input_words[1],word)]>0:
        backoff=bg[(input_words[1],word)]/ug[input_words[1]]
    else:
        backoff=ug[word]/sum(ug.values())

    i1,i2,i3=0.5,0.3,0.2

    if bg[(input_words[0],input_words[1])]>0:
        tri=tg[(input_words[0],input_words[1],word)]/bg[(input_words[0],input_words[1])]
    else:
        tri=0
    if ug[input_words[1]]>0:
        bi=bg[(input_words[1],word)]/ug[input_words[1]]
    else:
        bi=0
    uni=ug[word]/sum(ug.values())
    interp=i1*tri+i2*bi+i3*uni
    scores[word]=(laplace+addk+backoff+interp)/4

suggestions=sorted(scores.items(),key=lambda x:x[1],reverse=True)[:3]
print("Input:"," ".join(input_words))
print("Next word suggestions:")
for x,p in suggestions:
    print(x)
