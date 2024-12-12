#translate untis lang to imagegen
#by ingressy
# Standard Variablen festlegen um Fehlerrisiko zu minimieren:
Personalized_Msg = "0"

from IMAGEGEN.imagegen2 import gen_image

# Translator Funktion
def untis2imagegen(room,klasse1, teacher1, subject1, startdate1, enddate1, date, abw1):
    if abw1 == "cancelled":
        chabw1 = 1
    else:
        chabw1 =  0
    print(room, klasse1, teacher1,subject1, startdate1, enddate1, date)

    gen_image(room, startdate1, enddate1, teacher1, subject1, klasse1, chabw1, "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0",Personalized_Msg)
if __name__ == "__main__":
    untis2imagegen()