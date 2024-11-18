#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  7 11:49:58 2024

@author: agn
"""

from datetime import datetime

def save_log_to_txt(listsBuy,value, price,  filename):
    today = datetime.today().strftime('%Y-%m-%d') 
    
    filename= filename + "_" + today + "_.txt"
    """
    Save a list of dictionaries into a CSV file.
    Each dictionary has 'value' and 'price'.
    """

    listsBuy.append({"value": value, "price": price})
    
    with open(filename, mode='w') as file:
        # Write a header line
        file.write("Value (P)  | Price (P)\n")
        file.write("+------------+------------+\n")
        
        # Write each entry in the log list
        for entry in listsBuy:
                #print("Liste Log", entry)
                value = entry.get('value', 'N/A')
                price = entry.get('price', 'N/A')
                #
                file.write(f"| {value} | {price:<10} |\n | ")
            
        file.write("+------------+------------+\n")
    
    print(f"Log has been saved to {filename}")
