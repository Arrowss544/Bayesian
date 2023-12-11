#构建有向图网络
# 左边为父节点 右边为子节点
from pgmpy.models import BayesianNetwork
test_model = BayesianNetwork([('A','B'),
                              ('B','C')])
#设置CPT参数
from pgmpy.factors.discrete import TabularCPD
#无父节点的结点的条件概率表（CPT）
cpd_A = TabularCPD(variable='A', variable_card=2,
                      values=[[0.5], #0
                              [0.5]])#1
#一个父节点的结点的条件概率表（CPT）
cpd_B = TabularCPD(variable='B', variable_card=2,
                      values=[[0.4, 0.6],#0
                              [0.6, 0.4]],#1
                      evidence=['A'],#evidence_card 0 1
                      evidence_card=[2])
cpd_C = TabularCPD(variable='C', variable_card=2,
                      values=[[0.8, 0.4],#0
                              [0.2, 0.6]],#1
                      evidence=['B'],#evidence_card 0 1
                      evidence_card=[2])
#构建总的CPT拓扑网络
test_model.add_cpds(cpd_A, cpd_B, cpd_C)
#变量消除法是精确推断的一种方法.
from pgmpy.inference import VariableElimination
asia_infer = VariableElimination(test_model)
q = asia_infer.query(variables=['A'], evidence={'B':1})
print(q)
q = asia_infer.query(variables=['B'], evidence={'A':1})
print(q)
q = asia_infer.query(variables=['B'])
print(q)







