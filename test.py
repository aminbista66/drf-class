validated_data = {"username": "test", "password": "test1234", "email": "test@gmail.com"}

def test(username, password):
    print(username, password)
    pass

test(**validated_data)

test(username="test", password="test1234", email="test@gmail.com")