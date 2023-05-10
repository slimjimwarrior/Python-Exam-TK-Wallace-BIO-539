# Python-Exam-TK-Wallace-BIO-539
Repository for all python code and unit tests for python exam for BIO 539 for TK Wallace

## Content of Repository

### Python_script 
has all the neccesary functions required to calculate linguistic complexity, including functions to calculate all observed substrings in a string and all possible subtrings in a string. the linguistic complexity script takes a text file as the argument, while the other 2 function only take a string. However, the linguistic complexity function also outputs all possible strings and all observed strings in addition the linguistic complexity proportion.

  the files in this folder are :
  ``
    linguistic_complexity_final - calculates linguistic complexity of a string in a text file.
    count_observed_script_final - counts all observed substring of size k in a string. Arguments are a string of any size and k, which defines the substrings size you are hoping to find.
    count_possible_script_final - counts all possible substrings using the same arguments as count_observed_script_final file.
  ``
### Python_Unit_Tests_and_testing_text_files
has unit tests for each python script denoted in the file name. additionally, has example text files used for the unit tests for linguistic_complexity_final.

 the files in this folder are :
 
 ``
  Unit_test_for_count_observed_script_final - multiple test functions for counting observed substrings.
  Unit_test_for_count_possible_script_final - multiple test functions for counting possible subtrings.
  Unit_test_for_linguistic_complexity_final - multiple test functions for calculating lingusitic complexity of a string.
  test_text, test_text_ATT, & singlecharacterstring - text files NEEDED to run the unit test for linguistic complexity. these need to be loaded in the same directory for the respective unit test to work.
 ``
 
## Notes On Use

Remember that the intermediate function count observed and count possible functions only take a string, and k (size of target subtring). It does not take a text file. Linguistic complexity only takes a text file with a string, but it does provide all observed and possible subtrings all well as the linguistic complexity proportion

Also count possible substrings functions returns the result as a float. This is because the final function uses division and when dividing integers even if the result is a float it will come out to a zero.


