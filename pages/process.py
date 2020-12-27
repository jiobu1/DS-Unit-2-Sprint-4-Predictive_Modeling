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
            """
            # Process
            ### The Big Question

            #### Background
            Schools have been trying to measure the effectiveness of schools for many decades. The first standardized test appeared in 1845.
            There have been many critiques about testing but without another standardized procedure to measure student performance and thereby
            school effectiveness, these standardized tests have persisted.

            As a former educator, with a decade experience, school performance and student outcome are very important to me.
            In this project, I am trying to understand factors that affect this.
            For this dataset I chose the following question:
            **Does state expenditure affect student outcome on state tests?**

            #### Regression or Classification?

            Choosing whether or not this was a regression or classification problem took me some time to figure out. I wanted to do a
            regression analysis but since I wanted this information to be accessible to all, I felt that classification would allow users
            to better grasp outcomes. (I do have a regression version of this as well.)

            Noticings: Unfortunately, the state scores are not very good for any of the states for any of the years. Most states,
            across both Math and Reading, have underperformed; only a small percentage scored proficient (only in Math).

            #### Defining the Target

            With the dataset, there was a 4th and 8th grade Math and Reading Score columns. To create a classification
            problem, I chose the 8th grade reading scores as the Target column and then broke it down based on the NAEP's
            breakdown of scores:

            NAEP Reading Score Breakdown
            basic (0-280)
                This column was broken down into 3 categories:
                low,
                mid, and
                high basic
            proficient (281-322)
            advanced (323-500)

            #### Cleanup

            There was a lot of data cleaning that I had to do to make this dataset usable.
            * I first merged the state csv and the finance csv. I had to update finance csv to capture 2017
              census data so I had more usable data.

            * For this dataset, I would delete the years where the NAEP test scores are not available since that does not
              give anything for me to train/validate/test the data on. (2003, 2005, 2007, 2009, 2011, 2013, 2015, 2017)
            * I will also delete the years where I do not have the finacial information available (I updated 2017)
            * I adjusted the revenue and expenditures columns, using the consumer price index to reflect inflation
            * I dropped demographic data since this was only captured in 2009.

            Feature engineered 6 columns
            * look at % of total revenue spent on education
            * look at % of total expenditure spent on instruction, support other, and capital outlay
            * look at cost per student

            I went from 195 columns to 32 columns:
            'STATE','YEAR','ENROLL','GRADES_PK_G', 'GRADES_KG_G','GRADES_4_G', 'GRADES_8_G','GRADES_12_G','GRADES_1_8_G',
            'GRADES_9_12_G','GRADES_ALL_G','AVG_MATH_4_SCORE','AVG_READING_4_SCORE','AVG_MATH_8_SCORE','AVG_READING_8_SCORE',
            'MATH_PROF_8','READING_PROF_8','ADJUSTED_TOTAL_REVENUE','ADJUSTED_FEDERAL_REVENUE','ADJUSTED_STATE_REVENUE',
            'ADJUSTED_LOCAL_REVENUE','ADJUSTED_TOTAL_EXPENDITURE','ADJUSTED_INSTRUCTION_EXPENDITURE',
            'ADJUSTED_SUPPORT_SERVICES_EXPENDITURE','ADJUSTED_OTHER_EXPENDITURE','ADJUSTED_CAPITAL_OUTLAY_EXPENDITURE',
            '%TOTAL_REVENUE','%TOTAL_EXPENDITURE_INSTRUCTION','%TOTAL_EXPENDITURE_SUPPORT_SERVICES',
            '%TOTAL_EXPENDITURE_OTHER', '%TOTAL_EXPENDITURE_CAPITAL_OUTLAY', 'COST_PER_STUDENT'

            And from 1492 rows to 524 rows

            #### Metric and Baseline

            After defining the target it became a simple matter of choosing a metric and baseline to go off of. To start, I realized that
            squirrels were friendly in 1,581 observations and ran away in 1,410. This would mean that the baseline estimate someone could
            guess would be that a squirrel would be friendly 52.9 percent of the time and the remaining 47.1 percent it would run away.
            That just leaves choosing a metric to score my model on. I picked accuracy as my metric because if I could beat the baseline
            accuracy, I would be able to see how useful my model was.

            #### Leakage and Usefulness

            There were no features that gave leakage into my target column in fact when I dropped the inital 3 columns: Approaches,
            Indifferent, and Runs from. I was able to eliminate all leakage and so my model is watertight when its predictions
            are made. The usefulness of this model is in the eye of the beholder. Perhaps a scientist would like to figure out why
            a certain color of squirrel is more prone to running or why squirrels in northern centrall park respond differently
            than the ones in the southern part. My intention of making the model was to make it fun for park goers.

            """
        ),

    ],
)

layout = dbc.Row([column1])