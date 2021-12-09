from typing import Iterable, List, Union, overload

from dt.dgraph.graphql.i_graphql_serializable import IGraphQLSerializable


@overload
def GraphQL(val: IGraphQLSerializable) -> str:
    '''Convert single element to GraphQL string'''


@overload
def GraphQL(val: Iterable[IGraphQLSerializable]) -> List[str]:
    '''Convert list of element to list of GraphQL strings'''


def GraphQL(val: Union[IGraphQLSerializable, Iterable[IGraphQLSerializable]]) -> Union[str, List[str]]:
    if isinstance(val, IGraphQLSerializable):
        return val.to_graphql()
    return [GraphQL(el) for el in val]
