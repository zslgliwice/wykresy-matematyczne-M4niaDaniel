import plotly.graph_objects as go

partie = ['PiS', 'KO', 'Trzecia Droga', 'Nowa Lewica', 'Konfederacja', 'Bezpartyjni']
procentG = [35.38, 30.70, 14.40, 8.61, 7.16, 1.86]
procentM =[42.17, 34.13, 14.13, 5.65, 3.19, 0.00]

fig = go.Figure(data=[
    go.Bar(
        name='Procent Głosów',
        x=partie,
        y=procentG,
        marker_color='#66B2FF',
        width=0.4
    ),
    go.Bar(
        name='Procent Mandatów',
        x=partie,
        y=procentM,
        marker_color='#3385FF',
        width=0.3
    )
])

fig.update_layout(
    barmode='group',
    title='Wybory partyjne Polska 2023'
)

fig.show()
