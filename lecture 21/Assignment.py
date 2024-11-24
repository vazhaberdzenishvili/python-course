#Task 1
import json
import threading

def process_json_file(filename):
  with open(filename, 'r') as json_file:
    data = json.load(json_file)
    print(f"Processing file: {filename}")
    print("Data:")
    print(json.dumps(data, indent=4))

json_files = ["lecture 21/person1.json", "lecture 21/person2.json", "lecture 21/person3.json"]

for file in json_files:
  thread = threading.Thread(target=process_json_file, args=(file,))
  thread.start()
  thread.join()

print('All threads finished')


#Task 2
from queue import Queue

def worker(queue):
  while True:
    number = queue.get() 
    
    if number is None: 
      break
    
    thread_name = threading.current_thread().name
    is_even = "even" if number % 2 == 0 else "odd"
    print(f"{thread_name}, {number}, {is_even}")

    queue.task_done() 

queue = Queue()

num_threads = 3
threads = []

for _ in range(num_threads):
  thread = threading.Thread(target=worker, args=(queue,))
  thread.start()
  threads.append(thread)

numbers = [47, 91, 8, 13, 6, 17, 2, 35, 9]

for number in numbers:
  queue.put(number)

queue.join()

for _ in range(num_threads):
  queue.put(None)

for thread in threads:
  thread.join()
  
print("All tasks completed")