import plotly.graph_objs as go
titles = ["subs","offers","crd","funded"]
for i in range(len(avg_dfs)):
    avg = avg_dfs[i]["count"].mean()
    length = len(list(avg_dfs[i]["name"]))
    fig = go.Figure()
    fig.add_trace(go.Bar(
    x=list(avg_dfs[i]["name"]),
    y=list(avg_dfs[i]["count"]),
    name=str(titles[i])+" (units)"
    ))
    
    fig.add_trace(
    go.Scatter(
        x=list(avg_dfs[i]["name"]),
        y=[avg for i in range(length)],
        name="Mean"
    ))
    
    fig.layout.update(
        font=dict(family='Helvetica', size=18, color='#7f7f7f'),
        margin=dict(b=200),
        autosize=False,
        width=1800,
        height=700)
    plotly.offline.plot(fig,filename=str(r'friday_data\\'+titles[i])+"_avg_barchart.html")
