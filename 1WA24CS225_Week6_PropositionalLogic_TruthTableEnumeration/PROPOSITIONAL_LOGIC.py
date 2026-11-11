
from itertools import product

# Evaluate logical expression
def evaluate(expr, model):
    return eval(expr, {"__builtins__": {}}, model)


# Truth Table Enumeration
def TT_ENTAILS(KB, query, symbols):

    for values in product([True, False], repeat=len(symbols)):

        model = dict(zip(symbols, values))

        kb_true = all(evaluate(s, model) for s in KB)

        if kb_true:
            if not evaluate(query, model):
                return False

    return True


# Main Program
n = int(input("Enter number of propositions: "))

symbols = []

for i in range(n):
    symbols.append(input("Enter proposition: "))

m = int(input("Enter number of KB sentences: "))

KB = []

for i in range(m):
    KB.append(input("Enter KB sentence: "))

query = input("Enter query: ")

# Display Truth Table
print("\nTruth Table")

for values in product([True, False], repeat=n):
    model = dict(zip(symbols, values))

    kb_result = all(evaluate(s, model) for s in KB)
    query_result = evaluate(query, model)

    print(model, "KB:", kb_result,
          "Query:", query_result)

# Check entailment
if TT_ENTAILS(KB, query, symbols):
    print("\nKB entails the Query")
else:
    print("\nKB does not entail the Query")
