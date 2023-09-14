def caught(speed,bday):
    if(bday==True):
        speed=speed-5
    if(speed<=60):
        print('No Challan')
    elif(61<=speed<=80):
        print('Small Challan')
    else:
        print('Heavy Challan')
    
caught(81,False)