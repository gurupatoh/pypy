# define Person class using class keyword
class Person:
	# initilization 
	def _init_(self, names, age):
		# if names length is less than 1 means zero than
		# it will not create any object of Person
		# instead of it, it will throw an error
		if len(names)<1:
			raise TypeError("Name should be of more than zero length")

		# variables
		self.__names=names
		self.__age=age

	# getFullName method
	def getFullName(self):
		return ' '.join(self.__names)

	def birthday(self):
		self.__age+=1

	def getAge(self):
		return self.__age

	def getNameHarvardFromat(self):
		return self._names[-1]+', '+''.join([name[0] for name in self._names[:-1] ])

	# additional task
	def _str_(self):
		return 'Person: Name=\''+self.getFullName()+'\', Age='+str(self.getAge())

	def _repr_(self):
		return self.getNameHarvardFromat()

class Book:
	def _init_(self, authors, title, publisher, year, place):
		self.__authors=authors
		self.__title=title
		self.__publisher=publisher
		self.__year=year
		self.__place=place

	def displayAuthors(self):
		print(self.__authors)
	def getHarwardRefrence(self):
		book=''
		book=self.__authors[0].getNameHarvardFromat()
		
		if len(self.__authors)>1:
			for person in self.__authors[1:-1]:
				book+=', '
				book+=person.getNameHarvardFromat()
				
			book+=' & '
			book+=self.__authors[-1].getNameHarvardFromat()

		book+=' '
		book+=str(self.__year)
		book+=', '
		book+=self.__title
		book+=', '
		book+=self.__publisher
		book+=', '
		book+=self.__place
		return book

	def _str_(self):
		return self.getHarwardRefrence()


# Testing code
programmer = Person(['Augusta', 'Ada', 'King'], 36)

print(programmer.getFullName(), 'is', programmer.getAge())
programmer.birthday()
print(programmer.getFullName(), 'is', programmer.getAge())
print(programmer.getNameHarvardFromat())
print(programmer)

# p=Person([],45)
engineer = Person(['Charles','Babbage'],50)
actualAuthor = Person(['Sydney','Padua'],30)
book = Book([programmer, engineer, actualAuthor], 'The Thrilling Advantures of Lovelace and Babbage', 'Penguin Books', 2015, 'Westminister')
print(book)
book.displayAuthors()