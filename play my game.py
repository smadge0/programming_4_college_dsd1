import random as rand




quiz = {
    "what is the hit scran the northeast is known for":{"answer":"parmo","hint":"middlesbrough invented it!","possible answer":["toad in the hole","parmo","fried scallop","fish and chips"],"asked":False},
    "what is the best sandwich in the sainsburys meal deal":{"answer":"smoked salmon and cream cheese","hint":"contains a fish","possible answer":["smoked salmon and cream cheese sandwich","ham and cheese sandwich","BLT sandwich","trick question: the only good main is the southern fried chicken pasta"],"asked":False},
    "best mcdonalds burger (not including breakfast)":{"answer":"mccrispy","hint":"chicken burger","possible answer":["mccrispy","chicken big mac","mcchicken","chicken legend"],"asked":False},
    "best mcdonalds burger (including breakfast)":{"answer":"double sausage and egg mcmuffin","hint":"brekky","possible answer":["double sausage and egg mcmuffin","chicken selects (with sweet chilli sauce)","big mac","chicken nuggets meal (your sauce of choice)"],"asked":False},
    "which blue guy is the main character of deltarune":{"answer":"kris","hint":"failed to star in 'the sblurfs'","possible answer":["chara","kris","joseph","frisk"],"asked":False},
    "which yellow guy is the main character of undertale":{"answer":"frisk","hint":"giraffe","possible answer":["togore","sans","frisk","pluey"],"asked":False},
    "which hit skeleton is a recurring character in deltarune and undertale":{"answer":"sans","hint":"whoopee cushion","possible answer":["pluey","nubert","pluey","sans"],"asked":False},
    "am i right lads or am i right lads":{"answer":"you are right lad","hint":"no hint for this one","possible answer":["you are right lad","no","yes","you are wrong lad"],"asked":False},
    "who made hit vsynth song butcher vanity featuring yi xi":{"answer":"flavor foley","hint":"yum yum","possible answer":["vane lily","flavor foley","justin timberlake","mariah carey"],"asked":False},
    "how many are left in phase 3a of call of the void":{"answer":"one","hint":"look up the song","possible answer":["one","two","five","three"],"asked":False},
    "who made hit vsynth song fire!!! feeturing kasane teto":{"answer":"jamie p","hint":"known for other songs related to machines and birds","possible answer":["jamie p","flavor foley","justin bieber","adam sandler"],"asked":False}
}



def playmygame():
    score = 0
    morequestions = True
    while morequestions == True:
        question = rand.choice(list(quiz.keys()))
        if quiz[question]["asked"] == True:
            morequestions == True
            continue
        else:
            quiz[question]["asked"] = True
            print(question)
            for x in range (0,len(quiz[question]["possible answer"])):
                print(f"{x+1}: {quiz[question]["possible answer"][x]}")
            valid = False
            while valid == False:
                answer = input("pick an answer! >> ")
                if answer == quiz[question]["answer"] or answer == (quiz[question]["possible answer"][int(answer)]):
                    print("goodjob")
                    score = score + 1
                    valid = True
                else:
                    print(f"you suck. answer was {quiz[question]["answer"]}")
                    valid = True
    print(str(score))

playmygame()