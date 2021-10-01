from copy import deepcopy


def solution(tickets):
    answer = []
    tickets_dict = {}
    for ticket in tickets:
        if ticket[0] not in tickets_dict:
            tickets_dict[ticket[0]] = []
        if ticket[1] not in tickets_dict:
            tickets_dict[ticket[1]] = []

        tickets_dict[ticket[0]].append(ticket[1])
    for k, v in tickets_dict.items():
        v.sort()

    stack = [("ICN", ["ICN"], deepcopy(tickets_dict))]
    while stack:
        cur, routes, rest = stack.pop(0)
        if len(rest[cur]) > 0:
            for i, next_cur in enumerate(rest[cur]):
                new_rest = deepcopy(rest)
                new_rest[cur].pop(i)
                stack.append((next_cur, routes + [next_cur], new_rest))

        if len(routes) == len(tickets) + 1:
            answer = routes
            break

    return answer


assert solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]) == ["ICN", "JFK", "HND", "IAD"]
assert solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]) == ["ICN", "ATL",
                                                                                                      "ICN", "SFO",
                                                                                                      "ATL", "SFO"]
