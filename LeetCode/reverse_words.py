
def reverse(s: str) -> list[str]:
    res = ''
    l, r = 0, 0

    while r < len(s):
        if s[r] != ' ':
            r += 1
        else:
            res += s[l:r+1][::-1]
            r += 1
            l = r

    res += ' '
    res += s[l:r + 2][::-1]
    
    return res[1:]

# Mais rápido: return ' '.join(word[::-1] for word in s.split())