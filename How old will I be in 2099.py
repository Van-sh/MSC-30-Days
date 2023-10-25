def calculate_age(year_of_birth, current_year):
    diff = abs(current_year - year_of_birth)
    return (
        f"You are {diff} year{'s' if diff > 1 else ''} old."
        if current_year > year_of_birth
        else f"You will be born in {diff} year{'s' if diff > 1 else ''}."
        if year_of_birth > current_year
        else "You were born this very year!"
    )