import plotly.graph_objects as go
import numpy as np

xValues = np.linspace(0, 2*np.pi, 5000)
ySin = np.sin(xValues)
yCos = np.cos(xValues)

fig = go.Figure()
fig.add_trace(go.Scatter(x=xValues, y=ySin, mode='lines', name='y = sin(x)', marker_color= '#66B2FF'))
fig.add_trace(go.Scatter(x=xValues, y=yCos, mode='lines', name='y = cos(x)', marker_color= '#3385FF'))

tick_vals = [0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi]
tick_text = ['0', 'π/2', 'π', '3π/2', '2π']

fig.update_layout(
    title='Sinus i Cosinus x',
    xaxis=dict(
        tickvals=tick_vals,
        ticktext=tick_text,
        title='x'
    ),
    yaxis=dict(title='y'),
    template='plotly_white'
)

fig.show()