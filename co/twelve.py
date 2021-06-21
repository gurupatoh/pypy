class NumbersIterable:
      def __init__(self ,numbers=[]):
        self._numbers=numbers
        self._index=-1
      def __iter__(self):
        return self
      def __next__(self):
        self._index+=1
        if self._index >=len(self._numbers):
            self._index =-1
            raise StopIteration
        else:
            return self._numbers[self._index]
     
niterable=NumbersIterable(["1", 2.0, "4",5,6.1,"7",8,9.2])

integer_map = map(int, niterable)
# Maps each string to an int


integer_list = list(integer_map)
# Converts mapped output to a list of ints

for i in integer_list: 
    print(i)
    