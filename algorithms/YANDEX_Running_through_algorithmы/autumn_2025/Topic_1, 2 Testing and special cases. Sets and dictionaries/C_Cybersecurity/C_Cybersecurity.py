def main():
    s = input()
    n = len(s)
  
    char_dict = {}
  
    for char in s:
        if char not in char_dict:
            char_dict[char] = 0

        char_dict[char] += 1
    
    total_change = n * (n - 1) // 2 # формула из комбинаторики
  
    lie_change = 0
  
    for value in char_dict.values():
        lie_change += value * (value - 1) // 2

    return 1 + (total_change - lie_change)

print(main())