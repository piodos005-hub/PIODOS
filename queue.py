
print("=== 4. FLEXIBLE INTERACTIVE QUEUE PROGRAM ===")
queue = []
valid_letters = ['P', 'I', 'O', 'D', 'O', 'S']


def display_q(q):
    if not q:
        return "EMPTY"
    return "FRONT -> " + " -> ".join(q) + " <- REAR"


print("Created an empty queue.")
print(f"Available letters you can use: {valid_letters}")

print("\n--- MANUAL ENQUEUE (Any Order) ---")
print("Type any letter from PIODOS to add to the rear. Type 'done' when finished.")
while True:
    val = input(f"Current Queue: {display_q(queue)}\nEnter letter to enqueue (or 'done'): ").strip().upper()

    if val == 'DONE':
        break
    if val in valid_letters:
        queue.append(val)
        print(f"-> Enqueued '{val}'")
    else:
        print(f"-> Invalid! Please choose from {valid_letters}")

print(f"\nFinal Queue before dequeuing: {display_q(queue)}")

print("\n--- MANUAL DEQUEUE (Choose letter to remove) ---")
print("Type any letter currently inside the queue to remove it.")

while len(queue) > 0:
    print(f"\nCurrent Queue: {display_q(queue)}")
    choice = input("Enter letter to dequeue (or 'q' to quit): ").strip().upper()

    if choice == 'Q':
        break

    if choice in queue:
        queue.remove(choice)
        print(f"-> Successfully removed '{choice}' from the queue.")
    else:
        print(f"-> Letter '{choice}' is not currently in the queue! Try again.")

print(f"\nDISPLAY: {display_q(queue)}")
print("STOP")