Data = [1,2,3,4,5,6,7,8,9,10]


Subdata = Data[-5]
Subdata1 = Data[3:4]
Subdata2 = Data[2:]
Subdata3 = Data[-2:]
print(Subdata)
print(Subdata1)
print(Subdata2)
print(Subdata3)

Data2 = [100,200,300,400,500,600,700,800]

#Nambah List

Data3 = Data + Data2

#Merubah Content Data

print(Data)
Data[4] = 87
print(Data)

#Mencopy data kevariable baru.
a = Data[:]
a[3] = 90

print(a)


#Mengubah content list dengan menggunaak metode Slicing
Data[3:5] = [11,12]

#List dalam data
x = [Data, Data2]

# Mengakses list dalam multidimensional list

y = x[1][4]

print(x)
print(y)

# Methods untuk list
Data.append(30)

print(Data)

# Function yang  bisa kita gunakan kepad list

panjang_List = len(Data)
print(panjang_List)