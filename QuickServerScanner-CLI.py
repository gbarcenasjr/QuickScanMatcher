# Copyright (c) 2024 Gerardo Barcenas Jr.
import os
# Clearing the Screen

def editList(inputList: list, inputCount: list):
    print("Which SN do you want to edit/delete?")
    counter = 0
    for item in inputList:
        counter += 1
        print("\t" + str(counter) + ". " + item)
    print()

    userIndex = int(input("Input: ")) - 1

    print("Please enter new SN to edit or \nleave it blank to delete: ")
    userInput = str(input())
    userInput.strip()

    if userInput == "":
        inputList.pop(userIndex)
        inputCount.pop(userIndex)
    else:
        inputList[userIndex] = userInput
        inputCount[userIndex] = 0
    print()


def foundInList(searchkey: str, inputList: list, inputCount: list):
    os.system('cls')
    foundSN = False
    for x in range(len(inputList)):
        if inputList[x] == searchkey:
            foundSN = True
            inputCount[x] += 1
    if foundSN:
        print("!!![MATCH FOUND]!!!")
    else:
        print("[NO MATCH]")
    print("User entered: " + searchkey + "\n")


def main():
    os.system('cls')
    searchList = []
    searchCount = []
    barcode = ""

    while barcode != "finish":
        print("---LIST MODE---")
        print("Please enter the SN to search \nfor or enter the following commands:")
        print("\"finish\" to continue to Search Mode")
        print("\"edit\" to edit/delete in the search list\n")
        print("(Current List Size = " + str(len(searchList)) + ")")
        barcode = str(input("Input: "))
        barcode.strip()
        print()

        if barcode != "finish" and barcode != "edit" and barcode != "":
            searchList.append(barcode)
            searchCount.append(0)
        if barcode == "edit":
            editList(searchList, searchCount)

        os.system('cls')

    searchInput = ""

    print("[Blank]")
    print("(Please enter SN Below)")
    print()

    while searchInput != "finish":
        print("Search List")
        print("-----------")
        for x in range(len(searchList)):
            if searchCount[x] == 0:
                print("[ ] ", end="")
            else:
                print("[X] ", end="")
            print(searchList[x])
        print()

        print("---SEARCH MODE---")
        print("Please enter the SN to search \nfor or enter the following commands:")
        print("\"edit\" to edit/delete in the search list")
        print("\"finish\" to end program")
        searchInput = str(input("Input: "))
        print()

        if searchInput != "finish" and searchInput != "edit":
            foundInList(searchInput, searchList, searchCount)
        if searchInput == "edit":
            editList(searchList, searchCount)

    print("Program finished. Thank you for using Quick Server Scanner!\n")


if __name__ == '__main__':
    main()
