from docxtpl import DocxTemplate
from datetime import datetime
import pandas as pd

doc = DocxTemplate("en-template-manager-info.docx") # document name

my_name = "Randall Ang Zhi Xiong"
my_phone = "018-283 7077"
my_email = "randallang@gmail.com"
my_address = "11 Jalan Hantu"
today_date = datetime.today().strftime("%d %b, %Y")

my_context = {'my_name': my_name, 'my_phone': my_phone, 'my_email': my_email, 'my_address': my_address,
              'today_date': today_date}

df = pd.read_csv("en_fake_data.csv")

for index, row in df.iterrows():
    context = {
        'hiring_manager_name': row['name'],
        'address': row['address'],
        'phone_number': row['phone_number'],
        'email': row['email'],
        'job_position': row['job'],
        'company_name': row['company']}

    context.update(my_context)

    doc.render(context)
    doc.save(f"generated_doc_{index}.docx")