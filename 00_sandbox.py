import random

# generate random number...
num_1 = random.randint(1, 20)
num_2 = random.randint(1, 20)

question = "{} + {}".format(num_1, num_2)
display_question = "{} = ".format(question)
user_answer = int(input(display_question))

right_ans = eval(question)

# get the user answer
d=int(input("What is your answer?: "))

# check if it's right(and them the result)
if d==user_answer:
    print("correct")
else:
    print()
    print("incorrect:" ,user_answer)
    print()