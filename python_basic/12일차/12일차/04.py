from distutils import filelist
from fileinput import filelineno
import os
# print(os.environ['PATH'])

# os.chdir(원하는 경로)
print(os.getcwd())  # D:\이규영강사\이규영강사\workspace
# os.mkdir()

# 파일 복사
import shutil
shutil.copy("test.txt", "copy_test.txt")

#특정 파일들의 목록만들어서 리스트로 반환
import glob
fileList = glob.glob("D:/이규영강사/이규영강사/workspace/12일차/*.py")
print(fileList)