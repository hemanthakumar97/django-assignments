import os
import time

pro_name = input("Enter the project name: ")
os.system('django-admin startproject {}'.format(pro_name))
os.system("code C:/Users/Hemanth/Desktop/django-assignments/{}/.".format(pro_name))