
# 6
def make_inc():
    total = 0

    def helper():
        nonlocal total
        total += 2
        return total
    return helper


f = make_inc()
print(f())


