"""Practice exercise: analyze a collection of scores."""

def score_analyzer(scores):
    # length of score list
    score_length = len(scores)

    
    sum_score = 0
    highest_score = max(scores)
    lowest_score = min(scores)
    student_pass = 0
    student_fail = 0

    for score in scores:
        sum_score += score

        if score >= 50:
            student_pass +=1
            # return pass_
        else:
            student_fail +=1
            # return fail

    #highest score
    print(f"Highest score: {highest_score}")

    # lowest score
    print(f"Lowest score: {lowest_score}")

    # Number of students who passed
    print(f"Number of students who passed: {student_pass}")

    # Number of students who failed
    print(f"Number of students who passed: {student_fail}")

    
    # average score
    average_score = sum_score / score_length
    print(f"Average score: {average_score}")

scores = [76, 45, 89, 92, 67, 54, 100, 33]

if __name__ == "__main__":
    score_analyzer(scores)
