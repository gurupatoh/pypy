
from collections import Counter
count= Counter()
words = [
'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into', 'my',
'eyes', "you're", 'under'
]
for word in words:
      count[word] +=1

print(count)