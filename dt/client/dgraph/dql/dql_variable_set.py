from typing import Dict, Optional

from dt.client.dgraph.graphql.variable_set import VariableSet


class DQLVariableSet(VariableSet):
    def get_value_dict(self) -> Dict[str, Optional[str]]:
        value_dict = {}
        for variable in self.items:
            ref_str = variable.get_reference().to_graphql()
            value = None
            if variable.value is not None:
                value = variable.value.to_graphql()
            elif variable.default_value is not None:
                value = variable.default_value.to_graphql()
            value_dict[ref_str] = value
        return value_dict
