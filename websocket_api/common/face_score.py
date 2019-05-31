from aip import AipFace
import base64

APP_ID='16402117'
API_KEY='KOht83xXksU2LoqQW1wgcAso'
SECRET_KEY='uxg8pRBT6mpZbf5fpbCGkx1yZeSxsLI9'
aFace=AipFace(APP_ID,API_KEY,SECRET_KEY)
imageType="BASE64"

options={}
options["face_field"]= "age,gender,beauty"

def get_file_content(filePath):
    with open(filePath,'rb') as fp:
        content=base64.b64encode(fp.read())
        return content.decode('utf-8')

def FaceScore(filepath):
    result=aFace.detect(get_file_content(filepath),imageType,options)
    age=result['result']['face_list'][0]['age']
    beauty=result['result']['face_list'][0]['beauty']
    sex=result['result']['face_list'][0]['gender']['type']
    print(age)
    print(beauty)
    print(sex)
    return age,beauty,sex

filePath='./pic/1.jpg'
# get_file_content(filePath)
FaceScore(filePath)