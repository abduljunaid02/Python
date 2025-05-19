def print_rangoli(size):
    alpArr = [chr(i+65).lower() for i in range(size)]                   #Get the alphabets for the numbers
    linelength = 4*size-3                                               #calculate the width of the rangoli. (No. of letters + "-") 
    toprows = []                                                        #Declare a list to capture the top half of the design
    for i in range(size-1,-1,-1):                                       #Loop through the size in reverse.
        lett = alpArr[size-1:i:-1]+alpArr[i:size]                       #Get the alphabets that go in each row by slicing the alphabet array
        row = "-".join(lett).center(linelength, "-")                    #join the alphabets in each row with "-" and center them
        toprows.append(row)                                             #Append it to the toprows array
    bottomrows = toprows[::-1]                                          #Reverse the toprows array and create new bottomrows array
    full = toprows + bottomrows[1:]                                     #Add both arrays. Remove the first element to eliminate duplication
    for i in range(len(full)):                                          #Loop through the full array
        print(full[i])                                                  #Print each element of the full array


if __name__ == "__main__":
    n = int(input())
    print_rangoli(n)