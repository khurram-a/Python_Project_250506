#---------------------------------------------------
#------Name : Calculation_Functions.py
#------Created  : 05/02/2025 - Khurram Asif
#------Modified : 
#------Description : User Defined Functions Tutorial
#----------------------------------------------------


#-----Function to calcualte average---------------

def calculate_average(scores):
    return sum(scores) / len(scores)

#-----End Function to calcualte average---------------


#-----Function to assign grades based on score---------------

def assign_grade(average):
    if average >= 85:
        return 'A'
    elif average >= 75:
        return 'B'
    elif average >= 65:
        return 'C'
    elif average >= 50:
        return 'D'
    else:
        return 'F'

#-----End Function to assign grades based on score---------------