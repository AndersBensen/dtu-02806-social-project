# INTO 

intro_markdown = '''
Every year the New York Police Department publishes data for every motor vehicle collision in New York City, and has been doing so since 2012. 
The dataset contains information about injuries and deaths caused by accidents involving cars, cycles and pedestrians in New York City (NYC). The timespan 
ranges between the years 2012-2021 with 1,765,789 counts and 29 variables. This website sets out to investigate the different patterns which is hidden 
behind the rather large amount of data, and more specifically it sets out to investigate how COVID-19 has affected the data. NYC was one of the cities 
which was hit very hard by COVID-19 when it first started spreading around the world in March 2020. We want to explore and show you exactly how much this 
pandemic has meant for vehicle collisions in a city as busy as the Big Apple. A notebook explaining and showing the code and ideas behind the visualizations for 
this website can be found on deepnote [here](https://deepnote.com/project/Social-final-project-3g9PpVG0SxGUOlX_mQSFdg/%2Fsocial_data_explainer.ipynb). 
If deepnote does not render it, it can also be found on nbviewer [here](https://nbviewer.jupyter.org/github/AndersBensen/python_101/blob/main/social_data_explainer_nyc_aac.ipynb).

To get an initial overview of the data a so-called choropleth map is used. The map shows simply how many collisions there have been in each of the 5
boroughs in New York City: 
'''

intro_post_choro = '''
It is possible to hover over the colored areas, to see the exact number of collisions. In general all plots on the websites can be hovered over, and
some things can even be toggled. 

From the plot we can see that Brooklyn has the most vehicle collisions with around ~383k. Queens comes in second with ~327k, then Manhattan with ~285k, 
Bronx with ~176k and finally Staten Island with ~52k. Brooklyn is also the borough with the largest population, whereas Staten Island has the smallest 
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
collisions in each borough making the deaths and injuries comparable across boroughs. This allows the viewer to get an idea of what the outcome of 
an average collision in any of the five boroughs of NYC is likely to be.

As seen on the left bar plot, collisions in the Staten Island borough are more deadly than in any of the other boroughs. The collisions in Manhattan 
are also significantly less deadly than in the other boroughs.

The right bar plot shows the same tendency of Manhattan having fewer persons injured per collision. This could be caused by a lower 
average speed along with higher density of vehicles in Manhattan which would further limit the possibility of speeding. These factors are known to 
lower deaths in traffic collisions, as illustrated by the National Safety Council: *Speeding was a factor in 26% of all traffic fatalities in 2019*.
[[2]](https://injuryfacts.nsc.org/motor-vehicle/motor-vehicle-safety-issues/speeding/) 


The following bar plots illustrate the amount of injuries sustained per collision in each borough in three categories; Cyclist, Pedestrian and 
Motorist. The Person category above is a combination of those three categories:
'''

bs_months_pre_markdown = '''
The plots show key differences in how the different modes of transport play into danger levels of collisions in the five boroughs. In the Manhattan borough, you are 
much less likely to be injured in a collision as a motorist compared to the other boroughs.  In the Staten Island borough motorists are more likely to be 
injured in a collision than cyclists and pedestrians. This does not mean, that cyclists and pedestrians are not injured when involved in collisions but is 
likely to be due to a higher amount of collisions involving only motorists.

To see whether there is a difference in when the collisions happen throughout the year we plot the amount of collisions each month:
'''

bs_months_post_markdown = '''
The months are generally quite even in the amount of collisions. It is however clear that a few months, namely April and February are underrepresented comparatively. 
It also seems that more crashes happen in the second half of the year. The months from January to June all have fewer collisions than the months from July to December.

Collision patterns could also be hidden in the hours during the week. To investigate this we plot the hours of the week with the amount of collisions each hour: 
'''

bs_hours_weekly_markdown = '''
The collisions show a clear spike between 8AM and 6PM, especially on weekdays which makes sense given that most people drive during those hours to and from work as well as 
driving during work. There is a large spike present around 4-5PM on weekdays and especially on Fridays. This makes sense given that many people are driving home from work 
during those hours, leading to more traffic as well as tired motorists who just finished a days work. The collisions are at a low point in the hours around 1-5AM which is 
likely due to many people sleeping during those hours (even in the city that never sleeps) and therefore a decreased traffic load.

In general we can see that there are several patterns from our different plots, both temporal and geospatial. 
'''

# COVID-19 ANALYSIS 

cov_intro_markdown = '''
&nbsp;
&nbsp;
### COVID-19 and vehicle colissions
The first confirmed case of COVID-19 in New York City was found on the 1st of March in 2020. A 39 year old woman contracted the virus while traveling 
abroad in Iran [[3]](https://www.nbcnewyork.com/news/coronavirus/person-in-nyc-tests-positive-for-covid-19-officials/2308155/). Therefore, we are dividing 
the data into two sets by this date and will refer to them from now on as 'NO COVID' and 'COVID'. Below you can see the evolution of the confirmed COVID-19 cases 
in NYC plotted versus dates in 2020 starting with the 1st of March and ending at the 3rd of December. 
'''

cov_post_intro_markdown = '''
So from the data we can see that the pandemic started in march, and then grows extremely fast and peaks at around 6000 cases in April. Then it slows down and rises again 
in October. Sidenote: A clear weekly pattern can be observed in the case count, however, this is not subject of investigation.

To see if (and if, then how big) a impact COVID had on the amount of daily vehicle collisions, we plot the collisions each day from 2012 to 2021: 
'''

cov_incidents_post_markdown = ''' 
The above plot shows how COVID-19 has affected the number of collisions in NYC. Along the x-axis we have the dates from 2012 to 2021, where from 2012 to March 2020 is marked in 
green for pre-covid and from March 2020 to March 2021 is marked in red for during covid. The y-axis shows count per day, which can either be collions per day or injuries 
per day. The blue dots show the amount collision per day and can clearly be seen to drop a lot after the first confirmed COVID-19 case. The red dots show the injured persons 
per day, and also drops slightly after the onset of COVID-19 but in no way as much as the collision count per day. So it actually seems like the gap between amount of 
collisions and amount of injured persons have become smaller since March 1st. 

We plot the confirmed 19-cases on top of the red part of the above plot, to see if there seems to be a pattern between the two: 
'''

cov_change_post_markdown = '''
The plot shows the impact of COVID-19 on the number of collisions and injured persons. The x-axis shows the months from february 2020 (slightly before COVID) to januar 2021 
(slightly after our COVID data). The y-axes is actually two fold here, where the left axis shows vehicle collisions (blue dots) and injured persons (red dots) per day and 
the right axis shows the number of daily COVID cases (green line). We can see that initially when the number corona cases grows, the number of collisions and injuries falls.
And when corona cases per day slows down the number of collisions and injured persons per day grows. So there is some kind of inverse proportionality between collisions and 
corona cases. This makes good sense, as when the pandemic starting getting real bad in NYC, restrictions were being enforced. More people stayed in and thus less collisions 
(and less injuries related to collisions because of that) is the result. 

So we talked about the gap between injuries and collisions became smaller doing COVID, but can we measure exactly how much? In the plots below we explore this: 
'''

cov_kills_pre_markdown = '''
The left plot shows the persons killed per collision in each of the five NYC boroughs, where the blue bars are the numbers pre COVID and the red bars are the numbers during
COVID. The right plot shows the persons injured per collision, again in each of the boroughs both before and during the pandemic. So from this we can definetely see that 
there is a difference in the relative danger when in a collision before and after COVID. The percentage of people dying in a collision grew significantly in all boroughs 
when COVID hit and so did the percentage of people injured in a collision. This is a bit suprising, what exactly happened during COVID-19 that made collisions more 'dangerous'?

To investigate this phenomena related to more dangerous crashes we look at the factors for crashes: 
'''

cov_outro_markdown = '''
The plot shows the reason specified for why a vehicle collision happened, before and during COVID. The x-axis shows the different categories of reasons for the collision, 
and the y-axis shows the percentage that the category was responsible of. The most popular collision reason has been removed since it is simply called 'unspecified' and
is thus not very interesting. The most common reason is simply driver distraction, which rose a bit during COVID. It is difficult to see exactly from this what could
cause the increase in danger, but it has been investigated further from news articles: 

Seeing as NYC was hit hard by COVID-19 and many people worked from home, the amount of collisions dropped significantly, so why did the relative danger 
rise? In the article "*Why Emptier Streets Meant an Especially Deadly Year for Traffic Deaths*"[[4]](https://www.nytimes.com/2021/01/01/nyregion/nyc-traffic-deaths.html) 
that question is explored in detail. In the above bar plot Unsafe Speed is seen to have risen from being the primary factor contributing to a collision in **1%** to **3%**. 
This is also highlighted in the article as "*New York City's automated cameras issued nearly twice as many speeding tickets daily, and rush-hour traffic speeds in Brooklyn 
and Queens shot up more than 80 percent*". This signifies a change in driver behaviour, where drivers are much more likely to drive too fast which, as expressed earlier, is 
known to cause a much higher risk of fatalities in collisions. This change in driver behaviour is, according to the aforementioned article, due to a lot of young people 
driving at high speeds and taking risks to alleviate the stress caused by lockdowns. The article also mentions, that older people were more likely to stay home whereas 
the young risktakers were the ones driving and thus causing more severe collisions when driving and riding motorcycles at high speed.
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
Along the x-axis we see the dates from march to november in 2020 and along the y-axis we see the amount of collisions there were on that given date. 
The blue points marks the actual amount of collisions, and the red points marks the amount of collisions our model predicted. To be able to evaluate
how good our predictions are we use a measure called **Root Mean Square Error (RMSE)**. **RMSE** is a value which describes how close the predictions
are to the actual data, where a very large value of **RMSE** means the predictions were not very good and a small value means they were quite accurate. 
A value of 40.5 may not be perfect, but it does not seem terrible when looking at the figure.

What is really interesting about the value is whether it improves or not when we train a new machine learning model based on the same features, but also
with the COVID-19 dataset added. So besides the amount of persons etc. who were injured on a given day, we also see how many tested positive for COVID-19 that day, 
and in specific boroughs. The same specific part of the data from the last model was chosen to test the new model, the resulting figure can be seen below: 
'''

ml_markdown_2 = '''
So this time the **RMSE** was only 34.95, meaning that having more data to find patterns in did indeed improve performance. As mentioned, both of the models
were evaluated on the same specific test data. To ensure that it was not just this specific data that caused the improvement, a more technical approach
called cross-validation (CV) is used with 10-folds. In 10-fold CV the models are trained on several parts of the data and an average is computed in the end,
ensuring that both models are trained and tested on several parts of the data. By doing this the first model got an average value of **RMSE=42.8**, 
where the second model got an average value of **RMSE=40.5**. It can indeed be concluded by this that the model which also used the COVID-19 dataset
performs better. 

We can conclude that adding the COVID-19 dataset did indeed help in predicting the amount of collisions. It makes good sense that it improved our **RMSE** 
value (by reducing it) as we could see that COVID-19 had quite a big impact of the amount of vehicle collisions in NYC and thus made our predictions 
more precise by adding the data.
'''

# HEATMAP 
heatmap_pre_markdown = '''
&nbsp;
&nbsp;
### Interactive exploration 

By now you should have an idea of how vehicle collisions in NYC have certain patterns and how it is possible to use these patterns for several things, 
such as observing when coronavirus hit the hardest and Machine Learning. We can from the prior analysis indeed conclude that COVID had a *very* big impact
on the amount of collisions in NYC, and also how 'dangerous' these collisions are, so now its your turn as the reader to investigate further! 

Below is an interactive heatmap, which lets you explore the data yourself. You can choose which years you want to see data from, but also which kind of data. 
The data is by default the total amount of collisions but can be changed to see numbers of persons injured etc. The radius of each point can also be increased: 
'''

heatmap_post_markdown = '''
You can observe many interesting things by playing with the heatmap, and actually also see the things we put focus on thoroughout the analysis. You can see 
where most collisions occur, how it changes greatly when only looking at cyclicst or pedestrians but also see the change in collisions when changing the year.
The total collisions is quite dense so if you change to the other types of data you should increase the radius a bit, so the points easier can be seen.  
'''

final_words_markdown = '''
&nbsp;
&nbsp;
### Final words

This website and the corresponding notebook is the result of 3 master students at Denmarks Technical University (DTU) and their final project in the Social 
Data Analysis and Visualization course.
'''