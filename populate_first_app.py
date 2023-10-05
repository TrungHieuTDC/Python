import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'first_project.settings')
import django
django.setup()
from first_app.models import User
from faker import Faker

fakegen = Faker()

def add_user():
    # Tạo dữ liệu ngẫu nhiên cho các trường
    fake_first_name = fakegen.first_name()
    fake_last_name = fakegen.last_name()
    fake_email = fakegen.email()

    # Thêm đối tượng User vào cơ sở dữ liệu
    user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, 
     email=fake_email)
    return user
def populate(N=5):
    for user in range(N):
        user = add_user()  # Thêm một đối tượng User ngẫu nhiên
        
if __name__ ==  '__main__':
    print('populating topics')
    populate(20)
    print('Compuletes')