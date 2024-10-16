from replit import db

class Event:
  def __init__(self,EventID,Title,Description,Date,Address,Participants,Link)->None:
    self.EventID = EventID;
    self.Title = Title;
    self.Description = Description;
    self.Date = Date;
    self.Address = Address;
    self.Participants = [];
    self.Participants.append(Participants);
    self.Link = Link;
    
    db["EventID"] = self.EventID;
    db["Title"] = self.Title;
    db["Description"] = self.Description;
    db["Date"] = self.Date;
    db["Address"] = self.Address;
    db["Participants"] = self.Participants;
    db["Link"] = self.Link;

  pass
  pass
def modify(property,modification):
    if property == "Title":
      #self.Titale = modification;
      db["Title"] = modification 
    elif property == "Description":
      #self.Description = modification;
      db["Description"] = modification
    elif property == "Date":
      #self.Date = modification;
      db["Date"] = modification
    elif property == "Address":
      ##self.Address = modification;
      db["Address"] = modification
    elif property == "Link":
      #self.Link = modification;
      db["Link"] = modification
    
    pass


def delete(Title):
  if db["Title"]==Title:
    del db["Title"], db["Description"], db["Date"], db["Address"], db["Participants"], db["Link"];
  pass

def FormattedStr():
  return (f"Title: {db['Title']}\nDescription: {db['Description']}\nDate:{db['Date']}\nAddress: {db['Address']}\nParticipants: {db['Participants']}\nLink: {db['Link']}");

def addParticipant(Participant):
    
  db["Participants"].append(Participant);
  pass

def removeParticipant(Participant):
  db["Participants"].remove(Participant);
  pass
