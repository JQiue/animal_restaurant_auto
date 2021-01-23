import base
import event
import time

x ,y, r , b = base.first()
tm=0
while tm == 0:
    time.sleep(0.1)
    fox_exist, fox_x, fox_y = base.check_character('fox')
    bird_exist, bird_x, bird_y = base.check_character('bird')
    tv_exist, tv_x, tv_y = base.check_character('tv')
    fine_exist, fine_x, fine_y = base.check_character('fine')


    if fox_exist == 1:

        event.fuck_fox()

    elif bird_exist == 1:

        event.fuck_bird()

    elif tv_exist == 1:

        event.fuck_tv()

    elif fine_exist == 1:

        event.fuck_fine()



    print("fox" + str(fox_exist))
    print("bird" + str(bird_exist))
    print("tv" + str(tv_exist))
    print("fine" + str(fine_exist))
