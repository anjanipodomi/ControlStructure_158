1
def evaluate_performance (percentage): 
    #evaluate_performance untuk menerima input persentase nilai siswa
    #dan mengembalikan hasil nilai 
    if percentage >= 90:
        return "Excellent performance"
    elif percentage >= 80:
        return "Very Good performance"
    elif percentage >= 70:
        return "Good performance"
    elif percentage >= 60:
        return "Average performance"
    else:
        return "Below Average performance"
    
student_percentage = float(input("Enter the student's percentage: ")) #student_percentage mengambil persentase nilai siswa
performance = evaluate_performance(student_percentage) #evaluate_performance Menampilkan hasil penilaian dengan mencetak "The student's performance is:" diikuti dengan hasil nilai yg kita isi.
print("The student's performance is:", performance)

#2
def find_largest(num1, num2, num3): #memeriksa tiga angka yaitu num1, num2, dan num3 untuk menentukan mana yang terbesar
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
number3 = float(input("Enter the third number: "))

largest = find_largest(number1, number2, number3) #find_largest untuk menentukan nilai terbesar dari tiga angka yg dimasukkan.
print("The largest number is:", largest) #Mencetak hasilnya dengan menampilkan "The largest number is:" diikuti dengan nilai terbesar yang di isi.

#3
def fibonacci_series(n): #fibonacci_series untuk memberikan nilai a=0 dan b=1
    a, b = 0, 1
    while a <= n: #menggunakan while untuk mencetak nilai a selama a masih kurang dari atau sama dengan n
        print(a, end=" ")
        a, b = b, a + b
    print() 

n = int(input("Enter the value of n: ")) #masukan angka n yaitu 10
fibonacci_series(n)

#4
def print_odd_numbers(n): #fungsi untuk mencetak bilangan ganjil sampai dengan nilai n
    print("Odd numbers up to", n, "are:")
    for i in range(1, n + 1, 2):  #loop dari 1 sampai n dengan langkah 2, untuk menghasilkan bilangan ganjil
        print(i, end=" ")
    print() 

n = int(input("Enter the value of n: ")) #meminta pengguna memasukkan nilai n yaitu 10
print_odd_numbers(n) #memanggil fungsi untuk mencetak bilangan ganjil sampai dengan n

#5
def print_pattern(n): #fungsi untuk mencetak pola angka berdasarkan nilai n
    for i in range(1, n + 1): #loop dari 1 sampai n, untuk menentukan baris pola yang dicetak
        print((str(i) + " ") * i)

n = int(input("Enter the value of n: ")) #meminta pengguna memasukkan nilai n yaitu 5
print_pattern(n) #memanggil fungsi untuk mencetak pola angka sesuai nilai n
