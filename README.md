# Python Connector for Monday.com and Microsoft Power BI
A python connector that enables data analysis and visualization of Monday.com board data using Microsoft Power BI. The connector transforms JSON data from Monday.com API into a format that can be consumed by Power BI and creates dynamic reports and dashboards.

## Features
- The python connector supports connecting to any Monday.com board and retrieving its data using REST web services.
- The python connector handles data transformation and conversion from JSON to tabular format, including handling changes in the source data structure (such as new columns in Monday.com boards).
- The python connector integrates with Microsoft Power BI and allows creating custom queries, metrics, and visualizations using Monday.com board data.
- The python connector provides documentation and examples on how to use the connector and create reports and dashboards in Power BI.

## Usage

Then, you need to create a config file with your Monday.com API key and the board ID that you want to connect to. You will do this by entering the authentication token which is given if you are subscribed to Monday.com services:
```
headers = {"Authorization": ""} #ENTER AUTHORISATION TOKEN HERE
````

After you run the connector the data will be parsed into a format that can be read in Microsoft Power BI. To view the data in Microsoft Power BI you would need to <a href="https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-python-scripts" target="_blank">upload the python script in Power BI</a>

## Additional Resources

SoapUI is an open source API testing tool that allows you to test REST, SOAP, GraphQL, and other web services. It helps create, manage, and execute end-to-end tests on APIs and validate their functionality, performance, and security.

soapUI helped analyze the Monday.com web services and understand the structure, parameters, and responses. soapUI was used to send requests to the Monday.com API and inspect the JSON data that was returned. Additionally, soapUI was used to test the functionality and performance of the API and check for any errors or issues.

SoapUI helped ensure that the python connector was working correctly and that it was able to consume and transform the JSON data from the Monday.com API. It also helped debug and troubleshoot any problems that occurred during the development of the connector.


