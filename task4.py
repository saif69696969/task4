# ==========================================
# TASK 4: List Operations
# ==========================================

# Question 1: Smallest Number in List
print("--- Question 1: Smallest Number ---")
my_list = [3, 1, 0, 9, 5, 2, 6, 4, 9, 8, 7]
smallest = my_list[0]
for num in my_list:
    if num < smallest:
        smallest = num
print("Smallest number:", smallest)

# Question 2: Average of List
print("\n--- Question 2: Average of List ---")
total_sum = 0
for num in my_list:
    total_sum += num
average = total_sum / len(my_list)
print(f"Average: {average:.2f}")

# Question 3: Search Student
print("\n--- Question 3: Student Search ---")
students = ["Ali", "Ahmed", "Sara", "Ayesha", "Bilal"]
search_name = input("Enter student name to search: ").strip()
found = any(s.lower() == search_name.lower() for s in students)
print("Student Found" if found else "Student Not Found")

# Question 4: Shopping List
print("\n--- Question 4: Shopping List ---")
shopping = []
print("Enter 5 shopping items:")
for i in range(1, 6):
    shopping.append(input(f"Item {i}: ").strip())
print("\nComplete Shopping List:", shopping)