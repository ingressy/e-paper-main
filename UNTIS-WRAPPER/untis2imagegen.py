#translate untis lang to imagegen
#by ingressy
from IMAGEGEN.imagegen2 import gen_image

Bottom_Text = "0"
bla = "1"

def untis2imagegen(room,klasse, teacher, subject, startdate, enddate, abw, klasse1, teacher1, subject1, starttime1, endtime1, abw1, klasse2, teacher2, subject2, starttime2, endtime2, abw2):
    gen_image(room, startdate, enddate, teacher, subject, klasse, abw, starttime1, endtime1, teacher1, subject1, klasse1, abw1, starttime2, endtime2, teacher2, subject2, klasse2,
              abw2, Bottom_Text)

if __name__ == "__main__":
    untis2imagegen()
