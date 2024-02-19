while True:
    print("1: Sets\n2: Lists\n3: Exit")
    choice = int(input("Select your options: "))
    
    if choice == 1:
        s1 = set(input("Enter set1 (comma-separated) : ").split(','))
        s2 = set(input("Enter set2 (comma-separated) : ").split(','))
        
        while True:
            print("1: Union\n 2: Intersection\n 3: Difference\n 4: Symmetric Difference\n 5: Subset\n 6: Superset\n 7: Add\n 8: Remove\n 9: Clear\n 10: Back")
            op = int(input("Enter operation: "))
            
            if op == 1:
                print("Union: ", s1.union(s2))
            elif op == 2:
                print("Intersection: ", s1.intersection(s2))
            elif op == 3:
                print("Difference: ", s1.difference(s2))
            elif op == 4:
                print("Symmetric Difference:", s1.symmetric_difference(s2))
            elif op == 5:
                print("Is Subset: ",s1.issubset(s2))
            elif op == 6:
                print("Is Superset: ",s1.issuperset(s2))
            elif op == 7:
                ele = input("Enter element to add: ")
                s1.add(ele)
                print("Element added to set1: ", s1)
            elif op == 8:
                ele = input("Enter element to remove: ")
                s1.discard(ele)
                print("Element removed from set1: ", s1)
            elif op == 9:
                s1.clear()
                print("Set1 cleared: ",s1)
            elif op == 10:
                break;
            else:
                print("Invalid choice, Please try again")
                
    elif choice == 2:
        l1 = list(input("Enter list1(comma-separated) :").split(','))
        l2 = list(input("Enter list2 (comma-separated) :").split(','))
        
        while True:
            print("1: Concatenate\n 2: Element at Index\n 3: Slice\n 4: Length\n 5: Count\n 6: Append\n 7: Remove\n 8: Reverse\n 9: Sort\n 10: Back")
            op = int(input("Enter operation: "))
            
            if op==1:
                print("Concatenation: ",l1 + l2)
            elif op==2:
                index = int(input("Enter index to get element: "))
                print("Element at index: ",l1[index] if index < len(l1)  else "Index out of range")
            elif op==3:
                start = int(input("Enter start index for slice: "))
                end = int(input("Enter end index for slice: "))
                print("Slice: ",l1[start:end])
            elif op==4:
                print("Length of list1: ", len(l1))
            elif op==5:
                ele = input("Enter element to count occurrences: ")
                print("Occurrences in list1: ",l1.count(ele))
            elif op==6:
                ele = input("Enter element to append: ")
                l1.append(ele)
                print("Element appended to list1: ",l1)
            elif op==7:
                ele = input("Enter element to remove: ")
                l1.remove(ele)
                print("Element removed from list1: ",l1)
            elif op==8:
                l1.reverse()
                print("Reversed list1: ",l1)
            elif op==9:
                l1.sort()
                print("Sorted list1: ",l1)
            elif op==10:
                break;
            else:
                print("Invalid choice, Please try again")
                
            
    elif choice == 3:
        break;
        
    else:
        print("Invalid Input, Please try again.")