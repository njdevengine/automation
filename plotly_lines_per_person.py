import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

for i in range(len(all_reps)):
    subs = go.Scatter(
        x=[(" to ").join(ranges[4]),
           (" to ").join(ranges[3]),
           (" to ").join(ranges[2]),
           (" to ").join(ranges[1]),
           (" to ").join(ranges[0])],
        y= [int(i) for i in list(weekly.loc[all_reps[i]][s_d])],
        mode='lines',
        name="subs",
        line=dict(shape="spline",smoothing=0, width=4),
    )
    offers = go.Scatter(
        x=[(" to ").join(ranges[4]),
           (" to ").join(ranges[3]),
           (" to ").join(ranges[2]),
           (" to ").join(ranges[1]),
           (" to ").join(ranges[0])],
        y= [int(i) for i in list(weekly.loc[all_reps[i]][o_d])],
        mode='lines',
        name='offers',
        line=dict(shape="spline",smoothing=0, width=4),
    )
    crd = go.Scatter(
        x=[(" to ").join(ranges[4]),
           (" to ").join(ranges[3]),
           (" to ").join(ranges[2]),
           (" to ").join(ranges[1]),
           (" to ").join(ranges[0])],
        y= [int(i) for i in list(weekly.loc[all_reps[i]][c_d])],
        mode='lines',
        name="CRR",
        line=dict(shape="spline",smoothing=0, width=4),
    )
    funding = go.Scatter(
        x=[(" to ").join(ranges[4]),
           (" to ").join(ranges[3]),
           (" to ").join(ranges[2]),
           (" to ").join(ranges[1]),
           (" to ").join(ranges[0])],
        y= [int(i) for i in list(weekly.loc[all_reps[i]][f_d])],
        mode='lines',
        name="funding",
        line=dict(shape="spline",smoothing=0, width=4),
    )
    layout = go.Layout(
    title=str(all_reps[i]),
    font=dict(size=18, color='#7f7f7f')
    )
    
    data = [subs,offers,crd,funding]
    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename= r"directory\\"+str(all_reps[i])+'_chart.html')
