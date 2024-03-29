num_strings = ['15', '100', '55', '42']
num_ints = [15, 100, 55, 42]
num_floats = [2.2, 5.0, 1.245, 0.142857]
num_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("\t\tSummary Table")

print(f"\nThe variable num strings is a {type(num_strings)} ")
print(f"Its contains the elements: {num_strings}")
print(f"The element {num_strings[0]} is a {type(num_strings[0])}")

print(f"\nThe variable num strings is a {type(num_ints)} ")
print(f"Its contains the elements: {num_ints}")
print(f"The element {num_ints[0]} is a {type(num_ints[0])}")

print(f"\nThe variable num strings is a {type(num_floats)} ")
print(f"Its contains the elements: {num_floats}")
print(f"The element {num_floats[0]} is a {type(num_floats[0])}")

print(f"\nThe variable num strings is a {type(num_lists)} ")
print(f"Its contains the elements: {num_lists}")
print(f"The element {num_lists[0]} is a {type(num_lists[0])}")

num_strings.sort()
num_ints.sort()

print("\nNow sorting num_strings and num_ints...")
print(f"Sorted num_strings: {num_strings}")
print(f"Sorted num_ints: {num_ints}")
print("\nStings are sorted alphabetically while integers are sorted numerically!!!")
