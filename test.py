def Fungsi():
    global message
    global date
    message = Content("Halo")
    date = Date(29)


def Content(message):
    return "message"


def Date(date):
    return date


Fungsi()
print(message)
print(date)
