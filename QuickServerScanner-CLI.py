# MIT License
# Copyright (c) 2024 Gerardo Barcenas Jr.
from os import system as cmd
from datetime import datetime
from platform import system as os_system


def ClearScreen():
    if os_system() == "Linux":
        cmd("clear")
    elif os_system() == "Windows":
        cmd('cls')


def editList(inputList: list, inputCount: list, inputNote: list):
    print("Which SN do you want to edit/delete?")
    counter = 0
    for item in inputList:
        counter += 1
        print("\t" + str(counter) + ". " + item)
    print()

    userIndex = int(input("Input: ")) - 1

    print("You selected: " + inputList[userIndex] + "\n")
    print("Please enter new SN to edit or \nleave it blank to delete: ")
    userInput = str(input())
    userInput.strip()
    # TODO: Add an option to edit notes

    if userInput == "":
        inputList.pop(userIndex)
        inputCount.pop(userIndex)
        inputNote.append(userIndex)
    else:
        inputList[userIndex] = userInput
        inputCount[userIndex] = 0

    print()


def isFoundInList(searchKey: str, inputList: list, inputCount: list) -> bool:
    for x in range(len(inputList)):
        if inputList[x] == searchKey:
            inputCount[x] = 1
            return True
    return False


def addNote(notelist: list):
    note = input("Do you want to add a note? (Leave blank if not): ")
    notelist.append(note)


def main():
    ClearScreen()
    searchList = []
    searchNotes = []
    searchCount = []
    barcode = ""

    while barcode != "finish":
        print("---LIST MODE---")
        print("Please enter the SN to search \nfor or enter the following commands:")
        print("\t\"finish\" to continue to Search Mode")
        print("\t\"edit\" to edit/delete in the search list\n")
        print("(Current List Size = " + str(len(searchList)) + ")")
        barcode = str(input("Input: "))
        barcode.strip()
        print()

        if barcode != "finish" and barcode != "edit" and barcode != "" and barcode not in searchList:
            searchList.append(barcode)
            addNote(searchNotes)
            searchCount.append(0)
        if barcode == "edit":
            editList(searchList, searchCount)

        ClearScreen()

    searchInput = ""
    isFirstRun = True
    while searchInput != "finish":

        ClearScreen()
        print("Search List")
        print("-----------")
        for x in range(len(searchList)):
            if searchCount[x] == 0:
                print("[ ] ", end="")
            else:
                print("[X] ", end="")
            print(searchList[x] + "  \"" + searchNotes[x] + "\"")
        print()

        if isFirstRun:
            print("[Blank Result]")
            print("(Please enter SN below)")
            isFirstRun = False
        elif isFoundInList(searchInput, searchList, searchCount):
            print("!!! [MATCH FOUND] !!!")
            print("User entered: " + searchInput)
        else:
            print("[No Match Found]")
            print("User entered: " + searchInput)
        print()

        print("---SEARCH MODE---")
        print("Please enter the SN to search \nfor or enter the following commands:")
        print("\t\"edit\" to edit/delete in the search list")
        print("\t\"finish\" to end program")
        searchInput = str(input("Input: "))
        searchInput.strip()
        print()

        if searchInput != "finish" and searchInput != "edit":
            isFoundInList(searchInput, searchList, searchCount)
        if searchInput == "edit":
            editList(searchList, searchCount)

    print("Program finished. \"results.txt\" file will be made and in the same folder as this Python file.\n")
    with open('results.txt', 'w') as file:
        txt_out = ""

        current_time = datetime.now()
        formatted_time = current_time.strftime("%Y/%m/%d %H:%M:%S")

        txt_out += "Program finished on " + formatted_time + "\n"
        txt_out += "Search List\n"
        txt_out += "-----------\n"

        for x in range(len(searchList)):
            if searchCount[x] == 0:
                txt_out += "[ ] "
            else:
                txt_out += "[X] "
            #     searchList[x] + "  \"" + searchNotes[x] + "\"\n"
            txt_out += searchList[x] + "  \"" + searchNotes[x] + "\"\n"

        file.write(txt_out)


if __name__ == '__main__':
    main()
