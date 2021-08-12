"""
https://programmers.co.kr/learn/courses/30/lessons/72414
"""


def convert_to_seconds(time_str):
    h, m, s = map(int, time_str.split(":"))
    return h * 60 * 60 + m * 60 + s


def convert_to_str(time_seconds):
    total_m, s = divmod(time_seconds, 60)
    h, m = divmod(total_m, 60)
    return "{0:02d}".format(h) + ":" + "{0:02d}".format(m) + ":" + "{0:02d}".format(s)



def solution(play_time, adv_time, logs):
    answer = 0
    adv_time = convert_to_seconds(adv_time)
    play_time = convert_to_seconds(play_time)
    play_statics = [0 for _ in range(play_time+1)]


    for log in logs:
        log_start, log_end = tuple(map(convert_to_seconds, log.split("-")))
        play_statics[log_start] += 1
        if log_end + 1 < play_time:
            play_statics[log_end + 1] -= 1

    v = 0
    for i, d in enumerate(play_statics):
        v = v + d
        play_statics[i] = v

    # print(play_statics)
    start_time = 0
    end_time = start_time + adv_time
    adv_cc_duration = sum(play_statics[start_time:adv_time])
    # print(adv_cc_duration)
    # print(f'{convert_to_str(start_time)} - {convert_to_str(end_time)}')

    max_adv_cc_duration = 0
    while True:
        if end_time + 1 > play_time:
            break
        adv_cc_duration = adv_cc_duration - play_statics[start_time] + play_statics[end_time+1]

        start_time += 1
        end_time += 1


        if max_adv_cc_duration < adv_cc_duration:
            # print(f'[{adv_cc_duration}]{convert_to_str(start_time)} - {convert_to_str(end_time)}')
            max_adv_cc_duration = adv_cc_duration
            answer = start_time
    return convert_to_str(answer)

TEST_CASES = [
    {
        "play_time": "00:00:10",
        "adv_time": "00:00:04",
        "logs": ["00:00:01-00:00:05", "00:00:02-00:00:06","00:00:04-00:00:07",
                 "00:00:07-00:00:10","00:00:08-00:00:10","00:00:09-00:00:10", "00:00:09-00:00:10"],
        "result": "00:00:06"
    },
    # {
    #     "play_time": "02:03:55",
    #     "adv_time": "00:14:15",
    #     "logs": ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29",
    #              "01:37:44-02:02:30"],
    #     "result": "01:30:59"
    # },
    # {
    #     "play_time": "99:59:59",
    #     "adv_time": "25:00:00",
    #     "logs": ["69:59:59-89:59:59", "01:00:00-21:00:00", "79:59:59-99:59:59", "11:00:00-31:00:00"],
    #     "result": "01:00:00"
    # },{
    #     "play_time": "50:00:00",
    #     "adv_time": "50:00:00",
    #     "logs": ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"],
    #     "result": "00:00:00"
    # },
]
