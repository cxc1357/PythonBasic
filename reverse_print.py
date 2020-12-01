def reverse_print(s):
    if len(s) <= 1:
        return s
    return reverse_print(s[1:]) + s[0]

if __name__ == "__main__":
    s = "123"
    result = reverse_print(s)
    print(result)