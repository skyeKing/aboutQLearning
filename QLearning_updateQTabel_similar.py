# encoding:utf-8
print '''
*--|
Ŀ�꣺�����ٵĲ�������ߵķ���
'''
import random,pprint
trainTimes = 50
state = range(1,4+1)
action = ['toLeft','toRight','sleep']
action_value = [-1,1,0]#���ڸ���state
reward = [[-10,1,-1],[-1,1,-1],[-1,1,-1],[-1,-10,100]]
translate = [[1,2],[0,1,2],[0,1,2],[0,2]]#��ǰ״̬����Ĳ���
QTable = []#��ʼ��Q��
resultRecord = [[]]
for i in range(1,trainTimes+1):
    print u' ----- ��ʼ��%d��'%i
    episode = 0#�������Ӷ�
    finalReward = 0
    start_state = 1
    #before_state,current_state
    current_state = start_state
    while finalReward >= 0:#�趨��Ϸ��������һ
        before_state = current_state
        choice_action = random.choice(translate[before_state-1])
        if before_state == 4 and choice_action == 2:#�趨��Ϸ����������
            pass
        else:
            current_state = before_state+action_value[choice_action]
            finalReward += reward[before_state-1][choice_action]
            episode += 1
            print u'֮ǰ״̬��',before_state,u'ͨ����Ϊ��',action[choice_action],u'��ǰ״̬��',current_state,u'��ǰ������',finalReward,u'ʹ�ò�����',episode
        currentData = [before_state,action[choice_action]]
        #QTable.append(currentData)
        #����Q��
        if currentData not in QTable:
            QTable.append(currentData)
    print u' ----- ������%d��'%i
    print u''
print u'Q������Ϊ��'
pprint.pprint(QTable)
print u'����ִ�����'
