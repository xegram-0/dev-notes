import time

# use True and False for faster sorting (sort of)
def bubble_sort(unsortList:list):
    sorted_list = unsortList
    for i in range(len(sorted_list)):
        j = i + 1
        if i == len(sorted_list):
            break
        for j in range(len(sorted_list)):
            if sorted_list[i] < sorted_list[j]:
                sorted_list[i], sorted_list[j] = sorted_list[j], sorted_list[i]

    return sorted_list

def main():

    inputRange:int = int(input("How many numbers in the list: "))
    unsortedList:list = []
    for i in range(inputRange):
        unsortedList.append(int(input(f"No. 0{i+1}: "))) # append works but not assigning values
    print(bubble_sort(unsortedList))
    start_time = time.time()
    print("Process finished --- %s seconds ---" % (time.time() - start_time))


if __name__ == "__main__":
    main()
