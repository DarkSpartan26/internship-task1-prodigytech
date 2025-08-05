import string

def check_password_strength(password):
    length_score = 0
    upper_score = 0
    lower_score = 0
    digit_score = 0
    symbol_score = 0

    # Check length
    if len(password) >= 12:
        length_score = 2
    elif len(password) >= 8:
        length_score = 1

    # Check for different character types
    if any(c.isupper() for c in password):
        upper_score = 1
    if any(c.islower() for c in password):
        lower_score = 1
    if any(c.isdigit() for c in password):
        digit_score = 1
    if any(c in string.punctuation for c in password):
        symbol_score = 1

    # Calculate total score out of 6
    total_score = length_score + upper_score + lower_score + digit_score + symbol_score

    # Strength description
    if total_score == 6:
        strength = "Very Strong 💪"
    elif total_score >= 4:
        strength = "Strong ✅"
    elif total_score == 3:
        strength = "Moderate ⚠️"
    else:
        strength = "Weak ❌"

    # Give feedback
    feedback = []
    if length_score == 0:
        feedback.append("Make your password at least 8 characters long.")
    elif length_score == 1:
        feedback.append("Consider using 12 or more characters for better security.")
    if upper_score == 0:
        feedback.append("Add at least one uppercase letter.")
    if lower_score == 0:
        feedback.append("Add at least one lowercase letter.")
    if digit_score == 0:
        feedback.append("Include at least one digit.")
    if symbol_score == 0:
        feedback.append("Include at least one special symbol (e.g. !, @, #, $).")

    return strength, total_score, feedback

# Input handling
if __name__ == "__main__":
    password = input("Enter your password: ")
    strength, score, feedback = check_password_strength(password)

    print(f"\nPassword Strength: {strength}")
    print(f"Score: {score}/6")
    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print(f"- {f}")