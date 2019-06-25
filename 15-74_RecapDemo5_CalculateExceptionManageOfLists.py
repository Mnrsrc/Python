# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 20:40:01 2019

@author: Munire
"""
import sys
mylist=["Monica",4,74,0,0.254,"7"]
for i in mylist:
    try:
        print("Number: " + str(i))
        result=1/float(i)
        print("Result: " + str(result))
        print("*****")
    except ZeroDivisionError:
        print("Denominator cannot be zero!!!")
        print("Error Cause: " + str(sys.exc_info()[0]))
        print("*****")
    except ValueError:
        print("Denominator cannot be string value!!!")
        print("Error Cause: " + str(sys.exc_info()[0]))
        print("*****")
    except:
        print("Something went error!!!")
        print("Error Cause: " + str(sys.exc_info()[0]))
        print("*****")
    finally:
        print("Processes finished.")