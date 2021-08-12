def solution(answers):
    answer = []
    person_list = [
        [1, 2, 3, 4, 5],
        [2, 1, 2, 3, 2, 4, 2, 5],
        [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    ]
    person_score = []



    for person in person_list:
        score = 0
        for i, a in enumerate(answers):
            if a - person[i % len(person)] == 0:
                score += 1
        person_score.append(score)


    max_score = max(person_score)
    for i, score in enumerate(person_score):
        if score == max_score:
            answer.append(i+1)

    return answer

TEST_CASES = [
    {
        "answers": [1,2,3,4,5],
        "result": [1]
    },
    {
        "answers": [1,3,2,4,2],
        "result": [1,2,3]
    }
]