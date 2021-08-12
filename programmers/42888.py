"""
https://programmers.co.kr/learn/courses/30/lessons/42888
"""
ENTER = 0
LEAVE = 1

def solution(record):
    answer = []

    enter_leave_cmd = []
    user_info = {}
    for r in record:
        single_record = r.split()
        cmd = single_record[0]
        if cmd == "Enter":
            uid = single_record[1]
            nickname = single_record[2]

            user_info.update({
                uid: nickname
            })
            enter_leave_cmd.append((ENTER, uid))
        elif cmd == "Leave":
            uid = single_record[1]

            enter_leave_cmd.append((LEAVE, uid))
        elif cmd == "Change":
            uid = single_record[1]
            nickname = single_record[2]

            user_info[uid] = nickname

    for cmd, uid in enter_leave_cmd:
        if cmd == ENTER:
            answer.append(f"{user_info[uid]}님이 들어왔습니다.")
        elif cmd == LEAVE:
            answer.append(f"{user_info[uid]}님이 나갔습니다.")
    return answer


TEST_CASES = [
    {
        "record": ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"],
        "result": ["Prodo님이 들어왔습니다.", "Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]
    }
]
