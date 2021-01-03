# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            '''
            ### Does Education Expenditure Affect Student Performance?
            '''
            ),
        html.Br(),

        dcc.Markdown(
            '''
            State Expenditure Vs Student Outcome app allows users to see how a state's expenditure
            on education affects student outcome on standardized exams, specifically 8th grade reading.
            '''
        ),
        html.Br(),

        dcc.Link(dbc.Button('Student Outcome vs Education Expenditure', color='primary'), href='/predictions')
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.Img(src='assets/test_taking.jpg', className='img-fluid', style = {'height': '350px'})
    ]
)

layout = dbc.Row([column1, column2])