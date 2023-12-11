#2022年第九组贝叶斯网络程序
#成员：
#用到的第三方库 matplotlib networkx numpy
#吉布斯采样函数
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
#采样处理函数
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
        percentage_evidence = 1
        #无需贝叶斯公式
        if start_dot_flag == 0:
            #多次采样取平均
            percentage_list = []
            for i in range(sample_number):
                percentage=gibbs_sampling(cpt,all_dots,inquire_dot_states,evidence_dot_states,inquire_number)
                percentage_list.append(percentage)
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
#cpt.txt文件处理
def build_data(file_cpt):
    cpt = {}  # 所有CPT
    dot_cp = {}  # 过度CP
    dot_cpt = []  # 单点的CPT
    parent_dot = []  # 父节点
    child_dot = str()  # 子节点
    # 每一行遍历
    for i in file_cpt:
        # 过渡CP dot_cp处理
        if i[0] == "#" and dot_cp != {}:
            dot_cpt = [1, ] * (pow(2, len(parent_dot)) + 1)
            #将dot_cp数据写入cpt
            for j in dot_cp:
                tag = str()
                for k in j:
                    if k == "T":
                        tag = tag + "1"
                    elif k == "F":
                        tag = tag + "0"
                if j == str():
                    tag = "0"
                dot_cpt[int(tag, 2)] = dot_cp[j]
                dot_cpt[-1] = parent_dot
                cpt[child_dot] = dot_cpt
        #重置变量
        if i[0] == "#":
            dot_cp = {}  # 过度CP
            dot_cpt = []  # 单点的CPT
            parent_dot = []  # 父节点
            child_dot = str()  # 子节点
        #单个cpt处理
        if i[0] != "#":
            end1 = 0
            end2 = 0
            condition = str()
            percentage = str()
            # 找子节点child_dot
            for j in i:
                if j == ")":
                    end2 = end2 + 1
                if end1 != 0 and end2 == 0:
                    child_dot = child_dot + j
                if j == "(":
                    end1 = end1 + 1
            # 找父节点 parent_dot
            if end1 != 0 and end1 != 0:
                dot2 = str()
                for j in i:
                    if j == " ":
                        parent_dot.append(dot2)
                        dot2 = str()
                        continue
                    if j == "(":
                        break
                    dot2 = dot2 + j
            # 找对应CP
            if end1 == 0 and end2 == 0:
                for j in i:  # 找条件
                    if j == " ":
                        continue
                    if j in "1234567890":
                        break
                    condition = condition + j
                for j in i:  # 找概率
                    if j in "1234567890.":
                        percentage = percentage + j
                if condition in dot_cp:#检查条件是否重复
                    print("cpt.txt数据异常，请退出程序检查！")
                    main_first ()
                if float(percentage) > 1:#检查概率是否小于等于1
                    print("cpt.txt数据异常，请退出程序检查！")
                    main_first()
                dot_cp[condition] = float(percentage)
    return(cpt)
#绘制贝叶斯网络图
def networkx_draw(network_parent_nodes,network_child_nodes):
    print("正在绘制贝叶斯网络图...")
    floder_name = 'output'
    if os.path.exists(floder_name):
        pass
    else:
        os.mkdir(floder_name)
    G = nx.DiGraph()
    #添加有向边
    for i in range(len(network_parent_nodes)):
        if network_parent_nodes[i] == str() or network_child_nodes[i] == str() or network_parent_nodes[i] == network_child_nodes[i]:
            print("network.txt数据异常，请退出程序检查！")
            main_first()
        G.add_edge(network_parent_nodes[i],network_child_nodes[i])
    #绘制
    if True:
        nx.draw_planar(G,
                with_labels=True,
                edge_color='k',
                node_size=1000,
                node_shape='o',
                linewidths=5,
                width=2.0,
                alpha=1,
                style='solid',
                font_size=20,
                font_color='k'
                )
    #图像写出
    if True:
        real_time = time.asctime(time.localtime(time.time()))
        strpt_time = str(time.mktime(time.strptime(real_time, "%a %b %d %H:%M:%S %Y")))
        file_name = "output/贝叶斯网络"+strpt_time+".png"
        plt.savefig(file_name, format="PNG")
    print("绘制完成！已保存为程序同目录output文件夹下的:"+file_name)
#network.txt文件处理
def draw_data(network):
    for i in network:
        end1=0
        end2=0
        #有用行处理
        if i[0]!="#":
            #遍历单个字符
            #收集空格位置
            for j in i:
                if j==" ":
                    break
                end1= end1 + 1
            #收集结尾位置
            for j in i:
                if j=="\n":
                    break
                end2 = end2 + 1
            network_parent_nodes.append(i[:end1])
            network_child_nodes.append(i[(end1+1):end2])
    networkx_draw(network_parent_nodes, network_child_nodes)
#结束采样后选择函数
def main_third(cpt):
    print("请按数字选择一个选项。")
    print("1.继续。")
    print("2.退出。")
    ch2 = input("输入一个数字：")
    if ch2 == str(1):
        percentage=main_second(cpt)
        print('结果概率为:', percentage)
        main_third(cpt)
    elif ch2 == str(2):
        return ()
    else:
        print("请重新输入。")
        main_third(cpt)
#证据与查询变量输入函数
def main_second(cpt):
    print("请输入证据变量，多个变量用空格分开，例如:A=1 B=0")
    evidence_dots_input=input("证据变量：")
    print("请输入查询变量，多个变量用空格分开，例如:C=1 D=0")
    inquire_dots_input=input("查询变量：")
    print("请输入吉布斯采样函数的采样次数，推荐输入10000，按回车默认10000次。")
    inquire_number = input("采样次数：")
    print("请输入调用吉布斯采样函数次数，推荐输入100，按回车默认100次。")
    sample_number=input("采样次数：")
    if inquire_number == str():
        inquire_number=10000
    inquire_number=int(inquire_number)
    if sample_number == str():
        sample_number=100
    sample_number=int(sample_number)
    start_time = time.perf_counter_ns()
    percentage=sample_data(cpt,inquire_dots_input,evidence_dots_input,sample_number,inquire_number)
    end_time = time.perf_counter_ns()
    print('用时',round(end_time-start_time)/(10**9),'秒。')
    return(percentage)
#数据文件选择函数
def main_first():
    print("欢迎来到贝叶斯网络计算程序。")
    print("请选择一个数据文件目录：")
    print("1.默认目录，程序同文件下data/network.txt & cpt.txt。")
    print("2.自定义路径,相对路径或者绝对路径。")
    print("3.退出。")
    ch1 = input("输入一个数字：")
    if ch1 == str(1):
        try:
            file_network = open("data/network.txt", "r+", encoding='UTF-8')
            file_cpt = open("data/cpt.txt", "r+", encoding='UTF-8')
        except:
            print("文件路径异常，请退出程序并检查文件！")
            main_first()
    elif ch1 == str(2):
        print('需要network.txt和cpt.txt两个文件。')
        datapath=input("请输入数据路径：")
        network_datapath=datapath+"network.txt"
        cpt_datapath=datapath+"cpt.txt"
        try:
            file_network = open(network_datapath, "r+", encoding='UTF-8')
            file_cpt = open(cpt_datapath, "r+", encoding='UTF-8')
        except:
            print("文件路径异常，请退出程序并检查文件！")
            main_first()
    elif ch1 == str(3):
        return()
    else:
        print("请重新输入。")
        main_first()
    if ch1 == str(1) or ch1 == str(2):
        try:
            cpt=build_data(file_cpt)
            draw_data(file_network)
        except:
            return ()
        percentage=main_second(cpt)
        print('结果概率为:',percentage)
        main_third(cpt)
#初始化
if True:
    print('正在初始化...')
    #内置库 random time os
    import random
    import time
    import os
    #第三方库 matplotlib networkx numpy
    import matplotlib.pyplot as plt
    import networkx as nx
    import numpy as np
    network_dot = []
    network_parent_nodes = []
    network_child_nodes = []
    floder_name = 'data'
    if os.path.exists(floder_name):
        pass
    else:
        os.mkdir(floder_name)
main_first()
