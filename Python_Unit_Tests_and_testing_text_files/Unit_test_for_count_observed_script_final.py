from count_observed_script_final import *#import required function from other scripts
from count_possible_script_final import *
from linguistic_complexity_final import *
 #NOTE: while the final function this function feeds into uses a text file this one only uses a pre-defined string but since it runs with this smaller sample it will work with larger instances

#make sure the each defined function starts with "test" so it can recognized by the pytest function    
    
##this section is for count_observed_script_final
#below are just tests that mimic the provided example so we know it at least works for 1 possible strings   

def test_observed_substring_script_size_3():
    string,k = "ATTTGGATT", 3
    actual_output = count_observed_substrings(string,k)
    expected_output = 6
    assert actual_output == expected_output
    
def test_observed_substring_script_size_4():
    string,k = "ATTTGGATT", 4
    actual_output = count_observed_substrings(string,k)
    expected_output = 6
    assert actual_output == expected_output
    
def test_observed_substring_script_size_5():
    string,k = "ATTTGGATT", 5
    actual_output = count_observed_substrings(string,k)
    expected_output = 5
    assert actual_output == expected_output
    
def test_observed_substring_script_size_6():
    string,k = "ATTTGGATT", 6
    actual_output = count_observed_substrings(string,k)
    expected_output = 4
    assert actual_output == expected_output

def test_observed_substring_script_size_7():
    string,k = "ATTTGGATT", 7
    actual_output = count_observed_substrings(string,k)
    expected_output = 3
    assert actual_output == expected_output
    
def test_observed_substring_script_size_7():
    string,k = "ATTTGGATT", 7
    actual_output = count_observed_substrings(string,k)
    expected_output = 3
    assert actual_output == expected_output
    
def test_observed_substring_script_size_8():
    string,k = "ATTTGGATT", 8
    actual_output = count_observed_substrings(string,k)
    expected_output = 2
    assert actual_output == expected_output
    
#lets try with unknown example
    
def test_observed_substring_script_size_2(): # expected output should just be one since the maximum substring will be the total letters in a string
    string,k = "AT", 2
    actual_output = count_observed_substrings(string,k)
    expected_output = 1
    assert actual_output == expected_output
    
def test_observed_substring_script_size_1_new(): #since we are only counting 1 substring size, then the observed substrings should just be 2 due to 2 unique characters in strings 
    string,k = "AT", 1
    actual_output = count_observed_substrings(string,k)
    expected_output = 2
    assert actual_output == expected_output
    
#let's add another letter in string
    
def test_observed_substring_script_size_2_subtring_3(): #expanding on other sections with but just adding another letter
    string,k = "ATC", 2
    actual_output = count_observed_substrings(string,k)
    expected_output = 2
    assert actual_output == expected_output
    
def test_observed_substring_script_size_2_subtring_3_new(): # we use this in linguistic complexity unit testing
    string,k = "ATT", 3
    actual_output = count_observed_substrings(string,k)
    expected_output = 1
    assert actual_output == expected_output
    
def test_observed_substring_script_size_1_string_3():
    string,k = "ATC", 1
    actual_output = count_observed_substrings(string,k)
    expected_output = 3
    assert actual_output == expected_output
    
#i'm confident in saying this functions works as intended
    