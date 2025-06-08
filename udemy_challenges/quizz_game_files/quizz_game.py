"""A QUIZZ GAME THAT :
- get question list, possible answer, and correct answer from a csv file
- display question 1 by 1, until all are done
- when all questions are answered by user, display the result
"""

import csv


# Ask how many questions user want to play with
def ask_size_quizz() -> int:
    while True:
        try:
            value = int(input("How many questions do you want to answer? : "))
            if value > 0:
                return value
            else:
                print("Please enter a number greater than 0.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Capture csv data into a list of dictionaries
def read_csv_data(filepath: str) -> list[dict]:  # Return a list of dictionaries
    with open(filepath, "r", encoding="utf-8") as file:
        whole_quizz_data: list = list(csv.DictReader(file))
        return whole_quizz_data


# Get a random sub extract of quizz_data to match number of questions asked by user
import random


def sub_quizz_data(quizz_data: list[dict], size: int) -> list[dict]:
    if size > len(quizz_data):
        print(f"Only {len(quizz_data)} questions available. Returning all of them.")
        return quizz_data
    random.shuffle(quizz_data)
    return quizz_data[:size]


# Parse quizz_data into different lists
def parse_dict_data(dict_data: list[dict]) -> tuple[list, list, list, list]:
    questions: list = [row["Questions"] for row in dict_data]
    propositions: list = [row["Propositions"] for row in dict_data]
    index_correct_answers: list = [row["Correct_answer_index"] for row in dict_data]
    text_answers: list = [row["Correct_answer_text"] for row in dict_data]
    return questions, propositions, index_correct_answers, text_answers  # Tuple


# Ask all questions and store user's answers
def ask_questions_store_answers(questions, propositions) -> list:
    user_answers: list = []
    for question, proposition in zip(questions, propositions):
        print(f"{question}{proposition}")
        answer: int = int(input("Ta réponse: "))
        user_answers.append(answer)
    return user_answers


# Compare user's answers with correct answers stored in quizz_data, and create a list of that comparison results
def compare_score_answers(user_answers: list, index_correct_answers: list) -> list:
    comparison: list = [
        "Correct" if int(user) == int(correct) else "Wrong"
        for user, correct in zip(user_answers, index_correct_answers)
    ]
    return comparison


# Display results to user
def display_results(
    score: list, user_answers: list, index_correct_answers: list, text_answers: list
) -> None:
    for i in range(len(user_answers)):
        print(
            f"For question N°{i +1}, correct answer was {index_correct_answers[i]} ({text_answers[i]})."
            f"You answered {user_answers[i]} → {'✅' if score[i] == "Correct" else '❌'}"
        )
    print(f"----\nTotal score: {score.count("Correct")}/{len(score)}")


# MAIN LOGIC OF GAME
def quizz_game() -> None:
    quizz_size: int = ask_size_quizz()
    quizz_data: list = read_csv_data(filepath="quizz_game_data.csv")
    current_quizz_data: list = sub_quizz_data(quizz_data=quizz_data, size=quizz_size)
    questions, propositions, index_correct_answers, text_answers = parse_dict_data(
        dict_data=current_quizz_data
    )
    user_answers: list = ask_questions_store_answers(
        questions=questions, propositions=propositions
    )
    print(user_answers)
    user_scoring: list = compare_score_answers(
        user_answers=user_answers, index_correct_answers=index_correct_answers
    )
    display_results(
        score=user_scoring,
        user_answers=user_answers,
        index_correct_answers=index_correct_answers,
        text_answers=text_answers,
    )


quizz_game()
