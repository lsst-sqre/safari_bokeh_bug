
#safari_bokeh_bug

This example demonstrates a bug found on Safari>=10.1
dropping the web socket connection to the bokeh server.

To view the example, run:

    git clone  https://github.com/lsst-sqre/safari_bokeh_bug.git

    cd safari_bokeh_bug

    virtualenv env -p python3
    source env/bin/activate
    pip install -r requirements.txt

    bokeh serve safari_bokeh_bug.py

and navigate to:

    localhost:5006/safari_bokeh_bug