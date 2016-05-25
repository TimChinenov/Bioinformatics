# list_maker takes inputed file and returns a list of lists containing 
# the chromosome, the first and second interval, the peak, 0, and +. All parts
# of the list are strings.
def list_maker (file1):
    newlist = []
    for line in file1:
        temp = line.strip().split("\t")
        newlist.append(temp)
    return newlist


def dictionary_maker (list1):
    newdict = {}
    for item in range(len(list1)):
        if list1[item][0] not in newdict:
            newdict[list1[item][0]] = [[list1[item][1],list1[item][2],list1[item][3]]]
        else:
            newdict[list1[item][0]] += [[list1[item][1],list1[item][2],list1[item][3]]]
    return newdict



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

def print_results (dictionary, rag):
    for chrom in dictionary:
        counter = 1
        for ind in range(len(dictionary[chrom])):
            current_cluster = cluster_creator(dictionary, chrom, dictionary[chrom][ind][0],dictionary[chrom][ind][1],rag)
            if len(current_cluster) < 2:
                continue
            print
            print "Cluster %d" %(counter)
            print
            for intervals in range(len(current_cluster)):
                print "\t%s <%s> <%s>" %(chrom,current_cluster[intervals][0],current_cluster[intervals][1])
            counter += 1
    

f_in = open("Biostuff.txt")
x = list_maker(f_in)
x = dictionary_maker(x)
print_results(x, 1000)
    