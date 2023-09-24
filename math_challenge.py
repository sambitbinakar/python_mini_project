import random
import time


operators = ["+","-","*"]
min_operand = 3
max_operand = 12
Total_problem = 10

def generate_problem():
    left = random.randint(min_operand , max_operand)
    right = random.randint(min_operand , max_operand)
    operator = random.choice(operators)

    expr = str(left) + "" + operator + "" + str(right)
    answer = eval(expr)
    return expr , answer


wrong = 0
input("press enter to start!")
print("---------------------")

start_time = time.time()

for i in range(Total_problem):
    expr, answer = generate_problem()
    while True:
        guess = input("problem #" + str(i+1) + ":" + expr + "=")
        if guess == str(answer):
            break
        wrong += 1

end_time = time.time()
Total_time = round(end_time - start_time)

print("------------------")
print("nice work! you finshed in", Total_time, "secons!")