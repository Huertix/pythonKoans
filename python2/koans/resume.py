#LISTS
empty_list = list()
nums[0:] = [1] # pos and value
self.assertEqual([5, 1, -3], range(5, -7, -4))
knight.insert(2, 'not')
stack.append('last')
stack.pop(1) # pos to pop

queue = deque([1, 2])
queue.append('last')
queue.popleft()
list(queue)

set(mlist) # not repated



#TUPLES
list_count = list(count_of_three)
list_count.append("boom")
count_of_three = tuple(list_count)

('S', 'u', 'r', 'p', 'r', 'i', 's', 'e', '!') == tuple("Surprise!")


#DICCS

cards = {}.fromkeys(
            ('red warrior', 'green elf', 'blue valkyrie', 'yellow dwarf',
             'confused looking zebra'),
            42)

#STRINGS

decimal_places = 4
string = "The square root of 5 is {0:.{1}f}".format(math.sqrt(5), decimal_places)

string = "the,rain;in,spain"
pattern = re.compile(',|;')
words = pattern.split(string)

words = ["Now", "is", "the", "time"]
joines_words = ' '.join(words)

#reverse
name[::-1]




'my_global_function\(\) takes exactly 2 arguments \(3 given\)'


#FUNCTION

def function_with_the_same_name(self, a, b):
    return a + b


def function_with_the_same_name(a, b):  # global function without self
    return a * b


#STATEMENTS
round_table = [
            ("Lancelot", "Blue"),
            ("Galahad", "I don't know!"),
            ("Robin", "Blue! I mean Green!"),
            ("Arthur", "Is that an African Swallow or European Swallow?")
        ]
        result = []
        for knight, answer in round_table:
            result.append("Contestant: '" + knight + \
            "'   Answer: '" + answer + "'")


#SETS
"""http://www.python-course.eu/sets_frozensets.php"""


#ITERATORS
it = iter(range(1, 6))
stages = iter(['alpha', 'beta', 'gamma'])


#map & filter & reduce ???


#List Comprehensions
"""
    S = {x² : x in {0 ... 9}}
    V = (1, 2, 4, 8, ..., 2¹²)
    M = {x | x in S and x even}

    >>> S = [x**2 for x in range(10)]
    >>> V = [2**i for i in range(13)]
    >>> M = [x for x in S if x % 2 == 0]

    https://jeffknupp.com/blog/2013/04/07/improve-your-python-yield-and-generators-explained/
"""

feast = ['lambs', 'sloths', 'orangutans', 'breakfast cereals',
            'fruit bats']

comprehension = [delicacy.capitalize() for delicacy in feast]
comprehension = [delicacy for delicacy in feast if len(delicacy) > 6]

list_of_tuples = [(1, 'lumberjack'), (2, 'inquisition'), (4, 'spam')]
comprehension = [ skit * number for number, skit in list_of_tuples ]

list_of_eggs = ['poached egg', 'fried egg']
list_of_meats = ['lite spam', 'ham spam', 'fried spam']
comprehension = [ '{0} and {1}'.format(egg, meat) for egg in list_of_eggs for meat in list_of_meats]

comprehension = { x for x in 'aabbbcccc'}
'abc' == comprehension

# Generators & Yield



#print
print '%s : %d' % (number, c[number])



#-------- CLASSES ------------------------------------------

#
# MRO = Method Resolution Order
#
mro = type(self.Spiderpig()).__mro__
self.assertEqual('Spiderpig', mro[0].__name__)
self.assertEqual('Pig', mro[1].__name__)

#-------------------------------------------

name = property(get_name, set_name)

#-------------------------------------------

self.assertEqual('contemplate_koans', contemplate_koans.__name__)

#-------------------------------------------

fido = self.Dog()
self.assertEqual(18, len(dir(fido)))

#-------------------------------------------

class Dog(object):
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

chico = self.Chihuahua("Chico")
self.assertEqual("Chico", chico.name)

#-------------------------------------------


class BullDog(Dog):
    def bark(self):
        return super(AboutInheritance.BullDog, self).bark() + ", GRR"

# -------------------------------------------

max = functools.partial(self.maximum) --> max(7, 23) # max is now the function

#-------------------------------------------

@doubleit
    def foo(self):
        return "foo"   --> # return "foo, foo"

self.sound_check = self.doubleit(self.sound_check) --> # same stuff

#-------------------------------------------

@documenter("Increments a value by one. Kind of.")
    def count_badly(self, num):
self.count_badly.__doc__


# ---------------Inheritance------------------

class Spiderpig(Pig, Spider, Nameable):



# ------------ ERRORS -------------------

 StandardError, AttributeError

"'X' object has no attribute 'Y'"






