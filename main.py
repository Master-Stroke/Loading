import time
word = "loading"
choose = input("Hello, Please Choose variant of loading 1 or 2 ")
if choose == "1":
   while True:
    print("\r+ " + word, end="")
    time.sleep(0.3)
    print("\rx " + word, end="")
    time.sleep(0.3)
if choose == "2":    
   while True:
    time.sleep(0.3)
    print("\r- " + word, end="")
    time.sleep(0.3)
    print("\r\\ " + word, end="")
    time.sleep(0.3)
    print("\r| " + word, end="")
    time.sleep(0.3)
    print("\r/ " + word, end="")
else:
    print("sorry, but you didn't write correctly!")    