import math

class Solution:
    
    def fizzBuzz(self, n: int) -> List[str]:

        # Declare an empty list 'string_list'
        string_list = []

        # 'For loop' to evaluate every i index from 1 to n
        for i in range( 1 , n+1 ):

            # We calculate wheter it's divisible or not

            # -1 or 1 if it's divisible and 0 if it is not:
            div_3 , div_5 = (-1)*int(not bool(i % 3))  , int(not bool((i % 5)))

            # Expresion of 4 states:
            # -1 div by 3 / 1 div by 5  / 0 div by none / 2 or -2 div by both
            four_state_exp = max((div_5, div_3), key=abs) * ( abs( div_3 ) + abs( div_5 ) )

            # Match case to evaluate each of the 4 states
            match four_state_exp:

                # -1 if divisible by 3
                case -1:

                    # Add 'Fizz' as a string
                    string_list.append("Fizz")

                # 0 if divisible by none
                case 0:

                    # Add 'i' value as string
                    string_list.append(str(i))

                # 1 if divisible by 5
                case 1:

                    # Add 'Buzz' as a string
                    string_list.append("Buzz")

                # 2 or -2 if divisible by both
                case _:

                    # Add 'FizzBuzz' as a string
                    string_list.append("FizzBuzz")

        return string_list       
