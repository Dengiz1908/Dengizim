# Karta nomli fayl berilgan. Sizning vazifangiz:
# 1) Fayldagi davlatlarni nomlarini dictionary keysiga va qiymatiga esa ushbu davlatlar sonini yozib chiqaring.
# 2) Fayldagi Karta_turida visa qatnashgan davlatlarni alfavit tartibida chiqaring.
# 3) Karta_raqami orasida kamida hamma raqamlar, ya'ni 0,1,2,3,4,5,6,7,8,9,0 ishtirok etganlarni Karta_raqami, 
# Davlat, Valyute va Korxonasini chiqarib bering.
#################
#2-shart
v=[]
d=[]
with open("plas.txt",'r') as fp :
    text=fp.read()
for i in text.split('\n'):
    v.append(i.split(',')[1])
    
    if i.split(',')[1]=='visa' or i.split(',')[1]=='visa-electron' :
        d.append(i.split(',')[-1])   
        d.sort()
   # ls[t]=text.count(t)
x=set(d)
y=list(x)
y.sort()
print(y)


####################
#3-shart
v=[]
d=[]
with open("plas.txt",'r') as fp :
    text=fp.read()
for i in text.split('\n'):
    #v.append(i.split(',')[0])
    if '0' in i and '1' in i and '2' in i and '3' in i and '4' in i and '5' in i and '6' in i and '7' in i and '8' in i and '9' in i :
        
        print(i)        






















# country=dict()
# with open("plas.txt",'r') as f:
#     ls=f.read()
# for i in ls.split('\n'):
#     l1=i.split(',')[2]
#     country[l1]=ls.count(l1)
# print(country)
'''import colorama as c
a=input("Enter text: ")
for i in range(len(a)):
    if a[i] in 'AaBbCcDdEeFfGgHh':
        print(c.Fore.RED+a[i],end='')
    if a[i] in 'IiJjKkLlMmNnOoPp':
        print(c.Fore.YELLOW+a[i],end='')
    if a[i] in 'QqRrSsTtUuVvWwXxYyZz':
        print(c.Fore.GREEN+a[i],end='')

print()'''