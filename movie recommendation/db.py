import psycopg2
import datetime
import datetime

date = datetime.datetime.now().date()
con = psycopg2.connect(
    host = "127.0.0.1",
    database = "movierecommender",
    user = "postgres",
    password = "admin",
    port="5432")

cur=con.cursor()

firstnam="qweee"
lastnam="hjvysafgya"
phon=int(51684845864)
dob=datetime.date(2005,11,1)
ge="male"
gen = "sports,thriller,action"
email="qsawjqqab@htsfdss.com"
passw="nbsdvhb"




def lst2pgarr(alist):
    return '{' + ','.join(alist) + '}'

cur.execute("select * from public.user")

cur.execute("INSERT INTO public.user (firstname,lastname,phone,gender,genre,dob,email,passw) \
      VALUES (%s,%s,%s::bigint,%s,%s,%s::date,%s,%s)",(firstnam,lastnam,phon,ge,gen,dob,email,passw));

a='bhairavn22@gmail.com'
cur.execute("select email from public.user where email ='"+a+"'")
data=cur.fetchone()[0]
print(data)
rows = cur.fetchall()


def lst(a):
    for i in a:
        print(i)

for row in rows:
    print ("ID = ", row[0])
    print ("firstNAME = ", row[1])
    print ("lastNAME = ", row[2])
    print ("phone = ", row[3])
    print ("gender = ", row[4])
    t=row[5].split(',')
    t.append('emotional')
    # print(type(row[6]))
    # print(type(str(','.join(t))))
    print ("genre = ",row[5])
    print ("email = ", row[6])
    print ("password = ", row[7], "\n")


cur.close()
# con.commit()
con.close()




# pyarray = ['pippo', 'minni', 1, 2]

# conn = psycopg2.connection (  HERE PUT YOUR CONNECTION STRING  )
# c = conn.cursor()

# c.execute('select ... where pgarray_attr = %r' % (lst2pgarr(pyarray))
# c.execute('insert into tab(pgarray_attr) values (%r)' % (lst2pgarr(pyarray))
