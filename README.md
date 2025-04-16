### Description
A thin wrapper for XCaliber Health\'s FHIR++ APIs

### Installation
1. Clone this repository
2. Create a project for your application **skip if you already have one*
   - (Optional) Create a virtual environment  `python3 -m venv .venv`
3. Install the XC FHIR++ SDK `pip install <your_path>` **Replace <your_path> with location XC FHIR++ SDK was cloned.*
4. Now import the client in your project
    ```python
    from xc_fhirpp_sdk.xc_fhirpp_client import XCFHIRPPClient
    ```
    To instantiate the client...
   ```python
    if __name__ == '__main__':
        c = XCFHIRPPClient()
   ```

   There is also an example cli that uses the client

    ```python
    from xc_fhirpp_sdk.examples.cli import cli
    ```

    To run the CLI...
   ```python
    if __name__ == '__main__':
        cli()
   ```
