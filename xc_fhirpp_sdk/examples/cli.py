import inquirer
import json
import yaml

from pygments import highlight, lexers, formatters
from xc_fhirpp_sdk.xc_fhirpp_client import XCFHIRPPClient

class FHIRPlusPlusCLI:
    def __init__(self):
        self.client = XCFHIRPPClient()

    def enter_patient_name(self):
        question = [
            inquirer.Text(
                "name",
                message="Enter Patient Name",
                default="John Garcia"
            )
        ]

        return inquirer.prompt(question)["name"]
        
    def select_patients(self):
        name = self.enter_patient_name()
        patients = self.client.get_patients(name)

        choices = [
            (f'{patient["resource"]["name"][0]["text"]} ({patient["resource"]["id"]})', patient["resource"])
            for patient in patients]

        # Add an option to go back
        choices.append(("..", ".."))

        question = [
            inquirer.List(
                "patient",
                message="Select a patient",
                choices=choices
            )
        ]
        choice = inquirer.prompt(question)["patient"]
        if choice == "..":
            self.select_patients()
        self.select_patient_data(choice)

    def select_patient_data(self, patient_data):
        question = [
            inquirer.List(
                "data_type",
                message="Select data type",
                choices=["Demographics", "Allergies", "Encounters", ".."],
            ),
        ]

        data_type = inquirer.prompt(question)["data_type"]

        data = {}
        if data_type == "Demographics":
            data.update({"name": patient_data.get("name", "")})
            data.update({"birthDate": patient_data.get("birthDate", "")})
            data.update({"maritalStatus": patient_data.get("maritalStatus", "")})
            data.update({"identifier": patient_data.get("identifier", "")})
            data.update({"telecom": patient_data.get("telecom", "")})
            data.update({"identifier": patient_data.get("identifier", "")})
            data.update({"contained": patient_data.get("contained", "")})
            demographics = {data_type: data}
            self.colorful_print_yaml(demographics)
        elif data_type == "Allergies":
            allergies_data = self.client.get_allergy_intolerances(patient_data["id"])
            allergies = []
            for resource in allergies_data:
                data = {}
                allergy = resource["resource"]

                data.update({"id": allergy.get("id", "")})
                data.update({"coding": allergy.get("code", {}).get("coding", "")})
                data.update({"category": allergy.get("category", "")})
                data.update({"criticality": allergy.get("criticality", "")})
                data.update({"onsetDateTime": allergy.get("onsetDateTime", "")})
                data.update({"reaction": allergy.get("reaction", "")})
                allergies.append(data)
            self.colorful_print_yaml({data_type: allergies})
        elif data_type == "Encounters":
            encounters_data = self.client.get_encounters(patient_data["id"])
            encounters = []
            for resource in encounters_data:
                data = {}
                encounter = resource["resource"]

                data.update({"status": encounter.get("status", "")})
                data.update({"type": encounter.get("type", "")})
                data.update({"participant": encounter.get("participant", "")})
                data.update({"appointment": encounter.get("appointment", "")})
                data.update({"period": encounter.get("period", "")})
                data.update({"location": encounter.get("location", "")})
                data.update({"contained": encounter.get("contained", "")})

                encounters.append(data)
            self.colorful_print_yaml({data_type: encounters})
        elif data_type == "..":
            self.select_patients()

        question = [
            inquirer.List(
                "start_over",
                message="Start over?",
                choices=["Yes", "No"],
            ),
        ]

        if inquirer.prompt(question)["start_over"] == "Yes":
            self.select_patients()
        exit(0)



    @staticmethod
    def colorful_print_yaml(data):
        formatted_yaml = yaml.dump(json.loads(json.dumps(data)), indent=1)
        colorful_json = highlight(formatted_yaml, lexers.YamlLexer(), formatters.TerminalFormatter())
        print(colorful_json)

def cli():
    _cli = FHIRPlusPlusCLI()
    _cli.select_patients()

if __name__ == '__main__':
    cli()