from datetime import datetime

CURRENT_YEAR = datetime.now().year


def generate_profile(age: int) -> str:
    """Return life stage label for a given age."""
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


def get_user_input() -> None:
    """Collect user data interactively and prints the profile summary directly."""
    print(
        "Welcome to the Mini Profile Generator!\n"
        "Please provide the following information."
    )

    user_name = get_name()
    birth_year_str = get_birth_year()
    birth_year = int(birth_year_str)
    current_age = calculate_age(birth_year)

    hobbies = []
    while True:
        hobby = input("Enter a favorite hobby or type 'stop' to finish: ").strip()
        if hobby.lower() == 'stop':
            break
        elif any(char.isdigit() for char in hobby):
            print("Hobby cannot contain numbers. Please try again.")
            continue
        elif not hobby:
            print("Hobby cannot be empty. Please try again.")
            continue
        elif hobby in hobbies:
            print("You've already added this hobby. Please try a different one.")
            continue
        else:
            hobbies.append(hobby.lower().title())

    life_stage = generate_profile(current_age)

    user_profile = {
        "Name": user_name,
        "Age": current_age,
        "Life Stage": life_stage,
        "Favorite Hobbies": hobbies
    }

    print_profile_summary(user_profile)


def get_name(prompt: str = "Enter your full name: ") -> str:
    """
    Prompt for a full name, strip surrounding whitespace and validate.
    Accepts letters, spaces, hyphens and apostrophes. Returns title-cased name.
    """
    allowed_chars = set(" -'")  # space, hyphen, apostrophe
    while True:
        name = input(prompt).strip()
        if not name:
            print("Name cannot be empty. Please try again.")
            continue
        elif any(char.isdigit() for char in name):
            print("Name cannot contain numbers. Please try again.")
            continue
        elif any(char not in allowed_chars and not char.isalpha() for char in name):
            print("Name contains invalid characters. Use letters, spaces, hyphens or apostrophes. Please try again.")
            continue

        return name.title()


def get_birth_year(prompt: str = "Enter your birth year: ") -> str:
    """
    Prompt for a birth year and return it as a string.
    Valid range: 1900 - current year.
    """
    while True:
        try:
            birth_year = int(input(prompt).strip())
        except ValueError:
            print("Invalid input. Please enter a numeric year.")
            continue
        if birth_year < 1900 or birth_year > CURRENT_YEAR:
            print("Please enter a valid birth year.")
            continue
        return str(birth_year)


def calculate_age(birth_year: int) -> int:
    """
    Calculate age from a birth year relative to current year.
    """
    return CURRENT_YEAR - birth_year


def print_profile_summary(profile) -> None:
    """Prints a formatted profile summary from the provided profile dictionary."""
    separator = "-" * 3
    print(f"{separator}\nProfile Summary:")

    for key, value in profile.items():
        if key == "Favorite Hobbies":
            if not value:
                print(f"You didn't mention any hobbies.")
            else:
                print(f"Favorite Hobbies ({len(value)}):")
                for hobbies in value:
                    print(f"- {hobbies}")
        else:
            print(f"{key}: {value}")

    print(f"{separator}")


if __name__ == "__main__":
    get_user_input()
