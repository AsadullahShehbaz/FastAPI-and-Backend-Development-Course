from typing import Annotated 

temp : float = 25.5 

temperature : Annotated[float,"Celcius"]

Celcius = Annotated[float,"Celcius"]

temp2 : Celcius = 25.2

print(Celcius.__origin__)
print(Celcius.__metadata__)

