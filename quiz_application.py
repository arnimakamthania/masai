#PYTHON QUIZ GAME

name = input("Enter your name: ")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
print(name.upper(), "WELCOME TO THIS AMAZING GAME.....")
print("^^^^^^^^^^^^^^^^^^^^^^^^^^")
#making tuples of questions
questions = ("How many months have 28 days?: ",
             "A farmer has 17 goats. All of them but 8 die. How many goats are alive?: ",
             "If you have a bowl with six apples and you take away four, how many apples do you have?: ",
             "How many 0.5cm slices can you cut from a bread that is 25cm long?: ",
             "You're 4th place right now in a race. What place will you be in when you pass the person in 3rd place?: ")  

# a 2d tuple of options...each inner tuple will consist of 4 elements
options = (("A. 2", "B. 1", "C. all of them", "D. what's a month"),  #this first elemnt corresponds to my first ques
           ("A. 8", "B. 9", "C. 25", "D. 35"),
           ("A. two apples", "B. four apples", "C. six apples", "D. i don't like apples"),
           ("A. 50", "B. 25", "C. 39", "D. none of the above"),
           ("A. 1st", "B. 2nd", "C. 3rd", "D. 4th"))

#tuple of answers
answers = ("C", "A", "B", "A", "C")

#list of guesses, we will be appending guesses throught our list thats why we are using list rather than a tuple
guesses = []

# score variable
score = 0
question_num = 0

for question in questions:
    print("----------------------------------------------------------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
        
        
    guess = input("Enter (A, B, C, D): ").upper()   
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!!")
    else:
        print("INCORRECT!!")
        print(f"{answers[question_num]} is the cprret answer.")
    question_num +=1
    
print("*********************")   #displaying results
print("       RESULTS       ")
print("*********************")

# we will iterate overall of the answers and the guesses
print("answers: ", end="")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

#printing score
score = int(score / len(questions) * 100)
print(f"YOUR SCORE IS : {score}%")
