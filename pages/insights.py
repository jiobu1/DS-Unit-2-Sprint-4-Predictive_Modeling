# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            '''
            ## Insights
            '''
            ),
        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            #### The Classification Model
            '''
            ),
        html.Br(),

        dcc.Markdown(
            '''
            For this predictive model, I tried out about a dozen models, playing with almost every hyperparameter available to get a model with a validation accuracy
            that beat my baseline model. To make this a usable application I knew I would not be able to keep all 32 features, so I narrowed my features down to
            8 after looking at the feature permutations.
            '''
            ),
        html.Br(),

        html.Img(src='assets/permutation_importance.png', className='img-fluid', style={'height':'400px'} ),
        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            It can be seen that many of the different features didn't hold very much weight in how they affected the model. I opted to keep the ones that
            I was most interested in. Those 8 features are:
            '''
            ),

        dcc.Markdown(
            '''
            'ENROLL',  'COST_PER_STUDENT',  'AVG_READING_4_SCORE',  'AVG_MATH_4_SCORE',  'ADJUSTED_TOTAL_EXPENDITURE',  '%TOTAL_EXPENDITURE_INSTRUCTION',
            '%TOTAL_EXPENDITURE_SUPPORT_SERVICES',  'ADJUSTED_OTHER_EXPENDITURE'
            '''
            ),

        dcc.Markdown(
            '''
            Most of the features are self explanatory but below is how I calculated the feature engineered columns that I used in this model.
            - Cost per student is calculated by taking the updated education expenditure (based on the consumer price index) and dividing by the enrollment column.
            - To find out the percentage spent on instruction and support services, total instruction and support services  expenditure is divided by updated education expenditure
            - Adjusted other expenditure is also updated based on the consumer price index.
            '''
            ),
        html.Br(),

        dcc.Markdown(
            '''
            #### Model Explanation
            '''
            ),
        html.Br(),

        dcc.Markdown(
            '''
            Since most of the features did not have as predictive a quality as I would like, I wanted to look further to see how ADJUSTED_TOTAL_EXPENDITURE and
            %TOTAL_EXPENDITURE_INSTRUCTION affected the different student outcomes of 1,2, or 3.
            '''
        ),
        html.Br(),

        html.Img(src='assets/pdp_title.png', className='img-fluid', style={'height':'80px'} ),
        html.Img(src='assets/pdp2_title.png', className='img-fluid', style={'height':'80px'} ),
        html.Img(src='assets/pdp_class0.png', className='img-fluid', style={'height':'400px'} ),
        html.Img(src='assets/pdp2_class0.png', className='img-fluid', style={'height':'400px'} ),
        html.Img(src='assets/pdp_class1.png', className='img-fluid', style={'height':'400px'} ),
        html.Img(src='assets/pdp2_class1.png', className='img-fluid', style={'height':'400px'} ),
        html.Img(src='assets/pdp_class2.png', className='img-fluid', style={'height':'400px'} ),
        html.Img(src='assets/pdp2_class2.png', className='img-fluid', style={'height':'400px'} ),
        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            Looking at the effect of increased total education expenditure, you can see that class 0 (1, low basic) and class 2 (3, high basic), you can see a positive effect but with class 1 (2, mid basic)
            there is a negative effect. Funny enough, the percentage of education expenditure on instruction has the opposite effect on all classes, with class 0 (1, low basic) and class 2 (3, high basic), 
            you can see a negative effect but with class 1 (2, mid basic) there is a positive effect.
            '''
        ),

        dcc.Markdown(
            '''
            To examine this further, I created a partial dependence plot between ADJUSTED_TOTAL_EXPENDITURE and %TOTAL_EXPENDITURE_INSTRUCTION to see if the % of the
            budget spent on instruction affects student outcome. Here the results made a little bit more sense.
            With class 0 (1, low basic) the percentage of the education budget spent on instruction did not have a big effect.
            With class 1 (2, mid basic) and class 2 (3, high basic) you can see that the greater the percentage of the education
            budget spent on instruction the greater the effect on student outcome.
            '''
        ),
        html.Br(),

        html.Img(src='assets/pdp_two_0.png', className='img-fluid', style={'height':'450px'} ),
        html.Img(src='assets/pdp_two_1.png', className='img-fluid', style={'height':'450px'} ),
        html.Img(src='assets/pdp_two_2.png', className='img-fluid', style={'height':'450px'} ),
        html.Br(),
        html.Br(),

        dcc.Markdown(
            '''
            #### The Final Verdict
            '''
            ),
        html.Br(),

        dcc.Markdown(
            '''
            Now comes the worst part about real world data, it is subject to random chance. I reserved a little bit of my data known as the test set to give a final hoorah
            and see how my model would react to observations it wasn't trained on. Lucky enough, it did significantly better than validation set.
            My simplified model scored 62.7 percent on the test set... Everyone wants their model to do significantly better and have an accuracy of 85% or better
            but I was pleased that my test accuracy was better than my validation and that this condensed model scored better than using all 32 features.
            I understand that the more data that I collect and train on, the better my model would become. I have plotted a confusion matrix to show the times my model
            struggled to make the correct classification during the final prediction.
            '''
        ),
        html.Br(),

        html.Img(src='assets/confusion_matrix.png', className='img-fluid', style={'height':'400px'} ),

        dcc.Markdown(
            '''
            This topic is much bigger than what my model was capable of predicting. There is so much that rides on the outcome of
            tests scores but as an educator and homeschooling mom, I wonder if we are measuring the right thing.
            '''
        ),
        html.Br(),

    ],
)

layout = dbc.Row([column1])