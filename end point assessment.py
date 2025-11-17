# Subprograms
def steplogger(steps, stepgoal):
    percent_of_goal = round((steps/stepgoal) * 100, 2)
    remaining_steps = stepgoal - steps
    return int(percent_of_goal)


def bmicalc(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi > 18.5 and bmi < 25:
        return "Healthy"
    elif bmi > 25 and bmi < 30:
        return "Overweight"
    elif bmi > 30:
        return "Obese"
    
def flag_user(daily_screen_minutes, night_screen_minutes, steps):
    if daily_screen_minutes > 240 and steps < 5000:
        return True
    elif night_screen_minutes > 60:
        return True
    else:
        return False

def hydrationstreak(water_ml):
    singlepoints = water_ml // 250
    bonuspoints = water_ml // 2000
    totalpoints = singlepoints + bonuspoints*5
    return totalpoints  

def eligible_for_free_class(age,low_income,days_since_last_free):
    if age >= 16 and age <=25 and days_since_last_free > 30:
        return True
    elif low_income == "Y" and days_since_last_free > 30:
        return True
    else:
        return False

def weekly_tier(water_ml, steps):
    points = (steps // 1000) * 2 + (water_ml // 500)
    if points < 20:
        tier = "Bronze"
    elif points >= 20 and points < 40:
        tier = "Silver"
    elif points >= 40:
        tier = "Gold"
    return tier


def safe_average_minutes(total_minutes, sessions):
    if sessions > 0:
        avg = total_minutes / sessions
        return round(avg, 1)
    else:
        return 0
    
#night_screen_minutes = int(input("How many minutes of screentime have you had at night? "))
#daily_screen_minutes = int(input("How many minutes of screen time have you had today? "))
#steps = int(input("How many steps have you gotten today?: "))
#stepgoal = int(input("What is your step goal?"))
#age = int(input("How old are you? "))
#weight_kg = float(input("Enter your weight (in Kilograms): "))
#height_m = float(input("Enter your height (in Metres): "))
#water_ml = int(input("How much water have you drank (Millilitres): "))
#low_income = input("Are you registered as low-income? (Y/N): ")
#days_since_last_free = int(input("How many days has it been since you have received a free class? "))
#total_minutes = int(input("How many minutes of sessions have you done? "))
#sessions = int(input("How many sessions have you done? "))




# Mini program


def summary_line(steps,water_ml,daily_screen_minutes):
    percent_of_goal = steplogger(steps,stepgoal)
    totalpoints = hydrationstreak(water_ml)
    if daily_screen_minutes > 240:
        x = "High"
    else:
        x = "OK"
    print(f"Steps: {steps} ({percent_of_goal}% of goal), Water: {water_ml}, (+{totalpoints} pts), Screen: {daily_screen_minutes} mins - {x}")

summary_line(steps,water_ml,daily_screen_minutes)
    
    


    

    

