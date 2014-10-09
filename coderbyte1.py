def LongestWord(sen): 

  dictionnary=sen.split()
  for char in dictionnary:
    if len(dictionnary[int(char)+1])>len(dictionary[int(char)]):
      largestword=dictionnary[char+1]
  return largestword

answer=("What's your sentence?")
LongestWord(answer)