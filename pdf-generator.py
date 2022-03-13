from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image

#list fruits
fruit = {
    "elderberries": 1,
    "figs": 1,
    "apples": 2,
    "durians": 3,
    "bananas": 5,
    "cherries": 8,
    "grapes": 13
}

#generate pdf file
report = SimpleDocTemplate("./report.pdf")

#styling pdf
from reportlab.lib.styles import getSampleStyleSheet
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

#generate table from data
table_data = []
for key,value in fruit.items():
    table_data.append([key,value])

'''report_table = Table(data=table_data) -to make table only without styling-'''

#styling for table
from reportlab.lib import colors
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

#drawing pie chart
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie

report_pie = Pie(width=3, height=3)

'''need two separate lists: One for data, and one for labels. '''
report_pie.data = []
report_pie.labels = []
for fruit_name in sorted(fruit):
   report_pie.data.append(fruit[fruit_name])
   report_pie.labels.append(fruit_name)

report_chart = Drawing()
report_chart.add(report_pie)

#building pdf file
report.build([report_title, report_table, report_chart])