import re


def explain_line(line, context):
    line = line.strip()

    # if condition
    if line.startswith("if "):
        condition = line[3:].rstrip(":")

        return {
            "what": f"This line checks whether {condition}.",
            "why": "The condition controls whether the code inside this block should run.",
            "parts": explain_condition(condition),
            "simple": f"Check whether {condition}."
        }

    # return statement
    if line.startswith("return "):
        value = line[7:].strip()

        return {
            "what": f"This line returns {value} from the current function.",
            "why": "The function uses this statement to send a result back to the code that called it.",
            "parts": [
                "return → sends a value back from the function",
                f"{value} → the value being returned"
            ],
            "simple": f"Give back {value}."
        }

    # for loop
    if line.startswith("for "):
        return {
            "what": "This line starts a loop that repeatedly executes the indented code below it.",
            "why": "The loop allows the program to perform the same operation for multiple values.",
            "parts": [
                "for → starts a loop",
                "The loop variable → represents the current value",
                "The iterable → provides the values to process"
            ],
            "simple": "Repeat this operation for each value."
        }

    # function definition
    if line.startswith("def "):
        match = re.match(r"def\s+(\w+)\((.*?)\):", line)

        if match:
            name = match.group(1)
            parameters = match.group(2)

            return {
                "what": f"This line defines a function named {name}.",
                "why": "Functions group related instructions together so they can be reused.",
                "parts": [
                    "def → defines a function",
                    f"{name} → function name",
                    f"{parameters or 'no parameters'} → input values accepted by the function"
                ],
                "simple": f"Create a function called {name}."
            }

    # assignment
    if "=" in line and not line.startswith(("==", ">=", "<=", "!=")):
        variable, value = line.split("=", 1)

        return {
            "what": f"This line assigns {value.strip()} to {variable.strip()}.",
            "why": "The assignment stores a value so the program can use it later.",
            "parts": [
                f"{variable.strip()} → variable receiving the value",
                "= → assignment operator",
                f"{value.strip()} → value being assigned"
            ],
            "simple": f"Store {value.strip()} in {variable.strip()}."
        }

    # fallback
    return {
        "what": f"This line executes: {line}",
        "why": "This line contributes to the program's overall logic.",
        "parts": [
            "CodeLens has identified the selected line."
        ],
        "simple": "This line is part of the program's logic."
    }


def explain_condition(condition):
    parts = []

    if "%" in condition:
        parts.append("% → remainder operator")

    if "==" in condition:
        parts.append("== → checks whether two values are equal")

    if "!=" in condition:
        parts.append("!= → checks whether two values are different")

    if ">=" in condition:
        parts.append(">= → checks whether the left value is greater than or equal to the right")

    if "<=" in condition:
        parts.append("<= → checks whether the left value is less than or equal to the right")

    if ">" in condition and ">=" not in condition:
        parts.append("> → checks whether the left value is greater than the right")

    if "<" in condition and "<=" not in condition:
        parts.append("< → checks whether the left value is less than the right")

    if not parts:
        parts.append(f"{condition} → the condition being tested")

    return parts