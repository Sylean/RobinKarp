def rabin_karp(s, lookup):
    #Dictionary size is 256 letters ASCII
    dict_l = 256
    length = len(lookup)
    slength = len(s)
    #Pick an arbitrarily large prime number to make hash computation efficient
    q = 339758944988188431805839020467
    #Pre-compute the factor for the largest digit in the sliding hash value
    h = fast_pow(dict_l, length - 1, q)

    pattern_hash = 0
    slide_hash = 0

    #Compute the initial value of the sliding hash and the lookup hash
    for i in range(length):
        pattern_hash = ((pattern_hash * dict_l) + ord(lookup[i])) % q
        slide_hash = ((slide_hash * dict_l) + ord(s[i])) % q

    #print(pattern_hash)
    #print(slide_hash)

    #Check if the hashes match. If so, check if the substrings are equivalent. Otherwise, increment the sliding hash
    for i in range(length, slength):
        if pattern_hash == slide_hash:
            if substr_eq(lookup, s[(i - length):i]):
                #print("found candidate")
                #print(slide_hash)
                return i - length

        slide_hash = (((slide_hash - (ord(s[i - length]) * h)) * dict_l) + ord(s[i])) % q
        #print(slide_hash)

    #print(slide_hash)
    #Check the last value of the slide_hash
    if pattern_hash == slide_hash:
        if substr_eq(lookup, s[(slength - length):slength]):
            #print("found candidate")
            #print(slide_hash)
            #Return the index of where the matched pattern starts
            return slength - length
        else:
            #Return -1 if the pattern is not found
            return -1
    else:
        #Return -1 if the pattern is not found
        return -1

#Compute powers using the pre-generated prime for time efficiency and to avoid stack overflows
def fast_pow(n, p, q):
    x = 1
    for i in range(p):
        x = (x * n) % q

    return x

#Dummy function for checking substring equality. TBD: Compute substring equality by checking values one by one
def substr_eq(s1, s2):
    #print(s1)
    #print(s2)
    return (s1 == s2)


#Dummy test 1
potato = "This is a potato"
lookup = "potato"


print(rabin_karp(potato, lookup))

#Dummy test 2

middle_potato = "This is a potato but in the middle this time"

print(rabin_karp(middle_potato, lookup))

#Dummy test 3

beginning_potato = "potato in beginning, this is"

print(rabin_karp(beginning_potato, lookup))

#Interactive Loop

input_string = ""
input_pattern = ""
while input_string != "quit":
    input_string = input('string: ')
    input_pattern = input('pattern: ')
    print(rabin_karp(input_string, input_pattern))