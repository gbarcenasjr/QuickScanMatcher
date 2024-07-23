# Copyright (c) 2024 Gerardo Barcenas Jr.
import os
# Clearing the Screen

def editList(inputList: list):
    print("Which SN do you want to edit/delete?")
    for x in range(len(inputList)):
        print(("\t" + str(int(x) + 1) + ". " + str(inputList[x])))

    print()
    userIndex = int(input("Input: ")) - 1

    print("Please enter new SN to edit or \nleave it blank to delete: ")
    userInput = str(input())
    userInput.strip()

    if userInput == "":
        inputList.pop(userIndex)
    else:
        inputList[userIndex] = userInput
    print()


def foundInList(searchkey: str, inputList: list):
    if searchkey in inputList:
        print("!!![MATCH FOUND]!!!\n")
    else:

        print("[NO MATCH]\n")
    print(searchkey+"\n")


def main():
    os.system('cls')
    searchList = []
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
        if barcode == "edit":
            editList(searchList)
            
        os.system('cls')

    searchInput = ""
    while searchInput != "finish":
        print("Search List")
        print("-----------")
        for item in searchList:
            print("[ ] " + item)
        print()
        
        print("---SEARCH MODE---")
        print("Please enter the SN to search \nfor or enter the following commands:")
        print("\"edit\" to edit/delete in the search list")
        print("\"finish\" to end program")
        searchInput = str(input("Input: "))
        print()

        if searchInput != "finish" and searchInput != "edit":
            foundInList(searchInput, searchList)
        if searchInput == "edit":
            editList(searchList)

    print("Program finished. Thank you for using Quick Server Scanner!\n")


if __name__ == '__main__':
    main()
