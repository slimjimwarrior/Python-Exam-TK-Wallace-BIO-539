from count_observed_script_final import * #import required function from other scripts
from count_possible_script_final import *
from linguistic_complexity_final import *

#remember since linguistic_complecity outputs 3 numbers it's not just the proportion but also all observed substrings and all possible subtrings

#in this order (proportion, observed substrings, and possible substrings(this will always be a float))
#im fully aware this makes unit testing tedious but it's already tedious, just another grain of sand on the beach

# seems to work with expected values
def test_linguistic_complexity():
    file_path = "test_text.txt"
    actual_output = linguistic_complexity(file_path)
    expected_output = 0.875, 35, 40.0
    assert actual_output == expected_output
    
def test_linguistic_complexity_test_2():
    file_path = "test_text_ATT.txt"
    actual_output = linguistic_complexity(file_path)
    expected_output = 0.8333333333333334, 5, 6.0
    assert actual_output == expected_output
    
#let's test to see if it outputs 1 when we provide a single character string, wanted to use zero but cant divide by zero so it gave me an error

def test_linguistic_complexity_test_emptystring(): #since it's a single character string it should return one 
    file_path = "singlecharacterstring.txt"
    actual_output = linguistic_complexity(file_path)
    expected_output = 1, 1, 1
    assert actual_output == expected_output