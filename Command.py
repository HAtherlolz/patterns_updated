from __future__ import annotations
from abc import ABC, abstractmethod


class CompanyAnalysis(ABC):
    @abstractmethod
    def user_poc(self) -> UserDetail:#UserDetail
        pass

    @abstractmethod
    def company_proc(self) -> CompanyDetail:#CompanyDetail
        pass


class SimpleCompanyAnalysis(CompanyAnalysis):

    def __init__(self, payload: str) -> None:
        self._payload = payload

    def execute_oper(self) -> None:
        print(f"SimpleCommand: See, I can do simple things like printing"
              f"({self._payload})")


class ComplexCompanyAnalysis(CompanyAnalysis):

    def __init__(self, choosen_oper: ChooseOperation, a: str, b: str) -> None:
        self._choosen_oper = choosen_oper
        self._a = a
        self._b = b

    def execute_oper(self) -> None:
        print("ComplexCommand: Complex stuff should be done by a receiver object", end="")
        self._choosen_oper.simple_analtsis(self._a)
        self._choosen_oper.complex_analysis(self._b)


class ChooseOperation:

    def simple_analtsis(self, a: str) -> None:
        print(f"\nReceiver: Working on ({a}.)", end="")

    def complex_analysis(self, b: str) -> None:
        print(f"\nReceiver: Also working on ({b}.)", end="")


class InvokerOperation:

    _on_start = None
    _on_finish = None

    def set_on_start(self, compamy_analysis: CompanyAnalysis):
        self._on_start = compamy_analysis

    def set_on_finish(self, command: CompanyAnalysis):
        self._on_finish = compamy_analysis

    def info_proc(self) -> None:
        print("Invoker: Does anybody want something done before I begin?")
        if isinstance(self._on_start, CompanyAnalysis):
            self._on_start.execute_oper()

        print("Invoker: ...doing something really important...")

        print("Invoker: Does anybody want something done after I finish?")
        if isinstance(self._on_finish, CompanyAnalysis):
            self._on_finish.execute_oper()


if __name__ == "__main__":
    invoker_oper = InvokerOperation()
    invoker.set_on_start(SimpleCompanyAnalysis("Say Hi!"))
    receiver = ChooseOperation()
    invoker.set_on_finish(ComplexCompanyAnalysis(
        choosen_oper, "Send email", "Save report"))

    invoker_oper.info_proc()
