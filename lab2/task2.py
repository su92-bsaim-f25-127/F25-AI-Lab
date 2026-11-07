class ClassroomAgent:

    def __init__(self):
        self.previous_mode = None

    def act(self, temp, occupied):

        if not occupied:
            mode = "ECO"
        elif temp > 26:
            mode = "COOL"
        elif temp < 20:
            mode = "WARM"
        else:
            mode = "IDLE"

        if mode == self.previous_mode:
            command = "NO COMMAND"
        else:
            command = mode

        self.previous_mode = mode

        return mode, command


agent = ClassroomAgent()

percepts = [
    (29, True),
    (29, True),
    (20, True),
    (26, True),
    (19, True),
    (24, True),
    (18, False),
    (18, False),
    (28, True)
]

for step, percept in enumerate(percepts, 1):
    mode, command = agent.act(*percept)
    print(step, percept, mode, command)