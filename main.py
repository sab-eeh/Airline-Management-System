import random
import os

def Flight_Schedule():
    f = open('Schedule.txt','r')
    show = f.read()
    print(show,"\n")
    def book_yours():
        book_my_flight = input("Do want to book your flight? (Yes/No): ")
        options = book_my_flight.lower()
        if options == 'yes':
            Flight_Booking()
        elif options == 'no':
            main()
        else:
            print("Invalid Input")
            return book_yours()
    book_yours()
    
def Flight_Booking():
    loop = True
    while loop :
        try:
            passenger_name = input("Enter your full name: ")
            if True in [i.isdigit() for i in passenger_name]:
                print("Please enter letters only.")
                break
        except:
            print("\nPlease enter valid characters.\n")
        else:    
            flight_no = input("Enter the flight number you want to book for: ")
            if True in [i.isdigit() for i in flight_no]:
                f = open('Schedule.txt','r')
            else:
                print("Not a valid entry, please enter an integer.")
                break
        schedule_lines = f.read()
        lines = schedule_lines.split()
        if str(flight_no) in lines:
            phone_number = input("Enter your Phone number: ")
            if len(phone_number) == 11:
                email = input("Enter your Email id: ")
                if '@gmail.com' not in email:
                    print("Invalid Gmail Id! Please re-enter with correct format.")
                    break
                passport_no = input("Enter your Passport number: ") 
                passport_no.upper()
                if len(passport_no) != 9:
                    break
                else:
                    fare_selection = input("Enter fare class (Business/Economy): ")             
            else:
                print("Please enter a valid number")
                break
            fare_class = fare_selection.lower()
            if fare_class == 'business' or fare_class == 'economy':
                print(f"You choosed {fare_class} Class. ")
            else:
                print("Invalid Fare Selection.")
                return fare_selection
            if passenger_name in lines and str(passport_no) in lines:
                print("You have already booked a ticket.")
                f.close()
                return Passenger_Details()
            else:
                f = open(f'{passenger_name}.txt','x')
                f = open('passengers_data.txt','+a')
                f.write(f"Passenger Name : {passenger_name} | Flight number: {flight_no} | Passpot number: {passport_no} | Class: {fare_class}")
                f.close()
            DOB = input("Enter your Date of Birth according to the format (DD/MM/YYYY): ")
            if len(DOB) == 10:
                seats = int(input("How many seats you want to reserve? "))
            else:
                print("Incorrect date format. Please follow DD/MM/YYYY format.")
                break
            for i in range(0,seats):
                seat_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                seat_choice = random.choice(seat_alphabet)
                seat_number = random.randint(1,250)
                print(f"Your seat number {i+1} is: {seat_choice}-{seat_number} ")
            f = open("passengers_data.txt",'a')
            f.write(f" | Seats: {seats}\n")
            f = open('Schedule.txt','r')
            headings = f.readline()
            for line in f.readlines():
                if str(flight_no) in line:
                    print(headings + line)
            f = open(f'{passenger_name}.txt','a')
            user_details = f.write(f"Name: {passenger_name} \nFlight number: {flight_no} \nPassport number: {passport_no} \nPhone number: {phone_number} \nEmail Address: {email} \nClass: {fare_class} \nDate Of Birth: {DOB} \nSeats Reserved: {seats} \n{headings +line } " )
            f.close()
            return Passenger_Details()
        else:
            print("Flight not available.\nPlease check the availability or choose another flight.")
            return Flight_Booking()
    Flight_Booking()
    
def Passenger_Details():
    to_see_details = input("Do want to see your flight details? (Yes/No): ")
    options = to_see_details.lower()
    if options == 'yes':
        loop = True
        while loop:
            passenger_name = input("Enter your name: ")
            if True in [i.isdigit() for i in passenger_name]:
                    print('Invalid Name! Please enter a valid name with alphabets only. ')
                    break
            else:
                flight_no = input("Enter your flight number: ")
                if True in [j.isdigit() for j in flight_no]:
                    seats = input("Enter the number of seats you reserved: ")
                    f = open("passengers_data.txt",'r')
                    data = f.read()
                    data_split = data.split()
                    if passenger_name in data_split:
                        print("Here is your flight details.")
                        f = open(f"{passenger_name}.txt" , 'r')
                        flight_details = f.read()
                        print(flight_details)
                    else:
                        print("\nError ! details not found .")
                        print(f"\nPlease book your flight: \n ")
                        return Flight_Booking()
                else:
                    print('Invalid Input! Please Enter a Valid Flight Number.')
                    print("Try Again")
                    break
    else:
        return main()
    
def Cancel_Booking():
    confirmation = input("Do you want to cancel your flight? (Yes/No): ")
    def to_check():
        loop = True
        while loop:
            answer = confirmation.lower()
            if answer == 'yes':
                passenger_name = input("Enter your full name : ")
                if True in [i.isdigit() for i in passenger_name]:
                    print('Invalid Name! Please enter a valid name with alphabets only. ')
                    break
                else:
                    flight_no = input("Enter your flight number: ")
                    if True in [i.isdigit() for i in flight_no]:
                        passport_no = input("Enter your Passport number: ")
                        if len(passport_no) != 9:
                            print('Passport Number should be exactly 9 digits long.')
                            print('Try Again')
                            break
                        else:
                            f = open('passengers_data.txt','r')
                            data = f.read()
                            data_split = data.split()
                            if passenger_name in data_split and flight_no in data_split and passport_no in data_split:
                                f = open('passengers_data.txt', 'r')
                                passengers_data = f.read()
                                f.seek(0)
                                remove = ""
                                for user_data in f.readlines():
                                    if str(flight_no) in user_data and passport_no in user_data and passenger_name in user_data:
                                            remove += user_data
                                            change = passengers_data.replace(remove,"This flight has canceled by passenger./n")
                                            f.close()
                                os.remove(f"{passenger_name}.txt")
                                f = open('passengers_data.txt', 'w')
                                f.write(change)
                                f.close()
                                print(f"{passenger_name} your flight has beed canceled.")
                                return main()
                            else:
                                print("Invalid Details! Please try again.")
                                return to_check()
                    else:
                        print('Invalid Flight Number! Please enter a valid number.')
            else:
                return main()
    to_check()      
    
    
def main():
    a = True
    while a:
        print()
        print(" **********  WELCOME TO FLIGHT BOOKING SYSTEM  *********")
        print("")
        print("1 Flight Schedule \n2 Flight Booking \n3 Passenger Details \n4 Cancel Booking \n5 Exit")
        choice = input("Enter a number: ")
        if choice == '1':
            Flight_Schedule()
        elif choice == '2':
            Flight_Booking()
        elif choice == '3':
            Passenger_Details()
        elif choice == '4':
            Cancel_Booking()
        elif choice == '5':
            a = False
            print("Good Bye")   
        else:
            print("Invalid Choice Please Try Again" )
            return main()
main()