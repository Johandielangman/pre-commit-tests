import requests


def foo():
    x = 1 + 2
    # y = 3
    if x > 0:
        print("Hello")
        print("World")


def bar():
    # a = list(range(1, 31))
    # b = "some string"
    # c =  42
    print(foo(), bar())


def zar():
    a = "a"
    b = "b"
    response = requests.get(
        "https://google.com",
        timeout=30
    )
    print(response)
    if (
        a == "a" and
        b == "b"
    ):
        print("match!")
