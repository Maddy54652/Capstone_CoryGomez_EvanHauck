import plotly.graph_objs as go
from plotly.graph_objs import Scatter
import pandas as pd
import plotly.offline as offline
import sqlite3
import datetime
from tempfile import NamedTemporaryFile
from django.http import StreamingHttpResponse
import django
django.setup()
from WeatherStation.models import Record
from pytz import timezone
from datetime import datetime

pst = timezone('UTC')

#function to be called in order to plot desired column, then return string to be embeded on webpage
def plotGraph( column_num, startDate, endDate):
    file_str = ''
    x = []
    y = []

    if column_num == '0':
        for i in Record.objects.only("timeStamp", "battAvg").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.battAvg)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Battery Voltages')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Voltage', type='log'))
        }, output_type='div')
    elif column_num == '1':
        for i in Record.objects.only("timeStamp", "pTempCAvg").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.pTempCAvg)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='P_Temp')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Temperature (C)', type='log'))
        }, output_type='div')
    elif column_num == '2':
        for i in Record.objects.only("timeStamp", "airTCAvg").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.airTCAvg)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Air_Temp')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Temperature (C)', type='log'))
        }, output_type='div')
    elif column_num == '3':
        for i in Record.objects.only("timeStamp", "rH").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.rH)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='rH')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='rH', type='log'))
        }, output_type='div')
    elif column_num == '4':
        for i in Record.objects.only("timeStamp", "slrkW").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.slrkW)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='slrkW')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='slrkW', type='log'))
        }, output_type='div')
    elif column_num == '5':
        for i in Record.objects.only("timeStamp", "slrMJTot").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.slrMJTot)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='slrMJTot')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='slrMJTot', type='log'))
        }, output_type='div')
    elif column_num == '6':
        for i in Record.objects.only("timeStamp", "wSMs").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.wSMs)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='wSMs')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='wSMs', type='log'))
        }, output_type='div')
    elif column_num == '7':
        for i in Record.objects.only("timeStamp", "windDir").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.windDir)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='markers', name='direction')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Wind Direction (Degrees)', type='log'))
        }, output_type='div')
    elif column_num == '8':
        for i in Record.objects.only("timeStamp", "pARTotTot").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.pARTotTot)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='pARTotTot')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='pARTotTot', type='log'))
        }, output_type='div')
    elif column_num == '9':
        for i in Record.objects.only("timeStamp", "bPMmHg").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.bPMmHg)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Pressure')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Barometric pressure (mmHg)', type='log'))
        }, output_type='div')
    elif column_num == '10':
        for i in Record.objects.only("timeStamp", "rainMmTot").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.rainMmTot)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='Rainfall')]
        file_str =offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='Rainfall (mm)', type='log'))
        }, output_type='div')
    elif column_num == '11':
        for i in Record.objects.only("timeStamp", "pARDen").filter(timeStamp__range=(startDate, endDate)):
            x.append(i.timeStamp)
            y.append(i.pARDen)

        df = pd.DataFrame({'x': x, 'y': y})
        df.head()

        data = [go.Scatter(x=df['x'], y=df['y'], mode='lines', name='pARDen')]
        file_str=offline.plot({
            'data': data,
            'layout': go.Layout(xaxis=go.XAxis(title='Date'), yaxis=go.YAxis(title='pARDen', type='log'))
        }, output_type='div')


    #returns string to be embeded
    return file_str


# for downloading csv file between two dates with all columns
def queryToCSV( startDate, endDate):

    filename ='WeatherStation_' + datetime.datetime.now().strftime('%Y_%m_%d__%H_%M') + '.csv'

    #hardcoded for testing
    #startDate = "2016-03-01 19:30:00"
    #endDate = "2016-03-03 08:30:00"

    # Evan's
    conn = sqlite3.connect('/home/evan/Documents/Capstone_randomFiles/CapstoneProject/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    # Cory's Desktop
    #conn = sqlite3.connect('/home/batman/Documents/CSUCI/Capstone/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    # Cory's Laptop
    # conn = sqlite3.connect('/home/batman/Documents/Project/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')

    #query database
    qr = pd.read_sql_query("SELECT * FROM WeatherStation_record WHERE timeStamp BETWEEN '" +
                           startDate + "' AND '" + endDate + "'", conn)

    fl = NamedTemporaryFile(suffix='.csv')
    qr.to_csv(fl.name)

    response = StreamingHttpResponse(streaming_content=fl.name, content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="' + filename + '"'
    return response


def downloadDbToCSV():

    # Evan's
    conn = sqlite3.connect('/home/evan/Documents/Capstone_randomFiles/CapstoneProject/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    # Cory's Desktop
    #conn = sqlite3.connect('/home/batman/Documents/CSUCI/Capstone/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')
    # Cory's Laptop
    # conn = sqlite3.connect('/home/batman/Documents/Project/Capstone_CoryGomez_EvanHauck/db.ESRM_Sierra')

    tbl = pd.read_sql_query("SELECT * FROM WeatherStation_record", conn)
    tbl.to_csv('WeatherStation_' + datetime.datetime.now().strftime('%Y_%m_%d') + '.csv')