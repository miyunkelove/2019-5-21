import math

def eval_loop():
    while True:
        n = input('please input something: ')
        if n == 'done':
            print('Done')
            break
        print(eval(n))

eval_loop()


