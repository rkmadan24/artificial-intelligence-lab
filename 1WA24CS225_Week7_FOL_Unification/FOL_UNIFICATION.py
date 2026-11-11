
def is_variable(x):
    return isinstance(x, str) and x.islower()


def apply_substitution(x, subst):
    if isinstance(x, str) and x in subst:
        return apply_substitution(subst[x], subst)

    if isinstance(x, tuple):
        return tuple(apply_substitution(i, subst) for i in x)

    return x


def occurs_check(var, term, subst):
    term = apply_substitution(term, subst)

    if var == term:
        return True

    if isinstance(term, tuple):
        return any(occurs_check(var, i, subst) for i in term)

    return False


def unify(x, y, subst):
    x = apply_substitution(x, subst)
    y = apply_substitution(y, subst)

    if x == y:
        return subst

    if is_variable(x):
        if occurs_check(x, y, subst):
            return None

        subst[x] = y
        return subst

    if is_variable(y):
        if occurs_check(y, x, subst):
            return None

        subst[y] = x
        return subst

    if isinstance(x, tuple) and isinstance(y, tuple):

        if x[0] != y[0] or len(x) != len(y):
            return None

        for a, b in zip(x[1:], y[1:]):
            subst = unify(a, b, subst)

            if subst is None:
                return None

        return subst

    return None


def convert(p):
    name, args = p.split("(", 1)
    args = args.rstrip(")")
    return tuple([name.strip()] +
                 [a.strip() for a in args.split(",")])


# Main Program
print("UNIFICATION IN FIRST ORDER LOGIC")

p1 = input("Enter first predicate: ")
p2 = input("Enter second predicate: ")

try:
    expr1 = convert(p1)
    expr2 = convert(p2)

    result = unify(expr1, expr2, {})

    if result is not None:
        print("\nUnification Successful")
        print("Substitution:", result)
    else:
        print("\nUnification Failed")

except (ValueError, IndexError):
    print("Invalid Input")
