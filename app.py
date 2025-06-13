import plotly.graph_objects as go

fig = go.Figure(data=[
    go.Bar(
        x=['A', 'B', 'C', 'D'],
        y=[10, 20, 15, 25],
        marker_color=['red', 'green', 'blue', 'orange']  # Color per bar
    )
])
fig.show()
