# Simple AI response evaluation script

def evaluate_response(question, response, correct_answer):
    score = 0

    if correct_answer.lower() in response.lower():
        score += 5

    if len(response) > 10:
        score += 2

    if response.endswith("."):
        score += 1

    return score


question = "What is the capital of France?"
response = "Paris."
correct_answer = "Paris"

score = evaluate_response(question, response, correct_answer)

print("Question:", question)
print("Response:", response)
print("Score:", score)
