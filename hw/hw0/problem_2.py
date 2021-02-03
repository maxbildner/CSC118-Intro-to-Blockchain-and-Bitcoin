# 2/1/21, HW0

#*******************************************************************************
# 2)
# Write a class called AverageStream which, when instantiated, accumilates 
# numbers and outputs an average of all the numbers ever input into it. Thus:
# Write the class such that it does not keep a very large list stored within the 
# object. In other words, if you call add_element() 10 times, there should not be a
# list of size 10 containing each of the input numbers.

def main():

  class AverageStream:

    def __init__(self):
      self.sum = 0
      self.size = 0

    def add_element(self, number):
      self.sum += number
      self.size += 1

    def get_average(self):
      return self.sum/self.size


  avg_inst = AverageStream()
  avg_inst.add_element(5)            #=> None
  print(avg_inst.get_average())      #=> 5.0
  avg_inst.add_element(3)            #=> None
  print(avg_inst.get_average())      #=> 4.0



if __name__ == '__main__':
  main()