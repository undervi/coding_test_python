n = int(input())
result = 0
is_fin = "N"

if n % 5 == 0:
  print(n//5)
else:
  for i in range(n//5, 0, -1):
    if (n - (5*i)) % 3 == 0:
      print(i + (n - (5*i))//3)
      is_fin = "Y"
      break
       
  if n % 3 == 0 and is_fin == "N":
      print(n//3)
  elif is_fin == "N":
      print(-1)