name=input("Enter the name: ")
print("welcome to our quiz !!",name)
print("lets begin our quiz, best of luck!!")
print("first a fall i will you the rules of the quiz")
print("1. there will be 5 questions in the quiz")
print("2. each question will have 4 options")
print("3. you have to choose the correct option")
print("4. each correct answer will give you 1 point")
print("5. there is no negative marking for wrong answers")
print("now lets start the quiz")
score=0
print("question 1: what is the capital of india?")
print("a. delhi")      
print("b. mumbai")
print("c. kolkata")
print("d. chennai")
answer1=input("enter your answer: ")
if answer1=="a":
    print("correct answer")
    score=score+1
else:
    print("wrong answer")
    
print("question 2: who is the president of india?")
print("a. murmu ji")
print("b. narendra modi")
print("c. amit shah")
print("d. arun jaitley")
answeer2=input("enter your answer: ")
if answeer2=="a":
    print("correct answer")
    score=score+1  
else:
    print("wrong answer")
    
print("question 3: who is the prime minister of india?")
print("a. narendra modi")
print("b. amit shah")
print("c. arun jaitley")
print("d. manmohan singh")
answer3=input("enter your answer: ")
if answer3=="a":
    print("correct answer")
    score=score+1
else:
    print("wrong answer")

print("question 4: who is the chief minister of delhi?")
print("a. arvind kejriwal")
print("b. manish sisodia")
print("c. amit shah")
print("d. rekha ji ")
answer4=input("enter your answer: ")
if answer4=="a":  
    print("correct answer")
    score=score+1
else:
        
    print("wrong answer")

print("question 5: who is the chief minister of uttar pradesh?")
print("a. yogi adityanath")
print("b. akhilesh yadav")
print("c. mayawati")
print("d. mulayam singh yadav")
answer5=input("enter your answer: ")
if answer5=="a":
    print("correct answer")
    score=score+1
else:
    print("wrong answer")   
print("your final score is: ",score)
        