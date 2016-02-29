total = [1, 2, 3, 4, 5]
buahan = ['apples', 'oranges', 'pears', 'apricots']
ubah = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in total:
	print "This is count %d" % number

# same as above
for buah in buahan:
	print "Buah itu tipe dari buah: %s" % buah

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for  i in ubah:
	print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(1,10):
	print "Adding %d to the list." % i
	# append is a function that lists understand
	elements.append(i)

# now we can print them out too
for i in elements:
	print "Element was: %d" % i