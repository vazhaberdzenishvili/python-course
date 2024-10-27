#Task 1
def is_anagram(txt1,txt2):
  txt1 = txt1.replace(" ", "").lower()
  txt2 = txt2.replace(" ", "").lower()

  if len(txt1) == len(txt2):
    for symbol in set(txt1):
        if txt1.count(symbol) != txt2.count(symbol):
          return False
    return True
  return False

print(is_anagram("helloworld","dlrowolleh"))
print(is_anagram("helloworld","dlrowollehe"))


#Task 2
def search_symbol(txt,symbol):
  return txt.count(symbol)

print(search_symbol("helloworld","o"))


#Task 3
def fibonacci_seq(n):
  sequence = []
  if n <=0:
    return sequence
  elif n == 1:
    sequence.append(n)
    return sequence
  elif n > 1:
    sequence.append(0)
    sequence.append(1)
    count = 2
    while count < n:
      next_value = sequence[count - 1] + sequence[count - 2]
      sequence.append(next_value) 
      count += 1
  return sequence

print(fibonacci_seq(9))