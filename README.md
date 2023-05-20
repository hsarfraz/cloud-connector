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

-------------------------------------------------------------

Then, you need to create a config file with your Monday.com API key and the board ID that you want to connect to:

{
  "api_key": "your_api_key",
  "board_id": "your_board_id"
}
--------------------------------------------------------------

Next, you need to run the connector script with the config file as an argument:

python connector.py config.json

The connector will output a CSV file with the transformed data from the Monday.com board.
Finally, you can import the CSV file into Power BI and create your own queries, metrics, and visualizations using the board data.

