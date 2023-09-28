from abc import ABC, abstractmethod
import json
import time

class Operations(ABC):
    @abstractmethod
    def add_value():
        pass
    
    @abstractmethod
    def edit_value():
        pass

    @abstractmethod
    def delete_value():
        pass

    @abstractmethod
    def return_value():
        pass

    @abstractmethod
    def return_all():
        pass

    @staticmethod
    def read_events():
        try:
            with open('eventdatabase.json', 'r') as file:
                listof_event_lists = [json.loads(line) for line in file]
        except (FileNotFoundError, json.JSONDecodeError):
            listof_event_lists = []
        return listof_event_lists

# creating an events class 
class Events(Operations):
    def __init__(self, event_id:int, event_name:str, event_type:str, event_date:str):
        self.event_id = event_id
        self.__event_name = event_name
        self.event_type = event_type
        self.event_date = event_date
        self.listof_event_lists = super().read_events()

        @property 
        def event_name(self):
            return self.__event_name
        @event_name.setter
        def event_name(self, event_name):
            self.__event_name = event_name
    
    def return_all():
        for event in Operations.read_events():
            print("Event ID:", event[0])
            print("Event Name:", event[1])
            print("Event Type:", event[2])
            print("Event Date:", event[3])
            print("=" * 23)
        print("Completed. Returning you to the main menu.\n")
        time.sleep(2)

    def add_value(self):
        event = [self.event_id, self.__event_name, self.event_type, self.event_date]
        self.listof_event_lists.append(event)
        with open('eventdatabase.json', 'a') as file:
            json.dump(event, file)
            file.write('\n')
            print("Event details recorded to the database successfully!")
        print("Returning you to the main menu.\n")
        time.sleep(2)

    def return_value(*args):
        event_list = Operations.read_events()
        found_events = False
        for event in event_list:
            if all (arg in event for arg in args):
                found_events = True
                print("Event ID:", event[0])
                print("Event Name:", event[1])
                print("Event Type:", event[2])
                print("Event Date:", event[3])
                print("=" * 20)
        time.sleep(2)
        if not found_events:
            print("EVENT INFORMATION NOT FOUND. SEE A LIST OF ALL EVENTS IN THE DATABASE:\n")
            Events.return_all()
        time.sleep(2)
    
    def edit_value(self):
        event_ids = [event[0] for event in self.listof_event_lists]
        if self.event_id not in event_ids:
            print("Event ID not found in the database.")
            return
        for event in self.listof_event_lists:
            if event[0] == self.event_id:
                event[1] = self.__event_name
                event[2] = self.event_type
                event[3] = self.event_date
                break
        with open('eventdatabase.json', 'w') as file:
            for event in self.listof_event_lists:
                json.dump(event, file)
                file.write('\n')
            print("Event details updated successfully! Returning you to the main menu.\n")
            time.sleep(2)

    def delete_value(self):
        event_ids = [event[0] for event in Operations.read_events()]
        if self not in event_ids:
            print("Event ID not found in the database.")
            return
        Events.return_value(self)
        deleteconfirmation = input("ARE YOU SURE YOU WISH TO DELETE THIS RECORD? \nEnter 'Y' to confirm deletion, or any other letter if you've changed your mind: ").lower()
        if deleteconfirmation == "y":
            new_event_list = [event for event in Operations.read_events() if event[0] != self]
            with open('eventdatabase.json', 'w') as file:
                for event in new_event_list:
                    json.dump(event, file)
                    file.write('\n')
                print("Event deleted successfully! Returning you to the main menu.\n")
                time.sleep(2)
        else:
            print("Deletion of that event has NOT been carried out. Returning you to the main menu.\n")
            time.sleep(2)

class Attendees(Events, Operations):
    def __init__(self, att_id:int, att_fname:str, att_sname:str, att_email:str):
        self.att_id = att_id
        self.att_fname = att_fname
        self.att_sname = att_sname
        self.att_email = att_email
        self.listof_event_lists = super().read_events()

    def return_all(event_id):
        event_list  = Events.read_events()
        for event in event_list:
            if event[0] == event_id:
                print (f"EVENT ID:{event[0]} EVENT NAME: {event[1]} TYPE: {event[2]} DATE: {event[3]}")
                print('Total Attendees:', len(event[4:]))
                for attendee in event[4:]:
                    print(f"AttendeeID:{attendee[0]} Name:{attendee[1]} Surname:{attendee[2]} Email:{attendee[3]}")
                break
        if event[0] != event_id:
            print("No event found for that event ID number. Returning to the main menu.\n")
            time.sleep(2)

    def add_value(self, event_id):
        event_list = Operations.read_events()
        attendee = [self.att_id, self.att_fname, self.att_sname, self.att_email]
        
        for event in event_list:
            if event[0] == event_id:
                #list comprehension script to extract a list of attendee id's within the specified event to try and ensure unique attendee id's are within an event
                if self.att_id not in [elements[0] for elements in event[4:]]:
                    event.append(attendee)
                    with open('eventdatabase.json', 'w') as file:
                        for attendee_add in event_list:
                            json.dump(attendee_add, file)
                            file.write('\n')
                    print("Attendee added to the event successfully. Returning to the main menu.\n")
                    time.sleep(2)
                    break
                if self.att_id in [elements[0] for elements in event[4:]]:
                    print('An attendee with that attendee ID number already exists in that event. Attendee not added. Returning to main menu')
                    time.sleep(2)
                    break
        else:
            print(f"Event ID {event_id} not found. Returning to the main menu.\n")
            time.sleep(2)

    def delete_value(event_id, att_id):
        event_list = Operations.read_events()

        for event in event_list:
            if event[0] == event_id:
                if att_id not in [elements[0] for elements in event[4:]]:
                    print("An attendee with that ID doesn't exist for that event so cannot be deleted.\n")
                    time.sleep(2)
                    break
                else:
                    for att_id in [elements[0] for elements in event[4:]]:
                        print(f"Event and Attendee Details: {event}")
                        delete_confirmation = input("ARE YOU SURE YOU WISH TO DELETE THIS ATTENDEE FROM THIS EVENT? \nEnter 'Y' to confirm deletion OR if you wish to abort enter any other character instead: ").lower()
                        if delete_confirmation == "y":
                            event[4:] = [elements for elements in event[4:] if elements[0] != att_id]
                            with open('eventdatabase.json', 'w') as file:
                                for event_item in event_list:
                                    json.dump(event_item, file)
                                    file.write('\n')
                            print("Attendee deleted from the event successfully.\n")
                            time.sleep(2)
                            break
                        else:
                            print("Deletion aborted.\n")
                            time.sleep(2)    
            else:
                print(f"Event ID {event_id} not found.\n")
