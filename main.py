def most_common_chars(s):
    most_common = max(set(s), key=s.count)
    hz = s.count(most_common)
    print(f"The most common character is '{most_common}' and it appears {hz} times.")

most_common_chars("hello world")
most_common_chars("abwdiwdkwdw")
most_common_chars("aaaaa bbb cccc")