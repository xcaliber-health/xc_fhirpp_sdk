import os
import warnings

from fhirpy import SyncFHIRClient

warnings.filterwarnings('ignore')


class XCFHIRPPClient:
    """A thin wrapper over FHIR++ APIs that allows the user to retrieve a patient document list and documents.
    Reference: https://xc-dev-docs.xcaliberapis.com/en/api/interop
    """

    def __init__(self):
        self.patient_id = None
        self.source_id = None
        self.patients = None
        self._client = None


    def _new_client(self, source_id, params=None):
        self.source_id = source_id

        self._client = SyncFHIRClient(
            "https://xchange-sandbox.xcaliberapis.com/api/v1/",
            authorization=f"Bearer {os.environ['BEARER_TOKEN']}",
            requests_config={
                "verify": False,
                "params": params
            },
            extra_headers={
                # Pearl
                "X-Source-Id": f"{self.source_id}",
                "Accept": "application/fhir+json",
                "Content-Type": "application/fhir+json",
            }
        )

    def get_patients(self, name):
        # Pearl source
        self._new_client(os.environ['PEARL_SOURCE_ID'])

        resources = self._client.resources("Patient")
        resources = resources.search(name=name)
        self.patients = resources.fetch_raw()["data"]["entry"]
        return self.patients

    def get_allergy_intolerances(self, patient_id):
        self.patient_id = patient_id
        params = {
            "patient": self.patient_id,
            "departmentId": "1"
        }

        # Athena source
        self._new_client(os.environ['PEARL_SOURCE_ID'], params=params)
        resources = self._client.resources("AllergyIntolerance")
        return resources.fetch_raw()["data"]["entry"]

    def get_encounters(self, patient_id):
        self.patient_id = patient_id
        params = {
            "patient": self.patient_id,
            "departmentId": "1"
        }

        # Pearl source
        self._new_client(os.environ['ATHENA_SOURCE_ID'], params=params)
        resources = self._client.resources("Encounter")
        return resources.fetch_raw()["data"]["entry"]

if __name__ == "__main__":

    client = XCFHIRPPClient()
    print(client.get_allergy_intolerances("29197"))
