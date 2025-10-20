import sys

def main():
	if len(sys.argv) > 2:
		raise AssertionError("more than one argument is provided")
	elif len(sys.argv) < 2:
		pass
	else :
		try :
			arg = int(sys.argv[1])
		except Exception :
			raise AssertionError("argument is not an integer")
		else :
			print("I'm Even.") if arg%2 == 0 else print("I'm Odd.")


if __name__ == "__main__":
	try :
		main()
	except AssertionError as ae :
		print(f"AssertionError: {ae}")