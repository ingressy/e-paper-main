#translate untis lang to imagegen
#by ingressy
startdate1 = "0"
enddate1 = "0"
teacher1 = "0"
subject1 = "0"
klasse1 = "0"
chabw1 = 0
startdate2 = "0"
enddate2 = "0"
teacher2 = "0"
subject2 = "0"
klasse2 = "0"
chabw2 = 0
startdate3 = "0"
enddate3 = "0"
teacher3 = "0"
subject3 = "0"
klasse3 = "0"
chabw3 = 0
Personalized_Msg = "0"

from IMAGEGEN.imagegen2 import gen_image
# Hier musst du halt in diese Funktion auch den ganzen kack reinpacken wie ich in meiner. Also lohnt sich auch ne Char. Aber so mit den Standard Vars würde ich es lassen, weil so bei Fehlern sich der Code nicht so leicht aufhängen kann.
def untis2imagegen(room,klasse1, teacher1, subject1, startdate1, enddate1, date, abw1):
    if abw1 == "cancelled":
        chabw1 = 1
    else:
        chabw1 =  0
    print(room, klasse1, teacher1,subject1, startdate1, enddate1, date)

    gen_image(room, startdate1, enddate1, teacher1, subject1, klasse1, chabw1, startdate2, enddate2, teacher2, subject2, klasse2, chabw2, startdate3, enddate3, teacher3, subject3, klasse3,
              chabw3,Personalized_Msg)
if __name__ == "__main__":
    untis2imagegen()