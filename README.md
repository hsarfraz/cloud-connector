# Python Connector for Monday.com and Microsoft Power BI
A python connector that enables data analysis and visualization of Monday.com board data using Microsoft Power BI. The connector transforms JSON data from Monday.com API into a format that can be consumed by Power BI and creates dynamic reports and dashboards.

## Features
- The python connector supports connecting to any Monday.com board and retrieving its data using REST web services.
- The python connector handles data transformation and conversion from JSON to tabular format, including handling changes in the source data structure (such as new columns in Monday.com boards).
- The python connector integrates with Microsoft Power BI and allows creating custom queries, metrics, and visualizations using Monday.com board data.
- The python connector provides documentation and examples on how to use the connector and create reports and dashboards in Power BI.

## Usage
To use the python connector, you need to install the required dependencies:

```bash
pip install -r requirements.txt
````

Then, you need to create a config file with your Monday.com API key and the board ID that you want to connect to:

```
{
  "api_key": "your_api_key",
  "board_id": "your_board_id"
}
````

Next, you need to run the connector script with the config file as an argument:

```
python connector.py config.json
````

The connector will output a CSV file with the transformed data from the Monday.com board.
Finally, you can import the CSV file into Power BI and create your own queries, metrics, and visualizations using the board data.

## Additional Resources

SoapUI is an open source API testing tool that allows you to test REST, SOAP, GraphQL, and other web services. It helps you to create, manage, and execute end-to-end tests on APIs and validate their functionality, performance, and security.

In this project, soapUI helped me to analyze the Monday.com web services and understand their structure, parameters, and responses. I used soapUI to send requests to the Monday.com API and inspect the JSON data that was returned. I also used soapUI to test the functionality and performance of the API and check for any errors or issues.

SoapUI helped me to ensure that the python connector was working correctly and that it was able to consume and transform the JSON data from the Monday.com API. It also helped me to debug and troubleshoot any problems that occurred during the development of the connector.


