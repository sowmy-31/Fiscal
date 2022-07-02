import sqlite3 as s

c = s.connect("apple.db")
try:
    c.execute("Create table movies(name ,actor ,actress ,director ,year );")
   

except:

     pass

uni = ''
while(uni != '4'):
    print("(2) Insert\n(3) show all \n(4) search \n(5) quit ")
    uni = input ("ENTER OPTIONS:")
    if(uni == '2'):
        name = input ("Enter the name:")
        actor = input ("Enter the actor:")
        actress = input ("Enter the actress:")
        director = input ("Enter the director:")
        year = input ("Enter the year:")
        c.execute(f'insert into movies values("{name}","{actor}","{actress}","{director}","{year}");')
        c.commit()
    elif(uni == '3'):
        print("name * actor  * actress  *  director  *  year)")
        for i in c.execute("select * from movies;"):
            for j in i:
                print(j +" * ", end='' )
            print()
    elif(uni == '4'):
        x = input("Column name:")
        y = input("Enter value:")
        print("(name, actor, actress, director, year)")
        for i in c.execute(f'select * from movies where {x}="{y}";'):
            print(i)
            