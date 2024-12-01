      ## 1. Even or Odd ##
def even_or_odd(number): # String given to me by codewars #
    return "Even" if number % 2 == 0 else "Odd" # Answer i inputed and Tested suscesfully #

       ## 2. Convert a Number to a String ##
def number_to_string(num): # String given to me by codewars #
    return str(num) # Answer i inputed and Tested suscesfully #

       ## 3. Vowel Count ##
def get_count(sentence):# String given to me by codewars #
    vowels = "aeiou" # Answer i inputed and Tested suscesfully ( assigned vowels ) #
    return sum(1 for char in sentence if char in vowels) # Answer i inputed and Tested suscesfully #
