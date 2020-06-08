import json
from typing import Dict


class CompanyAnalysis():

    def __init__(self, user_detail: str) -> None:
        self._user_detail = user_detaile

    def get_info(self, company_detail: str) -> None:
        self._company_detail = company_detail
        u = json.dumps(self._user_detail)
        c = json.dumps(self._company_detail)
        print(f"Flyweight: Displaying user ({s}) and company ({u}) state.", end="")


class CompanyAnalysisFactory():

    _company_analysis: Dict[str, CompanyAnalysis] = {}

    def __init__(self, initial_company_analysis: Dict) -> None:
        for i in company_analysis:
            self._company_analysis[self.get_key(i)] = CompanyAnalysis(i)

    def get_key(self, i: Dict) -> str:
        return "_".join(sorted(i))

    def get_company_analysis(self, user_detaile: Dict) -> CompanyAnalysis:

        key = self.get_key(user_detaile)

        if not self._company_analysis.get(key):
            print("CompanyAnalysisFactory: Can't find a CompanyAnalysis, creating new one.")
            self._flyweights[key] = Flyweight(user_detaile)
        else:
            print("CompanyAnalysisFactory: Reusing existing company_analysis.")

        return self._company_analysis[key]

    def list_company_analysis(self) -> None:
        count = len(self._company_analysis)
        print(f"CompanyAnalysisFactory: I have {count} company_analysis:")
        print("\n".join(map(str, self._company_analysis.keys())), end="")


def add_info_to_database(
    factory: CompanyAnalysis, name: str, owner: str,
    brand: str, year: str, etc: str
) -> None:
    print("\n\nClient: Adding a new company info to database.")
    company_analysis = factory.get_company_analysis([brand, model, color])
    company_analysis.get_info([plates, owner])


if __name__ == "__main__":
    analysis = CompanyAnalysisFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_company_analysis()

    add_info_to_database(
        factory, "Coca", "Someone", "Drink", "1830", "redandblack")

    add_info_to_database(
        factory, "Pepsi", "Someone", "Drink", "1931", "blueandblack")

    print("\n")

    factory.list_company_analysis()
