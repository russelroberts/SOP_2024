class Guest:
    def __init__(self,name,age,ppt_no) -> None:
        self.name=name
        self.age=age
        self.ppt=ppt_no
    def __str__(self) -> str:
        return f"{self.name}({self.age})" # not sure if I should includ passport no here, seems a bit combersum, 
    #perhaps a method show guest details instead?

    def show_guest_details(self) ->str:
       return f"{self.name}({self.age}) passport no:{self.ppt}"
#*************************************************
    
class Room:
    def __init__(self,room_no,price_pernight,room_type):
        self.room_no = room_no
        self.price_pernight = price_pernight
        self.occupants=[]
        self.room_type=room_type

    def __str__(self): #show full detalis??
        return f"{self.room_no}(roomtype:{self.room_type} @${self.price_pernight}USD per night)"
    
    def add_guest(self,newOccupant):
        self.occupants.append(newOccupant)
        print("Successfully added Guest")
        input("press any key to continue")
    
    def guestsByAge(self,this_age):
       return [guest for guest in self.occupants if guest.age == this_age]

    def guestsByName(self,this_name):
       return [guest for guest in self.occupants if guest.name == this_name]
    
    def AtMaxCapacity(self) ->bool:
       if (self.room_type.upper() == "SINGLE") and (len(self.occupants) ==1):
            return True
       elif (self.room_type.upper() == "DOUBLE") and (len(self.occupants) == 2):
           return True
       elif (self.room_type.upper() == "FAMILY") and (len(self.occupants) == 4):
          return True
       else:
          return False
#******************************************************

class Hotel:
    def __init__(self): # hotel constructed with rooms.not sure if we were supposed to pull this from a file tho.?
        self.rooms=[
            Room("01","120","single"), # floor 1
            Room("02","220","double"),
            Room("03","300","family"),
            Room("11","120","single"), #floor 2
            Room("12","220","double"),
            Room("13","300","family"),
            Room("21","120","single"), #floor 3
            Room("22","220","double"),
            Room("23","300","famliy")
        ]
   
    def isValid_roomno(self,roomno)->bool:
        curRoom = [selRoom for selRoom in self.rooms if selRoom.room_no ==roomno ]
        if len(curRoom)==0:
           return False
        else:
           return True
    
          
    def get_room_by_roomno(self,roomno)->Room:
      curRoom = [selRoom for selRoom in self.rooms if selRoom.room_no ==roomno ]
      if len(curRoom)==1:
         return curRoom[0] #not all paths return ..
        
    #for fullfillment of assignment requirements
    def check_in(self,newGuest,roomno):
       #get room by roomno
       curRoom = self.get_room_by_roomno(roomno)
       if curRoom.AtMaxCapacity() ==False:
          curRoom.add_guest(newGuest)
       else:
          print("selected room at max capacity..returning to menu")
#****************************************************    
   #find this worked better for the scenario in my head, but buggy..
   
    def check_in_multiple(self,roomno):
       #get room by roomno
       curRoom = self.get_room_by_roomno(roomno)
       if curRoom.AtMaxCapacity() == False:
          maxGuest=0
          if (curRoom.room_type.upper() == "SINGLE") and (len(curRoom.occupants) ==0):
                maxGuest=1
          elif (curRoom.room_type.upper() == "DOUBLE") and (len(curRoom.occupants) < 2):
             maxGuest=2
          elif (curRoom.room_type.upper() == "FAMILY") and (len(curRoom.occupants) < 4):
            maxGuest=4

          print(f"This room accomodates {maxGuest} guests, and has {len(curRoom.occupants)} how many will you be entering ?")
          noOfGuests=5
          while noOfGuests not in [1,2,3,4]:
            noOfGuests=int(input(f"Enter a value between 1 and {maxGuest}")) #input comes as string so convert

          x=len(curRoom.occupants)
          while x <= noOfGuests:
            #get new instance fo guest for check-in
            newGuest =Guest(input("guest name:"),input("Guest age:"),input("Guest Pass Port number:"))
            curRoom.add_guest(newGuest)
            x=x+1 
          else:
             print("Check-in successful")
       else:
          print("Room is at max capacity")
       
    #************************************   
    def check_out(self,roomno):
        selRoom= self.get_room_by_roomno(roomno)
        selRoom.occupants.clear()
        print("check out Successful")    
    
    def get_guests(self, roomno):
        selRoom=self.get_room_by_roomno(roomno)
        print("room : ",selRoom.room_no,"Occupants : ")
        for occupant in selRoom.occupants:
           print (f"--{occupant}")
    
    def get_rooms(self):
       for room in self.rooms:
          print(room)

    def get_occupied_rooms(self):
       print("Occupied Rooms")
       occupied_rooms=[room for room in self.rooms if len(room.occupants) > 0 ]
       
       if len(occupied_rooms) > 0 :
        for room in occupied_rooms: #__str__ only works per instance not for entire set
           print(room)
       else:
        print("All Rooms available")

    def get_avail_rooms(self):
       availrooms=[room for room in self.rooms if len(room.occupants)==0 ]
       
       if len(availrooms) > 0 :
        for room in availrooms: #__str__ only works per instance not for entire set
           print(room)
       else:
        print("No Rooms available")
    
    def get_guests_by_age(self, age):
       #get rooms with occupants
       occupiedRooms = [room for room in self.rooms if len(room.occupants) > 0 ]
       if len(occupiedRooms)==0:
          print("No rooms occupied at the moment")
       else:
          for room in occupiedRooms:
             print(room)
             print("Guests at age :",age)
             myoccupants = room.guestsByAge(age)
             if len(myoccupants) >0 :
                for guest in myoccupants: #__str__ only works per instance not for entire set
                 print(guest)
      

    def get_guests_by_name(self,name):
       #get rooms with occupants
       occupiedRooms = [room for room in self.rooms if len(room.occupants) > 0 ]
       if len(occupiedRooms)==0:
          print("No rooms occupied at the moment")
       else:
          for room in occupiedRooms:
             print(room)
             print("Guests with name :",name)
             myoccupants = room.guestsByName(name)
             if len(myoccupants) >0 :
                for guest in myoccupants: #__str__ only works per instance not for entire set
                 print(guest)

#**************************************************************

#Menu area for testing.
choice=0
myHotel = Hotel()
#load old school cli menu
while choice != "x" :
   print("*******HOTEL MANAGEMENT**********")
   print ("Press 0 - check in(simple)")
   print ("Press 1 - check in")
   print ("Press 2 - check out")
   print ("Press 3 - List Guests")
   print ("Press 4 - List All Rooms")
   print ("Press 5 - List Available Rooms")
   print ("Press 6 - List Guests of age x")
   print ("Press 7 - List Guests with name x")
   print ("Press x - exit")
   print("***********************************")             
   choice =input("Please enter a Value From above : ")
   #wanted to use match-case but nt covered yet so.. 
   if choice == "0":
      print("AVailable rooms:")
      print(myHotel.get_avail_rooms())
      roomno =input("Please select a Room : ")
      if myHotel.isValid_roomno(roomno) ==False:
         print("Invalid room no...returning to menu")
      else:
         newGuest =Guest(input("guest name:"),input("Guest age:"),input("Guest Pass Port number:"))
         myHotel.check_in(newGuest,roomno)
         
   elif choice == "1":
      print("AVailable rooms:")
      print(myHotel.get_avail_rooms())
      roomno =input("Please enter a Room : ")
      if myHotel.isValid_roomno(roomno) ==False:
         print("Invalid room no...returning to menu")
      else:
         myHotel.check_in_multiple(roomno)
   elif choice == "2" :
      myHotel.get_occupied_rooms()
      selected_roomno = input("Enter room Number for checkout (from above)")
      if myHotel.isValid_roomno(selected_roomno) ==False:
         print("Invalid room no... returning to menu")
      else:
         myHotel.check_out(selected_roomno)
   elif choice == "3":
      myHotel.get_occupied_rooms()
      selroomno=input("Enter the room number to list guests for (from above) : ")
      if myHotel.isValid_roomno(selroomno) == False:
         print("Invalid Room no... returning to menu")
      else:
         myHotel.get_guests(selroomno)
   elif choice =="4":
      print("All Rooms : ")
      myHotel.get_rooms()
      choice = input("press any key to continue")
   elif choice =="5":
      print("Available Rooms : ")
      myHotel.get_avail_rooms()
      choice = input("press any key to continue")
   elif choice == "6":
      myHotel.get_guests_by_age(input("Enter Age Value to search for :"))
   elif choice =="7":
      myHotel.get_guests_by_name(input("Enter the name to search for :"))
   elif choice =="x":
      print("Thank you, please come again!!!")
   else:
      print("invalid Entry")
    