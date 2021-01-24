# AI Climate Crisis 2021

This is a machine learning project that takes weather/climate and pesiticide data as inputs and honey production per colony as output. These parameters are used to train a random 
forest regression algorithm to predict future honey production per bee colony. The granulation of the training data is monthly and is separated by US state along with 
latitude/longitude coordinates. This separation of paramater should allow for extrapolation to other North or South American countries without losing much accuracy.
Given future climate models that include parameters such as monthly precipitation, solar radiation, temperature, relative humidity and wind this project will be able to predict 
honey production per colony. This will be limited in terms of accuracy and distance in to the future by the climate model data fed.

This project was created using data from multiple sources including-------------ADD SOURCES-----------------. This data was then collated using both pandas, netCDF4 and manual 
methods. The data was split 85/15, where 85% was used to train the model and the other 15% to test.
