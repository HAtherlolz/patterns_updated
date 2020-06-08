from __future__ import annotations
from abc import ABC, abstractmethod


class CompanyAnalysis(ABC):#CompanyAnalysis
    @abstractmethod
    def user_poc(self) -> UserDetail:#UserDetail
        pass

    @abstractmethod
    def company_proc(self) -> CompanyDetail:#CompanyDetail
        pass


class ConcreteProcessing1(CompanyAnalysis):

    def search_user_info(self) -> ConcreteUserInfo:#ConcreteUserInfo
        return ConcreteUserInfo()#ConcreteUserInfo

    def search_company_info(self) -> ConcreteCompanyInfo:#ConcreteCompanyInfo
        return ConcreteCompanyInfo()#ConcreteCompanyInfo


class ConcreteProcessing2(CompanyAnalysis):

    def search_same_user_info(self) -> ConcreteSameUserInfo:#ConcreteSameUserInfo
        return ConcreteSameUserInfo()#ConcreteSameUserInfo

    def search_competitor_company_info(self) -> ConcreteCompetitorCompanyInfo:#ConcreteCompetitorCompanyInfo
        return ConcreteCompetitorCompanyInfo()#ConcreteCompetitorCompanyInfo


class UserComparator(ABC, ConcreteProcessing1, ConcreteProcessing2):

    @abstractmethod
    def difference_info(self) -> str:
        pass

    @abstractmethod
    def same_info(self) -> str:
        pass


class CompareDiffUserInfo(UserComparator):#CompareDiffUserInfo
    def difference_info(self) -> str:
        return "The compare result of the ConcreteUserInfo and ConcreteSameUserInfo is them difference inf."


class CompareSameUserInfo(UserComparator):#CompareSameUserInfo
    def same_info(self) -> str:
        return "The compare result of the ConcreteUserInfo and ConcreteSameUserInfo is them same inf.""


class CompanyComparator(ABC, ConcreteProcessing1, ConcreteProcessing2):

    @abstractmethod
    def difference_info(self) -> str:
        pass

    @abstractmethod
    def same_info(self) -> str:
        pass


class CompareDiffCompanyInfo(CompanyComparator):
    def difference_info(self) -> str:
        return "The compare result of the ConcreteCompanyInfo and ConcreteCompetitorCompanyInfo is them difference inf."



class CompareSameCompanyInfo(CompanyComparator):
    def same_info(self) -> str:
        return "The compare result of the ConcreteCompanyInfo and ConcreteCompetitorCompanyInfo is them same inf."



def client_code(analysis: CompanyAnalysis) -> None:
    user = analysis.search_user_info()
    company = analysis.search_company_info()
    same_user = analysis.search_same_user_info()
    same_company = analysis.search_competitor_company_info()



if __name__ == "__main__":
    print("Client: Testing client code with the first analysis type:")
    client_code(ConcreteProcessing1())

    print("\n")

    print("Client: Testing the same client code with the second analysis type:")
    client_code(ConcreteProcessing2())
