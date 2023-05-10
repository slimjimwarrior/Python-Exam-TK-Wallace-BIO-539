import sys

from count_observed_script_final import * #import required function from other scripts
from count_possible_script_final import * #this function and the function above only use a string as the argument and NOT a text file

def linguistic_complexity(file_path):
    '''
    calculate linguistic complexity by calculating the proportion of all observed substrings over all possible substrings
    
    args:
        file_path: a path to a file containing a string of any possible length
    
    Return:
        tuple: a tuple of three values representing the total number of observed substrings, the total number of possible substrings, and the complexity proportion
    '''
    with open(file_path, 'r') as f:#read the file
        string = f.read() #convert the read file into object "string"
    
    total_observed = 0 #make empty objects to allow something to be counted
    total_possible = 0
    for k in range(1, len(string)+1): #iterate over string for size substring k until it reaches a k values that is the maximum size of the string
        total_observed += count_observed_substrings(string, k) #adds to the total observed object if it isnt already in the object
        total_possible += count_possible_substrings(string, k) #same as above but for all possible subtrings
    complexity = total_observed / total_possible #simple division to calculate the proportion, note that the function that generates total_possible make it float otherwise if you divide 2 integers even if the result is a float it will be zero
    return complexity, total_observed, total_possible #returns the generated objects

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python linguistic_diversity.py <file_path>") #if a user doesn't provide the right argument this will pop up and remind them
        sys.exit(1)
    file_path = sys.argv[1] #defining function argument
    complexity, total_observed, total_possible = linguistic_complexity(file_path) #output objects so they can be printed
    print("This is the total observed subtrings {}".format(total_observed)) # i use f-strings so when the output is given we can also calculate by eye to determine if linguistic complexity is correct. it also comes out nice. {} is where the value in format() is placed
    print("This is the total possible subtrings {}".format(total_possible))
    print("This is the linguistic complexity {}".format(complexity))
    