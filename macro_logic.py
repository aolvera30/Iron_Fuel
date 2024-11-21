def calculate_macros(weight_lbs, height_feet, height_inches, age, gender, activity_level, goal):
    # Convert weight from lbs to kg, height from feet+inches to cm
    weight_kg = weight_lbs * 0.453592
    height_cm = (height_feet * 12 + height_inches) * 2.54

    # Step 1: Calculate BMR using Mifflin-St Jeor Equation
    if gender == 'male':
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161
    
    # Step 2: Calculate TDEE
    activity_factors = {
        'sedentary': 1.2,
        'lightly_active': 1.375,
        'moderately_active': 1.55,
        'very_active': 1.725,
        'super_active': 1.9
    }
    tdee = bmr * activity_factors[activity_level]
    
    # Step 3: Adjust calories based on goal
    if goal == 'lose_fat':
        daily_calories = tdee - 500
    elif goal == 'build_muscle':
        daily_calories = tdee + 250
    else:
        daily_calories = tdee  # maintain weight
    
    # Step 4: Calculate Macros
    # Protein: 2.0 grams per kg of body weight
    protein_grams = weight_kg * 2.0
    protein_calories = protein_grams * 4  # 1g protein = 4 kcal
    
    # Fat: 25% of total daily calories
    fat_calories = daily_calories * 0.25
    fat_grams = fat_calories / 9  # 1g fat = 9 kcal
    
    # Carbs: Remaining calories
    remaining_calories = daily_calories - (protein_calories + fat_calories)
    carbs_grams = remaining_calories / 4  # 1g carbohydrate = 4 kcal
    
    # Return the calculated macros
    return {
        'calories': daily_calories,
        'protein_grams': protein_grams,
        'fat_grams': fat_grams,
        'carbs_grams': carbs_grams
    }

# Example usage
macros = calculate_macros(weight_lbs=154, height_feet=5, height_inches=9, age=25, gender='male', activity_level='moderately_active', goal='lose_fat')
print(macros)