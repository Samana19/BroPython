#slicing: create a substring by extracting elements from another string
#         indexing[] or slice()
#         [start:stop:step]

name="Samana Shrestha"
first_name=name[:6]
print(first_name)
second_name=name[7:]
print(second_name)
funky_name= name[::2]
print(funky_name)
reverse_name=name[::-1]
print(reverse_name)

website="http://google.com"
slice=slice(7,-4)
print(website[slice])
