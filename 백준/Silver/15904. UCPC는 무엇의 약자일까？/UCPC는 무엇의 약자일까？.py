word = input()
out = "hate"

u_idx = word.find("U")
if u_idx != -1:
    word = word[u_idx+1:]
    c_idx = word.find("C")
    if c_idx != -1:
        word = word[c_idx+1:]
        p_idx = word.find("P")
        if p_idx != -1:
            word = word[p_idx+1:]
            c2_idx = word.find("C")
            if c2_idx != -1:
                out = "love"

print("I", out, "UCPC")