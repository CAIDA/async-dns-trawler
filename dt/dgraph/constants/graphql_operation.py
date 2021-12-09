from enum import Enum


class GraphQLOperation(Enum):
    QUERY = "query"
    SUBSCRIPTION = "subscription"
    MUTATION = "mutation"
