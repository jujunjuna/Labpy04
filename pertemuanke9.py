#LIST
#List of integers
mylist = [1,2,3]
#List with mixed data types
mylist2 = [1,"hello", 3.4]

#1.mengakses element dari list
list1 = ['physics','chemistry',1997,2000]
list2 = [1,2,3,4,5,6,7,8]
print("list1 [0]: ", list1[0])
print('list2 [1:5] :', list2[1:5])
#output: list1 [0] : physics
#        list2 [1:5] : [2,3,4,5]

#2.MENGISIRIS LIST
my_list = ['p','r','o','g','r','a','m','i','z']
#elements 3rd to 5th
print(my_list[2:5])
#out put : ['o','g','r']

#elements beginning to 4th
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[:-5])
#out put : ['p','r','o','g']

#elements 6th to end
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[5:])
#outout : ['a','m','i','z']

#elements beginning to end
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[:])
#output : ['p','r','o','g','r','a','m','i','z']

#3.MENGUBAH ATAU MENAMBAH ELEMENTS DI DALAM LIS
odd = [2,4,6,8]
#ubah item pertama
odd[0] = 1
print(odd)
#out put : ['1','4','6','8']

#mengubah item ke 2 sampai ke 4
odd = [1,4,6,8]
odd [1:4] = [3,5,7]
print(odd)
#output : ['1','3','5','7']

#menambah element
#menggunakan append
odd = [1,3,5]
odd.append(7)
print(odd)
#output : ['1','3','5','7']

#menggunakan extend menambahkan beberapa element
odd = [1,3,5,7]
odd.extend([9,11,13])
print(odd)
#output : ['1','3','5','7','9','11','13']

#bisa juga menggunakan operator + untuk menggabungkan 2 list
odd = [1,3,5]
print(odd + [9,7,5])
#output : [1,3,5,9,7,5]

#mengulang daftar beberapa kali menggunkan operator *
print (["re"]*3)
#output:["re","re","re"]


#4.REMOVE ELEMENT
#menghapus item dari list menggunakan del
my_list = ['p','r','o','b','l','e','m']
del my_list[2]
print(my_list)
#output: ['p','r','b','l','e','m']

#TUPPLE
tup1 = ('physics','chemistry',1997,2000)
tup2 = (1,2,3,4,5,6,7)
print (tup1[0])
#output : physics
print(tup1[2])
#output : 1997
print(tup2[1:5])
#output :(2,3,4,5)

#dictionary
dict = {'name': 'zara', 'age': 20,'clas':'seven'}
print(dict['name'])
#output : zara
print (dict['age'])
#output : 20

#delete dictionary elements
dict = {'name': 'zara','age': 20,'clas':'seven'}
del dict['name']
print (dict)
#output : {'age': 20,'clas':'seven'}
dict.clear()
print(dict)
#output : {}