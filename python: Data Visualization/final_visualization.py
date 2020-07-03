#Question 1
import numpy as np
import pandas as pd
df = pd.read_csv('https://cocl.us/datascience_survey_data', index_col=0)
df.head()

#Question 2
import matplotlib.pyplot as plt
import matplotlib as mpl
df.sort_values(['Very interested'], ascending=False, axis=0, inplace=True)
df = round((df/2233)*100, 2)
df.head()
ax1 = df.plot(kind='bar', figsize=(20, 8), color=['#5cb85c','#5bc0de','#d9534f'], width=0.8, fontsize=14)
ax1.set_title('Percentage of Respondents Interest in Data Science Areas',fontsize=16)
# ax.set_facecolor('white')
ax1.legend(fontsize=14,facecolor = 'white') 
ax1.get_yaxis().set_visible(False)
for p in ax1.patches:
    ax1.annotate(np.round(p.get_height(),decimals=2), (p.get_x()+p.get_width()/2., p.get_height()), ha='center', va='center', xytext=(0, 10), textcoords='offset points', fontsize = 14)
plt.show()

#Question 3
df2 = pd.read_csv('https://cocl.us/sanfran_crime_dataset')
df2.head()
df3 = df2['PdDistrict'].value_counts()
df4 = pd.DataFrame(data=df3.values, index = df3.index, columns=['Count'])
df4 = df4.reindex(["CENTRAL", "NORTHERN", "PARK", "SOUTHERN", "MISSION", "TENDERLOIN", "RICHMOND", "TARAVAL", "INGLESIDE", "BAYVIEW"])
df4 = df4.reset_index()
df4.rename({'index': 'Neighborhood'}, axis='columns', inplace=True)
df4.head()

#Question 4
import folium
sf_map = folium.Map(location = [37.77, -122.42], zoom_start = 12)
sf_map.choropleth(geo_data='https://cocl.us/sanfran_geojson', data=df4, columns=['Neighborhood', 'Count'], key_on='feature.properties.DISTRICT', fill_color='YlOrRd', fill_opacity=0.7, line_opacity=0.2, legend_name='Crime Rate in San Francisco')
sf_map

