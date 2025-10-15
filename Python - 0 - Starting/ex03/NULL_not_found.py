def NULL_not_found(object: any) -> int:
	match object:
		case None :
			print(f"Nothing: None {type(object)}")
		case float() :
			if float(object) != float(object):
				print(f"Cheese: nan {type(object)}")
			else:
				print("Type not Found")
				return 1
		case bool() :
			if object is False:
				print(f"Fake: False {type(object)}")
			else:
				print("Type not Found")
				return 1
		case int() :
			if object == 0:
				print(f"Zero: 0 {type(object)}")
			else:
				print("Type not Found")
				return 1
		case str() :
			if object == "":
				print(f"Empty: {type(object)}")
			else:
				print("Type not Found")
				return 1
		case _:
			print("Type not Found")
			return 1
	return 0