#Task 1
with open('text.txt', 'w') as file:
  for i in range(1, 1001):
      file.write("Lorem Ipsum is simply dummy text of the printing and typesetting industry {}\n".format(i))
with open('text.txt', 'r') as file:
  lines = file.readlines()
  total = len(lines)

print(f'Total: {total}')


#Task 2
lines = {
  2: "მეორე",
  8: "მერვე",
  10: "მეათე",
  13: "მეცამეტე",
  17: "მეჩვიდმეტე",
}

with open('text.txt', 'w', encoding='utf-8') as file:
  for num in range(1, 18):
      if num in lines:
        file.write(lines[num] + '\n')
      else:
        file.write('\n') 

#Task 3
text = ""
for filename in ['text1.txt', 'text2.txt']:
  with open(filename) as file:
    text += file.read() + "\n"

with open('combined.txt', 'w') as file:
  file.write(text)

print(text)

#Task 4
def palindrome_finder(file):
  with open(file, 'r') as file:
    lines = [line.strip() for line in file]

  for i in range(len(lines)):
    for j in range(i + 1, len(lines)):
      line1_standardized = lines[i].replace(" ", "").lower()
      line2_standardized = lines[j].replace(" ", "").lower()[::-1]
      if line1_standardized == line2_standardized:
        print(f'palindrome:\n{lines[i]} | {lines[j]}')
    
palindrome_finder('text1.txt') 

#Task 5
def split_file(file):
  with open(file, 'r', encoding='utf-8') as f:
    lines = f.readlines()

  for i in range(0, len(lines), 10):
    output_file = f'text{i // 10 + 1}.txt'
    with open(output_file, 'w',encoding='utf-8') as part_file:
      part_file.writelines(lines[i:i + 10])

split_file('text.txt')


#Task 6
def empty_lines_remover(input_file, output_file):
  with open(input_file, 'r') as file:
    lines = file.readlines()

  with open(output_file, 'w') as file2:
    for line in lines:
      if line.strip():
        file2.write(line)
        
empty_lines_remover('text.txt', 'text1.txt')