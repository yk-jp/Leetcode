package FinalPricesWithASpecialDiscountInAShop

// sample solution from https://www.youtube.com/watch?v=PW9jKsNVA1Y
func finalPrices(prices []int) []int {
	var stack []int

	for idx, price := range prices {
		for len(stack) > 0 && prices[stack[len(stack)-1]] >= price {
			edit_idx := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			prices[edit_idx] -= price
		}
		stack = append(stack, idx)
	}

	return prices
}
