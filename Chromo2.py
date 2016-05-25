"""
Author: Tim Chinenov
"""
# list_maker takes inputed file and returns a list of lists containing 
# the chromosome, the first and second interval, the peak, 0, and +. All parts
# of the list are strings.
def list_maker (file1):
    newlist = []
    for line in file1:
        temp = line.strip().split("\t")
        newlist.append(temp)
    return newlist

#dictionary_maker uses the specific list outputed by list_maker and turns it into
#a dictionary. The function searches for a chromosome number creating that the key 
#of the dictionary and uses a list of lists of intervals as its value. The result 
# will look something like: 
#newdict = {chrom1:[[interval1, interval2][interval3,intervale4][int...]], chrom2: [[int...]]}
def dictionary_maker (list1):
    newdict = {}
    for item in range(len(list1)):
        if list1[item][0] not in newdict:
            newdict[list1[item][0]] = [[list1[item][1],list1[item][2],list1[item][3]]]
        else:
            newdict[list1[item][0]] += [[list1[item][1],list1[item][2],list1[item][3]]]
    return newdict


#cluster_creator works togethar with print results. When print results is called, cluster_creator
#recieves a dictionary, a chromosome, starting interval, ending interval, and a range. 
#Cluster_creator finds the chromosome and the interval in the dictionary. The function starts 
#by checking if the numbers to the numbers to the right of it, or the larger numbers, are
#within the given range (rag). If so the interval is appended to the list of lists of cluster. The 
#function then does the same procedure except with the numbers to the left of it, or the lesser number and 
#inserting succesful intervals to the begining of the lists of lists cluster. The function returns the 
#list of clusters as: cluster.
def cluster_creator (dictionary,chrom,n1,n2,rag):
    reference_list = []
    index_of_interval = 0
    #Finds specific list of intervals
    for item in dictionary:
        if item == chrom:
            reference_list = dictionary[item]
    #Finds index of given intervals in list
    for index in range(len(reference_list)):
        if reference_list[index][0] == n1 and reference_list[index][1] == n2:
            index_of_interval = index
    #Start searching for clusters
    i = index_of_interval
    cluster = [[n1,n2]]
    while i + 1 < len(reference_list):
        if int(reference_list[i+1][0]) - int(reference_list[i][1]) <= rag:
            cluster.append(reference_list[i+1])
            i += 1
        else:
            break
    i = index_of_interval 
    
    while i - 1 >= 0:
        if int(reference_list[i][0]) - int(reference_list[i-1][1]) <= rag:
            cluster.insert(0,reference_list[i-1])
            i -= 1
        else:
            break  
    
    return cluster

#print_results goes through each key in the inputed dictionray. For each iteration, the function calls 
#cluster_creator and assigns the result to a temporary variable refered to as current_cluster. If
#current_cluster is indeed a cluster (The length of the list of intervals is greater than 1), then the
#cluster is printer in the form  
#"chromosome first_interval last_interval Cluster_number number_of_intervals_in_the_cluster"
def print_results (dictionary, rag):
    counter = 1
    for chrom in dictionary:
        
        for ind in range(len(dictionary[chrom])):
            current_cluster = cluster_creator(dictionary, chrom, dictionary[chrom][ind][0],dictionary[chrom][ind][1],rag)
            if len(current_cluster) < 2:
                continue
            print "%s %s %s Cluster %d %d" %(chrom, current_cluster[0][0], current_cluster[-1][1],counter, len(current_cluster))
            
            counter += 1
    

f_in = open("Biostuff.txt") #opens file
x = list_maker(f_in) #converts file to list of lists
x = dictionary_maker(x) #converts list of lists to dictionary
inrange = int(raw_input("Input a range ==> ")) #asks user for range
print_results(x, inrange) #gives results