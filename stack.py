
print("=== 3. INTERACTIVE STACK PROGRAM (LIFO) ===")
stack = []
print("Created an empty stack.")

print("\n--- MANUAL PUSH ---")
print("Type letters one by one. Type 'done' when you are finished.")
while True:
    val = input("Enter letter to push: ").strip()
    if val.lower() == 'done':
        break
    if val:
        stack.append(val)
        top_to_bottom = list(reversed(stack))
        print(f"Stack (Top to Bottom): {', '.join(top_to_bottom)}")

top_to_bottom = list(reversed(stack))
print(f"\nStack before popping (Top to Bottom): {', '.join(top_to_bottom)}")

print("\n--- MANUAL POP ---")
while len(stack) > 0:
    top_to_bottom = list(reversed(stack))
    input(f"Current stack top: {top_to_bottom[0]}. Press Enter to pop: ")
    popped = stack.pop()
    print(f"Popped: {popped}")

print("\nDISPLAY: EMPTY")
print("Final Stack after popping: EMPTY")
print("STOP")