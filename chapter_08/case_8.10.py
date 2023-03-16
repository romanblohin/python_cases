def send_messages(new_messages, sent_messages):
	while new_messages:
		message = new_messages.pop()
		print(f"Message '{message}' was sent")
		sent_messages.append(message)

def show_sent_messages(messages):
	print("\nThe following messages are sent:")
	for message in messages:
		print(f"\t{message}")

new_messages = ['I love Python', 'London is the capital of Great Britain', 'Hello people!']
sent_messages = []

send_messages(new_messages, sent_messages)
show_sent_messages(sent_messages)