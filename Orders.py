from collections import deque

orders_queue = deque()

while True:
    action = input("Do you want to make (m) or process the order (p). To finish type (f?\n")
    if action == "m":
        order = input("Input order content\n")
        orders_queue.append(order)
        print("Order is registered\n")
    elif action == "p":
        order = orders_queue.popleft()
        #Process the order.....
        print("Order : " + order + " - processed\n")
    elif action == "f":
        break
    else:
        print("Wrong input\n")