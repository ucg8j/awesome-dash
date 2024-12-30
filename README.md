# Awesome Dash [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

[<img src="logo.webp" align="right" width="250">](https://plot.ly/products/dash/)

A curated list of awesome Dash (plotly) resources

> [Dash](https://plot.ly/products/dash/) is a productive Python framework for building web applications.
> Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.

## Contents
- [Deployment](#deployment)
- [Tutorials](#tutorials)
- [Component Libraries](#component-libraries)
- [App Examples](#app-examples)
- [Idiomatic examples](#idiomatic-examples)
- [Galleries](#galleries)
- [Cheat sheets](#cheat-sheets)
- [Talks](#talks)
- [Books](#books)
- [Community](#community)
- [Contributors](#contributors)

## Deployment

- [Ploomber Cloud](https://ploomber.io) - The community plan allows free deployments

## Tutorials

- [Introducing Plotly Dash](https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503) - A high level introduction to Dash by Chris Parmer, the author of Dash. This essay was released as part of Dash's official launch (June 21, 2017).
- [Plotly's tutorials - Part 1: App Layout](https://dash.plotly.com/layout)
- [Plotly's tutorials - Part 2: Interactivity](https://dash.plotly.com/basic-callbacks)
- [Plotly's tutorials - Part 3: Interactive Graphing](https://dash.plotly.com/interactive-graphing)
- [Plotly's tutorials - Part 4: Callbacks With State](https://dash.plotly.com/sharing-data-between-callbacks)
- [Charming Data YouTube channel](https://www.youtube.com/charmingdata) - A channel dedicated to teaching Dash and Plotly with over 25k subscribers.
- [Interactive Web-Based Dashboards in Python](https://alysivji.github.io/reactive-dashboards-with-dash.html) - How the MVC model pertains to Dash and a walkthrough of building an app.
- [Using Plotly's Dash to deliver public sector decision support dashboards](https://medium.com/a-r-g-o/using-plotlys-dash-to-deliver-public-sector-decision-support-dashboards-ac863fa829fb) - Building a complex dashboard step-by-step.
- [OPS CodeDay: Dash Plotly Map + Graph](https://radumas.info/blog/tutorial/2017/08/10/codeday.html) - How to use Jupyter notebooks in tandom with Dash to create mapping viz.
- [Creating Interactive Visualizations with Plotly's Dash Framework](http://pbpython.com/plotly-dash-intro.html) - High level overview of how to get started with Dash.
- [ARGO Labs - Plotly Dash Tutorial (Video)](https://www.youtube.com/watch?v=yfWJXkySfe0) - Detailed introduction to creating interactive dashboards.
- [Data Visualization GUIs with Dash and Python (Video playlist)](https://www.youtube.com/watch?v=J_Cy_QjG6NE&list=PLQVvvaa0QuDfsGImWNt1eUEveHOepkjqt) - Five-part series exploring Dash features.
- [Interactive Visualization of Machine Learning and Computer Vision with Dash](https://www.youtube.com/watch?v=3F5AR-uUqJc) - Official introduction video.
- [Webinar: Converting React components to Dash components](https://www.youtube.com/watch?v=wifoPPRgG_I) - Official tutorial about how to convert React components to Dash components.
- [Interactive Image Processing with Dash-Canvas](https://www.youtube.com/watch?v=LKXSFBB5ccI) - Official introduction video to the Dash Canvas components.
- [Dash Cytoscape Component](https://www.youtube.com/watch?v=snXcIsCMQgk) - Official introduction video to the Dash Cytoscape components.
- [An introduction to Dash DataTable](https://www.youtube.com/watch?v=dueejcyrYh8) - Official introduction video to the Dash DataTable components.
- [Tutorial on creating custom Dash components with React.js.](https://dash.plotly.com/plugins)

## Component Libraries

- [Dash PDF](https://github.com/ploomber/dash-pdf) - Display inline PDFs
- [Dash MUI](https://github.com/ploomber/dash-mui) - Material UI components
- [Dash React Simple Maps](https://github.com/ploomber/dash-react-simple-maps) - Create interactive maps
- [Dash Mosaic](https://github.com/ploomber/mosaic-python#dash-mosaic) - Display [Mosaic](https://github.com/uwdata/mosaic) plots
- [Dash Tabler Icons](https://github.com/ploomber/dash-tabler-icons) - Beautiful icons for your Dash apps
- [Dash React Syntax Highlighter](https://github.com/ploomber/dash-react-syntax-highlighter) - Display code snippets with a copy button
- [Dash Canvas Components](https://dash.plotly.com/canvas) - Module for image annotation and image processing using 
Dash.
- [Awesome React Components](https://github.com/brillout/awesome-react-components) - Catalog of React.js components potentially interesting to be wrapped into Dash components.
- [Awesome React](https://github.com/enaqx/awesome-react) - Helpful resources for developing React.js components.
- [Dash Core Components](https://github.com/plotly/dash-core-components)
- [Dash Cytoscape Component](https://dash.plotly.com/cytoscape) - Graph visualization component for creating easily
customizable, high-performance, interactive, and web-based networks.
- [Dash DataTable Component](https://dash.plotly.com/datatable) - Interactive table that supports rich styling,
conditional formatting, editing, sorting, filtering, and more.
- [Dash DAQ Components](https://dash.plotly.com/dash-daq) - Set of controls that make it simpler to integrate data
acquisition and controls into your Dash applications.
- [Dash HTML Components](https://github.com/plotly/dash-html-components)
- [mydcc](https://github.com/jimmybow/mydcc) - Extension of Dash Core Components.
- [sd-material-ui](https://github.com/StratoDem/sd-material-ui) - StratoDem Analytics implementations of material-ui components for Dash.
- [sd-range-slider](https://github.com/StratoDem/sd-range-slider) - Range Slider Dash component.
- [dj-plotly-dash](https://github.com/pikhovkin/dj-plotly-dash) - Plotly Dash fork for Django.
- [dash-flexbox-grid](https://github.com/pikhovkin/dash-flexbox-grid) - Wrapper around react-flexbox-grid for Plotly Dash.
- [dash-color-picker](https://github.com/vivekvs1/dash-color-picker) - Wrapper around react-color.
- [dash-dual-listbox](https://github.com/vivekvs1/dash-dual-listbox) - Wrapper around react-duallist.
- [dash-bootstrap-components](https://dash-bootstrap-components.opensource.faculty.ai/) - Bootstrap components for Dash.
- [dash-uploader](https://github.com/np-8/dash-uploader) - Upload component for Dash. Supports large data files.
- [Dash Mantine Components](https://github.com/snehilvj/dash-mantine-components) - Collection of 40+ Dash components based on Mantine React Components library.
- [plotly-resampler](https://github.com/predict-idlab/plotly-resampler) - Wrapper for plotly figures that adds data downsampling (aggregating) functionality, enabling the visualization of large datasets.
- [dash-vega-components](https://github.com/altair-viz/dash-vega-components) - Dash component for Vega-Altair, Vega-Lite, and Vega charts.

## App Examples

- [Oil and Gas Explorer](https://dash.gallery/dash-oil-and-gas/) - Explore oil and gas production over time and with linked visualisations. [Source Code.](https://github.com/plotly/dash-oil-and-gas-demo)
- [Uber Rides](https://dash.gallery/dash-uber-rides-demo/) - Displays all of the Uber rides in New York City in 2014. Pandas on the backend filters a 0.5gig datafile. [Source Code.](https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-uber-rides-demo)
- [Drug Discovery](https://dash.gallery/dash-drug-discovery/) - Displays a description of the drug as you hover over points in the graph. [Source Code.](https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-drug-discovery)
- [Live Wind Streaming](https://dash.gallery/dash-wind-streaming/) - Continually queries a SQL database and displays live charts of wind speed and wind direction. [Source Code.](https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-wind-streaming)
- [3D Yield Curve](https://dash.gallery/dash-yield-curve/) - Adapted from NYTimes's excellent [A 3-D View of a Chart That Predicts The Economic Future: The Yield Curve](https://www.nytimes.com/interactive/2015/03/19/upshot/3d-yield-curve-economic-growth.html). [Source Code.](https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-yield-curve)
- [Visualize Earthquakes with Plotly Dash](https://dash-earthquakes-production-45eyyotfta-ey.a.run.app/) - Great UI and usage of geospatial analytics with Dash. Includes [basic unit tests](https://github.com/jackdbd/dash-earthquakes/tree/master/tests). [Source Code.](https://github.com/jackdbd/dash-earthquakes)
- [GutenSearch](https://gutensearch.com/) - Look inside the books of Project Gutenberg. [Source Code.](https://github.com/cordb/gutensearch)

## Idiomatic examples
- [Dash recipes](https://github.com/plotly/dash-recipes) - A collection of scripts and examples created of the plotly team while answering questions from the greater Dash community.

## Galleries
- [Dash Data Dashboards and Apps](https://www.dashboardom.com/) - Collection of data dashboards with real life data, for various topics, as well as a few apps for online marketing built with Dash.
- [Dash Gallery](https://dash.gallery/) - A collection of Dash apps.

## Talks
- [Dash: Data exploration web apps in pure Python](https://www.youtube.com/watch?v=eusglTlW4OA) - Chelsea Douglas, PyData DC 2018.
- [Overview of Dash](https://www.youtube.com/watch?v=sea2K4AuPOk) - Chris Parmer, creator of Dash (SciPy 2017).
- [We're Launching Dash](https://www.youtube.com/watch?v=5BAthiN0htc&t=1s) - Chris Parmer, creator of Dash, speaking about the motivations behind Dash before it was launched (Plotcon NYC 2016).
- [Plotly dash and data visualisation in Python, PyData, Berlin 2017](https://www.slideshare.net/vladimirkazantsev/plotly-dash-and-data-visualisation-in-python) - Volodymyr Kazantsev (slides only).

## Cheat sheets
- [plotly.py Cheat Sheet](https://images.plot.ly/plotly-documentation/images/python_cheat_sheet.pdf)

## Community
- [Plotly hosted Question and Answer community](https://community.plot.ly)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/plotly-dash)

## Contributors
- [Luke Singham](https://lukesingham.com/)
- [Aly Sivji](https://alysivji.github.io/)
- [Chris Parmer](https://github.com/chriddyp)
- [Sergey Pikhovkin](https://github.com/pikhovkin)
- [Pascal Bugnion](https://pascalbugnion.net)
- [Florian Kromer](https://github.com/fkromer)
- [Elias Dabbas](https://www.dashboardom.com)
- [vaexio](https://github.com/vaexio)
- [Fanchao MENG](https://github.com/pingf)
- [Snehil Vijay](https://github.com/snehilvj)
- [Eduardo Blancas](https://github.com/edublancas)

## License
This work is licensed under a Creative Commons Attribution 4.0 International License.
