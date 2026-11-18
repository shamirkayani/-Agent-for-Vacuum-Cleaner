room_status = {'A':'Dirty' , 'B' : 'Dirty'}
agent_locat = 'A'

for step in range(1,5):
    current_locat = agent_locat
    current_status = room_status[current_locat]
    print(f"The cuurent location is {agent_locat}")

    if current_status=="Dirty":
        action ="Suck"
    elif current_locat=='A':
        action="Right"
    elif current_locat=='B':
        action= "Left"
    print(f"The current action is {action}")

    if action=="Suck":
        print(f"Sucking dirt in the room {current_locat}")
    elif action=="Right":
        print(f"Moving to B")
    elif action=="Left":
        print("Moving to A")

    if action=="Suck":
        room_status[current_locat] = 'Clean'
    elif action=="Right":
        agent_locat ='B'
    elif action=="Left":
        agent_locat='A'
    print(f"Environment changes{room_status} , agent at {agent_locat} ")


    
        
