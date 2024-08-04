import os
import segno
from CleopatraApp.models import Dancer

def get_dancer_courses(dancer):
    courses = dancer.courses.all()
    course_names = [course.course_name for course in courses]
    return ' - '.join(course_names)


def qr_gen(id):

    save_path = os.path.join('CleopatraApp', 'static', 'Cleopatra_profile')
        # Ensure the directory exists
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    dancer = Dancer.objects.get(name=id)

    name = dancer.name
    email = dancer.email
    pais = dancer.country
    courses = get_dancer_courses(dancer)

    qr_content = f"Name: {name} \nCurses: {courses}  \nCountry: {pais}"
    qrcode = segno.make_qr(qr_content)
    file_name = f"{name}_qrcode.png"
    file_path = os.path.join(save_path, file_name)
    qrcode.save(file_path,scale=5,)
    
    relative_path = os.path.join('Cleopatra_profile', file_name)
    return relative_path