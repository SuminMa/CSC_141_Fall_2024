# 8-11. Archived Messages

# Start with my work from Exercise 8-10.
texts = ['Hi.', 'How are you?', 'How have you been?', 'I love you.']
send_message = []

def send_messages(texts):
    while texts:
        current_message = texts.pop()
        print(current_message)
        send_message.append(current_message)

# Call the function send_mssages() with a copy of list of messages.
send_messages(texts[:])
print() # Add a new line

# Print both of my lists to show that the original list has retained its messages.
print(texts)
print(send_message)