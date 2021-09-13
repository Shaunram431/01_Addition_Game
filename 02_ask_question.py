import random

# generate random number...
num_1 = random.randint(1, 20)
num_2 = random.randint(1, 20)

question = "{} + {}".format(num_1, num_2)
display_question = "{} = ".format(question)
user_answer = int(input(display_question))

right_ans = eval(question)
print(right_ans)