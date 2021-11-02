import types

def pig_latin(word:str) -> str:
  if word.startswith(('a','e','i','o','u')):
    return word+'way'
  else:
    return word[1:]+word[0]+'ay'

print(pig_latin(input('word: ')))