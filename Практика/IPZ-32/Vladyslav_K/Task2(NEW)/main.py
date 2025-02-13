
from stegano import lsb

secret = lsb.hide("img/1.jpg", "Your password: qwerty")
# secret = lsb.hide("img/1.png", "Привет друг")
secret.save("img/1_secret.png")

result = lsb.reveal("img/1_secret.png")
print(result)

