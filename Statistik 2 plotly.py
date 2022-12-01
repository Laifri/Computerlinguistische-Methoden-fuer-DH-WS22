import plotly.graph_objects as go
art=['Linguistik', 'Literaturwissenschaften']

fig = go.Figure(data=[
    go.Bar(name='Streuung', x=art, y=[28979.68, 25201.61]),
    go.Bar(name='Arithmetisches Mittel', x=art, y=[67035.9, 76863.07])
])
# Change the bar mode
fig.update_layout(barmode='group')
fig.show()