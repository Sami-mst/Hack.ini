from distutils.command.sdist import sdist
from pwn import *
r=remote("zero-to-hero.challs.shellmates.club",443,ssl=True)
text= r.recvline().decode('utf-8')
#r.send(winner.encode()+b'\n')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
text= r.recvline().decode('utf-8')
dict={}
text= r.recvline().decode('utf-8').split(" ")
dict[text[2]]=text[7][:-1].split("-")
m=10
while 1:
    i=0
    while i<m-1:
        text= r.recvline().decode('utf-8').split(" ")
        dict[text[2]]=text[7][:-1].split("-")
        i+=1
    skills=[]

    for i in dict.keys():
        if dict[i][0]=="":
            skills.append(i)
    i=0
    while i<m:
        for j in dict.keys():
            if j not in skills:
                if all(item in skills for item in dict[j]):
                    skills.append(j)
        i+=1
    if len(skills)==m:
        tosend="-".join(skills)
        print(tosend)
        r.send(tosend.encode()+b"\n")
    else:
        r.send(b"impossible"+b"\n")
        print("imposible")

    dict={}
    m+=1
    text= r.recvline().decode('utf-8').split(" ")
    print(text)
    dict[text[4]]=text[9][:-1].split("-")