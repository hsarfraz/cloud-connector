# Python Connector for Monday.com and Microsoft Power BI

The goal of this project is to enable data analysis and visualization of Monday.com board data using Microsoft Power BI. Monday.com is a cloud-based work operating system that allows teams to manage projects, workflows, and goals. Microsoft Power BI is a business analytics service that provides interactive visualizations and business intelligence capabilities. 

The project consists of a python connector that transforms JSON data from the Monday.com API into a format that can be consumed by Power BI. The connector supports connecting to any Monday.com board and retrieving its data using REST web services. The connector handles data transformation and conversion from JSON to tabular format, including handling changes in the source data structure (such as new columns in Monday.com boards). The connector integrates with Microsoft Power BI and allows creating custom queries, metrics, and visualizations using Monday.com board data.

## Features

- The python connector supports connecting to any Monday.com board and retrieving its data using REST web services.
- The python connector handles data transformation and conversion from JSON to tabular format, including handling changes in the source data structure (such as new columns in Monday.com boards).
- The python connector integrates with Microsoft Power BI and allows creating custom queries, metrics, and visualizations using Monday.com board data.
- The python connector provides documentation and examples on how to use the connector and create reports and dashboards in Power BI.

## Usage

To use the python connector, you need to create a config file with your Monday.com API key and the board ID that you want to connect to. You will do this by entering the authentication token which is given if you are subscribed to Monday.com services:
```
headers = {"Authorization": ""} #ENTER AUTHORISATION TOKEN HERE
````


After you run the connector, the data will be parsed into a format that can be read in Microsoft Power BI. To view the data in Microsoft Power BI, you need to <a href="https://learn.microsoft.com/en-us/power-bi/connect-data/desktop-python-scripts" target="_blank">upload the python script in Power BI</a>.

## Examples

Here are some examples of the reports and dashboards that I created using the python connector and Power BI:

[Insert screenshots or images of your reports and dashboards here]

## Additional Resources

To learn more about the topics related to this project, you can check out the following sources:

- [Monday.com API Documentation](https://monday.com/developers/v2)
- [Microsoft Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)
- [soapUI Documentation](https://www.soapui.org/docs/)
- [Python Documentation](https://docs.python.org/3/)

### Additional Info. about soapUI

SoapUI is an open source API testing tool that allows you to test REST, SOAP, GraphQL, and other web services. It helps you to create, manage, and execute end-to-end tests on APIs and validate their functionality, performance, and security.

In this project, soapUI helped me to analyze the Monday.com web services and understand their structure, parameters, and responses. I used soapUI to send requests to the Monday.com API and inspect the JSON data that was returned. I also used soapUI to test the functionality and performance of the API and check for any errors or issues.

SoapUI helped me to ensure that the python connector was working correctly and that it was able to consume and transform the JSON data from the Monday.com API. It also helped me to debug and troubleshoot any problems that occurred during the development of the connector.


