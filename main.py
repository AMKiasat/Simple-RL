import time


def state_print(state, p):
    if state == 0:
        print("|c | *|  |  |  |  |t |")
    elif state == 1:
        print("|c |  | *|  |  |  |t |")
    elif state == 2:
        print("|c |  |  | *|  |  |t |")
    elif state == 3:
        print("|c |  |  |  | *|  |t |")
    elif state == 4:
        print("|c |  |  |  |  | *|t |")
    elif state == 5:
        print("|c |  |  |  |  |  |t*|")
    print("Robot point:", p)


def reward(state, act, ):
    if state == 1 and act == "left":
        return 1
    if state == 4 and act == "right":
        return 5
    return 0


if __name__ == '__main__':
    actions = ["left", "right"]
    states = [0, 1, 2, 3, 4, 5]
    point = 0
    current_state = 1
    battery_percentage = 70
    print("Guide: robot location= '*', charging station: 'c', trash: 't'")
    while True:
        state_print(current_state, point)
        battery_percentage -= 5
        time.sleep(1)
