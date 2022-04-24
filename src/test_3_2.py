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