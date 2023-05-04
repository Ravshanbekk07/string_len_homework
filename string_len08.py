def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """
    n = len(s)
    if len(s)%2 == 0:
        b = int(n/2)+1
        q = int(n/2)-1 #int(n/2)-1
        return s[q:b]
    else:
        if len(s)% 2==1:
            w = int(n/2)
            e = int(n/2)+1
        return s[w:e]


v =  main('qwertyu')
print(v)