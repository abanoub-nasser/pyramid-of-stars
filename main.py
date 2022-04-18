# -*- coding: utf-8 -*-


levels = int(input("Enter the no. of pyramid levels: "))
# initial value fo the stars
stars = 0
# pyramid levels pattern
for level in range(1, levels + 1):
    #Spaces pattern
    for space in range(1, (levels - level) + 1):
        # 2 spaces * levels - current level +1
        print(end="  ")
    # stars pattern
    while stars != (2 * level - 1):
        
        print("* ", end="")
        stars += 1
    # reset the stars value
    stars = 0
    #breaker between every level
    print()
