# OPENPIBO 라이브러리 코드 분석

## audio

### cAudio

- play

  mp3, wav 파일을 실행한다.

  (omxplayer를 사용한다. 라즈베리파이 공식 미디어 프로그램임.)

- stop

  음악을 중지한다. (sudo pkill omxplayer)

## device

### cDevice

- locked

  thread를 잠금

- send_cmd

  raw데이터로 바꿔 send_raw로 전달

- send_raw

  raw데이터를 읽고 인코딩하여 메인컨트롤러한테 보내준다.

  그리고 응답을 받아서 디코딩하여 리턴한다.

## motion

### cMotion

- \__init__

  기본 모션 db에서 모션들을 가져와 self.profile에 저장해논다.

- set_profile(path)

  path에 있는 모션들을 self.profile에 저장한다.

- set_motor

  모터 하나를 움직인다.

  (servo 명령어를 실행한다.)

- set_motors(positions, movetime)

  10개의 모든 모터를 움직인다.

- set_speed

- set_acceleration

- set_speeds

- set_accelerations

- get_motion

  모터 프로필을 가져온다.(저장돼있는 모션들)

- set_motion(name, cycle=1)

  "name" 이라는 모션의 동작을 "cycle"번 실행한다.

  `exe["init_def"]`: 요게 모지?

- stop

  모터를 멈춘다.

set_motion을 하면 set이 False가 되고, db에있는 pos를 순차적으로 실행한다.

각 동작은 seq의 갭 만큼 실행하고 끝난다.

중간에 stop 명령어를 실행하면 self.stoped가 True가 되어 움직일 수 없는 형태로 변하나, 다시 set_motion을 하면 False가 되어 움직일 수 있으니 걱정하지 않아도 된다.



### cPyMotion

serial로 motor ctrller와 직접 통신한다.

motor_range가 [25,35,80,30,50,25,25,35,80,30]인데 뭔지 알아보자...

각 모터마다 제한을 걸어놨고, 그 범위가 위 처럼 된다. (절댓값 기준. 즉, 25면 -25 ~ 25)

- set_motor

  serial로 (chr(*0x*84) + chr(n) + chr(lsb) + chr(msb))이렇게 생긴 데이터를 인코딩하여 보내준다.

  chr(*0x*84)는 set_motor의 첫 명령어 글자인 것 같고, n은 어떤 모터인지, lsb와 msb는 각도를 나타내는 것 같다.

- set_motors

  10개의 모든 모터를 제어한다.

  serial로 명령어를 보내는데, 이건 chr(*0x*9F) + chr(10) + chr(0) 로 시작한다.

- set_speed (chr(*0x*87)로 시작함)

- set_acceleration (chr(*0x*89)로 시작)

- set_init (chr(*0x*A2)로 시작)



## oled

init을 하면 spi = busio.SPI(11, 10, 9)로 SPI포트가 정해진다.

이때, 11은 clock신호, 10은 MOSI(송신), 9는 MISO(수신)이다.

rst_pin, cs_pin, dc_pin은 각각 아래와 같다.

- rst: reset
- cs: chip select
- dc: data command

어렵다 요거



- set_font

  폰트 종류와 사이즈를 설정한다.

  PIL.ImageFont를 이용한다.

- draw_text

  text를 화면에 출력한다.

  PIL.ImageDraw를 이용한다.

- draw_image

  image를 화면에 출력한다.

  위와 같다.

- draw_data

  PIL.Image.fromarray(img)를 이용한다.

  img를 numpy배열로 변환하여 화면에 띄우는 것.

  그냥 이미지처럼 출력되는데 draw_image와의 차이점은 입력값이 파일명이냐 데이터냐의 차이

- draw_rectangle, ellipse, line

  각각 직사각형, 타원, 선을 그린다.

  points 인자는 왼쪽 위 xy좌표와 오른쪽 아래 xy좌표이다.

- invert

  색 반전이다.

- show

  그린 그림을 OLED판에 띄워준다.

  처음에 이게 없는줄알고 OLED판에 계속 안나오길래 oled.show()를 모든 함수에 추가하고있었는데;;;

  가이드에 진작 친절히 써져있으면 좋을듯

- clear

  그림을 초기화한다.

  fill(0)한 뒤 show()하는 방식

- size_check(filename)

  file의 크기를 반환한다.

  

## servo

servolib 파일은 없다.

motion에서 모터 제어하는 것의 더 low단 컨트롤로 보인다.

일단 보류



## speech

### cSpeech

번역은 google api, stt와 tts는 kakao api를 사용한다.

- translate

  google api를 이용해 외국어를 한국어로 번역한다.

- tts, stt

  kakao api를 이용해 외국어를 한국어로 번역한다.

  request 형식은 post(url, headers, data)

  ​	headers: content-type, authorization

  ​	data: 데이타



### cDialog

챗봇을 사용하기 위해 만들어진 모델.

자연어처리 파이썬 패키지인 konlpy를 사용해 형태소 분해를 한다.

그리고 챗봇은 입력값과 형태소가 유사한 대화를 dialog.csv에서 찾아 그 대답을 리턴한다.

- mecab_pos

  문장에서 형태소와 품사 정보를 함께 반환한다.

- mecab_morphs

  문장의 형태소를 반환한다.

- mecab_nouns

  문장의 명사를 추출한다.

- get_dialog

  입력 문장의 morphs를 추출하고, dialog.csv의 문장과 같은 단어가 가장 많은 것을 점수가 높다고 표현한다.

  그리고 가장 점수가 높은 대화의 대답을 반환한다. (개수가 같으면 그 중 랜덤 1)



## vision

### cCamera

v4l2-ctl이라는 프로그램을 사용해서 카메라 드라이버 개발, 간단한 제어를 할 수 있다.

init 시 v4l2-ctl -c vertical_flip=1,horizontal_flip=1,white_balance_auto_preset=3 이라는 명령어를 사용하는데 그 의미는 `물어봐야지`.



opencv를 사용한다.

- imread

  cv2를 사용해 파일의 이미지를 읽는다.

- read(w=640, h=480)

  videostreadming을 하자마자 그 이미지를 읽고 반환한다. vs는 바로 중지시킨다.

  근데 왜 640 480으로 할까? OLED는 128 64인데... 카메라가 2:1 비율이 없어서 그런가? 컨버팅하면 데이터 손실도 일어날텐데

- imwrite(filename, image)

  cv2의 imwrite와 같다.

  image를 filename으로 저장한다.

- imshow(img, title="IMAGE")

  img를 IMAGE라는 윈도우창에 띄운다. (GUI환경에서만 가능한데, 현재 os는 gui환경을 지원하지 않는 것으로 알고있음.. 근데 이게 왜있지? 모바일이나 pc에서 이미지를 확인하는거는 show 할 필요도 없지 않나?)

  -> OLED창에 띄우려는 것 같음. pibo.py의 camera_on을 보면, vs을 실행하고 입력되는 이미지를 읽어서 128, 64로 컨버팅 하고 rotate10 작업을 한다. (rotate10: 이미지를 평행성을 유지하면서 반시계로 10도 틀고, 크기를 0.9배 함. 카메라가 10도 틀어져있는지 모르겠지만 이걸 안하면 조금 안맞는 느낌.)

- waitKey

  cv2.waitKey와 같다.

  show와 함께 사용하여 이미지를 보는 시간을 설정할 수 있도록 한다. (0은 무한)

- streaming(w, h, timeout)

  w * h 크기의 화면으로 timeout초만큼 스트리밍한다.

  이것도 GUI환경에서만 동작 가능
  
- rectangle, putText

  cv2의 함수랑 같음.

  사각형 그리기랑 text입력

  자세한건 문서보고 사용하면 될듯

- cartoonize

  이미지를 만화처럼 바꿔준다.

  자세한 내용은 몰라도 될듯

- convert_img

  이미지를 리사이징한다.

  주로 OLED 사이즈에 맞추기 위해 사용

- bgr2hls

  bgr이었던 칼라값을 hls로 바꿔준다.

  bgr은 blue, green, red이고, hls는 색조, 채도, 명도이다.

  pibo.py에서 search_color 할때 입력 이미지를 hls값으로 받기 때문에 이 컨버터가 필요하다.

  참고로 search_color는 전체 이미지의 평균 패치를 측정해 생상을 반환한다.



### cFace

딥러닝 프레임워크인 caffe를 사용하여 나이와 성별을 파악한다. (caffe에서 이미 만들어놓은 age net, gender net을 사용.)

또한, 얼굴과 관련한 알고리즘들을 편하게 사용할 수 있는 라이브러리인 `dlib`을 사용해 face classification을 한다.

우선 cv2로 face detecting을 하고, dlib로 얼굴의 landmark를 찾아서 이 점들의 위치로 face encoding을 한다.



- \__init__

  facedb 배열을 생성한다. [[`이름`], [`인코딩 값`]]

  각종 인공지능 모델을 가져온다.

- get_db

  현재 사용중인 얼굴 데이터베이스를 반환한다.

- init_db

  facedb를 초기화한다.

- save_db

  현재 사용중인 얼굴 데이터베이스를 파일로 저장한다.

- load_db

  얼굴 데이터베이스 파일을 가져온다.

- train_face(img, face, name)

  이미지에서 얼굴 부분을 떼어서 인코딩하여 facedb에 저장한다.

  이미지는 gray로 바꿔서 저장하는데, dlib.shape_predictor 함수가 1채널 값을 받을 수 있기 때문이다.

- delete_face

  facedb에서 등록된 얼굴을 삭제한다.

- recognize

  얼굴을 인식한다.

  입력된 이미지를 facedb에 있는 다른 얼굴과 비교해 동일인(score < threshold(현재 0.4))의 이름과 점수를 반환한다.

- detect

  이미지에서 얼굴을 탐색하여 그 좌표를 반환한다.

  cv2.CascadeClassifier를 이용한다.

- get_ageGender

  얼굴의 성별과 나이를 반환한다.

  cv2의 caffe 프레임워크를 사용한다.



### cDetect

20개의 class classification이 가능한 디텍팅 모델이다. (modilenet 사용)

분류가능 클래스:

["background", "aeroplane", "bicycle", "bird", "boat", "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog", "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train", "tvmonitor"]

바코드(QR), OCR 인식이 가능하다.

- detect_object

  mobilenet을 이용하여 객체인식을 한다.

- detect_qr

  바코드 또는 QR코드를 인식한다.

  파이썬 바코드 인식 라이브러리인 pyzbar를 이용한다.

- detect_text

  OCR. 문자를 인식하여 반환한다.

  파이썬 라이브러리 pytesseract를 사용한다.

  한국어 OCR을 그리 성능이 좋지 않다.



## PIBO MCU decode

```c++
// Atmega328 Pin Mapping
#define BATTERY_PIN A1
#define TOUCH_PIN 2
#define DC_CONN_PIN 3
#define BUTTON_PIN 4
#define LED_PIN 5
#define PIR_PIN 8
#define POWER_EN_PIN 17

Adafruit_NeoPixel strip = Adafruit_NeoPixel(2, LED_PIN, NEO_GRB + NEO_KHZ800);

void setup(){
  pinMode(POWER_EN_PIN, OUTPUT);
  digitalWrite(POWER_EN_PIN, HIGH);
  
  pinMode(PIR_PIN, INPUT);
  pinMode(DC_CONN_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(DC_CONN_PIN), eventDC, CHANGE);

  pinMode(BATTERY_PIN, INPUT);
  pinMode(TOUCH_PIN, INPUT_PULLUP);
  attachInterrupt(digitalPinToInterrupt(TOUCH_PIN), eventTouch, FALLING);
  pinMode(BUTTON_PIN, INPUT);
```

__핀 매핑__

- 배터리 연결 유무 (INPUT)
- 터치센서 입력값 (INPUT_PULLUP)
- 어댑터 연결 유무 (INPUT_PULLUP)
- 버튼 입력값 (INPUT)
- LED 출력값 (네오픽셀 컨트롤하는 출력핀으로 사용)
- PIR 입력값 (INPUT)
- 파워 on/off 출력값 (OUTPUT, HIGH가 on)



```c++
// OPCODE
#define MSG_TYPE_VERSION 10
#define MSG_TYPE_HALT 11
#define MSG_TYPE_RESET 12
#define MSG_TYPE_BUTTON 13
#define MSG_TYPE_DC_CONN 14
#define MSG_TYPE_BATTERY 15
#define MSG_TYPE_REBOOT 17

#define MSG_TYPE_NEOPIXEL 20
#define MSG_TYPE_NEOPIXEL_FADE 21
#define MSG_TYPE_NEOPIXEL_BRIGHTNESS 22
#define MSG_TYPE_NEOPIXEL_EACH 23
#define MSG_TYPE_NEOPIXEL_FADE_EACH 24
#define MSG_TYPE_NEOPIXEL_LOOP 25
#define MSG_TYPE_NEOPIXEL_OFFSET_SET 26
#define MSG_TYPE_NEOPIXEL_OFFSET_GET 27
#define MSG_TYPE_NEOPIXEL_EACH_ORG 28

#define MSG_TYPE_PIR 30
#define MSG_TYPE_TOUCH 31

#define MSG_TYPE_SYSTEM 40

#define MSG_TYPE_TEST 97
#define MSG_TYPE_INVALID_PKT 98
#define MSG_TYPE_MGMT 99
```

devicelib.py로부터 send_raw가 되었을 때 명령을 구분하는 변수.

- MSG_TYPE_VERSION: 현재 버전을 반환
- MSG_TYPE_HALT: halt()함수 실행: 전원을 끈다.
- MSG_TYPE_DC_CONN: 전원이 연결되었는지 반환 (HIGH면 연결(on))
- MSG_TYPE_BATTERY: 배터리 잔량을 %로 반환
- MSG_TYPE_REBOOT: initConfig()함수 실행: 파이보 초기화 (센서, 버튼 등)
- MSG_TYPE_NEOLIXEL...:
  - 눈 색을 설정한다. OFFSET은 눈 색의 최댓값을 설정한다.
    예를들어, #26:255,0,0! 요청 후에 #20:255,255,255!를 하면 흰색이 아니라 빨간색 눈이 된다.
  - LOOP는 특정 시간 주기로 눈 색이 변한다.
  - EACH_ORG는 EACH랑 똑같은데 `strip`을 사용했는가의 차이다. (뭐가 다른건지 모르겠다.)
- MSG_TYPE_PIR: PIR센서를 켜고 끌 수 있다.
- MSG_TYPE_TOUCH: touch_en을 1 또는 0으로 만든다. 터치센서를 켜고 끄는 변수 같은데 실제 코드에서는 구상이 안 되어있다.
  예전에는 터치센서를 켜고 끌 수 있었지만 지금은 상시 켜놓는 것 같다.`?`
- MSG_TYPE_SYSTEM: PIR, 터치, DC, button_value, reset_value, halt_value에 관한 정보를 반환한다.



```c++
// value
int gDC_value;
int gDC_prior_value = -1;
int gPIR_value;
int gPIR_prior_value = -1;
int gButton_value;
int gHalt_value;
int gReset_value;
int gTouch_value;
long gBattery_value;
```

각각 의미는 다음과 같다.

- DC_CONN_PIN이 HIGH면 1 아니면 0

- 어댑터를 연결 할 때를 파악하기 위한 변수. gDC_value의 값을 따라간다.

- PIR_PIN이 HIGH면 1 아니면 0

- PIR에 사람이 감지되었을 때를 파악하기 위한 변수. PIR은 트리거 형식이기 때문에 사람이 앞에 계속 있으면 인식하지 못한다.

- BUTTON_PIN이 LOW이면(눌려있으면) 1 아니면 0.

  누르고있으면 gButton_clicked_cnt가 1초에 1씩 증가한다.

- gHalt_value가 1이 되면 파이보가 종료된다.

- SYSTEM opcode를 받으면 gReset_value가 1이라면 LED가 깜빡인다. 근데 이 변수가 뭐할라고 있는지 모르겠다.

- `attachInterrupt(digitalPinToInterrupt(TOUCH_PIN), eventTouch, FALLING)`

  예전에는 eventTouch 함수에서 터치의 유무를 판단했는데, 현재는 `attachInterrupt`를 사용해서 TOUCH_PIN 에 인터럽트가 생기면 eventTouch함수를 호출하는 식이 되었다. 당연히 eventTouch은 gTouch_value를 1로 바꿔준다.

- 배터리 잔량을 백분위로 표시한다.



```c++
SoftwareSerial serial(10, 9); // RX, TX

void setup(){
  ...
      
  for(int i=0;i<6;i++){
    gColorOffset[i] = EEPROM.read(i)/255.0;
  }

  strip.begin();
  strip.setBrightness(64);
  // Initialation Profile
  initConfig();

  // To Raspberrypi 
  serial.begin(9600);
  serial.setTimeout(10);
}
```

- 10번 9번 핀을 시리얼 통신을 위한 RX, TX로 설정한다.
  그리고 송수신 속도를 초당 9600bit,  최대 수신대기시간을 10ms로 설정한다.



### MCU와 cDevice의 통신

```c++
import serial
import time
from threading import Lock

class cDevice:
  def __init__(self):
    self.code = {
    "VERSION":"10",
    "HALT":"11",
    "BUTTON":"13",
    "DC_CONN":"14",
    "BATTERY":"15",
    ...
    }
    self.dev = serial.Serial(port="/dev/ttyS0", baudrate=9600)
    self.lock = Lock()

  def locked(self):
    return self.lock.locked()

  def send_cmd(self, code, data=""):
    return self.send_raw("#{}:{}!".format(code, data))

  def send_raw(self, raw):
    if self.lock.locked() == True:
      return False

    self.lock.acquire()
    self.dev.write(raw.encode('utf-8'))
    data = ""
    time.sleep(0.05)
    while True:
      ch = self.dev.read().decode()
      print(ch)
      if ch == '#' or ch == '\r' or ch == '\n':
        continue
      if ch == '!':
        break
      data += ch
    self.lock.release()
    return data

```

라즈베리파이에서 serial port(ttyS0)에 9600의 속도로 연결한다.

`send_raw` 함수를 실행하면 raw데이터를 인코딩하여 MCU로 전송하게 된다.

이때, 데이터 송신은 thread 안에서 이루어지는데, serial 포트를 동시에 사용할 수 없도록 lock을 걸어준다.



```c++
void setup(){
  ...
  strip.begin();
  strip.setBrightness(64);
  // Initialation Profile
  initConfig();

  // To Raspberrypi 
  serial.begin(9600);
  serial.setTimeout(10);
}

void loop(){
  if(serial.available()){
    String pkt = "";
    pkt = serial.readStringUntil('!');
    pkt.trim();

    if(pkt[0] != '#'){
      sendMSG(MSG_TYPE_INVALID_PKT, pkt);
    }
    else{
      pkt.remove(pkt.indexOf('#'),1);
  
      int first = pkt.indexOf(':');
      int second = pkt.indexOf(':', first+1);
      int opcode = pkt.substring(0, first).toInt();
      String data = pkt.substring(first+1, second);

      switch(opcode){
        case MSG_TYPE_VERSION:
          sendMSG(MSG_TYPE_VERSION, SW_VERSION);
          break;
        ...
```

MCU에서도 9600의 속도로 serial 통신을 연결한다.

데이터를 받으면 `!`까지의 데이터를 뽑아 파싱한다.

입력받은 opcode에 따른 처리를 한 후 라즈베리파이로 다시 응답한다.



### openpibo-example 에러 정리

- device/device_test:

  No such file or dir: '/dev/ttyS0'

  -> raspi-config에서 serial port 열면 됨.

- translate/translate_test:

  JSONDecodeError: Extra data 1

  -> /usr/local/lib/python3.7/dist-packages/google_trans_new/google_trans_new.py (151line)
  response = (decoded_line + '[') -> response = decoded_line으로 변경

- camera_test:
  -> serial과 마찬가지로 raspi-config에서 camera 허용 하면 됨.

- cDevice에서 serial 통신할 때 발생하는 문제

  - UnicodeDecodeError
  - Serial.serialutil: Input/Output error

