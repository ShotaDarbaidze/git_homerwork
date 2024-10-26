def count(s):
    countt = {}
    
    for char in s:
        countt[char] = countt.get(char, 0) + 1
            
    return countt
