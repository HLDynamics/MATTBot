import Consciousness
from HLEngine import HLEngine_audioProcess
from HLEngine import HLEngine_communications
HLEngine_audioProcess.playsound("voice/login.mp3")
HLEngine_audioProcess.playsound("voice/welcome.wav")
while(True):
    request=str(input("\nMATTbot:Hi, how may I help you sir? \nme:"))
    fetchGr=Consciousness.greeting(request)
    fetchBy=Consciousness.bye(request)
    PORT=Consciousness.utilCOM(request)
    Emotion=Consciousness.EmotionDetector(request)
    Fight=Consciousness.fight(request)
    #responser=Consciousness.superLogic(request)
    hyperLearn=Consciousness.hyperLogic(request)
    playBoy=Consciousness.playSome(request)
    shutdown=Consciousness.down(request)
    reboot=Consciousness.reboot(request)
    spy=Consciousness.spy(request)
    kill=Consciousness.killSpy(request)
    reminder=Consciousness.create_reminder(request)

    Consciousness.soundCloud(request)
    Consciousness.introduction(request)
    Consciousness.purpose(request)    
    Consciousness.automata(request)
    Consciousness.motionRef(request)
    Consciousness.vectorBot(request)
    Consciousness.analog_Controller(request)
    Consciousness.facebook(request)
    Consciousness.youtube(request)
    Consciousness.leave(request)
    Consciousness.target_identification(request)
    Consciousness.wakeup(request)
    Consciousness.radioMango(request)
    Consciousness.clubFM(request)
    Consciousness.akashavani(request)
    Consciousness.chatClient(request)
    Consciousness.chatServer(request)
    #Consciousness.IRIS(request)
    
    if(fetchBy=="off"):
        break
    if(fetchGr==None):
        flag=0
    else:
        print("MATTbot:"+fetchGr)
    if(fetchBy==None):
        flag=0
    else:
        print("MATTbot:"+fetchBy)

    if(reminder==None):
        flag=0
    else:
        print("MATTbot:"+reminder)
    
    if(PORT==None):
        flag=0
    else:
        print("MATTbot:"+PORT)
        while(True):
            data=input("\nMattDevice:Enter the command...\ncmd:")
            if(data=="exit"):
                break
            else:
                HLEngine_communications.serSend(PORT,9600,data)
                HLEngine_audioProcess.playsound("voice/sent.wav") 


    if(Emotion==None):
        flag=0
    else:
        print("MATTbot:"+Emotion)

    if(Fight==None):
        flag=0
    else:
        print("MATTbot:"+Fight)

    """if(responser==None):
        flag=0
    else:
        print(responser)"""

    if(hyperLearn==None):
        flag=0
    else:
        print(hyperLearn)

    if(playBoy==None):
        flag=0
    else:
        print(playBoy)

    

 
    
  
    
