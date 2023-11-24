def are_same(str1, str2):
    # Eliminating if lengths are different, obviously they can't be the same
    if len(str1) != len(str2):
        return False
    str1_concat = str1 + str1  # Concatenating one string with itself to make the other string, if present, complete
    return str2 in str1_concat  # Checking if str2 is a substring of str1_concat


print("The two strings are similar" if are_same("HF1AF2GQ", "F1AF2GQH")
      else "The strings are not similar")

# Problem:
# Write a program to find if two strings are same.
# two string are considered same if both strings have same letters in the same order, but from different starting point
# eg: abcd is same as bcda ('a' is moved to the right)
# abcd is same as cdab
# abcd is  not same as cdba
