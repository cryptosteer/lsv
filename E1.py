"""
Given an array of integers [a0, a1, ..., an] (1<=ai<=100) determine which is the most popular number. 

Most popular number appears more times that the others into given array.

If two numbers are equal of popularity algorith must return the minor of them.

Ej: [1, 3, 5, 6, 3, 6, 7, 8, 9, 6] => 6 (six is the most popular number)

"""
import re


def popular(l):
   
    # turn global var into a string
    global_list_str = [str(x) for x in l]
    global_list_str = "".join(global_list_str)
    # print("this is the global list to a string: {}".format(global_list_str))

    # list of current numbers
    unique_numbers = set(l)
    unique_numbers = list(unique_numbers)
    unique_numbers_str = [str(x) for x in unique_numbers]
    unique_numbers_str = "".join(unique_numbers_str)
    # print("this is the unique list to a string: {}".format(unique_numbers_str))
    
    # popularity list
    popularity_list = []

    for number in unique_numbers:
        
        # check for patterns
        result = re.findall("{}".format(number), global_list_str)
        # print(result)
        
        # gemerate popularity list       
        buffer = [len(result)]
        popularity_list.extend(buffer)
        # print(popularity_list)
    
    
    # getting propularity
    
    ## turning popularity list to string
    popularity_list_str = [str(x) for x in popularity_list]
    popularity_list_str = "".join(popularity_list_str)
    # print("this is the propularity list to a string: {}".format(popularity_list_str))
    
    ## find highest number 
    highest = str(max(popularity_list))
    
    ## find index number of the highest number
    index = re.search(highest, popularity_list_str).start()
    # print(index) 
    
    # getting most popular number
    print("The most propular number of {} is the number {}".format(lista, unique_numbers[index]))


    # testing stuff 
    # print(unique_numbers)
    # print(popularity_list)

lista = [1, 3, 5, 6, 3, 6, 7, 8, 9, 6]
# print("{} is the most popular.".format(popular(lista)))

popular(lista)
