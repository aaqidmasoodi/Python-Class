s = "ac"
class Solution:

	@classmethod
	def longestPalindrome(self, s: str) -> str:

		str_buffer = ''

		for i in range(len(s)):
			for j in range(len(s), i, -1):
				curr_str = s[i:j+1]
				if curr_str == curr_str[::-1] and len(curr_str) > len(str_buffer):
					str_buffer = curr_str
			if curr_str == s and curr_str == curr_str[::-1]:
				break

		return str_buffer

print(Solution.longestPalindrome(s))