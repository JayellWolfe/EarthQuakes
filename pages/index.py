import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app

"""
https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
Layout in Bootstrap is controlled using the grid system. The Bootstrap grid has 
twelve columns.
There are three main layout components in dash-bootstrap-components: Container, 
Row, and Col.
The layout of your app should be built as a series of rows of columns.
We set md=4 indicating that on a 'medium' sized or larger screen each column 
should take up a third of the width. Since we don't specify behaviour on 
smaller size screens Bootstrap will allow the rows to wrap so as not to squash 
the content.
"""

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Predicting Earthquakes 
            
            Earthquakes have devastatingly deadly consequences. The ability to predict earthquakes
            is one of the most important challenges facing Earth Science today. And being able to
            predict and forecast earthquakes before they occur would mean saving countless lives
            and billions of dollars in infrastucture
            
            Three focus key points are when the event will occur, where it will occur, and how 
            large it will be.

            Using real-time siesmic signal data in a laboratory setting, this will focus on the 
            when, predicting the time remaining until the next earthquake. 

        
            """
        ),
        dcc.Link(dbc.Button('Predictions', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/earthquake_heatmap.jpg',
                className='img-fluid'),

    ]
)

layout = dbc.Row([column1, column2])
