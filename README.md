# Bloc N°1
## Construction_et_alimentation_d_infrastructure_de_gestion_de_donnees

## Vidéo:
[LIEN VIDEO DE PRESENTATION](https://share.vidyard.com/watch/MmWJycfYebg2VFEiabr678?)

# Plan your trip with Kayak
![image](https://user-images.githubusercontent.com/115455973/222426897-6d77f93f-5368-4253-b27e-0d8c6f1ac00f.png)

Kayak is a travel search engine that helps user plan their next trip at the best price.

## Scope of the Project 🚧
The marketing team needs help on a new project. After doing some user research, the team discovered that 70% of their users who are planning a trip would like to have more information about the destination they are going to.
Therefore, Kayak Marketing Team would like to create an application that will recommend where people should plan their next holidays. The application should be based on real data about:

    Weather
    Hotels in the area

The application should then be able to recommend the best destinations and hotels based on the above variables at any given time.

## Steps

- Collect Data:
  1- Using 2 API's to get GPS coordinates and the weather of 35 cities in France
  2- Scrap Booking.com to get the 20 TOP hotels in these cities
  
- ETL:
  1- Store the collected information on a S3 bucket using AWS
  2- Extract transform and load the datas to a warehouse using RDS
 
 - Vizualisation:
 Using SQL requests, get back the needed information to plot on 2 maps:
   * TOP 5 best cities regarding the weather (highest temperature for me)
   * TOP 20 hotels on booking.com in these 5 cities
     
## Files:
You'll find these files in the repository:
  - Requirements.txt: the libraries you'll need
  - Scrap_Booking.py: the python script to scrap booking.com
  - projetkayak.ipynb: the global notebook with the whole project
  - the .json files with the API and scrapping results
  - kayakdata.csv: csv file put on AWS 
  - kayak.csv: file loaded from AWS
