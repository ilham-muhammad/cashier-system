# Cashier Management System

## Problem/Background
A supermarket wants to improve their cashier to become a self-service cashier so that customers can add, edit, & purchase their items on their own.

## Requirements & Flowchart
The cashier system should have these features :
- adding items with their quantity & price
- editing entry that has been inputted
- deleting entire row/entry
- deleting entire purchase data
- checking purchase summary & its price
- check out purchase & save transaction data to the database

The flowchart of this system is defined below :

![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/5c475e22-8a6c-4c80-8121-c2ceca1ab9e2)

## Code Explanation
To use this code : 
- Download all of the files and put in one directory
- Run 'main.py' and choose your features
  
![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/e8ddcaba-4fce-46c8-b674-42b0d9c8531a)

- Each customer purchase will be defined as Transaction Class from 'cashier_management_system.py' module
- Below is the description of Transaction Class

![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/2f2ab393-5013-4092-9a22-250c2230a7d0)

## Test Case
1. Adding 2 items on purchase

![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/fdb629d2-073a-4b00-94c1-41ac860b4622)
![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/537a1f52-300b-4310-8c01-33d206bc45d1)
![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/874163bf-bc67-4f56-b801-79b69ebf182b)

2. Delete an item entry

![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/f3369251-ec1e-4aa6-9245-b687ac5d4945)
![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/fb50c883-32cd-4ed2-96e5-5179a5c611a9)

3. Reset purchase

![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/a2ef8ebf-b032-4918-aec2-239146c03a7a)

4. Check out the purchase

![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/11e4258e-b03e-4b8a-a7f7-7f0d7a472d70)
![image](https://github.com/ilham-muhammad/cashier-system/assets/105138863/15a5b110-5c9d-4ba8-81cd-f3c55dff47bc)

## Conclusions & Further Improvements
This code is just a simplified version of real cashier software, there are still many improvements that can be done such as :
- Automatic exit during some errors
- Operational errors when choosing feature 8. Check out during database exporting (might be a permission issue)
- Unable to edit multiple entries with the same item name
- and so on
But it will still be functional in a simple use case.
