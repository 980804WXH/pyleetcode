

def show_guest(guest):
    for i in guest:
        print(f'we need to invite {i}')
    print("\n",end='')

# 邀请宾客小程序
guest = ['A','B','C']
show_guest(guest)

guest.remove('A')
show_guest(guest)
guest.append('D')
show_guest(guest)
guest.insert(0,'S1')
guest.insert(int(len(guest)/2),'S2')
show_guest(guest)

while len(guest)>2:
    temp=guest.pop()
    print(temp,end=' ')
print()
show_guest(guest)                                                                                                                                                                                                                    