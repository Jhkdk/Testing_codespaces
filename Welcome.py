import os

width = os.get_terminal_size().columns
message = "You are currently in " + os.getcwd()
padding = (width - len(message)) // 2
print("-"*width)
print(" " * padding + message)
print("-"*width)