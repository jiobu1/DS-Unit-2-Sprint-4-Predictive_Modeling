# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_daq as daq
import dash_html_components as html
from dash.dependencies import Input, Output
from joblib import load
import pandas as pd

# Imports from this application
from app import app
print('Pipeline loaded!')

# Load Pipeline used for predicting
pipeline = load('assets/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout

column1 = dbc.Col(
    [
        dcc.Markdown('##### Enrollment'),
        daq.Slider(
            id = 'ENROLL',
            min = 44199,
            max = 6307022,
            step = 100000,
            value = 3175610,
            color = 'black',
            className = 'mb-2'
        ),
        html.Div(id='slider-output-container1'),
        html.Br(),
        html.Br(),

        dcc.Markdown('##### Cost Per Student'),
        daq.Slider(
            id = 'COST_PER_STUDENT',
            min = 4.50,
            max = 29.35,
            step = 0.50,
            value = 15.00,
            color = 'black',
            className = 'mb-2'
        ),
        html.Div(id='slider-output-container2'),
        html.Br(),
        html.Br(),

        dcc.Markdown('##### Average 4th Grade Reading'),
        daq.Slider(
            id = 'AVG_READING_4_SCORE',
            min = 178.558,
            max = 236.774,
            step = 10.000,
            value = 207.000,
            color = 'black',
            className = 'mb-2'
        ),
        html.Div(id='slider-output-container3'),
        html.Br(),
        html.Br(),

        dcc.Markdown('##### Average 4th Grade Math'),
        daq.Slider(
            id = 'AVG_MATH_4_SCORE',
            min = 192.600,
            max = 253.396,
            step = 10.000,
            value = 222.500,
            color = 'black',
            className = 'mb-2'
        ),
        html.Div(id='slider-output-container4'),
        html.Br(),
        html.Br(),
    ],
    md=4
)

column2 = dbc.Col(
    [
        dcc.Markdown('##### Total Expenditure'),
        daq.Slider(
            id = 'ADJUSTED_TOTAL_EXPENDITURE',
            min = 959725,
            max = 89096395,
            step = 50000,
            value = 959725,
            color = 'black',
            className = 'mb-2'
        ),
        html.Div(id='slider-output-container5'),
        html.Br(),
        html.Br(),

        dcc.Markdown('##### % Spent on Instruction'),
        daq.Slider(
            id = '%TOTAL_EXPENDITURE_INSTRUCTION',
            min = 0.37,
            max = 0.65,
            step = 0.01,
            value = 0.50,
            color = 'black',
            className = 'mb-2'
        ),
        html.Div(id='slider-output-container6'),
        html.Br(),
        html.Br(),

        dcc.Markdown('##### % Spent on Support Services'),
        daq.Slider(
            id = '%TOTAL_EXPENDITURE_SUPPORT_SERVICES',
            min = 0.22,
            max = 0.50,
            step = 0.01,
            value = 0.30,
            color = 'black',
            className = 'mb-2'
        ),
        html.Div(id='slider-output-container7'),
        html.Br(),
        html.Br(),

        dcc.Markdown('##### % Spent on Other'),
        daq.Slider(
            id = 'ADJUSTED_OTHER_EXPENDITURE',
            min = 34305.84,
            max = 4479926.65,
            step = 500000,
            value = 2257116.24,
            color = 'black',
            className = 'mb-2'
        ),
        html.Div(id='slider-output-container8'),
        html.Br(),
        html.Br(),
    ],
)

column3 = dbc.Col(
    [dcc.Markdown(
        """
        ### **Predict**
        Use the controls to predict student outcome on standardized tests:
        """
        ),
    html.Div(id='prediction-content', style={'fontWeight':'bold'}),
    html.Br(),

    html.H4('Student Outcome'),
    html.Div(id='prediction-content', className='lead')
    ]
)

layout = dbc.Row([column1, column2, column3])

@app.callback(
    Output('prediction-content', 'children'),
    [Input('ENROLL', 'value'),
    Input('COST_PER_STUDENT', 'value'),
    Input('AVG_READING_4_SCORE', 'value'),
    Input('AVG_MATH_4_SCORE', 'value'),
    Input('ADJUSTED_TOTAL_EXPENDITURE', 'value'),
    Input('%TOTAL_EXPENDITURE_INSTRUCTION', 'value'),
    Input('%TOTAL_EXPENDITURE_SUPPORT_SERVICES', 'value'),
    Input('ADJUSTED_OTHER_EXPENDITURE', 'value')]
)

def predict(ENROLL, COST_PER_STUDENT, AVG_READING_4_SCORE, AVG_MATH_4_SCORE, ADJUSTED_TOTAL_EXPENDITURE, TOTAL_EXPENDITURE_INSTRUCTION, TOTAL_EXPENDITURE_SUPPORT_SERVICES, ADJUSTED_OTHER_EXPENDITURE):
    df = pd.DataFrame(
        columns=['ENROLL','COST_PER_STUDENT','AVG_READING_4_SCORE','AVG_MATH_4_SCORE',
                 'ADJUSTED_TOTAL_EXPENDITURE', '%TOTAL_EXPENDITURE_INSTRUCTION',
                 '%TOTAL_EXPENDITURE_SUPPORT_SERVICES', 'ADJUSTED_OTHER_EXPENDITURE'],
        data=[[ENROLL, COST_PER_STUDENT, AVG_READING_4_SCORE, AVG_MATH_4_SCORE, ADJUSTED_TOTAL_EXPENDITURE, TOTAL_EXPENDITURE_INSTRUCTION, TOTAL_EXPENDITURE_SUPPORT_SERVICES, ADJUSTED_OTHER_EXPENDITURE]]
    )
    y_pred = pipeline.predict(df)[0]
    if y_pred == 1:
        return f'Student performance is 1, or basic'
    if y_pred == 2:
        return f'Student performance is 2, or mid-basic'
    else:
        return f'Student performacne is 3, or mid-basic'

@app.callback(
    dash.dependencies.Output('slider-output-container1', 'children'),
    [dash.dependencies.Input('ENROLL', 'value')])
def update_output(value):
    return 'You have entered "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container2', 'children'),
    [dash.dependencies.Input('COST_PER_STUDENT', 'value')])
def update_output(value):
    return 'You have entered "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container3', 'children'),
    [dash.dependencies.Input('AVG_READING_4_SCORE', 'value')])
def update_output(value):
    return 'You have entered "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container4', 'children'),
    [dash.dependencies.Input('AVG_MATH_4_SCORE', 'value')])
def update_output(value):
    return 'You have entered "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container5', 'children'),
    [dash.dependencies.Input('ADJUSTED_TOTAL_EXPENDITURE', 'value')])
def update_output(value):
    return 'You have entered "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container6', 'children'),
    [dash.dependencies.Input('%TOTAL_EXPENDITURE_INSTRUCTION', 'value')])
def update_output(value):
    return 'You have entered "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container7', 'children'),
    [dash.dependencies.Input('%TOTAL_EXPENDITURE_SUPPORT_SERVICES', 'value')])
def update_output(value):
    return 'You have entered "{}"'.format(value)

@app.callback(
    dash.dependencies.Output('slider-output-container8', 'children'),
    [dash.dependencies.Input('ADJUSTED_OTHER_EXPENDITURE', 'value')])
def update_output(value):
    return 'You have entered "{}"'.format(value)