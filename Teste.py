import plotly as py        
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
import plotly.graph_objs as go

##Importando as bibliotecas necessarias para o funcionamento do mapa

data = dict (type= 'choropleth', 
            locations = ['TX', 'CA', 'MI', 'FL'],
            locationmode = 'USA-states',
            colorscale = 'Hot',
            text = ['Texas', 'California', 'Michigan', 'Florida'],
            z = [1.2,4.3,3.3,2,7],
            colorbar = {'title' : 'Colorbar'})

layout = dict(geo={'scope' : 'usa'})      

choromap = go.Figure(data = [data], layout = layout)     
choromap.show() 