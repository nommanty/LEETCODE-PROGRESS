class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        unique_chs = ""
        foll_dict = {}

        # We create a string that contains the unique characters of "magazine"
        for ch in magazine:

            if ( ch not in unique_chs ):
                unique_chs = unique_chs + ch

        # Now "unique_chs" contains  

        # A for loop to iterate trough all the characters of "unique_chs" to add it to the dictionary
        for ch in unique_chs:

            # We add to the dict the key "character" of "unique_chs" and associate its value "times_it_appears" in "magazine"
            foll_dict[ch] = magazine.count(ch)

        # Now "foll_dict" contains as keys all the characters that appears one time and as their associated values the number of times each characters apperar in "magazine"

        # Now we evaluate wheter each character from "magazine" appears less times than it appears on "ransomNote"
        for char in ransomNote:
            
            # The first part evaluates whether "char" does not appear in "ransomNote" 
            # it also ensures to avoid errors when evaluating "foll_dict[char]" if "char" is not a key in "foll_dict" (if a character from ransomNote does not appear in magazine)

            # The second part evaluates wheter the appeareances of "char" is greater in "ransomNote" than "magazine"

            if (char not in magazine) or (foll_dict[char] < ransomNote.count(char)):

                return False
                
        return True




            

