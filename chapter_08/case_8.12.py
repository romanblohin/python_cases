def make_sandwich(*args):
	print("\nYour sandwich will include:")
	for item in args:
		print(f"\t- {item}")

make_sandwich('potato', 'tuna')
make_sandwich('tuna', 'egg', 'bacon')

