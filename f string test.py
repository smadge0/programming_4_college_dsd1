milk = int(input("how many milks do you wanna buy. "))
if milk > 50:
    print(f"dude. why are you buying {milk} milks. thats insane.")
elif milk < 50 and milk > 10:
    print(f"ok . like. {milk} is a lot of milks but you do you")
elif milk < 10 and milk > 0:
    print(f"go crazy i guess i mean i dont have the kinda money for {milk} milks but to each their own")
elif milk == 0:
    print(f"no milks? really?")
elif milk < 0:
    print(f"why are. what. how are you gonna buy {milk} milks. thats literally negative. how are you going to un buy milk ????? who are you ???")