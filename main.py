import time
import numpy as np


def state_print(state, p, b, t):
    if t:
        if state == 0:
            print("|c*|  |  |  |  |t |")
        elif state == 1:
            print("|c | *|  |  |  |t |")
        elif state == 2:
            print("|c |  | *|  |  |t |")
        elif state == 3:
            print("|c |  |  | *|  |t |")
        elif state == 4:
            print("|c |  |  |  | *|t |")
        elif state == 5:
            print("|c |  |  |  |  |t*|")
        print("Robot point:", p, "Battery persentage:", b)
    else:
        if state == 0:
            print("|c*|  |  |  |  |  |")
        elif state == 1:
            print("|c | *|  |  |  |  |")
        elif state == 2:
            print("|c |  | *|  |  |  |")
        elif state == 3:
            print("|c |  |  | *|  |  |")
        elif state == 4:
            print("|c |  |  |  | *|  |")
        elif state == 5:
            print("|c |  |  |  |  | *|")
        print("Robot point:", p, "Battery persentage:", b)


def calculate_reward_table(battery, t):
    charging_reward = (100 - battery) / 10
    if t:
        table = [[0, charging_reward, 0],
                 [charging_reward, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 5],
                 [0, 5, 0]]
    else:
        table = [[0, charging_reward, 0],
                 [charging_reward, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0],
                 [0, 0, 0]]
    return table


def calculate_q_table(reward_t, gama):
    table = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]
    for _ in range(len(reward_t)):
        for i in range(len(reward_t)):
            for j in range(len(reward_t[i])):
                if j == 0 and i != 0:
                    table[i][j] = reward_t[i][j] + gama * max(table[i - 1])
                elif (j == 1) or (j == 0 and i == 0) or (j == 2 and i == len(reward_t) - 1):
                    table[i][j] = reward_t[i][j] + gama * max(table[i])
                elif j == 2:
                    table[i][j] = reward_t[i][j] + gama * max(table[i + 1])
    return table


if __name__ == '__main__':
    gama = 0.5
    actions = ["left", "stay", "right"]
    states = [0, 1, 2, 3, 4, 5]
    point = 0
    current_state = 4
    battery_percentage = 30
    trash = True
    print("Guide: robot location= '*', charging station: 'c', trash: 't'")
    while True:
        if current_state == 0:
            battery_percentage += 10
            if battery_percentage > 100:
                battery_percentage = 100
            trash = True
            point += 1
        else:
            battery_percentage -= 5

        state_print(current_state, point, battery_percentage, trash)

        if battery_percentage <= 0 and current_state != 0:
            print("Robot shuting down Goodbye!")
            break

        reward_table = calculate_reward_table(battery_percentage, trash)
        q = calculate_q_table(reward_table, gama)
        # for i in q:
        #     print(i)

        best_action = np.argmax(q[current_state])

        if actions[best_action] == "left":
            current_state += -1
        elif actions[best_action] == "right":
            current_state += 1
        if current_state == 5:
            trash = False
            point += 5


        time.sleep(1)
