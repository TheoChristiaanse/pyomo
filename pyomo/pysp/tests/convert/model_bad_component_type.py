#
# a model that declares the wrong component type
# within an annotation
#
from pyomo.pysp.tests.convert.utils import *

pysp_scenario_tree_model_callback = \
    simple_twostage_scenario_tree

def pysp_instance_creation_callback(scenario_name, node_names):
    model = simple_twostage_model()
    assert model.find_component("b") is None
    model.b = Block()
    model.b.c = Constraint(expr=model.y == 1)
    model.smat = StochasticConstraintBodyAnnotation()
    model.smat.declare(model.o)
    return model
