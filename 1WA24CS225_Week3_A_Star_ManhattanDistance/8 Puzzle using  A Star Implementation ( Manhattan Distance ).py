# A* 8-Puzzle using Manhattan Distance Heuristic
# 0 represents the blank space (_)


def manhattan_distance(state, goal):
    distance = 0

    for i in range(3):
        for j in range(3):

            tile = state[i][j]

            # Ignore blank
            if tile == 0:
                continue

            # Find tile position in goal
            for x in range(3):
                for y in range(3):

                    if goal[x][y] == tile:
                        distance += abs(i - x) + abs(j - y)

    return distance


def get_neighbors(state):
    neighbors = []

    # Find blank position
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x = i
                y = j

    # Possible movements
    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dx, dy in moves:

        nx = x + dx
        ny = y + dy

        # Check valid position
        if 0 <= nx < 3 and 0 <= ny < 3:

            new_state = [row[:] for row in state]

            # Move blank
            new_state[x][y], new_state[nx][ny] = \
                new_state[nx][ny], new_state[x][y]

            neighbors.append(new_state)

    return neighbors


def state_to_tuple(state):
    return tuple(tuple(row) for row in state)


def print_state(state):

    for row in state:

        for value in row:

            if value == 0:
                print("_", end=" ")
            else:
                print(value, end=" ")

        print()

    print()


def print_trace(step, state, g, h, f):

    print("--------------------------------")
    print("STEP:", step)

    print("g =", g)
    print("h =", h)
    print("f =", f)

    print("State:")

    print_state(state)


def a_star(initial, goal):

    open_list = []
    closed_list = set()

    # Initial state values
    g = 0
    h = manhattan_distance(initial, goal)
    f = g + h

    # Add initial state
    open_list.append(
        (f, g, initial, [])
    )

    step = 0

    print("\n========== A* MANHATTAN TRACE ==========")

    while open_list:

        # Select state with smallest f
        open_list.sort(key=lambda x: x[0])

        f, g, current, path = open_list.pop(0)

        current_tuple = state_to_tuple(current)

        # Ignore already visited states
        if current_tuple in closed_list:
            continue

        closed_list.add(current_tuple)

        step += 1

        h = manhattan_distance(current, goal)

        # Display current step
        print_trace(
            step,
            current,
            g,
            h,
            f
        )

        # Goal test
        if current == goal:

            print("GOAL REACHED!")
            print("Total moves:", g)

            return path + [current]

        # Generate neighbors
        print("Possible next states:")

        for neighbor in get_neighbors(current):

            neighbor_tuple = state_to_tuple(neighbor)

            if neighbor_tuple in closed_list:
                continue

            new_g = g + 1
            new_h = manhattan_distance(
                neighbor,
                goal
            )

            new_f = new_g + new_h

            print("\ng =", new_g,
                  "h =", new_h,
                  "f =", new_f)

            print_state(neighbor)

            open_list.append(
                (
                    new_f,
                    new_g,
                    neighbor,
                    path + [current]
                )
            )

    return None


# =====================================================
# INPUT INITIAL STATE
# =====================================================

print("Enter Initial State")
print("Use 0 for blank (_)")

initial = []

for i in range(3):

    row = list(
        map(
            int,
            input("Enter row: ").split()
        )
    )

    initial.append(row)


# =====================================================
# INPUT GOAL STATE
# =====================================================

print("\nEnter Goal State")

goal = []

for i in range(3):

    row = list(
        map(
            int,
            input("Enter row: ").split()
        )
    )

    goal.append(row)


# =====================================================
# A* SEARCH
# =====================================================

solution = a_star(
    initial,
    goal
)


# =====================================================
# DISPLAY FINAL SOLUTION
# =====================================================

if solution:

    print("\n\n========== FINAL SOLUTION ==========")

    print(
        "Number of moves:",
        len(solution) - 1
    )

    print("\nPath:")

    for i, state in enumerate(solution):

        print("Step", i)

        print_state(state)

else:

    print("No solution found.")
