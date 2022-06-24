import random

from datacenter.models import Mark, Chastisement, Lesson,\
    Commendation, Schoolkid, Subject



LAUDATORY_PHRASES = [
    'Молодец!',
    'Отлично!',
    'Хорошо!',
    'Гораздо лучше, чем я ожидал!',
    'Ты меня приятно удивил!',
    'Великолепно!',
    'Прекрасно!',
    'Ты меня очень обрадовал!',
    'Именно этого я давно ждал от тебя!',    
    'Сказано здорово – просто и ясно!',
    'Ты, как всегда, точен!',
    'Очень хороший ответ!',
    'Талантливо!',
    'Ты сегодня прыгнул выше головы!',
    'Я поражен!'
    'Уже существенно лучше!',
    'Потрясающе!',
    'Замечательно!',
    'Прекрасное начало!',
    'Так держать!',
    'Ты на верном пути!',
    'Здорово!',
    'Это как раз то, что нужно!',
    'Я тобой горжусь!',
    'С каждым разом у тебя получается всё лучше!',
    'Мы с тобой не зря поработали!',
    'Я вижу, как ты стараешься!',
    'Ты растешь над собой!',
    'Ты многое сделал, я это вижу!',
    'Теперь у тебя точно все получится!'
]


def get_schoolkid(name):
    try:
        schoolkid = Schoolkid.objects.get(full_name__contains=name)
        return schoolkid
    except:
        raise Schoolkid.DoesNotExist(
            "Введи полное имя и фамилию. Как пример: Иван Васильев"
        )

def fix_marks(schoolkid):
    marks = Mark.objects.all()
    bad_marks = marks.filter(
        points__lt=4, 
        schoolkid__full_name=schoolkid.full_name
    )
    bad_marks.update(points=5)


def remove_chastisements(schoolkid):
    chastisements = Chastisement.objects.all()
    schoolkid_chastisements = chastisements.filter(
        schoolkid__full_name=schoolkid.full_name
    )
    schoolkid_chastisements.delete()


def create_commendation(schoolkid, subject):
    try:
        lessons = Lesson.objects.filter(
            subject__title=subject,
            year_of_study=schoolkid.year_of_study,
            group_letter=schoolkid.group_letter
        )
        lesson = random.choice(lessons)
        phrase = random.choice(LAUDATORY_PHRASES)
        commendation = Commendation.objects.create(
            text=phrase, 
            created=lesson.date, 
            schoolkid=schoolkid,
            subject=lesson.subject,
            teacher=lesson.teacher
        )
    except IndexError:
        return "Введи правильное название предмета с большой буквы"
