try:
    with open("first.txt" "r") as f:
        print(f.read())
except Exception as e:
    print (e)

try:
    with open("second.txt" "r") as f:
        print(f.read())
except Exception as e:
    print (e)

try:
    with open("third.txt" "r") as f:
        print(f.read())
except Exception as e:
    print (e)