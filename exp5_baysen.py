from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

traffic_model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('Construction', 'TrafficJam'),
    ('TrafficJam', 'Honking'),
    ('TrafficJam', 'LateForWork')
])

cpd_rain = TabularCPD(
    variable='Rain', variable_card=2,
    values=[[0.80], [0.20]], 
    state_names={'Rain': ['No', 'Yes']}
)

cpd_construction = TabularCPD(
    variable='Construction', variable_card=2,
    values=[[0.90], [0.10]], 
    state_names={'Construction': ['No', 'Yes']}
)

cpd_traffic = TabularCPD(
    variable='TrafficJam', variable_card=2,
    values=[
        [0.95, 0.40, 0.30, 0.05],
        [0.05, 0.60, 0.70, 0.95]
    ],
    evidence=['Rain', 'Construction'], 
    evidence_card=[2, 2],
    state_names={'TrafficJam': ['No', 'Yes'], 'Rain': ['No', 'Yes'], 'Construction': ['No', 'Yes']}
)

cpd_honking = TabularCPD(
    variable='Honking', variable_card=2,
    values=[
        [0.90, 0.15],
        [0.10, 0.85]
    ],
    evidence=['TrafficJam'], 
    evidence_card=[2],
    state_names={'Honking': ['No', 'Yes'], 'TrafficJam': ['No', 'Yes']}
)

cpd_late = TabularCPD(
    variable='LateForWork', variable_card=2,
    values=[
        [0.90, 0.20],
        [0.10, 0.80]
    ],
    evidence=['TrafficJam'], 
    evidence_card=[2],
    state_names={'LateForWork': ['No', 'Yes'], 'TrafficJam': ['No', 'Yes']}
)

traffic_model.add_cpds(cpd_rain, cpd_construction, cpd_traffic, cpd_honking, cpd_late)
assert traffic_model.check_model()

engine = VariableElimination(traffic_model)
print("--- Evaluating 3 Network Queries ---\n")

print("Query 1: P(TrafficJam | Rain=Yes)")
q1 = engine.query(variables=['TrafficJam'], evidence={'Rain': 'Yes'})
print(q1)

print("\nQuery 2: P(Rain | LateForWork=Yes)")
q2 = engine.query(variables=['Rain'], evidence={'LateForWork': 'Yes'})
print(q2)

print("\nQuery 3: P(TrafficJam, Honking | Construction=Yes)")
q3 = engine.query(variables=['TrafficJam', 'Honking'], evidence={'Construction': 'Yes'})
print(q3)
