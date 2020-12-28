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


# 'COST_PER_STUDENT','AVG_MATH_4_SCORE', 'AVG_READING_4_SCORE',
# 'ADJUSTED_TOTAL_EXPENDITURE', 'ENROLL', '%TOTAL_EXPENDITURE_INSTRUCTION',
# '%TOTAL_EXPENDITURE_SUPPORT_SERVICES', 'ADJUSTED_OTHER_EXPENDITURE'

column1 = dbc.Col(
    [
        dcc.Markdown('#### Enrollment'),
        dcc.Slider(
            id='Enrollment', 
            min= 44199.0, 
            max=- 6307022.0, 
            step= 0.0005, 
            value=-3,175,610, 
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [

    ]
)

layout = dbc.Row([column1])