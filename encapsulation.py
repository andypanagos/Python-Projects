

##Encapsulation assignment
##Andy Panagos
##9/26/2022



##Set protected variables
class myPlayer():
  def __init__(self,height,weight):
    self.__height=height
    self.__weight=weight

  def set_weight(self): 
    self.__weight=225 #private method

  def get_weight(self): #private method
    return self.__weight
    
  def __data_print(self): # private method
    print("The weight of this player is stored within a private method")  


if __name__ == "__main__":
  playerone = myPlayer(62,225)
  print("The weight of this player is {}. ".format(playerone.get_weight())) 
   
