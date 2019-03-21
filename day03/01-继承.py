class Animal(object):
	def eat(self):
		print("---吃")
	def drink(self):
		print("---喝")
	def sleep(self):
		print("---睡")
	def run(self):
		print("---跑")

class Dog(Animal):
	def run(self):
		print("小狗在愉快的玩耍...")
		super().run()
#		Animal().run()
dog = Dog()
dog.eat()
dog.run()
