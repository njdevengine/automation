import plotly
import plotly.plotly as py
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot

from numpy import arange,array,ones
from scipy import stats

length = len([int(i) for i in list(weekly.sum()[s_d])])
xi = arange(0,length)
A = array([ xi, ones(length)])
y = [int(i) for i in list(weekly.sum()[s_d])]
slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
line = slope*xi+intercept
trace1 = go.Scatter(
                  x=[i for i in reversed([(" to ").join(ranges[i]) for i in range(len(ranges))])],
                  y=line,
                  opacity=0.25,
                  hoverinfo='skip',
                  mode='lines',
                  marker=go.Marker(color='rgb(33, 150, 243)'),
                  name='Subs (Trend)',
                  line=dict(shape="spline",smoothing=0, width=4)
                  )
traces1 = go.Scatter(
                  x=[i for i in reversed([(" to ").join(ranges[i]) for i in range(len(ranges))])],
                  y=y,
                  mode='lines',
                  marker=go.Marker(color='rgb(33, 150, 243)'),
                  name='Subs',
                  line=dict(shape="spline",smoothing=0, width=4)
                  )
####
length = len([int(i) for i in list(weekly.sum()[o_d])])
xi = arange(0,length)
A = array([ xi, ones(length)])
y = [int(i) for i in list(weekly.sum()[o_d])]
slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
line = slope*xi+intercept
trace2 = go.Scatter(
                  x=[i for i in reversed([(" to ").join(ranges[i]) for i in range(len(ranges))])],
                  y=line,
                  opacity=0.25,
                  hoverinfo='skip',
                  mode='lines',
                  marker=go.Marker(color='rgb(255, 87, 34)'),
                  name='Offer (Trend)',
                  line=dict(shape="spline",smoothing=0, width=4)
                  )
traceo2 = go.Scatter(
                  x=[i for i in reversed([(" to ").join(ranges[i]) for i in range(len(ranges))])],
                  y=y,
                  mode='lines',
                  marker=go.Marker(color='rgb(255, 87, 34)'),
                  name='Offer',
                  line=dict(shape="spline",smoothing=0, width=4)
                  )
####
length = len([int(i) for i in list(weekly.sum()[c_d])])
xi = arange(0,length)
A = array([ xi, ones(length)])
y = [int(i) for i in list(weekly.sum()[c_d])]
slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
line = slope*xi+intercept
trace3 = go.Scatter(
                  x=[i for i in reversed([(" to ").join(ranges[i]) for i in range(len(ranges))])],
                  y=line,
                  opacity=0.25,
                  hoverinfo='skip',
                  mode='lines',
                  marker=go.Marker(color='rgb(76, 175, 80)'),
                  name='CRD (Trend)',
                  line=dict(shape="spline",smoothing=0, width=4)
                  )
tracec3 = go.Scatter(
                  x=[i for i in reversed([(" to ").join(ranges[i]) for i in range(len(ranges))])],
                  y=y,
                  mode='lines',
                  marker=go.Marker(color='rgb(76, 175, 80)'),
                  name='CRD',
                  line=dict(shape="spline",smoothing=0, width=4)
                  )
####
length = len([int(i) for i in list(weekly.sum()[f_d])])
xi = arange(0,length)
A = array([ xi, ones(length)])
y = [int(i) for i in list(weekly.sum()[f_d])]
slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
line = slope*xi+intercept
trace4 = go.Scatter(
                  x=[i for i in reversed([(" to ").join(ranges[i]) for i in range(len(ranges))])],
                  y=line,
                  opacity=0.25,
                  hoverinfo='skip',
                  mode='lines',
                  marker=go.Marker(color='rgb(244, 67, 54)'),
                  name='Funded (Trend)',
                  line=dict(shape="spline",smoothing=0, width=4)
                  )
tracef4 = go.Scatter(
                  x=[i for i in reversed([(" to ").join(ranges[i]) for i in range(len(ranges))])],
                  y=y,
                  mode='lines',
                  marker=go.Marker(color='rgb(244, 67, 54)'),
                  name='Funded',
                  line=dict(shape="spline",smoothing=0, width=4)
                  )
####
layout = go.Layout(
xaxis=dict(tickangle=45,tickfont=dict(size=12)),
title="Company Totals Year Lookback (Weekly)",
font=dict(size=18, color='#7f7f7f'),
margin=go.layout.Margin(
        l=50,
        r=50,
        b=150,
        t=100,
        pad=20
    )
)
data = [trace1,traces1,trace2,traceo2,trace3,tracec3,trace4,tracef4]
fig = go.Figure(data=data, layout=layout)
plot(fig, filename= r"directory\yearly_fit_totals_chart.html")
