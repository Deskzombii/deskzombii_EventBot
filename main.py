from replit import db

class Event:
  def __init__(self,Title,Description,Date,Address,Participant,Link)->None:
    self.Title = Title;
    self.Description = Description;
    self.Date = Date;
    self.Address = Address;
    self.Participants = [];
    self.Participants.append(Participant);
    self.Link = Link;
    db[self.Title] = [self.Title, self.Description, self.Date, self.Address, self.Participants, self.Link];
    print(db[self.Title])
  pass

  def modify(self,property,modification):
    if property == "Title":
      self.Title = modification;
    elif property == "Description":
      self.Description = modification;
    elif property == "Date":
      self.Date = modification;
    elif property == "Address":
      self.Address = modification;
    elif property == "Link":
      self.Link = modification;
    
    pass
  pass

  def delete(Title):
    if db[Title]==TRUE:
      del db[Title];
    pass

  def addParticipant(self,Participant):
    self.Participants.append(Participant);
    pass

  def removeParticipant(self,Participant):
    self.Participants.remove(Participant);
    pass
Main_Event = Event("BlueDream", "Come One, Come All for a Blues Harmonica Jam Sesh!",10/9/2024,"80 University Ave W, Waterloo, ON N2L 3C7","Lucky",None)

Main_Event.addParticipant("Cyro")

print(Main_Event.Participants)

Main_Event.removeParticipant("Cyro")

print(Main_Event.Participants)
