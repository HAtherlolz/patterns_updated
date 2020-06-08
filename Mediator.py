from __future__ import annotations
from abc import ABC


class CompanyAnalysis(ABC):

    def info_taker(self, sender: object, event: str) -> None:
        pass


class ConcreteInfo(CompanyAnalysis):
    def __init__(self, user_info: UserInfo, company_info: CompanyInfo) -> None:
        self._user_info = user_info
        self._user_info.mediator = self
        self._company_info = company_info
        self._company_info.mediator = self

    def comparator(self, sender: object, event: str) -> None:
        if event == "A":
            print("Mediator reacts on A and triggers following operations:")
            self._company_info.do_c()
        elif event == "D":
            print("Mediator reacts on D and triggers following operations:")
            self._user_info.do_b()
            self._company_info.do_c()


class BaseCompanyInfoAnalysis:

    def __init__(self, company_analysis: CompanyAnalysis = None) -> None:
        self._company_analysis = company_analysis

    @property
    def company_analysis(self) -> CompanyAnalysis:
        return self._company_analysis

    @mediator.setter
    def company_analysis(self, company_analysis: CompanyAnalysis:) -> None:
        self._company_analysis = company_analysis


class CompareUserInfo(BaseCompanyInfoAnalysis):
    def do_a(self) -> None:
        print("Component 1 does A.")
        self.company_analysis.info_taker(self, "A")

    def do_b(self) -> None:
        print("Component 1 does B.")
        self.company_analysis.info_taker(self, "B")


class CompareCompanyInfo(BaseCompanyInfoAnalysis):
    def do_c(self) -> None:
        print("Component 2 does C.")
        self.company_analysis.info_taker(self, "C")

    def do_d(self) -> None:
        print("Component 2 does D.")
        self.company_analysis.info_taker(self, "D")


if __name__ == "__main__":
    c1 = CompareUserInfo()
    c2 = CompareCompanyInfo()
    company_analysis = ConcreteInfo(c1, c2)

    print("Client triggers operation A.")
    c1.do_a()

    print("\n", end="")

    print("Client triggers operation D.")
    c2.do_d()
