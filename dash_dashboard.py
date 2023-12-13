# Import necessary libraries
import dash
from dash import dash_table
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import pandas as pd

# Load CSV data
csv_file_path = 'performance_metrics.csv'  # Replace with the path to your CSV file
df = pd.read_csv(csv_file_path)

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    # Dropdown for selecting a column
    html.Label('Select a column:'),
    dcc.Dropdown(
        id='column-dropdown',
        options=[{'label': col, 'value': col} for col in ['A&E attendances Type 1','Total Admissions','Type 1 Proportion attendances over 4hrs','Proportion waiting over 4hrs for admission','Proportion waiting over 12hrs for admission']],
        value=df.columns[0]  # Default selected column
    ),
    
    # Bar chart to display department metrics
    dcc.Graph(id='department-metrics'),
])

@app.callback(
    Output('department-metrics', 'figure'),
    [Input('column-dropdown', 'value')]
)
def update_department_metrics(selected_metric):
    fig = {
        'data': [
            {'x': df['Org name'], 'y': df[selected_metric], 'type': 'bar', 'name': selected_metric},
        ],
        'layout': {
            'title': f'Department {selected_metric}',
            'xaxis': {'title': 'Department'},
            'yaxis': {'title': selected_metric},
        }
    }
    return fig

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)