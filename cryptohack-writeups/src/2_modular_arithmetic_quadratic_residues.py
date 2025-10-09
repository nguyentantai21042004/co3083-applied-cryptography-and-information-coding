p = 29
ints = [14, 6, 11]

def square_roots_mod_p(x, p):
    roots = []
    for a in range(p):  # brute force vì p nhỏ
        if (a * a) % p == x % p:
            roots.append(a)
    return sorted(set(roots))

qr_candidates = {}
for x in ints:
    rts = square_roots_mod_p(x, p)
    qr_candidates[x] = rts

print("Roots by x:", qr_candidates)

# Lấy phần tử là quadratic residue (có ít nhất 1 nghiệm),
# rồi lấy nghiệm nhỏ hơn để làm flag
for x, rts in qr_candidates.items():
    if rts:
        flag = min(rts)  # nghiệm nhỏ hơn trong {a, -a}
        print("Quadratic residue:", x, "roots:", rts, "flag:", flag)