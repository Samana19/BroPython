#if statement

age=int(input("Enter your age :"))
if age==100:
    print('You are a century old!')
elif age>=18 :
    print("You are an adult! ")
elif age<=18:
    print('You are a minor!')
else:
    print('!invalid age!')
