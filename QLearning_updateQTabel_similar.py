# encoding:utf-8
print '''
*--|
目标：用最少的步数，最高的分数
'''
import random,pprint
trainTimes = 50
state = range(1,4+1)
action = ['toLeft','toRight','sleep']
action_value = [-1,1,0]#用于更新state
reward = [[-10,1,-1],[-1,1,-1],[-1,1,-1],[-1,-10,100]]
translate = [[1,2],[0,1,2],[0,1,2],[0,2]]#当前状态允许的操作
QTable = []#初始化Q表
resultRecord = [[]]
for i in range(1,trainTimes+1):
    print u' ----- 开始第%d次'%i
    episode = 0#步数复杂度
    finalReward = 0
    start_state = 1
    #before_state,current_state
    current_state = start_state
    while finalReward >= 0:#设定游戏结束条件一
        before_state = current_state
        choice_action = random.choice(translate[before_state-1])
        if before_state == 4 and choice_action == 2:#设定游戏结束条件二
            pass
        else:
            current_state = before_state+action_value[choice_action]
            finalReward += reward[before_state-1][choice_action]
            episode += 1
            print u'之前状态：',before_state,u'通过行为：',action[choice_action],u'当前状态：',current_state,u'当前分数：',finalReward,u'使用步数：',episode
        currentData = [before_state,action[choice_action]]
        #QTable.append(currentData)
        #更新Q表
        if currentData not in QTable:
            QTable.append(currentData)
    print u' ----- 结束第%d次'%i
    print u''
print u'Q表最终为：'
pprint.pprint(QTable)
print u'程序执行完毕'
