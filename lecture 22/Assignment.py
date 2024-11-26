import asyncio
from datetime import datetime

#Task 1
async def task1():
  print("task1 started")
  await asyncio.sleep(2)
  print("task1 finished")

async def task2():
  print("task2 started")
  await asyncio.sleep(5)
  print("task2 finished") 

async def main():
  start_time = datetime.now()

  async_task1 = asyncio.create_task(task1())
  async_task2 = asyncio.create_task(task2())

  await async_task1
  await async_task2

  end_time = datetime.now()
  print('Elapsed time: {}'.format(end_time - start_time))

if __name__ == '__main__':
  asyncio.run(main())


#Task 2
import random

async def random_sleep():
  print("task started")

  rand_num = random.randint(1,11)

  print(f"estimated time: {rand_num} sec")
  await asyncio.sleep(rand_num)

  for num in range(1, 11):
    print(num)

  print("task done")

async def main():
  start_time = datetime.now()

  task = asyncio.create_task(random_sleep())
  await task

  end_time = datetime.now()
  print("Elapsed time {}".format(end_time - start_time))

if __name__ == '__main__':
  asyncio.run(main())


#Task 3
async def square_if_even(num):
  output = num ** 2 if num % 2 == 0 else num
  status = "even" if num % 2 == 0 else "odd"
  print(f"{num} is {status}: result = {output}")
  return output

async def main():
  numbers = [2, 3, 4, 5, 6]
  await asyncio.gather(*(square_if_even(num) for num in numbers))
  
if __name__ == '__main__':
  asyncio.run(main())


#Task 4
async def write_txt(filename, text):
  print(f"Task started - {filename}")
  await asyncio.sleep(2)

  with open(filename, 'w') as file:
    file.write(text)
  print(f"Task finished - {filename}")

async def main():
  files = [
    ('lecture 22/file1.txt', 'Random text1'),
    ('lecture 22/file2.txt', 'Random text2'),
    ('lecture 22/file3.txt', 'Random text3')
  ]
    
  tasks = [asyncio.create_task(write_txt(filename, text)) for filename, text in files]
  
  await asyncio.gather(*tasks)

if __name__ == '__main__':
  asyncio.run(main())