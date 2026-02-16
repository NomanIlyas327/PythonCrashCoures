import time
if __name__ == "__main__":
    current_hour = time.localtime().tm_hour

    if 5 <= current_hour < 12:
        print("Good Morning, Sir!")
    elif 12 <= current_hour < 17:
        print("Good Afternoon, Sir!")
    elif 17 <= current_hour < 21:
        print("Good Evening, Sir!")
    else:
        print("Good Night, Sir!")
    

    #  other methods to greet based on time
    # Using 24-hour format
    if 0 <= current_hour < 6:
        greeting = "It's quite late, Sir. Good Night!"
    elif 6 <= current_hour < 12:
        greeting = "Wishing you a productive morning, Sir!"
    elif 12 <= current_hour < 18:
        greeting = "Hope you're having a great afternoon, Sir!"
    else:
        greeting = "Relax and unwind, Sir. Good Evening!"
    print(greeting)

    #  using time.strftime for more detailed greeting
    current_time = time.strftime("%H:%M:%S", time.localtime())
    print(f"Current time is {current_time}, Sir.")
    if current_hour < 12:
        print("Have a wonderful day ahead, Sir!")
    elif 12 <= current_hour < 18:
        print("Enjoy your afternoon, Sir!")
    else:
        print("Have a peaceful night, Sir!")

# change the seconds in terminal to see different greetings based on time

    #  using a dictionary to map time ranges to greetings
    greetings_dict = {
        (0, 6): "It's late night, Sir. Good Night!",
        (6, 12): "Good Morning, Sir! Rise and shine!",
        (12, 18): "Good Afternoon, Sir! Hope you're having a great day!",
        (18, 24): "Good Evening, Sir! Time to relax!"
    }
    for time_range, greet in greetings_dict.items():
        if time_range[0] <= current_hour < time_range[1]:
            print(greet)
            break
    #  using functions to encapsulate greeting logic
    def greet_based_on_time(hour):
        if 0 <= hour < 6:
            return "Good Night, Sir! Time to rest."
        elif 6 <= hour < 12:
            return "Good Morning, Sir! Have a great day ahead."
        elif 12 <= hour < 18:
            return "Good Afternoon, Sir! Keep up the good work."
        else:
            return "Good Evening, Sir! Unwind and relax."
    print(greet_based_on_time(current_hour))

    #  using ternary operator for a simple greeting
    simple_greeting = "Good Day, Sir!" if 6 <= current_hour < 18 else "Good Night, Sir!"
    print(simple_greeting)
    #  using time module to get more details
    current_minute = time.localtime().tm_min
    print(f"Current time is {current_hour}:{current_minute}, Sir.")
    if current_hour == 12 and current_minute == 0:
        print("It's noon, Sir! Time for lunch.")
    elif current_hour == 0 and current_minute == 0:
        print("It's midnight, Sir! A new day begins.")
    #  using formatted strings for personalized greeting
    formatted_greeting = f"Hello Sir, the current hour is {current_hour:02d}:00."
    print(formatted_greeting)
    if 5 <= current_hour < 12:
        print("Good Morning, Sir!")
    elif 12 <= current_hour < 17:
        print("Good Afternoon, Sir!")
    elif 17 <= current_hour < 21:
        print("Good Evening, Sir!")
    else:
        print("Good Night, Sir!")
    #  using a loop to demonstrate multiple greetings
    for hour in [6, 12, 18, 22]:
        if 5 <= hour < 12:
            print(f"At {hour}:00 - Good Morning, Sir!")
        elif 12 <= hour < 17:
            print(f"At {hour}:00 - Good Afternoon, Sir!")
        elif 17 <= hour < 21:
            print(f"At {hour}:00 - Good Evening, Sir!")
        else:
            print(f"At {hour}:00 - Good Night, Sir!")
    # End of Good Morning Sir program
    