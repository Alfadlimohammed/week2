name = "Your Name"
address = "Your Address"
contact_details = "Your Contact Details"
print("Name:", name)
print("Address:", address)
print("Contact Details:", contact_details)
name_length = len(name)
print("Length of Name:", name_length)
if __name__ == '__main__':
    age = input("Enter your age: ")
    age = int(age)
    print("In one year, you will be", age + 1)
if __name__ == '__main__':
    # Prompt the user to input two numeric values
    num1 = float(input("Enter the first numeric value: "))
    num2 = float(input("Enter the second numeric value: "))
    product = num1 * num2
    print("The product of", num1, "and", num2, "is:", product)
if __name__ == '__main__':
    print("\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\nHello there!\n\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\n")
if __name__ == '__main__':
    surname = "Palin"
    third_letter = surname[2]
    print("The third letter of the surname is:", third_letter)
if __name__ == '__main__':
    surname = "Palin"
    last_letter = surname[-1]
    print("The last letter of the surname is:", last_letter)
if __name__ == '__main__':
    surname = "Palin"
    second_last_letter = surname[-2]
    print("The second-to-last letter of the surname is:", second_last_letter)
if __name__ == '__main__':
    surname = "Palin"
    tail = surname[1:]
    print("All characters of the surname except the first one:", tail)
if __name__ == '__main__':
    surname = "Palin"
    all_except_last = surname[:-1]
    print("All characters of the surname except the last one:", all_except_last)
if __name__ == '__main__':
    surname = "Palin"
    all_except_last = surname[:-3]
    print("All characters of the surname except the last one:", all_except_last)
if __name__ == '__main__':
    surname = "Palin"
    all_except_last = surname[1:10000]
    print("All characters of the surname except the last one:", all_except_last)
if __name__ == '__main__':
    primes = [2, 3, 5, 7, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    first_four_primes = primes[:4]
    print("The first four prime numbers are:", first_four_primes)
if __name__ == '__main__':
    names = ["Alice", "Bob", "Charlie", "David", "Eva"]
    new_name1 = "Frank"
    new_name2 = "Grace"
    names[-1:-1] = [new_name2, new_name1]
    print("Updated 'names' list after slicing:", names)
    names.append("Brian")
    print("Updated 'names' list after appending:", names)
if __name__ == '__main__':
    names = ["Alice", "Bob", "Charlie"]
    names = names + ["Mark"]
    print("Updated 'names' list after concatenation:", names)
if __name__ == '__main__':
    names = ["Alice", "Bob", "Charlie"]
    names += ["Jacob"]
    print("Updated 'names' list after using +=:", names)
if __name__ == '__main__':
    nums = [1, 2, 3] * 5
    print("Resulting list:", nums)