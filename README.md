# Python Connector for Monday.com and Microsoft Power BI

This project aims to enable data analysis and visualization of Monday.com board data using Microsoft Power BI. Monday.com is a cloud-based work operating system that allows teams to manage projects, workflows, and goals. Microsoft Power BI is a business analytics service that provides interactive visualizations and business intelligence capabilities. I chose to use these two platforms as my data sources and tools because I wanted to explore how to extract, transform, and analyze data from a web service using python, and how to create dynamic and interactive reports and dashboards using Power BI.

To achieve this goal, I built a python connector that transforms JSON data from the Monday.com API into a format that can be consumed by Power BI. The connector supports connecting to any Monday.com board and retrieving its data using REST web services. The connector handles data transformation and conversion from JSON to tabular format, including handling changes in the source data structure (such as new columns in Monday.com boards). The connector integrates with Microsoft Power BI and allows creating custom queries, metrics, and visualizations using Monday.com board data.

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
```



