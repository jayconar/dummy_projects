def are_same(str1, str2):
    # Eliminating if lengths are different, obviously they can't be the same
    if len(str1) != len(str2):
        return False
    str1_concat = str1 + str1  # Concatenating one string with itself to make the other string, if present, complete
    return str2 in str1_concat  # Checking if str2 is a substring of str1_concat


print(are_same("HF1AF2GQ", "F1AF2GQH"))  # Output: True
