import os
import time

pro_name = input("Enter the project name: ")
os.system('django-admin startproject {}'.format(pro_name))
os.system('mkdir C:\\Users\\Hemanth\\Desktop\\django-assignments\\APIs\\{}\\templates'.format(pro_name))
time.sleep(1)
os.system('copy NUL C:\\Users\\Hemanth\\Desktop\\django-assignments\\APIs\\{}\\templates\\index.html'.format(pro_name))
settings_file = 'C:/Users/Hemanth/Desktop/django-assignments/APIs/{}/{}/settings.py'.format(pro_name,pro_name)

with open(settings_file,"r") as file:
	data = file.readlines()
data[15]+="TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')\n"
data[56]="        'DIRS': [TEMPLATE_DIR],\n"
with open(settings_file,"w") as file:
	file.writelines(data)

os.system("code C:/Users/Hemanth/Desktop/django-assignments/APIs/{}/.".format(pro_name))