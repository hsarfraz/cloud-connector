# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:16:47 2020

@author: hussainsarfraz
"""
import requests #This is the module that allows you to perform API Calls
import json #This is the a module thah helps you parse data
from pandas import DataFrame #this is the module that interacts with PowerBI.
from datetime import datetime # I am importing this module since it would be used for the date conversion    
url="https://api.monday.com/v2"  #this is the base URL to perform API Calls
headers = {"Authorization": ""} #ENTER AUTHORISATION TOKEN HERE


#==========================================           
# this function gets the json data from monday.com
# The input is the specified query that I have written below. The first one gets the board names and ID's while the second one gets specific info. from each board   
#========================================== 
def web_API_call(query):
    webAPI_data_request=requests.post(url,headers=headers,params={'query' : query})
    json_board_data=json.loads(webAPI_data_request.text)
    return json_board_data

#==========================================           
# this function returns the table values and creates the seperate tables. It also appears first in the code so python can store the function in its memory
#  it uses JSON from moday.com as input parameter    
#==========================================               
def convert_json_to_dataframe_table(json_data):
    #-----------------------------------------------------------------
    # The section below would set up the first hearders of the table  
    #-----------------------------------------------------------------
    cols = [] # I have created this list to get the top heading/labels of the table
    
    for board_info in json_data['data']['boards']:  # I have specified what I want from the data

        cols.append('Board Name')  
        cols.append('Board ID') 
        cols.append('Creator Name')     
        cols.append('Creator ID') 
        cols.append('Name')     
        cols.append('state')      
    #    cols.append('owner')      
    #    cols.append('creator')   # lines 44-48 can be used outside of the for loop and these are hardcore names meaning they occur once which is why I have not put them in a for loop       
        for board_items_info in board_info['items']:  # this for loop that looks into the "items" list 
            for board_column_info in board_items_info['column_values']: # I then look into the "column_values list
                cols.append(board_column_info['title'])  # I add the different titles in the list "cols" 
            break
        break
    
    
    #-----------------------------------------------------------------
    # The section below would make the list "element" and store in all the data from the json data
    #-----------------------------------------------------------------
    
    elements = [] # A list is created to store values of the rows
    
    for board_info in json_data['data']['boards']:   
        for board_items_info in board_info['items']: # this gets in the values of all the rows and stores it in the list
            elements.append([])        
    
    #-----------------------------------------------------------------
    #   Now the section below would organize the json data into categories and append them into rows
    #-----------------------------------------------------------------
    counter = -1 # This is going to be used to get data from each row 
    
    for board_info in json_data['data']['boards']:
        for board_items_info in board_info['items']:  
            counter = counter + 1 # This is the row index that will be used to get data in the rows
            elements[counter].append(board_items_info['board']['name']) # This goes to "board" and "name" and get the value there to store in 
            elements[counter].append(board_items_info['board']['id']) 
            
            try:              #The try and exept module is here to still store in a "null" value to the rows that do not have a value stored
               elements[counter].append(board_items_info['creator']['id'])
            except TypeError:
               elements[counter].append('null')
               
            try:              
               elements[counter].append(board_items_info['creator']['name']) 
            except TypeError:
               elements[counter].append('null')
               
            elements[counter].append(board_items_info['name'])
            elements[counter].append(board_items_info['state'])
    #        elements[counter].append(g['group']['id']) 
    #        elements[counter].append(g['owner'])     
            #    elements[counter].append(f['creator'])         
            for board_column_info in board_items_info['column_values']:
#                H = h['type']
                if board_column_info['type'] == "date": # this for loop seperates the dates so the format can be changed
                        date_string = board_column_info['text'] #the variable "date_string" gets the date value
                        try:
                            date_object = datetime.strptime(date_string,'%Y-%m-%d') # the variable "date_object" transforms the date from a string to an object since python only chnages dates if they are in a dateobject format                       
                            date_conversion = date_object.strftime('%d-%m-%Y') # the variable "date_conversion" changes the format of the date to "D-M-Y" (the format was "Y-M-D" before the conversion)                           
                            elements[counter].append(date_conversion)
                            
                        except ValueError:
                            elements[counter].append('null') #some date values had no value so a value error would occur and I said if this occurs then "null" should be placed 
                        
                elif board_column_info['type'] == "board-relation":                 
                    try:              
                        tempz = board_column_info['value'] 
                        json_string_converter = json.loads(tempz) # This data is not given to us as json data, it comes as a string so I have to convert it to json format
                        
                        for connected_board_ID in json_string_converter['linkedPulseIds']:                            
                            elements[counter].append(connected_board_ID['linkedPulseId'])
#                        elements[counter].append(json_string_converter['linkedPulseIds'][0]['linkedPulseId']) # Right now I am getting the fist value from the list. If I need more values I would need to add in a for loop
                    
                    except TypeError: # Sometimes the values for linkedPulseID are not there, so I replace the blanks with null
                        elements[counter].append('null')
                  
        
                else: # if the the column type is not equal to "board-relation" then the "title" value should be stored as a column value
                    elements[counter].append(board_column_info['text'])
    
    
    return DataFrame(data=elements,columns=cols) # This uses the pandas data frame to create the table


#==========================================           
# THIS IS WHERE THE CODE STARTS  
# Thr first query is displayed below and the second one is concatenated
#==========================================            

# This query does not have hardcoded board IDs and will return all the boards (active, archived, deleted)
# It dynamically gets the board name, ID, and state that the user is given access too based on their token/ authorization code
mondaycom_board_name_query=""" 
{
  boards(state: all) {
        name
        id
        state
  }
}
"""
board_name_web_query = web_API_call(mondaycom_board_name_query) # I have called the 1st function seen in the code
counter = 0
for board_name_json in board_name_web_query['data']['boards']:  # I am specifying what I want from the data to find the board ID's and table values 
    counter = counter + 1
    table_name_in_powerBI= board_name_json['name'] # I get the board name
    table_name_in_powerBI =table_name_in_powerBI.replace("?", "")
    table_name_in_powerBI = table_name_in_powerBI + str(counter)
    
    board_id = board_name_json['id']   

    querypart1 = "{ boards(ids:"
    querypart2 = board_id
    querypart3 = """
     ) {
        items {
          board {
            name
            id
          }
          creator {
            name      
            id
          }
          name
          state
          group {
            id
          }
          column_values {
            title
            type
            text
            value
          }
        }
      }
    }
        """   
    fullquery = querypart1 + str(querypart2) + querypart3 # I have split the query and have concatenated it because the board values change and I need to change the query along with it

    webqueryjson = web_API_call(fullquery) # I am called the 2nd function seen in the code, this function creates the seperate tables and arranges their information accordingly
    
    globals()[table_name_in_powerBI] = convert_json_to_dataframe_table(webqueryjson) # The globals function allows dynamic variable names for each table in Power BI. So in each loop the board_name changes as well as the table values
    print(globals()[table_name_in_powerBI]) # Each table then get displayed and the loop runs again

