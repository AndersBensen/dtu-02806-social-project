# INTO 

intro_markdown = '''
Every year the New York Police Department publishes data for every motor vehicle collision in New York City, and has been doing so since 2012. 
The dataset contains information about injuries and deaths caused by accidents involving cars, cycles and pedestrians in New York. The timespan 
ranges from the years 2012-2021 with 1,765,789 counts and 29 variables. This website sets out to investigate the different spatial patterns 
which is hidden behind the rather large amount of data, and more specifically it sets out to investigate how COVID-19 have affected the data. 
NYC was one of the cities which was hit very hard by COVID-19 when it first started spreading around the world in March 2020. We want to explore
and show you exactly how much this pandemic has meant for vehicle collisions in a city as busy as the Big Apple.A notebook explaining and showing 
the code behind the visualizations for this website can be found on nbviewer 
[here](https://nbviewer.jupyter.org/github/AndersBensen/python_101/blob/main/social_data_explainer_nyc_aac.ipynb). If nbviewer does not render it, it
can also be found on google drive [here](https://github.com/AndersBensen/python_101/blob/main/social_data_explainer_nyc_aac.ipynb).

To get an initial overview of the data a so-called choropleth map is used. The map shows simply how many collisions there have been in each of the 5
boroughs in New York City: 
'''

intro_post_choro = '''
It is possible to hover over the colored areas, to see the exact number of collisions. In general all plots on the websites can be hovered over, and
some things can even be toggled. 

From the plot we can see that Brooklyn has the most vehicle collisions with around ~ 383k. Queens comes after with ~ 327k, then Manhattan with ~ 285k, 
Bronx with ~176k and finally staten island with ~ 52k. Brooklyn is also the borough with the biggest population, where Staten Island has the smallest 
population of all the boroughs [[1]](https://en.wikipedia.org/wiki/Boroughs_of_New_York_City).
'''

# BASIC STATS 
bs_intro_markdown = '''
&nbsp;
&nbsp;
&nbsp;
### Initial statistics and plots 

The relative danger of collisions can be seen as the average amount of persons injured or killed per collision. The two plots below displays 
the relative danger of collisions in each of the five boroughs. This allows comparison of the relative danger of the traffic in the five boroughs:
&nbsp;
'''

bs_intro_post_markdown = '''
The left bar plot shows the amount of persons killed relative to the amount of crashes in each borough. The right bar plot shows the amount persons 
injured relative to the amount of crashes in each borough. These statistics are important, given that the plots are made relative to the amount of 
collisions in each borough making the deaths and injuries comparable across boroughs. This allows the viewer to get an idea of what the outcomes of 
an average collision in any of the five boroughs of NYC is likely to be.

As seen on the left bar plot, collisions in the Staten Island borough are more deadly than in any of the other boroughs. The collisions in Manhattan 
are also significantly less deadly than the other boroughs.

The right bar plot shows the same tendency of Manhattan having fewer persons injured per collision. This could be caused by a lower 
average speed along with higher density of vehicles in Manhattan which would further limit the possibility of speeding. These factors are known to 
lower deaths in traffic collisions, as illustrated by the National Safety Council: *Speeding was a factor in 26% of all traffic fatalities in 2019*.
[[2]](https://injuryfacts.nsc.org/motor-vehicle/motor-vehicle-safety-issues/speeding/) 


The following bar plots illustrates the amount of injuries sustained per collision in each borough in three categories; Cyclist, Pedestrian and 
Motorist. The Person category above is a combination of these three categories:
'''

bs_months_pre_markdown = '''
The plots show key differences in how the different modes of transport play into danger levels in the five boroughs. In the Manhattan borough, you are 
much more likely to be injured in a collision as a pedestrian or cyclist compared to a motorist. This is likely due to a high amount of collisions 
involving pedestrians and cyclists compared to other boroughs. In the Staten Island borough motorists are more likely to be injured in a collision than 
cyclists and pedestrians. This does not mean, that cyclists and pedestrians are not injured when involved in collisions but is likely to be due to a 
higher amount of collisions only involving motorists.

To see whether there is a difference in when the collisions happen throughout the year we plot the amount of collisions each month:
'''

bs_months_post_markdown = '''
The months are generally quite even in the amount of collisions. It is however clear that a few months, namely April and February are underrepresented comparetively. 
It also seems that more crashes happen in the second half of the year. The months from January to June all have fewer collisions than the months from July to December.

Collision patterns could also be hidden in the hours during the week. To investigate this we plot the hours of the week with the amount of collisions there is each hour: 
'''

bs_hours_weekly_markdown = '''
The collisions show a clear spike between 8AM and 6PM, especially on weekdays which makes sense given that most people drive during those hours to and from work as well as 
driving during work. There is a large spike present around 4-5AM on weekdays and especially on Fridays. This makes sense given that many people are driving home from work 
during those hours, leading to more traffic as well as tired motorists who just finished a days work. The collisions are at a low point in the hours around 1-5AM which is 
likely due to many people sleeping during those hours (even in the city that never sleeps) and therefore a decreased traffic load.

In general we can see that there are several patterns from our different plots, both temporal and geospatial. 
'''

# COVID-19 ANALYSIS 

cv_pre_markdown = '''
&nbsp;
&nbsp;
### COVID-19 and vehicle colissions
yesfuuf

'''

# MACHINE LEARNING 

ml_intro_markdown = '''
&nbsp;
&nbsp;
### Using Machine Learning to predict collisions  

As it can be seen from the prior analysis there definetely is temporal and geospatial patterns regarding collisions and injuries. 
We could also see from the COVID-19 investigation, that COVID-19 definetely had an impact on the amount collisions and related fatalities in NYC. 
To further investigate these patterns, we will use a Machine Learning model to see if we can predict how many collisions there is on a given day. 
Afterward we will try to add COVID-19 data in NYC from the same dates, to see if that can improve the performance of our model. 
The data we are prediction upon is restriced to 2020, so we later can predict on the same data when merging with the COVID-19 dataset. 

When doing Machine Learning we need to define what our input data is (called features). Features are what we want to predict based on, and choosing these 
are very important for how well your model performs. To be able to predict how many collisions there are on a given day we will use the following features: 
**persons injured**, **cyclists injured**, **motorists injured**, **day** and **month**. These features both give us an in insight into how many were 
injured but also the time aspect of the data. As what we want to predict is an continuous variable, we will use a linear regression model. 
A specific part of the data is choosen to test the model and see how well it performs, and the result can be seen in below figure: 
'''

ml_markdown_1 = '''
Along the x-axis we see the dates from march to november in 2020, and along the y-axis we see the amount of collisions there were on that given date. 
The blue points marks the actual amount of collisions, and the red points marks the amount of collisions our model predicted. To be able to evaluate
how good our predictions are we use a measure called **Root Mean Square Error (RMSE)**. **RMSE** is a value which describes how close the predictions
are to the actual data, where a very large value of **RMSE** means the predictions were not very good, and a small value means they were quite accurate. 
A value of 40.5 may not be insanely good, but it does not look too bad when looking at the figure. 

What is really interesting about the value is whether it improves or not when we train a new machine learning model based on the same features, but also
with the COVID-19 dataset added. So besides the amount of persons etc. were injured on a given day, we also see how many tested positive for COVID-19 that day, 
and in specific boroughs. The same specific part of the data from the last model was chosen to test the new model, the resulting figure can be seen below: 
'''

ml_markdown_2 = '''
So this time the **RMSE** was only 34.95, meaning that it did indeed improve by having more data to find patterns in. As mentioned both of the models
were evaluated on the same specific test data. To ensure that it was not just this specific data that caused the improvement a more technical approach
called 10-fold cross-validation (CV) is used. In 10-fold CV the models are trained on several parts of the data, and an average is computed in the end,
ensuring that both models are trained and tested on several parts of the data. By doing this the first model got an average value of **RMSE=42.8**, 
where the second model got an average value of **RMSE=40.5**. It can indeed be concluded by this that the model which also used the COVID-19 dataset
performs better. 

We can conclude that adding the COVID-19 dataset did indeed help in predicting the amount of collisions. It makes good sense that it improved our **RMSE** 
value (by reducing it) as we could see that COVID-19 had quite a big impact of the amount of vehicle collisions in NYC, and thus made our predictions 
more precise by adding the data.  
'''

# HEATMAP 
heatmap_pre_markdown = '''
&nbsp;
&nbsp;
### Interactive exploration 

By now you should have an idea of how vehicle collisions in NYC have patterns hidden in it and how it is possible to use these patterns for several things, 
such as observing when coronavirus hit the hardest and Machine Learning. Below is an interactive heatmap, which lets you explore the data itself. You can choose 
which years you want to see data from, but also which kind of data. The data is by default the total amount of collisions, but can be changed to see numbers of 
persons injured etc. The radius of each point can also be increased: 
'''

heatmap_post_markdown = '''
&nbsp;
&nbsp;
### Final words

It can be concluded that coronavirus did indeed have a huge impact on vehicle collisions in New York City. By 
'''