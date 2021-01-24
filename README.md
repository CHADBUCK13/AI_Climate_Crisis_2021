# AI Climate Crisis 2021

##Inspiration
Honey bees play the leading role in the pollination of many wild plants and crops: a global yield of $200B of crops depend on the pollination services provided by managed bees. Meanwhile, various causes are making it more challenging to raise healthy honey bees. Climate change is pointed out as one of the causes of the colony collapse disorder. Understanding the response of bees to the new climate change scenario is essential to face this challenge, that is why we decided to create a predictive model of honey production using climate data: Coast-to-Coast Pollinator.

##What it does
This is a machine learning project that takes weather/climate and pesticide data as inputs and annual honey production per colony and annual change in colony size as output. These parameters are used to train a random forest regression algorithm to predict future honey production per bee colony and change in colony size. The granulation of the training data is monthly and is separated by US state along with latitude/longitude coordinates. This separation of parameter should allow for extrapolation to other North or South American countries without losing much accuracy. Given future climate models that include parameters such as monthly precipitation, solar radiation, temperature, relative humidity and wind this project will be able to predict honey production per colony and changes in colony size. This will be limited in terms of accuracy and distance into the future by the climate model data used.

##How we built it
This project was created using data from multiple sources including National Agricultural Statistics Service, NASA and NA-Cordex. This data was then collated using both pandas, netCDF4 and manual methods. The data was split 85/15, where 85% was used to train the model and the other 15% to test. We developed several models using Jupyter and Python, adding new predictors in each phase of development, such as latitude and longitude, and pesticide data. We started predicting only honey production and then added predicting change in colony size as well. We obtained the best results using LGBM. We then optimized the model. More specific information on the model can be found on the github linked below.

##Challenges we ran into
Finding useful data in usable format and collating the data was the most time consuming part of the project.

##What's next for BEE-HEALTHY
Correlating honey production and subsequent pollination of particular plants.
Simulating scenarios (i.e best case, worst case,..) for different regions
Getting more robust data both for training and projection including disease data. Disease data will be absolutely necessary because this is a major factor in honey production.
Apply to Canadian future climate data.
