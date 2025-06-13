import plotly.graph_objects as go
import math
import random

def midpoint(xy1, xy2):
    x1, y1 = xy1
    x2, y2 = xy2
    mid_x = (x1 + x2) / 2
    mid_y = (y1 + y2) / 2
    return (mid_x, mid_y)


side = 4

A = (0, 0)

B = (side, 0)

angle_rad = math.radians(60)
C_x = side / 2
C_y = side * math.sin(angle_rad)
C = (C_x, C_y)

D=(1,1)

x_coords = [A[0], B[0], C[0], A[0]]
y_coords = [A[1], B[1], C[1], A[1]]

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=x_coords,
    y=y_coords,
    mode='lines+markers',
    line=dict(color='black'),
    marker=dict(size=4, color='black')
))

coords = (D[0], D[1])
colours = ['#3385FF', '#66B2FF']
triangleP = [A,B,C]

for i in range(5000):
    coords = midpoint((coords[0], coords[1]), random.choice(triangleP))
    fig.add_trace(go.Scatter(
        x=[coords[0]],
        y=[coords[1]],
        mode='markers',
        marker=dict(size=3, color=random.choice(colours))
    ))

fig.update_layout(
    title="Trójkąt Sierpińskiego",
    xaxis=dict(scaleanchor="y", showgrid=True, zeroline=False),
    yaxis=dict(showgrid=True, zeroline=False),
    showlegend=False
)

fig.show()