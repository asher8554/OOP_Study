def fFloor(bFinish, bBroom, nDustpan, nClassroom):
    while not bFinish:
        if nDustpan <= 100:
            if nDustpan == 0:
                print("바닥 청소 "+str(nClassroom)+"호 시작 : ", end='')
            nDustpan += 10 if bBroom == True else 0
            print("⬜", end=' ')

        else:
            nDustpan = 0 if nDustpan >= 100 else nDustpan
            bFinish = True if nDustpan == 0 else False
            if bFinish:
                print("  종료", end='\n')
    return bFinish, bBroom, nDustpan, nClassroom


def fWindow(bFinish, bRag, nCleaner, nClassroom):
    while not bFinish:
        if nCleaner >= 0:
            if nCleaner == 100:
                print("창문 청소 "+str(nClassroom)+"호 시작 : ", end='')
            nCleaner -= 10 if bRag == True else 0
            print("⬜", end=' ')
        else:
            nCleaner = 100 if nCleaner <= 0 else nCleaner
            bFinish = True if nCleaner == 100 else False
            if bFinish:
                print("  종료", end='\n')
    return bFinish, bRag, nCleaner, nClassroom


def fBlackboard(bFinish, bEraser, nDirty, nClassroom):
    while not bFinish:
        if nDirty <= 100:
            if nDirty == 0:
                print("칠판 닦이 "+str(nClassroom)+"호 시작 : ", end='')
            nDirty += 10 if bEraser == True else 0
            print("⬜", end=' ')

        else:
            nDirty = 0 if nDirty >= 100 else nDirty
            bFinish = True if nDirty == 0 else False
            if bFinish:
                print("  종료", end='\n')
    return bFinish, bEraser, nDirty, nClassroom


def test_Answer():
    bResult_Finish = False
    bFinish = []
    bFloor_Broom = []
    nFloor_Dustpan = []
    bFloor_Finish = []
    bWindow_Rag = []
    nWindow_Cleaner = []
    bWindow_Finish = []
    bBlackboard_Eraser = []
    nBlackboard_Dirty = []
    bBlackboard_Finish = []
    nTarget_Classroom = []

    for i in range(2):
        bFinish.append(False)
        bFloor_Broom.append(True)
        nFloor_Dustpan.append(0)
        bFloor_Finish.append(False)
        bWindow_Rag.append(True)
        nWindow_Cleaner.append(100)
        bWindow_Finish.append(False)
        bBlackboard_Eraser.append(True)
        nBlackboard_Dirty.append(0)
        bBlackboard_Finish.append(False)
        nTarget_Classroom.append(101+i)

        bFloor_Finish[i], bFloor_Broom[i], nFloor_Dustpan[i], nTarget_Classroom[i] = fFloor(
            bFloor_Finish[i], bFloor_Broom[i], nFloor_Dustpan[i], nTarget_Classroom[i])

        bWindow_Finish[i], bWindow_Rag[i], nWindow_Cleaner[i], nTarget_Classroom[i] = fWindow(
            bWindow_Finish[i], bWindow_Rag[i], nWindow_Cleaner[i], nTarget_Classroom[i])

        bBlackboard_Finish[i], bBlackboard_Eraser[i], nBlackboard_Dirty[i], nTarget_Classroom[i] = fBlackboard(
            bBlackboard_Finish[i], bBlackboard_Eraser[i], nBlackboard_Dirty[i], nTarget_Classroom[i])

        bFinish[i] = True if (bFloor_Finish[i] and bWindow_Finish[i]
                              and bBlackboard_Finish[i]) == True else False
    bResult_Finish = True if bFinish[0] and bFinish[1] else False

    assert bResult_Finish


test_Answer()
