<!--
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
	•	I can be placed before V (5) and X (10) to make 4 and 9.
	•	X can be placed before L (50) and C (100) to make 40 and 90.
	•	C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
Input: s = "III"
Output: 3

Input: s = "LVIII"
Output: 58

Input: s = "MCMXCIV"
Output: 1994


           -->

/**
* @param {number[]} prices
* @return {number}
*/
def romanToInt(self, s: str) -> int:

    convertionDic = {

    }
    Special_cases = {
    X: [l,c]
    C: [d,m]
    I: [v,x]
    }
	Result = 0
	Cur_number = 0
	Array = s.split(“”)

	For i in range(len(array)):
		Char = array[x]
		If array[x] in Special_cases.keys()
			Complement = Special_cases[Char]
			if(array[i+1] == complement):
				Cur_number = convertionDic[complement] - convertionDic[Char]
			Else:
				Cur_number = convertionDic[Char]
		Else:
			Cur_number = convertionDic[Char]

		Result += cur_number




<!--


Input: s = "LVIII"
50 + 5 + 1 + 1 + 1 = 58

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I x c

Input "MCMXCIV"
1000 + 900 + 90 + 4 = 1994
Pseudocode

	•	Split roman number to convert into array
	•	Create a result variable eq 0
	•	Transverse the Roman number from left to right checking wether is a single char or two char
	•	Take cur chart and translate to integers
	•	Sum last value and continue
 -->
