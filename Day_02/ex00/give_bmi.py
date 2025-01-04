def give_bmi(height: list[float], weight: list[float]) -> list[float]:
    """
    Calculate BMI from height (m) and weight (kg) using basic arithmetic.
    """
    if not all(isinstance(h, (int, float)) for h in height) or not all(isinstance(w, (int, float)) for w in weight):
        raise ValueError("Height and weight must be lists of numbers.")
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must be of the same length.")

    bmi = []
    for h, w in zip(height, weight):
        bmi.append(w / (h ** 2))  # BMI formula: weight (kg) / height (m)^2
    return bmi


def apply_limit(bmi: list[float], limit: int) -> list[bool]:
    """
    Check if BMI values exceed a given limit using basic Python lists.
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise ValueError("BMI must be a list of numbers.")

    result = []
    for b in bmi:
        result.append(b > limit)  # True if BMI > limit
    return result


def main():
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))  # Expected: [22.507863455018317, 29.0359168241966]
    print(apply_limit(bmi, 26))  # Expected: [False, True]

if __name__ == "__main__":
    main()
