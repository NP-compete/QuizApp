import parse_json as pj
import create_quiz as cq

QUIZ_FILE = 'quiz.json'

if __name__ == '__main__':
    # Parse JSON
    quiz_data = pj.parseNformat_json(QUIZ_FILE)
    # User option for category
    print("Choose Group: Sport, Maths : ", end="")
    group = input()
    group = group.lower()
    # Removing Human intervention error
    if group == "math":
        group = "maths"
    if group == "sports":
        group = "sport"
    # Create Quiz
    Score = cq.create_quiz(quiz_data, group)
    # Print Final Score
    print("Your Score : " + str(Score))
