# plotly_pandas

Python package providing basic tools to create plotly charts from pandas DataFrames:
- thin wrapper around plotly library
- layout&column settings are passed as dictionary-based layout specs rather than plotly Graph Objects
- sequences of charts and dataframes/styled dataframes can be plotted together in tables using chart_table()

Refactor of code that originally needed some changes to plotly.py (no longer needed, so separate package now possible instead): https://github.com/hottwaj/plotly.py/

There is some overlap between this library and plotly-express, though the main job performed by this library is to translate DataFrame data to plotly data, and allow all styling to be done using dictionaries (plotly-js style), whereas plotly-express provides a wrapper around most styling operations.
