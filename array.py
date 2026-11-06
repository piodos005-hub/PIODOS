
print("=== 1. INTERACTIVE ARRAY PROGRAM ===")
my_array = []
print("Created an empty array.")

print("\n--- MANUAL INSERTION ---")
print("Type letters one by one. Type 'done' when you are finished.")
while True:
    val = input("Enter letter to append: ").strip()
    if val.lower() == 'done':
        break
    if val:
        my_array.append(val)
        print(f"Current Array: {my_array}")

print(f"\nFinal Array before deletion: {my_array}")

print("\n--- MANUAL DELETION ---")
print("Press Enter to remove elements one by one from the start, or type 'q' to quit.")
while len(my_array) > 0:
    action = input(f"Current array: {my_array}. Press Enter to remove next element: ")
    if action.lower() == 'q':
        break
    removed = my_array.pop(0)
    print(f"Removed: {removed}")

print(f"\nFinal Array after deletion: {my_array if my_array else '[] (empty array)'}")
print("STOP")