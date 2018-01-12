def feature_mapping_of_substring(s, k):
    head, *tail = s
    substrings = list()
    for c in range(len(s)):
        for v in s[c+1:len(s)]:
            substrings.append(s[c] + v)
    return set(substrings)


def subsequence_kernel(s, t):
    
    return


def main():
    print(feature_mapping_of_substring("cart", 3))
    s = "science is organized knowledge"
    t = "wisdom is organized life"
    subsequence_kernel(s, t)



if __name__ == '__main__':
    main()


