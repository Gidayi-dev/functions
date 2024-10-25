def life_in_weeks(age):
    # Calculate the total weeks in 90 years
    total_weeks = 90 * 52
    # Calculate the weeks lived so far
    weeks_lived = age * 52
    # Calculate the weeks left
    weeks_left = total_weeks - weeks_lived
    # Print the result with proper formatting
    print(f"You have {weeks_left} weeks left.")

# Call your function with hard-coded values
life_in_weeks(56)