from count_possible_script_final import count_possible_substrings

#let's start by running the example provided in the exam
def test_count_possible_substrings_examplestring_size_3():
    string, k = "ATTTGGATT", 3
    actual_output = count_possible_substrings(string, k)
    expected_output = 7
    assert actual_output == expected_output

def test_count_possible_substrings_examplestring_size_4():
    string, k = "ATTTGGATT", 4
    actual_output = count_possible_substrings(string, k)
    expected_output = 6
    assert actual_output == expected_output
    
def test_count_possible_substrings_examplestring_size_5():
    string, k = "ATTTGGATT", 5
    actual_output = count_possible_substrings(string, k)
    expected_output = 5
    assert actual_output == expected_output

#now let's test to see with unknown strings were we don't have the confirmed values. starting with testing the maximum

def test_count_possible_substrings_examplestring_size_3_stringsize_3(): #same as below, we use this in linguistic complexity unit testing
    string, k = "ATT", 3
    actual_output = count_possible_substrings(string, k)
    expected_output = 1
    assert actual_output == expected_output
    
def test_count_possible_substrings_examplestring_size_4_stringsize_4(): #since the maximum possible substrings has to be limited by the number of characters in the string, this should be right
    string, k = "ATTC", 4
    actual_output = count_possible_substrings(string, k)
    expected_output = 1
    assert actual_output == expected_output
    
def test_count_possible_substrings_examplestring_size_4_stringsize_final(): #same as above
    string, k = "ATTCGATTGCAAC", 4
    actual_output = count_possible_substrings(string, k)
    expected_output = 10
    assert actual_output == expected_output
    
#the function appears to work with wide variety of string sizes and correctly estimate the maximum. confidant stating thisworks