#构建有向图网络
# 左边为父节点 右边为子节点
from pgmpy.models import BayesianNetwork
cancer_model = BayesianNetwork([('Pollution', 'Cancer'),
                              ('Smoker', 'Cancer'),
                              ('Cancer', 'Xray'),
                              ('Cancer', 'Dyspnoea')])
#设置CPT参数
from pgmpy.factors.discrete import TabularCPD
#无父节点的结点的条件概率表（CPT）
cpd_poll = TabularCPD(variable='Pollution', variable_card=2,
                      values=[[0.9], #Pollution_0
                              [0.1]])#Pollution_1
cpd_smoke = TabularCPD(variable='Smoker', variable_card=2,
                       values=[[0.7],#Smoker_0
                               [0.3]])#Smoker_1
#一个父节点的结点的条件概率表（CPT）
cpd_xray = TabularCPD(variable='Xray', variable_card=2,#需要X光检查
                      values=[[0.9, 0.2],#Xray_0
                              [0.1, 0.8]],#Xray_1
                      evidence=['Cancer'],#evidence_card Cancer_0 Cancer_1
                      evidence_card=[2])
cpd_dysp = TabularCPD(variable='Dyspnoea', variable_card=2,#呼吸困难
                      values=[[0.65, 0.3],#Dyspnoea_0
                              [0.35, 0.7]],#Dyspnoea_1
                      evidence=['Cancer'],#evidence_card Cancer_0 Cancer_1
                      evidence_card=[2])
#两个父节点的结点的条件概率表（CPT）
#Pollution   Pollution_0   Pollution_0   Pollution_1   Pollution_1
#Smoker      Smoker_0      Smoker_1      Smoker_0      Smoker_1
#Cancer_0    0.03          0.05          0.001         0.02
#cancer_1    0.97          0.95          0.999         0.98

cpd_cancer = TabularCPD(variable='Cancer', variable_card=2,
                        values=[[0.03, 0.05, 0.001, 0.02],#Cancer_0
                                [0.97, 0.95, 0.999, 0.98]],#Cancer_1
                        # 1 F  F  T  T
                        # 2 F  T  F  T
                        # N(1)(2)(3)(4)
                        evidence=['Pollution', 'Smoker'],#1,2
                        evidence_card=[2, 2])
#构建总的CPT拓扑网络
cancer_model.add_cpds(cpd_poll, cpd_smoke, cpd_cancer, cpd_xray, cpd_dysp)
#变量消除法是精确推断的一种方法.
from pgmpy.inference import VariableElimination
asia_infer = VariableElimination(cancer_model)

q = asia_infer.query(variables=['Cancer'], evidence={'Pollution':1, 'Smoker': 0})
#q = asia_infer.query(variables=['Xray'], evidence={'Cancer':0})
print(q)



