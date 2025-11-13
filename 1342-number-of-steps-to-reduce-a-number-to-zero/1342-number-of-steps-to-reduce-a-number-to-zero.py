class Solution:

    def numberOfSteps(self, num: int) -> int:
        
        # Initialize our control variables so we can start the while loop:
        div_by_two = 1
        rest_one_to_be_div_by_two = 1

        # Initialize the counter of steps
        i_count = 0

        # We create a control variable so we can perform math operations in such
        num_2 = num

        # A whle loop that's gonna evaluate 2 condition for divisibility and one to check if the number is different than zero
        while (div_by_two or rest_one_to_be_div_by_two) and (num_2 != 0):
        
            # We update our boolean control variables
            # To see if the number is div by 2
            div_by_two = num_2 % 2 == 0 and num_2 >= 2
            # To see if we can substract one from the number
            rest_one_to_be_div_by_two = num_2 % 2 != 0

            # If true the number is divided by two and the step counter adds one
            if div_by_two:

                num_2 = num_2 / 2

                i_count = i_count + 1

            # If true the number is reduced by one and the step counter adds one
            elif rest_one_to_be_div_by_two:

                num_2 = num_2 - 1

                i_count = i_count + 1

            # When the two previousa conditions are false this means the number is equal to zero, then the loops breaks
            else:

                break

        # The value of steps (dividing by two and substracting one) needed for the number to become zero is returned
        return i_count





