# A* 8-Puzzle using Misplaced Tiles Heuristic
# Blank tile is represented by 0 internally
# but displayed as _

def misplaced_tiles(state, goal):
    count = 0

    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != goal[i][j]:
                count += 1

    return count


def get_neighbors(state):
    neighbors = []

    # Find blank (0)
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j

    moves = [
        (-1, 0),   # Up
        (1, 0),    # Down
        (0, -1),   # Left
        (0, 1)     # Right
    ]

    for dx, dy in moves:
        nx = x + dx
        ny = y + dy

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
    print("g =", g, " h =", h, " f =", f)
    print("State:")
    print_state(state)


def a_star(initial, goal):

    # OPEN list
    open_list = []

    # CLOSED set
    closed_list = set()

    # Initial values
    g = 0
    h = misplaced_tiles(initial, goal)
    f = g + h

    # (f, g, state, path)
    open_list.append((f, g, initial, []))

    step = 0

    print("\n========== A* TRACE ==========")

    while open_list:

        # Sort according to f
        open_list.sort(key=lambda x: x[0])

        # Select state with smallest f
        f, g, current, path = open_list.pop(0)

        current_tuple = state_to_tuple(current)

        # Skip already visited state
        if current_tuple in closed_list:
            continue

        closed_list.add(current_tuple)

        step += 1

        h = f - g

        # Print current step
        print_trace(step, current, g, h, f)

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
            new_h = misplaced_tiles(neighbor, goal)
            new_f = new_g + new_h

            print("\n  g =", new_g,
                  "h =", new_h,
                  "f =", new_f)

            print_state(neighbor)

            open_list.append(
                (new_f, new_g, neighbor, path + [current])
            )

    return None


# =====================================================
# INPUT
# =====================================================

print("Enter Initial State")
print("Use 0 for blank (_)")

initial = []

for i in range(3):
    row = list(map(int, input("Enter row: ").split()))
    initial.append(row)


print("\nEnter Goal State")
goal = []

for i in range(3):
    row = list(map(int, input("Enter row: ").split()))
    goal.append(row)


# =====================================================
# A* SEARCH
# =====================================================

solution = a_star(initial, goal)


# =====================================================
# FINAL SOLUTION
# =====================================================

if solution:

    print("\n\n========== FINAL SOLUTION ==========")

    print("Number of moves:", len(solution) - 1)

    for i, state in enumerate(solution):

        print("Step", i)

        print_state(state)

else:

    print("No solution found.")
