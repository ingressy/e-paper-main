#translate untis lang to imagegen
#by ingressy

from IMAGEGEN.imagegen2 import gen_image

def untis2imagegen(room,klasse, teacher, subject, startdate, enddate, abw, klasse1, teacher1, subject1, starttime1, endtime1, klasse2, teacher2, subject2, starttime2, endtime2,):
    if abw == "cancelled":
        chabw = 1
    else:
        chabw =  0
    #print(room, klasse, teacher,subject, startdate, enddate)

    gen_image(room, startdate, enddate, teacher, subject, klasse, chabw, starttime1, endtime1, teacher1, subject1, klasse1, "0", starttime2, endtime2, teacher2, subject2, klasse2,
              "0")
if __name__ == "__main__":
    untis2imagegen()
