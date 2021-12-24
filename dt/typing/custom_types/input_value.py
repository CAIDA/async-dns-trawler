from typing import Union

from dt.client.dgraph.graphql.value import Value
from dt.client.dgraph.graphql.variable_reference import VariableReference

InputValue = Union[Value, VariableReference]
