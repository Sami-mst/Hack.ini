from pwn import *
f=""
prev = {"winner":"hi" , "points":0}
j=1
def calc(a,b):
    if a==b:
        return 0    
    if a=="S" and b=="R":
        return -1
    if a=="S" and b=="P":
        return 1
    if a=="R" and b=="S":
        return 1
    if a=="R" and b=="P":
        return -1
    if a=="P" and b=="S":
        return -1
    if a=="P" and b=="R":
        return 1

r=remote("rps.challs.shellmates.club",443,ssl=True)
sum_alice=0
sum_bob=0
while j<96:
    alice= r.recvline().decode('utf-8')
    alice=alice.split(" ")[1]
    bob= r.recvline().decode('utf-8').split(" ")[1]
    for i in range(0,len(alice)):
        value = calc(alice[i],bob[i])
        if value ==1:
            if prev["winner"]=="alice":
                prev["points"]*=2
                sum_alice+=prev["points"]
            else:
                sum_alice+=3
                prev["points"]=3
                prev["winner"]="alice"
        elif value==-1:
            if prev["winner"]=="bob":
                prev["points"]*=2
                sum_bob+=prev["points"]
            else:
                sum_bob+=3
                prev["points"]=3
                prev["winner"]="bob"
        elif value==0:
            prev = {"winner":"hi" , "points":0}
            sum_bob+=1
            sum_alice+=1
    if sum_alice>sum_bob:
        winner=f"A:{sum_alice-1}"
    elif sum_alice<sum_bob:
        winner=f"B:{sum_bob-1}"
    else:   
        winner="D"
    
    r.send(winner.encode()+b'\n')
    print(j)
    j+=1
    text= r.recvline().decode('utf-8')
    print(text)
    sum_alice=0
    sum_bob=0
    prev = {"winner":"hi" , "points":0}

flag = r.recvline().decode('utf-8')
print(flag)
flag = r.recvline().decode('utf-8')
print(flag)
flag = r.recvline().decode('utf-8')
print(flag)
flag = r.recvline().decode('utf-8')
print(flag)