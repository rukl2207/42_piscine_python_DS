import sys


def caesar_encode(encode_str: str, shift: int) -> str:
	encode_lst = list(encode_str)
	ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
	ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for index, elem in enumerate(encode_lst):
		if elem.islower():
			encode_lst[index] = ascii_lowercase[(ord(elem) - ord('a') + shift) % len(ascii_lowercase)]
		elif elem.isupper():
			encode_lst[index] = ascii_uppercase[(ord(elem) - ord('A') + shift) % len(ascii_uppercase)]
	return ''.join(encode_lst)


def caesar_decode(decode_str: str, shift: int) -> str:
	decode_lst = list(decode_str)
	ascii_lowercase = 'abcdefghijklmnopqrstuvwxyz'
	ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
	for index, elem in enumerate(decode_lst):
		if elem.islower():
			decode_lst[index] = ascii_lowercase[(ord(elem) - ord('a') - shift) % len(ascii_lowercase)]
		elif elem.isupper():
			decode_lst[index] = ascii_uppercase[(ord(elem) - ord('A') - shift) % len(ascii_uppercase)]
	return ''.join(decode_lst)


def caesar():
	if len(sys.argv) != 4:
		raise AttributeError(
			"Error: Wrong number of arguments.\n"
			"Usage: python3 caesar.py <mode (encode / decode)> <input_string> <shift(integer)>\n"
			"Example: python3 caesar.py encode 'Hello, World!' 12")
	try:
		shift = int(sys.argv[3])
	except ValueError as err:
		raise ValueError("Error: The shift must be an integer.", err)
	if not sys.argv[2].isascii():
		raise ValueError("Error: The script does not support your language yet.")
	if sys.argv[1] == 'encode':
		print(caesar_encode(sys.argv[2], shift))
	elif sys.argv[1] == 'decode':
		print(caesar_decode(sys.argv[2], shift))
	else:
		raise ValueError("Error: Incorrect mode. Select encode or decode.")


if __name__ == '__main__':
	caesar()
