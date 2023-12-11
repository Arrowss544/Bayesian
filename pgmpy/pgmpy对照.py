#构建有向图网络
# 左边为父节点 右边为子节点
from pgmpy.models import BayesianNetwork
alarm_model = BayesianNetwork([('B', 'A'),('E', 'A'),('T', 'A'),
                                ('B', 'DB'),('T', 'DB'),
                                ('A', 'JC'),('DB', 'JC'),
                                ('A', 'MC')])
#设置CPT参数
from pgmpy.factors.discrete import TabularCPD
#无父节点的结点的条件概率表（CPT）
#条件概率表(b)
cpd_Earthquake = TabularCPD(variable='E', variable_card=2,
                      values=[[0.997], #0
                              [0.003]])#1
#条件概率表(a)
cpd_Burglary = TabularCPD(variable='B', variable_card=2,
                      values=[[0.998], #0
                              [0.002]])#1
#条件概率表(c)
cpd_Thunder = TabularCPD(variable='T', variable_card=2,
                      values=[[0.99], #0
                              [0.01]])#1
#一个父节点的结点的条件概率表（CPT）
#条件概率表(e)
cpd_Marycall = TabularCPD(variable='MC', variable_card=2,#需要X光检查
                      values=[[0.9, 0.25],#0
                              [0.1, 0.75]],#1
                      evidence=['A'],#evidence_card 0 1
                      evidence_card=[2])
#两个父节点的结点的条件概率表（CPT）
#条件概率表(h)
cpd_Dogbark = TabularCPD(variable='DB', variable_card=2,
                        #(1) (2) (3) (4)
                        values=[[0.999, 0.78, 0.15, 0.05],#0
                                [0.001, 0.22, 0.85, 0.95]],#1
                        # 1 F  F  T  T
                        # 2 F  T  F  T
                        # N(1)(2)(3)(4)
                        evidence=['B', 'T'],#1,2
                        evidence_card=[2, 2])
#条件概率表(i)
cpd_Johncall = TabularCPD(variable='JC', variable_card=2,
                        #(1) (2) (3) (4)
                        values=[[0.999, 0.65, 0.2, 0.15],#0
                                [0.001, 0.35, 0.8, 0.85]],#1
                        #1 F  F  T  T
                        #2 F  T  F  T
                        #N(1)(2)(3)(4)
                        evidence=['A', 'DB'],#1,2
                        evidence_card=[2, 2])
#三个父节点的结点的条件概率表（CPT）
#条件概率表(i)
cpd_Alarm = TabularCPD(variable='A', variable_card=2,
                        #(1) (2) (3) (4)
                        values=[[0.999, 0.73, 0.66, 0.58, 0.1, 0.06, 0.04, 0.01],#0
                                [0.001, 0.27, 0.34, 0.42, 0.9, 0.94, 0.96, 0.99]],#1
                        #1 F  F  F  F  T  T  T  T
                        #2 F  F  T  T  F  F  T  T
                        #3 F  T  F  T  F  T  F  T
                        #N(1)(2)(3)(4)(5)(6)(7)(8)
                        evidence=['B', 'E', 'T'],#1,2,3
                        evidence_card=[2, 2, 2])
#构建总的CPT网络
alarm_model.add_cpds(cpd_Earthquake, cpd_Burglary, cpd_Thunder, cpd_Alarm, cpd_Dogbark, cpd_Johncall, cpd_Marycall)
#变量消除法是精确推断的一种方法.
from pgmpy.inference import VariableElimination
asia_infer = VariableElimination(alarm_model)
print("（a）已知两个邻居都给你打电话，出现盗贼的概率？")
q = asia_infer.query(variables=['B'], evidence={'MC': 1,'JC': 1})
print(q)
print("b）当出现盗贼且不打雷时，John和Mary给你打电话的概率分别是多少？")
q = asia_infer.query(variables=['JC'], evidence={'B': 1,'T': 0})
print(q)
q = asia_infer.query(variables=['MC'], evidence={'B': 1,'T': 0})
print(q)
print("c）当发生打雷且出现警报，但不出现盗贼时，John和Mary给你打电话的概率分别是多少？")
q = asia_infer.query(variables=['JC'], evidence={'A': 1,'T': 1, 'B':0})
print(q)
q = asia_infer.query(variables=['MC'], evidence={'A': 1,'T': 1, 'B':0})
print(q)
print("（d）当John给你打电话时，出现盗贼的概率是多少？")
q = asia_infer.query(variables=['B'], evidence={'JC': 1})
print(q)









