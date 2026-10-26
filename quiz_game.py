# score = 0

# while True:
#     questions = [
        
#         {"question": "What sound does a dog make?", "answer": "Bark"}

#     ]
#     for question in questions:
#     # print(animal["question"])

#     solution = input("What's your answer: ")
#     if solution.lower() == animal["answer"].lower():
#         print("Correct!")
#     else:
#         print("Wrong!")

question = {"question": "What is the capital of France?: ", "answer": "paris"}

user_answer = input(question["question"])
print(user_answer)

if user_answer == question["answer"]:
    print("ooh Emmilie you got it Correct....🥹")
else:
    print(f"ooh Emmilie you're Wrong 🥹 but it's ok to try again! The was answer {question['answer']}")