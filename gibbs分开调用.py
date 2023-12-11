#用到第三方库networkx,matplotlib
import numpy as np
#cpt输入
cpt={'B': [0.002, []], 'E': [0.003, []], 'T': [0.01, []], 'MC': [0.1, 0.75, ['A']], 'DB': [0.001, 0.22, 0.85, 0.95, ['B', 'T']], 'JC': [0.001, 0.35, 0.8, 0.85, ['A', 'DB']], 'A': [0.001, 0.27, 0.34, 0.42, 0.9, 0.94, 0.96, 0.99, ['B', 'E', 'T']]}
#cpt={'A':[0.5,[]],'B':[0.6,0.4,['A']],'C':[0.4,0.6,['A']],'D':[0.3,0.4,0.5,0.6,['B','C']],'E':[0.3,0.4,0.5,0.6,['B','C']]}
#cpt={'A':[0.5,[]],'B':[0.6,0.4,['A']],'C':[0.4,0.6,['A']],'D':[0.3,0.4,0.5,0.6,['B','C']]}
#cpt={'A':[0.5,[]],'B':[0.6,0.4,['A']],'C':[0.4,0.6,['B']]}
#题目选择
evidence_dots_input = ""
inquire_dots_input = "JC=1"
sample_number=100
question = 0
if False:
    if question==1:
        evidence_dots_input = "MC=1 JC=1"
        inquire_dots_input = "B=1"
    elif question==2:
        evidence_dots_input = "B=1 T=0"
        inquire_dots_input = "JC=1"
    elif question==3:
        evidence_dots_input = "B=1 T=0"
        inquire_dots_input = "MC=1"
    elif question==4:
        evidence_dots_input = "A=1 T=1 B=0"
        inquire_dots_input = "JC=1"
    elif question==5:
        evidence_dots_input = "A:1 T:1 B:0"
        inquire_dots_input = "MC=1"
    elif question==6:
        evidence_dots_input="JC=1"
        inquire_dots_input="B=1"
global inquire_number
inquire_number=10000
network_dot = []
network_parent_nodes = []
network_child_nodes = []
def gibbs_sampling(cpt,all_dots,inquire_dot_states,evidence_dot_states,inquire_number):
    # 非证据变量初始化状态处理
    if True:
        non_evidence_dots = []  # 非证据变量
        non_evidence_dot_states = {}  # 非证据变量状态
        for i in all_dots:
            non_evidence_dots.append(i)
            non_evidence_dot_states[i] = 1
        for i in evidence_dot_states:
            non_evidence_dots.remove(i)
            del non_evidence_dot_states[i]
    # 吉布斯采样
    if True:
        import random
        true_count = 0  # 计数
        all_dot_states = {}  # 所有结点状态
        which_non_evidence_dot = 0
        for i in range(inquire_number):
            # 回归
            if which_non_evidence_dot == len(non_evidence_dots):
                which_non_evidence_dot = 0
            # 所有结点状态处理
            all_dot_states.update(non_evidence_dot_states)
            all_dot_states.update(evidence_dot_states)
            # 计数
            multiple_inquire_one_count = 0  # 辅助计数
            for j in inquire_dot_states:
                if non_evidence_dot_states[j] == inquire_dot_states[j]:
                    multiple_inquire_one_count = multiple_inquire_one_count + 1
                if multiple_inquire_one_count == len(inquire_dot_states):
                    true_count = true_count + 1
            sample_dot = non_evidence_dots[which_non_evidence_dot]  # 采样变量
            sample_dot_parent_dots = cpt[sample_dot][-1]  # 采样变量的父节点
            sample_dot_parent_dots_state = str()
            for j in sample_dot_parent_dots:  # 采样变量的父节点状态处理
                if all_dot_states[j] == 1:
                    sample_dot_parent_dots_state = sample_dot_parent_dots_state + "1"
                else:
                    sample_dot_parent_dots_state = sample_dot_parent_dots_state + "0"
            if sample_dot_parent_dots == []:
                sample_dot_parent_dots_state = "0"
            # 采样变量概率
            magnification=10**4
            sample_dot_true_percentage = int(cpt[sample_dot][int(sample_dot_parent_dots_state, 2)] * magnification)
            sample_dot_random_percentage = random.randint(1, magnification)
            if sample_dot_random_percentage <= sample_dot_true_percentage:
                non_evidence_dot_states[sample_dot] = 1
            else:
                non_evidence_dot_states[sample_dot] = 0
            which_non_evidence_dot = which_non_evidence_dot + 1
        percentage=true_count/inquire_number
    return(percentage)
def sample_data(cpt,inquire_dots_input,evidence_dots_input,sample_number,inquire_number):
    # 所有结点处理
    if True:
        all_dots = []  # 所有结点
        for i in cpt:
            all_dots.append(i)
    # 证据变量处理
    if True:
        evidence_dot = str()  # 单个证据变量
        evidence_dots = []
        evidence_dot_state = str()  # 单个证据变量状态
        evidence_dot_states = {}  # 所有证据变量状态
        end1 = 0
        for i in range(len(evidence_dots_input)):
            if evidence_dots_input[i] == "=":
                end1 = 1
                continue
            if evidence_dots_input[i] == " " and i != evidence_dots_input[-1]:
                end1 = 0
                evidence_dots.append(evidence_dot)
                evidence_dot_states[evidence_dot] = int(evidence_dot_state)
                evidence_dot = str()
                evidence_dot_state = str()
                continue
            if end1 == 0:
                evidence_dot = evidence_dot + evidence_dots_input[i]
            if end1 != 0:
                evidence_dot_state = evidence_dot_state + evidence_dots_input[i]
            if i == len(evidence_dots_input) - 1:
                end1 = 0
                evidence_dots.append(evidence_dot)
                evidence_dot_states[evidence_dot] = int(evidence_dot_state)
                evidence_dot = str()
                evidence_dot_state = str()
                continue
    # 查询变量处理
    if True:
        inquire_dot = str()  # 单个查询变量
        inquire_dots = []  # 所有查询变量
        inquire_dot_state = str()  # 单个查询变量状态
        inquire_dot_states = {}  # 所有查询变量状态
        end1 = 0
        for i in range(len(inquire_dots_input)):
            if inquire_dots_input[i] == "=":
                end1 = 1
                continue
            if inquire_dots_input[i] == " " and i != inquire_dots_input[-1]:
                end1 = 0
                inquire_dots.append(inquire_dot)
                inquire_dot_states[inquire_dot] = int(inquire_dot_state)
                inquire_dot = str()
                inquire_dot_state = str()
                continue
            if end1 == 0:
                inquire_dot = inquire_dot + inquire_dots_input[i]
            if end1 != 0:
                inquire_dot_state = inquire_dot_state + inquire_dots_input[i]
            if i == len(inquire_dots_input) - 1:
                end1 = 0
                inquire_dots.append(inquire_dot)
                inquire_dot_states[inquire_dot] = int(inquire_dot_state)
                inquire_dot = str()
                inquire_dot_state = str()
                continue
    # 判断查询结点是否是只有子节点的结点
    if True:
        start_dot_flag = 0  # 标志
        start_dot_jugement_count = 0  # 辅助计数
        for i in inquire_dot_states:
            if cpt[i][-1] == []:
                start_dot_jugement_count = start_dot_jugement_count + 1
        if start_dot_jugement_count == len(inquire_dot_states) and evidence_dots_input != str():
            evidence_dot_states, inquire_dot_states = inquire_dot_states, evidence_dot_states
            evidence_dots, inquire_dots = inquire_dots, evidence_dots
            start_dot_flag = 1
    # 非证据变量初始化状态处理
    if True:
        non_evidence_dots = []  # 非证据变量
        non_evidence_dot_states = {}  # 非证据变量状态
        for i in all_dots:
            non_evidence_dots.append(i)
            non_evidence_dot_states[i] = 1
        for i in evidence_dot_states:
            non_evidence_dots.remove(i)
            del non_evidence_dot_states[i]
    # 判断是否用到贝叶斯公式
    if True:
        import numpy as np
        percentage_evidence = 1
        #无需贝叶斯公式
        if start_dot_flag == 0:
            #多次采样取平均
            percentage_list = []
            for i in range(sample_number):
                percentage=gibbs_sampling(cpt,all_dots,inquire_dot_states,evidence_dot_states,inquire_number)
                percentage_list.append(percentage)
            fi=open('3.txt','w+')
            for i in percentage_list:
                fi.write(str(i)+'\n')
            percentage_average=np.mean(percentage_list)
            return (percentage_average)
        #需要贝叶斯公式
        if start_dot_flag == 1:
            #P(parents(Xi))成立概率
            for i in evidence_dot_states:
                if evidence_dot_states[i] == 1:
                    percentage_evidence = percentage_evidence * cpt[i][0]
                else:
                    percentage_evidence = percentage_evidence * (1 - cpt[i][0])
            #P(parents(Xi)|Xi)成立概率
            percentage_list = []
            for i in range(sample_number):
                percentage=gibbs_sampling(cpt,all_dots,inquire_dot_states,evidence_dot_states,inquire_number)
                percentage_list.append(percentage)
            percentage_average=np.mean(percentage_list)
            #P(parents(Xi))成立概率
            percentage_list = []
            for i in range(sample_number):
                percentage = gibbs_sampling(cpt, all_dots, inquire_dot_states,{},inquire_number)
                percentage_list.append(percentage)
            percentage_inquire = np.mean(percentage_list)
            return(percentage_average*percentage_evidence/percentage_inquire)
real_percentage=0.0073
percentage=sample_data(cpt,inquire_dots_input,evidence_dots_input,sample_number,inquire_number)
print(percentage)
print((percentage-real_percentage)/real_percentage*100)
