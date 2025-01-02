#  4. Write a program to append new data to an existing file.
with open('Lecture6/Mohammed.txt','a+') as file:
    file.writelines("Mohammed was born around 570, AD in Mecca (now in Saudi Arabia).\nHis father died before he was born and he was raised first by his grandfather and then his uncle.\nHe belonged to a poor but respectable family of the Quraysh tribe.\nThe family was active in Meccan politics and trade.")
    file.seek(0)
    print(file.read())