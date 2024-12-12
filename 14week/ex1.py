from faker import Faker
from openpyxl import Workbook

fake = Faker('ko_KR')

wb = Workbook()
ws = wb.active

ws.append(['이름','성별','이메일','전화번호','주소'])

for i in range(1000):
    name = fake.name()
    gender = fake.random_element(elements=('남', '여'))
    email = fake.email()
    phone_number = fake.phone_number()
    address = fake.address()
    ws.append([name, gender, email, phone_number, address])
    
wb.save('fakeinfo.xlsx')