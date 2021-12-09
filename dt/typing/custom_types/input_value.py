from typing import Union

from dt.dgraph.graphql.value import Value
from dt.dgraph.graphql.variable_reference import VariableReference

InputValue = Union[Value, VariableReference]
