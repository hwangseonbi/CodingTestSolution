def solution(participant, completion):
    answer = ''
    participant_dict = {}
    for p in participant:
        if p in participant_dict:
            participant_dict[p] += 1
        else:
            participant_dict.update({p: 1})
    for c in completion:
        if c in participant_dict:
            participant_dict[c] -= 1
            if participant_dict[c] < 1:
                participant_dict.pop(c)
    answer = list(participant_dict.keys())[0]
    return answer

TEST_CASES = [
    {
        "participant": ["leo", "kiki", "eden"],
        "completion": ["eden", "kiki"],
        "result": "leo"
    },
    {
        "participant": ["marina", "josipa", "nikola", "vinko", "filipa"],
        "completion": ["josipa", "filipa", "marina", "nikola"],
        "result": "vinko"
    },
    {
        "participant": ["mislav", "stanko", "mislav", "ana"],
        "completion": ["stanko", "ana", "mislav"],
        "result": "mislav"
    }
]
