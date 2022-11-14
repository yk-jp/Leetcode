package LongestPalindrome

func longestPalindrome(s string) int {
	hashmap := make(map[string]int)

	for _, ch := range s {
		str := string(ch)
		if _, found := hashmap[str]; found {
			hashmap[str] += 1
		} else {
			hashmap[str] = 1
		}
	}

	ans := 0
	isAdded := false

	for key := range hashmap {
		ans += hashmap[key] / 2 * 2
		hashmap[key] -= hashmap[key] / 2 * 2
		if !isAdded && hashmap[key] > 0 {
			ans += 1
			isAdded = true
		}
	}

	return ans

}
