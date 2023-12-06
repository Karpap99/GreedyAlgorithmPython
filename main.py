import math
import time


def read_data(path): #reading file with data, your file must be as bcl380 in repository
    data = {}
    with open(path, 'r') as f:
        for each in f:
            x = each.split(" ")
            data[str(x[0])] = ((int(x[1])*10,int(x[2])*10))
    return data


def euclid_distance(A, B): #calculate distance within points
    return int(math.sqrt(((B[0]-A[0])**2) + ((B[1]-A[1])**2)))


def sort_list(datalist): #sorting algorithm
    for i in range(len(datalist)):
        j = i + 1
        while j != len(datalist):
            if datalist[i][1] > datalist[j][1]:
                temp = datalist[i]
                datalist[i] = datalist[j]
                datalist[j] = temp
            j += 1
    return datalist



locations = read_data("bcl380.tsp")
best_path = []
optimal_tour = int(input("optimal price>"))
start_location_index = input("start location>")
begin = time.time_ns()
best_path.append((str(start_location_index), locations[start_location_index]))
locations.pop(start_location_index)
price = 0
while len(locations) > 0:
    distantions = []
    for key in locations:
        distantions.append([key, euclid_distance(best_path[len(best_path)-1][1], locations[key])])
    distantions = sort_list(distantions)
    price += distantions[0][1]
    best_path.append((distantions[0][0], locations[distantions[0][0]]))
    locations.pop(distantions[0][0])
end = time.time_ns()
counter = 0
print("solution:")
for each in best_path:
    counter += 1
    print(f"{each[0]} >",end='')
    if counter % 30 == 0:
        print("")
price += euclid_distance(best_path[0][1], best_path[len(best_path)-1][1])
print(start_location_index)
print(f"solution price:{price}")
print(f"solution error:{int(100 - (optimal_tour/price * 100))}%")
print(f"solution time:{(end - begin) / 1000000000} seconds")