def test_3_1(input): 
  coin_types = [500, 100, 50, 10]
  ans = 0
  for coin in coin_types: 
    ans += input // coin
    input %= coin
  return ans