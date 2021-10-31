import pyttsx3
import random
import time
engine=pyttsx3.init()
voices=engine.getProperty('voices')
rate=engine.getProperty('rate')
engine.setProperty('rate',180)
engine.setProperty('voice',voices[0].id)

#follow proper coding standards
#do error handling correctly
#add some  test cases and validation

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def countdown(t=20):
    while t:
        mins,secs=divmod(t,60)
        timeformat='{:02d}:{:02d}'.format(mins,secs)
        print(timeformat,end='\r')
        time.sleep(1)
        t-=1
    speak('Time Up..!' )
def gamerules():
    speak("The Rules are As Follows:")
    speak(":-There will be Multiple Questions and the Options For Those")
    speak(":-You have to Clear All The Questions To Reach The Winner Position")
    speak(":- In Case if you Gave a Wrong Answer You Have To Do An Activity Given After The Question")
    speak("Press 1 to Go to Main Menu")
    inp=int(input())
    if inp is 1:
        mainmenu()
    else:
        speak("Please Give A Valid No....")
        gamerules()
def gamecred():
    speak("This Is An Environmental Game Built with a Concept to Aware People About the Nature...")
    speak("This Game Is Just A Thought To Remind And Educate The People About Nature..")
    speak("Through This Game You Can Gain Knowledge Of how the habitats and Animals are being destroyed..")
    speak("Its not my intention to hurt the feelings of anyone, i am just echoing you the truth..")
    speak("Please Don't Forget To Give A Feedback..!")
    speak("Regards,Mihir Sharma..!")
    speak("Press 1 to Go to Main Menu")
    inp=int(input())
    if inp is 1:
        mainmenu()
    else:
        speak("Please Give A Valid No....")
        gamecred()
def startgame():
    speak("The Game is Starting")
    speak("Beware Humans! Truth Ahead..!")
    speak("Please Select Yor Genre..!")
    speak("1: Extinct Wildlife")
    speak("2: Plastic Ocean")
    # speak("3: Earth's Lungs")
    # speak("4: Atmosphere")
    n=int(input())
    if n is 1:
        ExAn()
    elif n is 2:
        AqLi()
    # elif n is 3:
    #     EaLu()
    # elif n is 4:
    #     Atm()
    else:
        speak("Wrong Input!")
        speak("Please Input A Valid No.")
        startgame()
def ExAn():
    speak("You Have Chosen Extinct Wildlife")
    speak("Be Ready To Face The Truth About Extincting WildLife")
    speak("So Here We go..")
    speak("What is the name of the world's last surviving male northern white rhinoceros(he went viral in 2017 when a picture of him was posted on Twitter)?")
    speak("The Options Are..")
    speak("1:Syria")
    speak("2:Sri Lanka")
    speak("3:Somalia")
    speak("4:Sudan")
    i1=int(input())
    if i1 is 4:
        speak("Correct Answer..")
        speak("Sudan was the name of the world's last surviving male northern white rhinoceros!")
        speak("Next Question ..")
        speak("Elephants are now better protected from ivory trade,but poachers have turned their attention to another animal,now at risk from extinction.Which is it?")
        speak("The Options Are..")
        speak("1:Hippo")
        speak("2:Mammoth")
        speak("3:Walrus")
        speak("4:Narwhal")
        i2=int(input())
        if i2 is not 1:
            Act()
        else:
            speak("Correct Answer..")
            speak("Hippo is now Slowly Coming up into the list of entinction!")
            speak("Question No. 3..")
            speak("Scientists have reported that Earth is undergoing a new mass extinction because of the biological anhilation of wildlife in recent decades.How many of these events have occurred in the planet's history?")
            speak("The Options Are..")
            speak("1:0")
            speak("2:1")
            speak("3:3")
            speak("4:5")
            i3=int(input())
            if i3 is not 4:
                Act()
            else:
                speak("Correct Answer..")
                speak("There had been 5 mass extinction Till now..!")
                speak("Next Question ..")
                speak("What Controversial dish made from an endangered species did Donald Trump eat on a recent trip to Vietnam?")
                speak("The Options Are..")
                speak("1:Roast monitor lizard")
                speak("2:porpoise stew")
                speak("3:Shark Fin Soup")
                speak("4:Turtle Soup")
                i4=int(input())
                if i4 is not 3:
                    Act()
                else:
                    speak("Correct Answer..")
                    speak("Donald Trump Eat Shark fin soup which was in a great controversy!")
                    speak("Next Question No. 5..")
                    speak("The ploughshare tortoise is now critically endangered and could be extinct in the wild in around two years.how many are now thought to exist in the wild in their native home of Madagascar?")
                    speak("The Options Are..")
                    speak("1:10")
                    speak("2:100")
                    speak("3:1000")
                    speak("4:1100")
                    i5=int(input())
                    if i5 is not 2:
                        Act()
                    else:
                        speak("Correct Answer..")
                        speak("Congratulations..!,you are half way there..")
                        speak("Only 100 tortoise are thought to be in madagascar!")
                        speak("Next Question ..")
                        speak("Which popular animal is the most suffered animal due to global warming?")
                        speak("The Options Are..")
                        speak("1:Lion")
                        speak("2:snow Leopard")
                        speak("3:Walrus")
                        speak("4:Polar Bear")
                        i6=int(input())
                        if i6 is not 4:
                            Act()
                        else:
                            speak("Correct Answer..")
                            speak("Polar Bears are regarded as the most suffered animals due to the melting of glaciers by global warming!")
                            speak("Next Question coming up..")
                            speak("What percentage of world's wild primate is on course to die out?")
                            speak("The Options Are..")
                            speak("1:40")
                            speak("2:50")
                            speak("3:60")
                            speak("4:70")
                            i7=int(input())
                            if i7 is not 3:
                                Act()
                            else:
                                speak("Correct Answer..")
                                speak("About 60 percent of world's wildlife is about to die out!")
                                speak("Next Question ..")
                                speak("About How many species have died due to humans?")
                                speak("The Options Are..")
                                speak("1:1 million")
                                speak("2:10 million")
                                speak("3:17 million")
                                speak("4:1 billion")
                                i8=int(input())
                                if i8 is not 1:
                                    Act()
                                else:
                                    speak("Correct Answer..")
                                    speak("you are going great buddy")
                                    speak("About 1 million species of animals have died out due to humans!")
                                    speak("Question No. 9..")
                                    speak("About How many animals are being killed every day around the world?")
                                    speak("The Options Are..")
                                    speak("1:1 million")
                                    speak("2:3 billion")
                                    speak("3:1 billion")
                                    speak("4:10 million")
                                    i9=int(input())
                                    if i9 is not 2:
                                        Act()
                                    else:
                                        speak("Correct ..")
                                        speak("you are going to be a champion")
                                        speak("yes you guessed it right!, About 3 billion animals are being slaughtered daily..!")
                                        speak("Here comes the Last and Final Question..Be Ready..!")
                                        speak("what has Stephen Hawking warned could lead to the extinction of humans?")
                                        speak("The Options Are..")
                                        speak("1:Artificial Intelligence")
                                        speak("2:Obesity")
                                        speak("3:Stupidity")
                                        speak("4:Climate Change")
                                        i10=int(input())
                                        if i10 is not 1:
                                            Act()
                                        else:
                                            speak("You Won..!")
                                            speak("congratulations for winning the quiz of this genre..")
                                            speak("You deserve A Pat for This..")
                                            speak("press any number key to go to main menu")
                                            i11=int(input())
                                            speak("Redirecting you to main menu..")
                                            if i11 is str:
                                                mainmenu()
                                            else:
                                                mainmenu()                                          
    else:
        Act()
def Act():
    speak("Wrong Answer Buddy..")
    speak("Now As per the rules get ready to do the Activities...")
    a1="Place a Container of water outside your house or on terrace for birds to drink"
    a2="Feed the stray dogs for atleast seven days regularly"
    a3="Plant a seedling in your home or anywhere else and take care of it"
    a4="Make a Zero waste Day atleast twice in a week by not using plastics"
    a5="Pledge to use paper or cloth bags instead of plastic bags"
    a6="Never use or throw single use plastic bottles,use alternative instead"
    a7="Go and feed any animal near you regularly"
    a8="Being a Human, show humanity. Make sure that atleast in your neighbourhood no poor sleeps hungry"
    a9="Pledge to never throw garbage into the rivers"
    a=[a1,a2,a3,a4,a5,a6,a7,a8,a9]
    r=random.choice(a)
    speak(r)
    speak("Press any key to go to main menu")
    n=input()
    speak("Redirecting you to main menu..")
    if n is str:
        mainmenu()
    else:
        mainmenu()   
def AqLi():
    speak("You have Chosen Aquatic Life")
    speak("Be Ready To Face The Truth About Marine Life")
    speak("So Here We go..")
    speak("Why is Plastic dangeroues for marine life?")
    speak("The Options Are..")
    speak("1:They mistake it for food and cannot digest")
    speak("2:They can get tangled in it which hinders their ability to swim")
    speak("3:Both 1 and 2")
    speak("4:It's not dangerous because they use plastic waste for habitats")
    i1=int(input())
    if i1 is 3:
        speak("Correct Answer..")
        speak("You guessed it right.Plastics are a real threat to our marine life because of this reasons!")
        speak("Next Question ..")
        speak("where does the majority of plastic waste end up?")
        speak("The Options Are..")
        speak("1:Oceans")
        speak("2:Burned for energy")
        speak("3:landfills")
        speak("4:Recycled")
        i2=int(input())
        if i2 is not 1:
            Act()
        else:
            speak("Correct Answer..")
            speak("Taking hundreds of years to break up,plastic is not going anywhere soon.While some of it does make it to the landfills and recycling centers,the majority of plastic wastes end up in oceans!")
            speak("Question No. 3..")
            speak("How many million tons of plastic are dumped in oceans every year?")
            speak("The Options Are..")
            speak("1:1 million tons")
            speak("2:8 million tons")
            speak("3:20 million tons")
            speak("4:50 million tons")
            i3=int(input())
            if i3 is not 2:
                Act()
            else:
                speak("Correct Answer..")
                speak("According to Ellen MacArthur Foundation at least 8 million tons of plastic is dumped into our oceans each year..!")
                speak("Next Question ..")
                speak("How many marine species are harmed by plastic pollution?")
                speak("The Options Are..")
                speak("1:52")
                speak("2:1326")
                speak("3:693")
                speak("4:5489")
                i4=int(input())
                if i4 is not 3:
                    Act()
                else:
                    speak("Correct Answer..")
                    speak("A 2015 Plymouth University compiled reports recorded from around the world and found evidence of 44500 animals becoming entangled or swallowing plastic debris,accounting for a total of 693 marine species.!")
                    speak("Next Question No. 5..")
                    speak("There are 51 trillion microplastic particles in the ocean today,which is __ times more than the stars in our galaxy?")
                    speak("The Options Are..")
                    speak("1:10")
                    speak("2:500")
                    speak("3:1070")
                    speak("4:100")
                    i5=int(input())
                    if i5 is not 2:
                        Act()
                    else:
                        speak("Correct Answer..")
                        speak("Congratulations..!,you are half way there..")
                        speak("You guessed it right.There are 51 trillion microplastic particles in the ocean today,which is 500 times more than the stars in our galaxy!")
                        speak("Next Question ..")
                        speak("By what year do scientists predict plastic will outweigh fish in the ocean,pound for pound?")
                        speak("The Options Are..")
                        speak("1:2020")
                        speak("2:2050")
                        speak("3:2250")
                        speak("4:3000")
                        i6=int(input())
                        if i6 is not 2:
                            Act()
                        else:
                            speak("Correct Answer..")
                            speak("There will be more plastics than fish in the ocean by 2050!")
                            speak("Next Question coming up..")
                            speak("What percentage of emitted carbon dioxide is absorbed by the oceans?")
                            speak("The Options Are..")
                            speak("1:10")
                            speak("2:70")
                            speak("3:50")
                            speak("4:40")
                            i7=int(input())
                            if i7 is not 4:
                                Act()
                            else:
                                speak("Correct Answer..")
                                speak("About 40 percent of world's carbon dioxide is absorbed by the oceans!")
                                speak("Next Question ..")
                                speak("On average how long is a plastic bag used by a person before being thrown away?")
                                speak("The Options Are..")
                                speak("1:12 minutes")
                                speak("2:1 hour")
                                speak("3:1 day")
                                speak("4:1 week")
                                i8=int(input())
                                if i8 is not 1:
                                    Act()
                                else:
                                    speak("Correct Answer..")
                                    speak("you are going great buddy")
                                    speak("The average working life of a plastic bag is just 12 minutes before it is thrown away!")
                                    speak("Question No. 9..")
                                    speak("About 71 percent of the Earth is covered with water.How much of it is fresh water?")
                                    speak("The Options Are..")
                                    speak("1:50 percent")
                                    speak("2:32 percent")
                                    speak("3:2.5 percent")
                                    speak("4:10 percent")
                                    i9=int(input())
                                    if i9 is not 3:
                                        Act()
                                    else:
                                        speak("Correct ..")
                                        speak("you are really amazing")
                                        speak("yes you guessed it right!, About 2.5 percent of the Earth's water is freshwater..!")
                                        speak("Here comes Another Question..Be Ready..!")
                                        speak("More than half of the breathable oxygen in world comes from?")
                                        speak("The Options Are..")
                                        speak("1:The oceans")
                                        speak("2:The forests")
                                        speak("3:Lakes")
                                        speak("4:Clouds")
                                        i10=int(input())
                                        if i10 is not 1:
                                            Act()
                                        else:
                                            speak("Correct ..")
                                            speak("About two-thirds of the world's breathable oxygen comes from the ocean or,more specifically from tiny marine plants,called phytoplankton..!")
                                            speak("Final Question coming up..Be Ready..!")
                                            speak("How much water does it take to produce one bottle of water?")
                                            speak("The Options Are..")
                                            speak("1:No water is used to produce plastic")
                                            speak("2:1 bottle of water")
                                            speak("3:6 bottles of water")
                                            speak("4:3 bottles of water")
                                            i11=int(input())
                                            if i11 is not 4:
                                                Act()
                                            else:
                                                speak("You Won The Quiz..!")
                                                speak("congratulations for winning the quiz of this genre..")
                                                speak("You deserve A Pat for This..")
                                                speak("Press any key to go to main menu")
                                                i12=int(input())
                                                speak("Redirecting you to main menu..")
                                                if i12 is str:
                                                    mainmenu()
                                                else:
                                                    mainmenu()                                            
    else:
        Act()

def mainmenu():
    while True:
        speak("Welcome To The Game")
        speak("Press The Following To Proceed")
        speak("1:Start Game")
        speak("2:Rules")
        speak("3:About Game")
        speak("4:Exit")
        speak("Your Choice..?")
        i=int(input())
        if i is 1:
            startgame()
        if i is 2:
            gamerules()
        if i is 3:
            gamecred()
        if i is 4:
            speak("Thanks for Playing..")
            exit()
        else:
            speak("Wrong Choice")
            continue

if __name__ == "__main__":
     mainmenu()
    # countdown()