def data_types():
	var1, var2, var3, var4, var5, var6, var7, var8 = 0, "[", 0.0, False, [], {}, tuple(), set()
	for v in (var1, var2, var3, var4, var5, var6, var7):
		var2 += type(v).__name__ + ", "
	var2 += type(var8).__name__ + "]"
	expected_str = "[int, str, float, bool, list, dict, tuple, set]"
	if var2 == expected_str:
		print(var2)
	else:
		print("Error: Wrong output.")


if __name__ == '__main__':
	data_types()
