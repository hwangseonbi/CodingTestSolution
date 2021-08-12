"""
https://programmers.co.kr/learn/courses/30/lessons/81303
"""

PREV = "PREV"
NEXT = "NEXT"
CANCELED = "CANCELED"
ID = "ID"
def solution(n, k, cmd):
    answer = ''

    table = []
    for i in range(n):
        if i == 0:
            table.append({
                ID: i,
                PREV: i,
                NEXT: i + 1,
                CANCELED: False
            })
        elif i == n-1:
            table.append({
                ID:i,
                PREV: i - 1,
                NEXT: i,
                CANCELED: False
            })
        else:
            table.append({
                ID: i,
                PREV: i - 1,
                NEXT: i + 1,
                CANCELED: False
            })
    undo_stack = []

    current_id = k
    for c in cmd:
        if c.split()[0] == 'D':
            d = int(c.split()[1])
            while d > 0:
                current_id = table[current_id].get(NEXT)
                d -= 1

        elif c.split()[0] == 'U':
            d = int(c.split()[1])
            while d > 0:
                current_id = table[current_id].get(PREV)
                d -= 1

        elif c.split()[0] == 'C':

            undo_stack.append(current_id)
            table[current_id][CANCELED] = True
            if table[current_id].get(PREV) == current_id:
                #id가 처음일때
                table[table[current_id].get(NEXT)][PREV] = table[table[current_id].get(NEXT)][ID]
                current_id = table[table[current_id].get(NEXT)][ID]
            elif table[current_id].get(NEXT) == current_id:
                #id가 마지막일떄
                table[table[current_id].get(PREV)][NEXT] = table[table[current_id].get(PREV)][ID]
                current_id = table[table[current_id].get(PREV)][ID]
            else:
                table[table[current_id].get(PREV)][NEXT] = table[current_id].get(NEXT)
                table[table[current_id].get(NEXT)][PREV] = table[current_id].get(PREV)
                current_id = table[current_id].get(NEXT)



        elif c.split()[0] == 'Z':
            restore_id = undo_stack.pop(-1)
            table[restore_id][CANCELED] = False
            if table[restore_id].get(NEXT) == restore_id:
                #마지막
                table[table[restore_id].get(PREV)][NEXT] = restore_id
            elif table[restore_id].get(PREV) == restore_id:
                #첫번째
                table[table[restore_id].get(NEXT)][PREV] = restore_id
            else:
                table[table[restore_id].get(NEXT)][PREV] = restore_id
                table[table[restore_id].get(PREV)][NEXT] = restore_id

        else:
            raise Exception("Unsupported Cmd")



    for info in table:
        if info[CANCELED]:
            answer += "X"
        else:
            answer += "O"
    # print(answer)
    return answer


# assert solution(8, 2, ["D 2", "C", "U 1", "Z", "D 1", "D 1", "D 1"]) == "OOOOXOOO"

assert solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z"]) == "OOOOXOOO"
assert solution(8,2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]) == "OOXOXOOO"
