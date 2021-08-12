N = int(input())


def solution():
    global N

    answer = 0

    for length in range(1, N + 1):
        for i in range(1,N+1):
            start = i
            end = i+length
            if end > N:
                continue
            # if (N[start]+N[end])/2

            # print(N[start]+N[end])

            if int((end-start+1)*(1+end)/2) == N:
                print(f'{start} - {end} - {(end - start + 1) * (1 + end) / 2}')
                answer += 1
    print(answer)





solution()
