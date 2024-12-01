class Solution:
    def checkIfExist(self, arr):
        d = {}
        for i in range(len(arr)):
            if arr[i] in d:
                return True
            d[arr[i] / 2] = [arr[i]]
            d[arr[i] * 2] = [arr[i]]
        return False


def main():
	sol = Solution()
	input = [10,2,8,4]
	print(sol.checkIfExist(input))

if __name__ == "__main__":
	main()
