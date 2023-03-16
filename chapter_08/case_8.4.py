def make_shirt(size='L', message='I love Python'):
	print(f"Футболка с размером {size.upper()} с надписью {message}")

make_shirt()
make_shirt('xs', 'I love Irkutsk')
make_shirt(message='I love pizza', size='m')