# Labpy04
## List
 • List (Daftar) adalah salah satu datatype yang paling sering digunakan dan sangat serbaguna yang digunakan dengan pyton\
 • Pada pemrograman Python, List dibuat dengan menempatkan semua item (elemen) di dalam kurung siku [], dipisahkan dengan tanda koma.\
 •Untuk mengakses nilai dalam daftar, gunakan tanda kurung siku untuk mengiris bersama dengan indeks atau indeks untuk mendapatkan nilai yang tersedia pada indeks tersebut.\
 • Indeks dimulai dari 0. Jadi, daftar yang memiliki 5 elemen akan memiliki indeks dari 0 ke 4.\
 • Indeks harus bilangan bulat.
1. contoh cara mengakses element dari list\
![list](list/mengakses_element.png) \
 penjelasan :\
 list1 = ['physics','chemistry',1997,2000]\
 print list [0]\
 karena dimulai dari 0 maka outputnya adalah physics\

2. contoh mengiris list \
![list1](list/mengiris_list_1.png) \
penjelasan :\
my_list = ['p','r','o','g','r','a','m','i','z'] \
print my_list[2:5] \
disini di minta element ke 2 sampai ke 5 \ 
maka outputnya o,g,r \
![list2](list/mengiris_list_2.png) \
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[:-5]) \
disini di minta elemen pertama sampai elemen 4 maka hasilnya : 'p','r','o','g' \

![list3](list/mengiris_list_3) \
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[5:])
disini diminta elemen ke 5 sampai terakhir maka hasil nya 'a','m','i','z'\

![list](list/mengiris_list_4.png) \
my_list = ['p','r','o','g','r','a','m','i','z']
print(my_list[:]) \
disini di minta semua element maka hasil nya
 'p','r','o','g','r','a','m','i','z' \

3. mengubah list \
 ![list1](list/mengubah_list_1.png) \
odd = [2,4,6,8] \
odd[0] = 1 \
print(odd) \
karena elemen pertama di ubah menjadi 1 maka : ['1','4','6','8'] \

contoh lagi cara mengubah item ke 2 sampai ke 4 \
odd = [1,4,6,8] \
odd [1:4] = [3,5,7] \
print(odd) \
maka hasilnya ['1','3','5','7'] \
element ke 1 adalah 4 digantikan dengan 3 element ke 2 adalah 6 digantikan dengan 5 element ke 3 adalah 8 digantikan dengan 7 \
![list2](list/mengubah_list_2.png)  \

menambah element, bisa menggunakan append\
contoh\
odd = [1,3,5] \
odd.append(7) \
print(odd) \
list dari odd di tambah 7 maka hasilnya : \
['1','3','5','7'] \
![list3](list/mengubah_list_3.png)
