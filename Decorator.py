from __future__ import annotations
from abc import ABC, abstractmethod


class ComponentCompanyAnalysis():

    def get_user_info(self) -> str:
        pass

    def get_company_info(self) -> str:
        pass


class ConcreteComponentAnalysis(ComponentCompanyAnalysis):

    def get_same_user_info(self) -> str:
        return "ConcreteInfo"

    def get_same_company_info(self) -> str:
        return "ConcreteInfo"


class Decorator(ComponentCompanyAnalysis):

    _component_comp_analysis: ComponentCompanyAnalysis = None

    def __init__(self, component_comp_analysis: ComponentCompanyAnalysis) -> None:
        self._component_comp_analysis = component_comp_analysis

    @property
    def component_comp_analysis(self) -> str:
        return self._component_comp_analysis

    def comparator(self) -> str:
        return self._component_comp_analysis.operation()


class UserDetailCompare(Decorator):

    def info_taker(self) -> str:
        return f"UserDetailCompare({self._component_comp_analysis.comparator()})"


class CompanyDetailCompare(Decorator):

    def info_taker(self) -> str:
        return f"CompanyDetailCompare({self._component_comp_analysis.comparator()})"


def client_code(component_comp_analysis: ComponentCompanyAnalysis) -> None:
    print(f"RESULT: {component_comp_analysis.comparator()}", end="")


if __name__ == "__main__":
    # This way the client code can support both simple components...
    simple = ConcreteComponentAnalysis()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")

    # ...as well as decorated ones.
    #
    # Note how decorators can wrap not only simple components but the other
    # decorators as well.
    user_detail = UserDetailCompare(simple)
    company_detail = CompanyDetailCompare(simple)
    print("Client: Now I've got a decorated component:")
    client_code(simple)
