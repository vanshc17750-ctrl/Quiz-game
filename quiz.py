Name = input("Enter your name :")
Score = 0
print("welcome", Name, "to the Quiz Gamel!🎯")
print("Good luck! 🍀")

print("\n1. What is the capital of India?")
print("A. Mumbai")
print("B. New Delhi")
print("C. Kolkata")
print("D. Chennai")

answer = input("Enter your answer (A/B/C/D): ")

if answer.lower().strip() == "b":
    print("Correct ✔️")
    Score += 1
else:
    print("Incorrect ❌")

print("\n2. How many days are there in a week?")
print("A. 5")
print("B. 6")
print("C. 7")
print("D. 8")

answer = input("Enter your answer (A/B/C/D): ")

if answer.lower().strip() == "c":
    print("Correct ✔️")
    Score += 1
else:
    print("Incorrect ❌")

print("\n3. Who is the current president of India :")
print("A. Narendra Modi")
print("B. Rajendra Prasad")
print("C. Jwaharlal Nehru")
print("D. Dropdi Murmu")

answer = input("Enter your answer (A/B/C/D): ")
if answer.lower().strip() == "d":
    print("Correct✔️")
    Score += 1
else:
    print("Incorrect ❌")

print("\n4. 🎉 Quiz Completed!")
print("Your total score is :", Score)
print("And your total percentage is :", Score/3*100)
