inputs = [
    "A",
    "B",
    "C",
]

for input in inputs:
    match input:
        case "A":
            data = "something A"
        case "B":
            data = "something B"
        case "C":
            data = "something C"

    print(data)
