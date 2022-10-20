from hashlib import md5
from timeit import default_timer as timer


start_time = timer()

sugar = "198";
spice = "471";
everythingnice = "hello"

for i in range(9999999999):
    string = sugar + str(i) + spice + everythingnice

    hashed = md5(string.encode()).hexdigest()

    print(f'{string} --> {hashed}')

    if hashed[:2] == '0e' and hashed[2:].isnumeric():
        print(f"Magic word: {i}")
        print(f"Time to bruteforce: {timer() - start_time} second")
        break