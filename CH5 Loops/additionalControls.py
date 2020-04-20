a="Python"
b=''
auth=False
max_attm=5
count=0
while a!=b:
    count+=1
    if count>max_attm:
        break
    if count==3:
        continue
    b=input("{}: what is the secret word?".format(count))
else:
    auth=True

print("Authorized"  if auth else "calling FBI ...")



