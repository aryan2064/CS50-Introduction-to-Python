exp = input("Expression: ").strip()

op1, sign, op2 = exp.split()

op1 = int(op1)
op2 = int(op2)

match sign:
    case "+":
        result = op1 + op2
    case "-":
        result = op1 - op2
    case "*":
        result = op1 * op2
    case "/":
        result = op1 / op2

print(f"{result:.1f}")
