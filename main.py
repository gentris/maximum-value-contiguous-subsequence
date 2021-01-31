def get_max_subsequence(array: list, size: int) -> tuple:
	start: int = 0
	end: int = 0
	max: int = array[0]

	sum = array[0]
	sum_start_index = 0;

	for i in range(1, size):
		print("i: ", i)
		if (sum > 0):
			sum = sum + array[i]
		else:
			sum = array[i]
			sum_start_index = i

		if (sum > max):
			start = sum_start_index
			end = i
			max = sum
	
	return (max, start, end)

def main():
	array: list = [5, 3, 6, -6, 9, 12, -5, 3, 5, 8, -1]
	print(get_max_subsequence(array, len(array)))

if __name__ == "__main__":
	main()
