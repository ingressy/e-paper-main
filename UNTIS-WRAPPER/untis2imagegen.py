#translate untis lang to imagegen
#by ingressy

from IMAGEGEN.imagegen2 import gen_image

def untis2imagegen(room,klasse, teacher, subject, startdate, enddate, date, abw):

    if abw == "cancelled":
        chabw = 1
    print(room, klasse, teacher,subject, startdate, enddate, date)

    gen_image(room, startdate, enddate, teacher, subject, klasse, "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0",
              "0")
if __name__ == "__main__":
    untis2imagegen()