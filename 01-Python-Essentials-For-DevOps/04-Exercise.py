# Write a generator that alternates between returning even and odd
def even_or_odd():
    n = 0
    while True:
        if n % 2 == 0:
            yield "Even"
        else:
            yield "False"
        n+=1

is_what = even_or_odd()
print(is_what)
print(next(is_what))
print(next(is_what))