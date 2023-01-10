#ocr 로 pc카카오톡 하단에서 생성되는 내용들을 자동문자인식으로 바꿔서 정리할예정임.
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'

a = Image.open('영수증.jpeg') # >> pdf 파일도 화면분석해서 텍스트로 전환가능함.
b = Image.open('IMG_6006.PNG')
result = pytesseract.image_to_string(a, lang='kor')
print(result)
result2 = pytesseract.image_to_string(b,lang='kor')
print(result2)

#출력 완료후에