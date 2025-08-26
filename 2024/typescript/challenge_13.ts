const INVERSION_MAP: Record<string, string> = {
    "L": "R", 
    "R": "L", 
    "U": "D", 
    "D": "U"
};

const OPERATIONS = ["!", "*", "?"] as const;

type Operation = typeof OPERATIONS[number];

function isRobotBack(moves: string): boolean | [number, number] {
    const movsDone = new Set<string>();
    let x = 0, y = 0; // start position

    let opt: Operation | "" = "";
    
    for (let idx = 0; idx < moves.length; idx++) {
        let numExecutions = 1;
        let move = moves[idx];

        if (OPERATIONS.includes(move as Operation)) {
            opt = move as Operation;
            continue;
        } else {
            switch (opt) {
                case "!":
                    move = INVERSION_MAP[move];
                    break;
                case "*":
                    numExecutions = 2;
                    break;
                case "?":
                    if (movsDone.has(move)) {
                        numExecutions = 0;
                    }
                    break;
            }
            opt = "";
        }

        for (let i = 0; i < numExecutions; i++) {
            switch (move) {
                case "L":
                    x -= 1;
                    break;
                case "R":
                    x += 1;
                    break;
                case "U":
                    y += 1;
                    break;
                case "D":
                    y -= 1;
                    break;
            }
            movsDone.add(move);
        }
    }

    return (x === 0 && y === 0) ? true : [x, y];
}

console.log(isRobotBack('R'));        // [1, 0]
console.log(isRobotBack('RL'));       // true
console.log(isRobotBack('RLUD'));     // true
console.log(isRobotBack('*RU'));      // [2, 1]
console.log(isRobotBack('R*U'));      // [1, 2]
console.log(isRobotBack('LLL!R'));    // [-4, 0]
console.log(isRobotBack('R?R'));      // [1, 0]
console.log(isRobotBack('U?D'));      // true
console.log(isRobotBack('R!L'));      // [2, 0]
console.log(isRobotBack('U!D'));      // [0, 2]
console.log(isRobotBack('R!U?U'));    // [1, 0]
console.log(isRobotBack('UU!U?D'));   // [0, 1]
