def test_3_1(): 
  input = map(int, input().split())
  coin_types = [500, 100, 50, 10]
  ans = 0
  for coin in coin_types: 
    ans += input // coin
    input %= coin
  return ans

def test_3_2(): 
  N, M, K = map(int, input().split())
  n = list(map(int, input().split()))
  n.sort(reverse=True)
  ans = 0
  K_temp = K
  for temp in range(M):
    K_temp-=1
    if K_temp < 0:
      K_temp = K
      ans += n[1]
    else: 
      ans += n[0]
  return ans

def test_3_3(): 
  N, M = map(int, input().split())
  ans = 0
  for temp in range(N): 
    n = list(map(int, input().split()))
    min_val = min(n)
    ans = max(ans, min_val)
  return ans