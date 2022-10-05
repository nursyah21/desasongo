#define pb1 11
#define pb2 9
#define pb3 8
#define pk 10
#define TDS A5

const int UltrasonikTrig1 = 2;
const int UltrasonikEcho1 = 3;

const int UltrasonikTrig2 = 4;
const int UltrasonikEcho2 = 5;

const int UltrasonikTrig3 = 6;
const int UltrasonikEcho3 = 7;

const int microsecondsKeCenti = 0;

bool mode_auto = true;
int pompa[4] = {false, false, false, false};
// pompa[0] -> pb1 || pompa[2] -> pb3
// pompa[1] -> pb2 || pompa[3] -> pk

float ppm;
int ppmtarget=1000;
float jaraktarget=40;
int hidroponikrun = 0;

void ision() { //pompa1 isi
  digitalWrite(pb1, HIGH);
  digitalWrite(pk, LOW);
  digitalWrite(pb2, LOW);
  digitalWrite(pb3, LOW);
  pompa[0] = true;
}
void isioff() {
  digitalWrite(pk, LOW);
  digitalWrite(pb1, LOW);
  digitalWrite(pb2, LOW);
  digitalWrite(pb3, LOW);
  pompa[1] = false;
}
void nutrision() { //pompa4 nutrisi
  digitalWrite(pk, HIGH);
  digitalWrite(pb1, LOW);
  digitalWrite(pb2, LOW);
  digitalWrite(pb3, LOW);
  pompa[3] = true;
}
void nutrisioff() {
  digitalWrite(pk, LOW);
  digitalWrite(pb1, LOW);
  digitalWrite(pb2, LOW);
  digitalWrite(pb3, LOW);
  pompa[3] = false;
}
void kurason() { //pompa2 kuras
  digitalWrite(pb2, HIGH);
  digitalWrite(pk, LOW);
  digitalWrite(pb1, LOW);
  digitalWrite(pb3, LOW);
  pompa[1] = true;
}
void kurasoff() {
  digitalWrite(pk, LOW);
  digitalWrite(pb1, LOW);
  digitalWrite(pb2, LOW);
  digitalWrite(pb3, LOW);
  pompa[1] = false;
}
void hidroponikon(){ //pompa3 hidroponik
  digitalWrite(pk, LOW);
  digitalWrite(pb1, LOW);
  digitalWrite(pb2, LOW);
  digitalWrite(pb3, HIGH);
  pompa[2] = true;
}
void hidroponikoff(){
  digitalWrite(pk, LOW);
  digitalWrite(pb1, LOW);
  digitalWrite(pb2, LOW);
  digitalWrite(pb3, LOW);
  pompa[2] = false;
}

void setup() {
  Serial.begin(9600);
  pinMode(UltrasonikTrig1, OUTPUT);
  pinMode(UltrasonikTrig2, OUTPUT);
  pinMode(UltrasonikTrig3, OUTPUT);
  pinMode(pb1, OUTPUT); //pompa1
  pinMode(pb2, OUTPUT); //pompa2
  pinMode(pb3, OUTPUT); //pompa3
  pinMode(pk, OUTPUT); //pompa4

  pinMode(UltrasonikEcho1, INPUT);
  pinMode(UltrasonikEcho2, INPUT);
  pinMode(UltrasonikEcho3, INPUT);
  pinMode(TDS, INPUT);
}

// hidroponik, pake hitungan jam, sec: 5
// hidroponik on, everybody off



long duration1, duration2, duration3 ;
long cm1, cm2, cm3 ;
int  state = 0;


void loop()
{
/// aktifin sensor jarak ///
  digitalWrite(UltrasonikTrig1, LOW);
  digitalWrite(UltrasonikTrig1, HIGH);

  digitalWrite(UltrasonikTrig2, LOW);
  digitalWrite(UltrasonikTrig2, HIGH);

  digitalWrite(UltrasonikTrig3, LOW);
  digitalWrite(UltrasonikTrig3, HIGH);

  delayMicroseconds(10);

  digitalWrite(UltrasonikTrig1, LOW);
  duration1 = pulseIn(UltrasonikEcho1, HIGH);

  digitalWrite(UltrasonikTrig2, LOW);
  duration2 = pulseIn(UltrasonikEcho2, HIGH);

  digitalWrite(UltrasonikTrig3, LOW);
  duration3 = pulseIn(UltrasonikEcho3, HIGH);
  

  cm1 = duration1 * 0.034 / 2;
  cm2 = duration2 * 0.034 / 2;
  cm3 = duration3 * 0.034 / 2;

  //hitung ppm//
  float ppm = analogRead(A5) * 1.953;
  ppm = 2.4969 * ppm - 0.0006 * ppm * ppm - 120.32;

  
  
  //readstring
  String test = Serial.readString();
  test.trim();
  
  if(test != ""){
    Serial.println(test);
    //split text, pompa1, pompa2, pompa3, pompa4, auto, ppm
    String pompa1 = getValue(test,',',0);
    String pompa2 = getValue(test,',',1);
    String pompa3 = getValue(test,',',2);
    String pompa4 = getValue(test,',',3);
    String mode = getValue(test,',',4);
    String ppm = getValue(test,',',5); //ppm target

    mode_auto = (mode == "True") ? true:false;
    
    ppmtarget = ppm.toInt();
    
    
    if(pompa1 == "True") ision(); else isioff();
    if(pompa2 == "True") kurason(); else kurasoff();
    if(pompa3 == "True") hidroponikon(); else hidroponikoff();
    if(pompa4 == "True") nutrision(); else nutrisioff();
    
  }else{
    // state
    Serial.print("State = ");
    Serial.print(state);
    Serial.print(" || jarak1 = ");
    Serial.print(cm1);
    Serial.print(" || jarak2 = ");
    Serial.print(cm2);
    Serial.print(" || jarak3 = ");
    Serial.print(cm3);
    Serial.print(" || ppm = ");
    Serial.print(ppm);
    Serial.print(" || ppmtarget = ");
    Serial.print(ppmtarget);
  
    //pompa1
    Serial.print(" || pompa1 = ");
    if(pompa[0])Serial.print("on"); else Serial.print("off");
    //pompa2
    Serial.print(" || pompa2 = ");
    if(pompa[1])Serial.print("on"); else Serial.print("off");
    //pompa3
    Serial.print(" || pompa3 = ");
    if(pompa[2])Serial.print("on"); else Serial.print("off");
    //pompa4
    Serial.print(" || pompa4 = ");
    if(pompa[3])Serial.print("on"); else Serial.print("off");
      
    //mode
    Serial.print(" || Mode = ");
    if(mode_auto)Serial.println("auto"); else Serial.println("manual");
       
  }
  if(mode_auto){
    mode_auto_hidroponik();
  }
  
  hidroponikrun++;
  //hidroponik run every 1hour
  if(hidroponikrun >= 1800){
    hidroponikon();
    //off after 1minutes
    if(hidroponikrun >= 1830){
      hidroponikoff();
      hidroponikrun = 0;
    }
  }
  
  delay(2000);
}

void mode_auto_hidroponik(){
  if (state == 0){  /// ngisi air ///
    if (cm1 > jaraktarget){
      ision();
    }
    else if (cm1 < jaraktarget){
      isioff();
      state = 1;
    }
  }
  else if (state == 1){ /// nutrisi ///
//    float ppm = analogRead(A5) * 1.953;
//    ppm = 2.4969 * ppm - 0.0006 * ppm * ppm - 120.32;

    if (ppm < ppmtarget){
      nutrision();
    }
    else if (ppm >= ppmtarget){
      nutrisioff();
      state = 2;
    }
  }
  else if (state == 2){ /// kuras air///
    if ((ppm < (ppmtarget-100))&&(cm1 > (40.00))){
      kurasoff();
       state=0;
     
    }
    else if ((ppm > (ppmtarget+100))||(cm1 < (10.00))){
      kurason();
      state=2;
    }
  }
}

 