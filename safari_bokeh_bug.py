""" This example demonstrates a bug found on Safari>=10.1
dropping the web socket connection to the bokeh server.
"""

from bokeh.io import curdoc
from bokeh.models.widgets import Select, Div
from bokeh.layouts import column

# configure some bokeh widgets
select = Select(title="Options:", value="0", options=["0","1","2","3"])
label = Div(text="Selected option: 0")

# create a layout for this document
layout = column(select, label)
curdoc().add_root(layout)

# update the text label to the selected option
def update(attr, old, new):
    label.text = "Selected option: {}".format(new)

select.on_change("value", update)
