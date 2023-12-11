fo = open("data/cpt.txt", "r+", encoding='UTF-8')
cpt={}#所有CPT
dot_cp = {}#过度CP
dot_cpt = []#单点的CPT
parent_dot = []#父节点
child_dot = str()#子节点
for i in fo:#每一行遍历
    if i[0] == "#" and dot_cp != {}:#过渡CP dot_cp处理
        dot_cpt = [1, ] * (pow(2, len(parent_dot)) + 1)
        for j in dot_cp:
            tag = str()
            for k in j:
                if k =="T":
                    tag=tag+"1"
                elif k =="F":
                    tag=tag+"0"
            if j == str():
                tag="0"
            dot_cpt[int(tag,2)]=dot_cp[j]
            dot_cpt[-1]=parent_dot
            cpt[child_dot]=dot_cpt
    if i[0] == "#":
        dot_cp = {}  # 过度CP
        dot_cpt = []  # 单点的CPT
        parent_dot = []  # 父节点
        child_dot = str()  # 子节点
    if i[0] != "#":
        end1=0
        end2=0
        condition = str()
        percentage = str()
        for j in i:#找子节点child_dot
            if j == ")":
                end2=end2+1
            if end1!=0 and end2==0:
                child_dot=child_dot+j
            if j == "(":
                end1=end1+1
        if end1!=0 and end1!=0:#找父节点 parent_dot
            dot2=str()
            for j in i:
                if j == " ":
                    parent_dot.append(dot2)
                    dot2=str()
                    continue
                if j == "(":
                    break
                dot2 = dot2 + j
        if end1 == 0 and end2 == 0:#找对应CP
            for j in i:#找条件
                if j == " ":
                    continue
                if j in "1234567890":
                    break
                condition = condition + j
            for j in i:#找概率
                if j in "1234567890.":
                    percentage = percentage + j
            dot_cp[condition]=float(percentage)
fi = open("output.txt", "w+", encoding='UTF-8')
for i in cpt:
    fi.write(i)
    fi.write("\n")
    fi.write(str(cpt[i]))
    fi.write("\n")
fo.close()
fi.close()