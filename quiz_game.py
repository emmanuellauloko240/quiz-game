score = 0

while True:
    animal = [
        
        {"question": "What sound does a dog make?", "answer": "Bark"}

    ]
    print(animal["question"])

    solution = input("What's your answer: ")
    if solution.lower() == animal["answer"].lower():
        print("Correct!")
    else:
        print("Wrong!")