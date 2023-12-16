user_name = input("Hello, what is your name? ")
print("Hello, " + user_name + ". Good to meet you!")
if __name__ == '__main__':
    celsius_temperature = float(input("Enter a temperature in Celsius: "))
    fahrenheit_temperature = (celsius_temperature * 9 / 5) + 32
    print(f"{celsius_temperature}C is equivalent to {fahrenheit_temperature}F.")
if __name__ == '__main__':
    num_students = int(input("How many students? "))
    group_size = int(input("Required group size? "))
    num_groups = num_students // group_size
    students_left_over = num_students % group_size
    print(f"There will be {num_groups} groups with {students_left_over} students left over.")
if __name__ == '__main__':
    total_sweets = int(input("Enter the total number of sweets: "))
    num_pupils = int(input("Enter the number of pupils: "))
    sweets_per_pupil = total_sweets // num_pupils
    leftover_sweets = total_sweets % num_pupils
    print("Each pupil will receive", sweets_per_pupil, "sweets, and there will be", leftover_sweets,
          "sweets left over.")