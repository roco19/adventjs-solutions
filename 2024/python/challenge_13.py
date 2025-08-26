INVERSION_MAP = {"L": "R", "R": "L", "U": "D", "D": "U"}
OPERATIONS = ["!", "*", "?"]


# Challenge
def is_robot_back(moves: str) -> bool | list[int]:
    movs_done = set()
    x, y = 0, 0  # start position

    opt = ""
    for idx in range(len(moves)):
        num_executions = 1
        move = moves[idx]

        if move in OPERATIONS:
            opt = move
            continue

        else:
            match opt:
                case "!":
                    move = INVERSION_MAP[move]
                case "*":
                    num_executions = 2
                case "?":
                    if move in movs_done:
                        num_executions = 0
            opt = ""

        for i in range(num_executions):
            match move:
                case "L":
                    x -= 1
                case "R":
                    x += 1
                case "U":
                    y += 1
                case "D":
                    y -= 1
            movs_done.add(move)

    return True if (x, y) == (0, 0) else [x, y]


if __name__ == "__main__":
    print(is_robot_back("R"))
    print(is_robot_back("RL"))
    print(is_robot_back("RLUD"))
    print(is_robot_back("*RU"))
    print(is_robot_back("R*U"))
    print(is_robot_back("LLL!R"))
    print(is_robot_back("R?R"))
    print(is_robot_back("U?D"))
    print(is_robot_back("R!L"))
    print(is_robot_back("U!D"))
    print(is_robot_back("R?L"))
    print(is_robot_back("U?U"))
    print(is_robot_back("*U?U"))
    print(is_robot_back("U?D?U"))
