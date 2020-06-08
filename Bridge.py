from __future__ import annotations
from abc import ABC, abstractmethod


class CompanyAnalysis:

    def __init__(self, info_processing: InfoProcessing) -> None:
        self.info_processing = info_processing

    def searcher(self) -> str:
        return (f"Abstraction: Base operation with:\n"
                f"{self.info_processing.searcher_info_processing()}")


class ExtendedCompanyAnalysis(CompanyAnalysis):

    def searcher(self) -> str:
        return (f"ExtendedAbstraction: Extended operation with:\n"
                f"{self.info_processing.searcher_info_processing()}")


class InfoProcessing(ABC):

    @abstractmethod
    def proc_company_info(self) -> str:
        pass


class ProcessingCompanyInfo(InfoProcessing):
    def searcher_info_processing(self) -> str:
        return "ConcreteImplementationA: Here's the result on the platform A."


class ProcessingCompetitorCompanyInfo(InfoProcessing):
    def searcher_info_processing(self) -> str:
        return "ConcreteImplementationB: Here's the result on the platform B."


def client_code(analysis: CompanyAnalysis) -> None:
    print(analysis.searcher(), end="")



if __name__ == "__main__":
    info_processing = ProcessingCompanyInfo()
    analysis = CompanyAnalysis(info_processing)
    client_code(analysis)

    print("\n")

    info_processing = ProcessingCompetitorCompanyInfo()
    analysis = ExtendedCompanyAnalysis(info_processing)
    client_code(analysis)
