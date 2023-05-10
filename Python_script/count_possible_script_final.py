import sys

def count_possible_substrings(string, k): #defining arguments, you can't use a file_name for this since it woudl intefer with the linguistic complexity function
    '''
    count all possible substrings of size k for a specified string
    only works with strings not integer
    
    args:
        string: a string of any possible length
        k: the size of substring your attempting count
    
    Return:
        float: the number of possible substrings within your provided string,for compatibility with linguistic_complexity function
    
    '''
    
    num_substrings = min(len(string) - k + 1, 4**k) #len(string) generates the maximum number of substrings of length k
    #4**k represents the total number of substrings possible 
    #min returns the smaller of these 2 numbers becausese the actual possible is limited by the size 4**k
    #otherwise we get a much higher number
    return float(num_substrings) # this results in an integer but i convert it into a float, otherwise in the final linguisitc complexity function we get a zero since division with 2 integers always result into zero

if __name__ == '__main__': # this sections lets us use the argument string and k in the command line, then it prints them
    string = sys.argv[1] #define the string argument
    k = int(sys.argv[2]) #define the k substring argument
    result = count_possible_substrings(string, k) 
    print(result) #print the result