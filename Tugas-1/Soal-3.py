def scoreCheck(x, y):
    if x >= 70 and y >= 70:
        print("Congratulations, you passed!")
    elif x >=70 and y < 70:
        print("You must retake the practical exam.")
    elif x < 70 and y >= 70:
        print("You must retake the theoretical exam.")
    else:
        print("You must retake both theoretical and practical exams.")

tExamScore = int(input("Input your theoretical exam score here: "))
pExamScore = int(input("Input your practical exam score here: "))

scoreCheck(tExamScore, pExamScore)