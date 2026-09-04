Name = input("Enter your name :")
print("welcome", Name, "to the Quiz Gamel!🎯")
print("Good luck! 🍀")

question = input("what is capital of India? ")
if question.lower().strip() == "new delhi":
    print("Correct ✔️")
else:
    print("Incorrect ❌")