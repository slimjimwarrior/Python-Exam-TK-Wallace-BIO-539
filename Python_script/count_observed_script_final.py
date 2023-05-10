import sys

def count_observed_substrings(string, k): #define our function
    '''
    count all observed substrings of size k for a specified string
    only works with strings not integers
    
    args:
        string: a string of any possible length
        k: the size of substring your attempting count
    
    Return:
        int: the number of possible substrings within your provided string
    
    '''
    
    substring_counts = {} # create empty dictionary 
    num_substrings = max(len(string) - k + 1, 0) #calculate maximum number of k for given string
    
    for i in range(num_substrings): # iterate over the string 
        substring = string[i:i+k]  #extract substring of size k using slicing
        if substring in substring_counts: 
            substring_counts[substring] += 1 #if it is then add a value of 1 to that substring value in dictionary
        else:
            substring_counts[substring] = 1 # if is not then add it to the dictionary with a value of 1
    
    return len(substring_counts) #return the length so we know how many keys are in there rather than the complete dictionary

if __name__ == '__main__':
    string = sys.argv[1] #specift ordering and argument used in command line
    k = int(sys.argv[2]) #specify this needs to be an integer
    result = count_observed_substrings(string, k) #grab result from function
    print(result) #print the result