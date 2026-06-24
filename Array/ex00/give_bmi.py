def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    "This function takes two lists of height and weight values, and returns a list of BMI values calculated from them."
    if len(height) != len(weight) or type(height) is not list[int | float] or type(weight) is not list[int | float]:
        raise ValueError("Height and weight lists must be of the same length and same type.")
    bmi: list[int | float] = []
    for h, w in zip(height, weight):
        if h <= 0:
            raise ValueError("Height must be greater than zero.")
        bmi.append(w / (h ** 2))
    return bmi

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    "This function takes a list of BMI values and a limit, and returns a list of booleans indicating whether each BMI value exceeds the limit."
    if limit <= 0:
        raise ValueError("Limit must be greater than zero.")
    if not bmi:
        raise ValueError("BMI list cannot be empty.")
    return [b > limit for b in bmi]

def main():
    try:
        height = [2.71, 1.15, -1.0, 1.75]
        weight = [165.3, 38.4, 72.6, 58.9]
        bmi = give_bmi(height, weight)
        print(bmi, type(bmi))
        print(apply_limit(bmi, 26))
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
