nilai1 = 75
nilai2 = 60

if nilai1 == 75:
    print(f'Nilai anda adalah {nilai1}')
    print('Step 1')
    if nilai2 == 80: #Nesting if (if didalam if)
        print(f'Nilai anda adalah {nilai2}')
        print('Step 2')

nilai = 50

if nilai == 75: #eksplisit
    print("Nilai Anda:",nilai)
if nilai is  60: #equal
    print("Nilai anda:",nilai)
if nilai is not 60: # not equal
    print("Nilai anda:",nilai)

nilai = 65
print("---------------------")
if 80 <= nilai <= 100:
    print('Nilai anda buka A')
elif 70 <= nilai <= 80:
    print('Nilai anda buka B')
elif 60 <= nilai <= 70:
    print('Nilai anda buka C')
elif 50 <= nilai <= 60:
    print('Nilai anda buka C')
else:
    print('Maaf anda tidak Lulus Kuliah Ini')