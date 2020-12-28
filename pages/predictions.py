# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load

# Imports from this application
from app import app
print('Pipeline loaded!')

# Load Pipeline
pipeline = load('assets/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout


# 'COST_PER_STUDENTx','AVG_MATH_4_SCOREx', 'AVG_READING_4_SCOREx',
# 'ADJUSTED_TOTAL_EXPENDITUREx', 'ENROLLx', '%TOTAL_EXPENDITURE_INSTRUCTIONx',
# '%TOTAL_EXPENDITURE_SUPPORT_SERVICES', 'ADJUSTED_OTHER_EXPENDITURE'

column1 = dbc.Col(
    [
        dcc.Markdown('#### Enrollment'),
        dcc.Slider(
            id='Enrollment',
            min= 44199.0,
            max=- 6307022.0,
            step= 500000.0,
            value= 3175610.0,
        ),
        html.Div(id='slider-output-container1'),

        dcc.Markdown('#### Cost Per Student'),
        dcc.Slider(
            id='COST_PER_STUDENT',
            min= 4.50,
            max=- 29.35,
            step= 0.50,
            value= 15.00,
        ),
        html.Div(id='slider-output-container2'),

        dcc.Markdown('#### Average 4th Grade Reading'),
        dcc.Slider(
            id='AVG_READING_4_SCORE',
            min= 178.558,
            max=- 236.774,
            step= 10.000,
            value= 207.000,
        ),
        html.Div(id='slider-output-container3'),

        dcc.Markdown('#### Average 4th Grade Math'),
        dcc.Slider(
            id='AVG_MATH_4_SCORE',
            min= 192.600,
            max= 253.396,
            step= 10.000,
            value= 222.500,
        ),
        html.Div(id='slider-output-container4'),

        dcc.Markdown('#### Total Expenditure'),
        dcc.Slider(
            id='ADJUSTED_TOTAL_EXPENDITURE',
            min= 959724.58,
            max=- 89096394.79,
            step= 50000.00,
            value= 959724.58,
        ),
        html.Div(id='slider-output-container5'),

        dcc.Markdown('#### % Spent on Instruction'),
        dcc.Slider(
            id= '%TOTAL_EXPENDITURE_INSTRUCTION',
            min= 0.37,
            max=- 0.65,
            step= 0.01,
            value=-0.50,
        ),
        html.Div(id='slider-output-container6'),

        dcc.Markdown('#### % Spent on Support Services'),
        dcc.Slider(
            id= '%TOTAL_EXPENDITURE_SUPPORT_SERVICES',
            min= 0.22,
            max=- 0.50,
            step= 0.01,
            value= 0.30,
        ),
        html.Div(id='slider-output-container7'),

        dcc.Markdown('#### % Spent on Other'),
        dcc.Slider(
            id= 'ADJUSTED_OTHER_EXPENDITURE',
            min= 34305.84,
            max=- 4479926.65,
            step= 500000,
            value= 2257116.24,
        ),
        html.Div(id='slider-output-container8'),

    ],
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1])