# 8-10. Sending Messages

# Start with a copy of my program from Exercise 8-9.
texts = ['Hi.', 'How are you?', 'How have you been?', 'I love you.']
send_message = []

# Write a function called send_messages() that prints each text message.
# And moves each message to a new list called send_messages as it's printed.
def send_messages(texts):
    while texts:
        current_message = texts.pop()
        print(current_message)
        send_message.append(current_message)
send_messages(texts)
print() # Add a new line.

# Print both of my lists to make sure the messages were moved corretcly.
print(texts)
print(send_message)
