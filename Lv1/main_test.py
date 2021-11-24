def test_Answer():
    bFinish = False
    bFloor_Broom = True
    nFloor_Dustpan = 0
    bFloor_Finish = False
    bWindow_Rag = True
    nWindow_Cleaner = 100
    bWindow_Finish = False
    bBlackboard_Eraser = True
    nBlackboard_Dirty = 0
    bBlackboard_Finish = False
    nTarget_Classroom = 101

    while not bFinish:
        while not bFloor_Finish:
            if nFloor_Dustpan <= 100:
                if nFloor_Dustpan == 0:
                    print("바닥 청소 "+str(nTarget_Classroom)+"호 시작 : ", end='')
                nFloor_Dustpan += 10 if bFloor_Broom == True else 0
                print("⬜", end=' ')

            else:
                nFloor_Dustpan = 0 if nFloor_Dustpan >= 100 else nFloor_Dustpan
                bFloor_Finish = True if nFloor_Dustpan == 0 else False
                if bFloor_Finish:
                    print("  종료", end='\n')

        while not bWindow_Finish:
            if nWindow_Cleaner >= 0:
                if nWindow_Cleaner == 100:
                    print("창문 청소 "+str(nTarget_Classroom)+"호 시작 : ", end='')
                nWindow_Cleaner -= 10 if bWindow_Rag == True else 0
                print("⬜", end=' ')
            else:
                nWindow_Cleaner = 100 if nWindow_Cleaner <= 0 else nWindow_Cleaner
                bWindow_Finish = True if nWindow_Cleaner == 100 else False
                if bWindow_Finish:
                    print("  종료", end='\n')

        while not bBlackboard_Finish:
            if nBlackboard_Dirty <= 100:
                if nBlackboard_Dirty == 0:
                    print("칠판 닦이 "+str(nTarget_Classroom)+"호 시작 : ", end='')
                nBlackboard_Dirty += 10 if bBlackboard_Eraser == True else 0
                print("⬜", end=' ')

            else:
                nBlackboard_Dirty = 0 if nBlackboard_Dirty >= 100 else nBlackboard_Dirty
                bBlackboard_Finish = True if nBlackboard_Dirty == 0 else False
                if bBlackboard_Finish:
                    print("  종료", end='\n')

        bFinish = True if (bFloor_Finish and bWindow_Finish
                           and bBlackboard_Finish) == True else False

    assert bFinish


test_Answer()
