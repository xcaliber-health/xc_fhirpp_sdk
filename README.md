### Description
A wrapper for XCaliber Health\'s FHIR++ APIs.

### Installation
1. Clone this repository
2. Create a project for your application **skip if you already have one*
   - (Optional) Create a virtual environment  `python3 -m venv .venv`
   - (Optional) If you created a virtual environment activate it `source .venv/bin/activate`
3. Install the XC FHIR++ SDK `pip install <path>` **Replace <path> with the location XC FHIR++ SDK was cloned.*
4. Set client configurations in environment variables. Theses can be set in you IDE or the terminal.

    Example terminal setup:
    ```shell
    % export BEARER TOKEN <token>
    % export PEARL_SOURCE_ID=<source_id
    % export ATHENA_SOURCE_ID=<source_id
    ```
   
    Example PyCharm setup:

    ![PyCharm environment variable setup](/assets/images/pycharm_env_variables.png)
    
   
5. Now import the client in your project
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

