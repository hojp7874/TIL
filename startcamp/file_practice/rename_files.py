#1. os를 임포트 한다.
import os

#2. 작업하려는 폴더에 들어간다.
os.chdir(r'C:\Users\aclass\Desktop\홍진표\file_practice\dummy')

#3. 폴더에 있는 파일들을 불러온다.
filenames = os.listdir('.')

#4. 파일들을 반복하면서 파일명을 바꾼다.
for filename in filenames:
    os.rename('SAMSUNG', 'SSAFY')