This is the main branch of the deskzombii Event Bot repl on repl.it. It features code that when executed provides a system for creating events,
modifying event object properties, deleting events, adding new participants, deleting new participants. This is the new framework for which I
will be making changes to. The main changes that currently begs for my attention is: the conversion of code inputs to chat inputs. In layman's 
terms, this means that instead of code in the format of:

Return_Var = Function_Name(ParameterOne,ParameterTwo,...,ParameterK)

The Chat input will be in the format of:

$Function_Name ParamterOne ParameterTwo ... ParameterK

Utilizing each function, we shall convert them to chat commands:

Main_Event = Event("BlueDream", "Come One, Come All for a Blues Harmonica Jam Sesh!",10/9/2024,"80 University Ave W, Waterloo, ON N2L 3C7",
"Lucky",None)

$NewEvent "BlueDream" "Come One, Come All for a Blues Harmoniuca Jam Sesh!" "10/9/2024" "80 University Ave W, Waterloo, ON N2L 3C7" "[Lucky]"
"None"

Main_Event.addParticipant("Cyro")

$JoinEvent "Cyro"

Main_Event.removeParticipant("Cyro")

$LeaveEvent "Cyro"

This is the first consideration when translating pure pythonXRepl code into language that discord users can understand. The next consideration
is simply to understand how the discord api works. This can be done in 10 minutes. 

intents = discord.Intents.default()
intents.message_content = True

intents = discord.Intents.default()
intents.message_content = True
