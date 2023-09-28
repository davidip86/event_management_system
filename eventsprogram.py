from classes import *

print(">"*43+"\n"+"DAVID'S EVENT MANAGEMENT SYSTEM\n"+">" * 43+"\n")

def mainmenu():
    min_selection = 1
    max_selection = 9
    print("Enter a number from the following menu:\n"+"~"*39)
    while True:
        try:
            menu0 = int(input("1) View all events\n2) View an individual event\n3) Add an event\n4) Edit details of an event\n5) Delete an event\n6) View all attendees at an event\n7) Add an attendee to an event\n8) Delete an attendee from an event\n9) Exit application\n"))
            if menu0 not in range(min_selection, max_selection + 1):
                print(f"Invalid option. Please enter a number between {min_selection} and {max_selection}.\n") 
            else:
                return menu0
        except ValueError:
            print("Unrecognised input. Please only enter a number 1-9 for the option you would like then press the enter key on your keyboard.")

while True:
    menu0_selection = mainmenu()

    if menu0_selection == 1: #call on Events.return_all() method in classes file to show details of all events in the database
        Events.return_all()

    if menu0_selection == 2: #calls on Events.return_value() method in classes file to show the details of an event(s)
        try:
            menu0_2 = int(input("Enter the number of the Event ID for the event you'd like to view. Alternatively enter a non number character, if you wish to search by event name/type/date :\n"))
            Events.return_value(menu0_2)
        except ValueError:
            try:
                menu0_2 = input("Search by event name, event type or event date (DD/MM/YYYY): (input needs to exact and case sensitive to find any matches in the database)\n")
                Events.return_value(menu0_2)
            except Exception:
                print("Nothing found in the database.")

    if menu0_selection == 3: #calls on Events.add_value() method in classes file to add a new event to the database
        if len(Events.read_events())>0:
            menu0_3_eventid = max(event[0] for event in Events.read_events()) + 1 #Automatically assigning an event ID based on max ID number in database plus 1
        else:
            menu0_3_eventid = 1
        print(f"New event with Event ID {menu0_3_eventid} to be created.")
        
        while True:
            menu0_3_event_name = input("Enter a name you'd like to set for this new event:\n")
            if menu0_3_event_name.strip(): # Check if input is not empty
                break
            else:
                print("Event name cannot be empty. Please enter a name.")

        # Input validation for event type
        while True:
            menu0_3_event_type = input("Enter a description for the type of event:\n")
            if menu0_3_event_type.strip():  # Check if input is not empty i.e true when a value exists
                break
            else:
                print("Event type cannot be empty. Please enter a description for the type of event.")

        # Input validation for event date
        while True:
            menu0_3_event_date = input("Enter a date for the event in the format DD/MM/YYYY:\n")
            if menu0_3_event_date.strip(): # Check if the input is not empty
                try:
                    day, month, year = map(int, menu0_3_event_date.split('/'))
                    if (1 <= day <= 31 and 1 <= month <= 12 and 2023 <= year <= 2100):  # You can adjust the year range as needed
                        break
                    else:
                        print("Invalid date format or out of range. Please use DD/MM/YYYY format.")
                except ValueError:
                    print("Invalid date format. Please use DD/MM/YYYY format.")

        print(f"\nNEW DETAILS FOR EVENT ID {menu0_3_eventid}:")
        print(f"Event Name: {menu0_3_event_name}")
        print(f"Event Type: {menu0_3_event_type}")
        print(f"Event Date: {menu0_3_event_date}") 

        confirm_add = input("Are you sure you wish to add this event to the database? Y or N:\n").lower()
        if confirm_add == 'y':
            event_to_add = Events(menu0_3_eventid, menu0_3_event_name, menu0_3_event_type, menu0_3_event_date)
            event_to_add.add_value()
        else:
            print("Cancelling the addition of this event to the database and returning to the main menu.\n")
            time.sleep(2)

    if menu0_selection == 4: #calls on Events.edit_value() method in classes file to edit the details of an event
        try:
            menu0_4_eventid = int(input("Enter the Event ID of the event you wish to edit details for:\n"))
            if type(menu0_4_eventid) == int and menu0_4_eventid in [event[0] for event in Operations.read_events()]:
                print("CURRENT DETAILS OF THE EVENT YOU WISH TO CHANGE:")
                Events.return_value(menu0_4_eventid)
                confirm = input("Are you sure you wish to continue with editing this event? Y or N:\n").lower()
                if confirm == 'y':
                    while True:
                        menu0_4_event_name = input("Enter what you'd like the event name to now be:\n")
                        if menu0_4_event_name.strip(): # Check if input is not empty
                            break
                        else:
                            print("Event name cannot be empty. Please enter a name.")

                    # Input validation for event type
                    while True:
                        menu0_4_event_type = input("Enter a description for the type of event:\n")
                        if menu0_4_event_type.strip():  # Check if input is not empty
                            break
                        else:
                            print("Event type cannot be empty. Please enter a description for the type of event.")

                    # Input validation for event date
                    while True:
                        menu0_4_event_date = input("Enter a date for the event in the format DD/MM/YYYY:\n")
                        if menu0_4_event_date.strip(): # Check if the input is not empty
                            # Check if it matches the format DD/MM/YYYY
                            try:
                                day, month, year = map(int, menu0_4_event_date.split('/'))
                                if (1 <= day <= 31 and 1 <= month <= 12 and 2023 <= year <= 2100):  # You can adjust the year range as needed
                                    break
                                else:
                                    print("Invalid date format or out of range. Please use DD/MM/YYYY format.")
                            except ValueError:
                                print("Invalid date format. Please use DD/MM/YYYY format.")

                    print(f"\nNEW DETAILS FOR EVENT ID{menu0_4_eventid}:")
                    print(f"Event Name: {menu0_4_event_name}")
                    print(f"Event Type: {menu0_4_event_type}")
                    print(f"Event Date: {menu0_4_event_date}") 

                    confirm_edit = input("Do you want to apply these changes? Y or N:\n").lower()
                    if confirm_edit == 'y':
                        event_to_edit = Events(menu0_4_eventid, menu0_4_event_name, menu0_4_event_type, menu0_4_event_date)
                        event_to_edit.edit_value()
                    else:
                        print("Cancelling the edit of this event.\n")
                else:
                    print("Cancelling and returning you to the main menu.\n")
                    time.sleep(2)
            else:
                print("No event ID with that number found. Returning you to the main menu:\n")
                time.sleep(2)     
        except:
            print("Incorrect value entered: Event ID must be a number. Returning you to the main menu:\n")
            time.sleep(2) 

    if menu0_selection == 5: #calls on Events.delete_value() method in classes file to delete an event from the database (and attendees linked to that event)
        try:
            menu0_5_eventid = int(input("Enter the Event ID number of the event you wish to delete:\n"))
            if type(menu0_5_eventid) == int and menu0_5_eventid in [event[0] for event in Operations.read_events()]:
                Events.delete_value(menu0_5_eventid)
            else:
                print("No event found with that Event ID number. Returning you to the main menu.\n")
                time.sleep(2)
        except:
            print("Invalid entry: Event ID must be a number. Returning you to the main menu.\n")
            time.sleep(2)

    if menu0_selection == 6: #calls on Attendees.return_all() method in classes file to view all the attendees at an event
        while True:
            try:
                event_id = int(input("Enter the Event ID number that you wish to show all the attendees for:\n"))
                Attendees.return_all(event_id)
                break
            except ValueError:
                print("Incorrect input. You must enter a number for event ID.")

    if menu0_selection == 7: #calls on Attendees.add_value() method in classes file to add an attendee to an event
        while True:
            try:
                event_id = int(input("Enter the Event ID you wish to add an attendee to: "))
                if type(event_id) == int and event_id in [event[0] for event in Operations.read_events()]:
                    view_attendees = input("Would you like to view a list of the attendees at that event first before entering a new attendee? Y/N:\n")
                    if view_attendees == 'y':
                        Attendees.return_all(event_id)
                        break
                    else:
                        break
                else:
                    print("No such Event ID number. Returning to main menu.")
                    break
            except ValueError:
                print("Incorrect input. You must enter a number for event ID.")
        
        while True:
            try:
                att_id = int(input("\nEnter an Attendee ID number for the person you would like to add: \n"))
                break
            except ValueError:
                print("Invalid entry: Attendee ID must be a number.\n")
    
        att_fname = input("Enter their First Name: ")
        att_sname = input("Enter their Surname: ")
        att_email = input("Enter their Email address: ")
        
        print(f"\nSummary of the attendee's details you'd like to add to Event {event_id}:")
        print("Attendee ID number:",att_id)
        print("Attendee First Name:",att_fname)
        print("Attendee First Name:",att_sname)
        print("Attendee First Name:",att_email)

        confirm = input("Do you wish to add the details of this attendee to the event? Y/N\n").lower()
        if confirm == 'y':
            a = Attendees(att_id, att_fname, att_sname, att_email)
            a.add_value(event_id)
        else:
            print("Cancelling addition of attendee to the event and returning to the main menu.\n")
            time.sleep(2)

    if menu0_selection == 8: #calls on Attendees.delete_value() method in classes file to delete an attendee from an event
        event_id = int(input("First input the Event ID number that the attendee is part of:\n"))
        att_id = int(input("Now input the Attendee ID number from the event who you would like to delete:\n"))
            
        Attendees.delete_value(event_id, att_id)

    if menu0_selection == 9:
        print("Exiting programme\n")
        time.sleep(2)
        break