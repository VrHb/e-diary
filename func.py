import random

from datacenter.models import Mark, Chastisement, Lesson, Subject, \
    Commendation, Schoolkid



def fix_marks(schoolkid):
    marks = Mark.objects.all()
    bad_marks = marks.filter(
        points_lt=4, 
        schoolkid__full_name=schoolkid.full_name
    )
    bad_marks.update(points=5)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.all()
    schoolkid_chastisements = chastisements.filter(
        schoolkid__full_name=schoolkid.full_name
    )
    schoolkid_chastisements.delete()


def create_commendation(schoolkid, subject, text):
    lessons = Lesson.objects.filter(
        subject__title=subject,
        year_of_study=schoolkid.year_of_study,
        group_letter=schoolkid.group_letter
    )
    lesson = random.choice(lessons)
    commendation = Commendation.objects.create(
        text=text, 
        created=lesson.date, 
        schoolkid=schoolkid,
        subject=lesson.subject,
        teacher=lesson.teacher
    )
    
