# Awesome Dash  [![Awesome](https://awesome.re/badge-flat.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://cdn.rawgit.com/plotly/dash-docs/b1178b4e/images/dash-logo-stripe.svg" align="right" width="250">](https://plot.ly/products/dash/)


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
- [Plotly's tutorials - Part 1: App Layout](https://plot.ly/dash/getting-started)
- [Plotly's tutorials - Part 2: Interactivity](https://plot.ly/dash/getting-started-part-2)
- [Plotly's tutorials - Part 3: Interactive Graphing](https://plot.ly/dash/interactive-graphing)
- [Plotly's tutorials - Part 4: Callbacks With State](https://plot.ly/dash/state)
- [Charming Data YouTube channel](https://www.youtube.com/charmingdata) - A channel dedicated to teaching Dash and Plotly with over 25k subscribers.
- [Interactive Web-Based Dashboards in Python](https://alysivji.github.io/reactive-dashboards-with-dash.html) - How the MVC model pertains to Dash and a walkthrough of building an app.
- [Using Plotly’s Dash to deliver public sector decision support dashboards](https://medium.com/a-r-g-o/using-plotlys-dash-to-deliver-public-sector-decision-support-dashboards-ac863fa829fb) - Buiding a complex dashboard step-by-step.
- [OPS CodeDay: Dash Plotly Map + Graph](https://radumas.info/blog/tutorial/2017/08/10/codeday.html) - How to use Jupyter notebooks in tandom with Dash to create mapping viz.
- [Creating Interactive Visualizations with Plotly’s Dash Framework](http://pbpython.com/plotly-dash-intro.html) - High level overview of how to get started with Dash.
- [Finding Bigfoot with Dash, Part 1](https://timothyrenner.github.io/posts/bigfoot-with-dash-part-1/) - Walkthrough of building a dashboard of Bigfoot sightings. [Part 2](https://timothyrenner.github.io/posts/bigfoot-with-dash-part-2), [Part 3](https://timothyrenner.github.io/posts/bigfoot-with-dash-part-3/).
- [Visualize Earthquakes with Plotly Dash](https://www.giacomodebidda.com/visualize-earthquakes-with-plotly-dash/) - Environmental scan of alternatives to Dash followed with a tutorial.
- [ARGO Labs - Plotly Dash Tutorial (Video)](https://www.youtube.com/watch?v=yfWJXkySfe0) - Detailed introduction to creating interactive dashboards.
- [Data Visualization GUIs with Dash and Python (Video playlist)](https://www.youtube.com/watch?v=J_Cy_QjG6NE&list=PLQVvvaa0QuDfsGImWNt1eUEveHOepkjqt) - Five-part series exploring Dash features.
- [Interactive Visualization of Machine Learning and Computer Vision with Dash](https://www.youtube.com/watch?v=3F5AR-uUqJc) - Official introduction video.
- [Webinar: Converting React components to Dash components](https://www.youtube.com/watch?v=wifoPPRgG_I) - Official tutorial about how to convert React components to Dash components using the Dash Component Boilerplate cookiecutter template.
- [Interactive Image Processing with Dash-Canvas](https://www.youtube.com/watch?v=LKXSFBB5ccI) - Official introduction video to the Dash Canvas components.
- [Dash Cytoscape Component](https://www.youtube.com/watch?v=snXcIsCMQgk) - Official introduction video to the Dash Cytoscape components.
- [An introduction to Dash DataTable](https://www.youtube.com/watch?v=dueejcyrYh8) - Official introduction video to the Dash DataTable components.

## Component Libraries

- [Dash PDF](https://github.com/ploomber/dash-pdf) - Display inline PDFs
- [Dash MUI](https://github.com/ploomber/dash-mui) - Material UI components
- [Dash React Simple Maps](https://github.com/ploomber/dash-react-simple-maps) - Create interactive maps
- [Dash Mosaic](https://github.com/ploomber/mosaic-python#dash-mosaic) - Display [Mosaic](https://github.com/uwdata/mosaic) plots
- [Dash Tabler Icons](https://github.com/ploomber/dash-tabler-icons) - Beautiful icons for your Dash apps
- [Dash React Syntax Highlighter](https://github.com/ploomber/dash-react-syntax-highlighter) - Display code snippets with a copy button
- [Tutorial on creating custom Dash components with React.js.](https://plot.ly/dash/plugins)
- [Dash Bio Components](https://dash.plot.ly/dash-bio) - Suite of bioinformatics components that make it simpler to analyze and visualize bioinformatics data and interact with them in a Dash application.
- [Dash Canvas Components](https://dash.plot.ly/canvas) - Module for image annotation and image processing using Dash.
- [Awesome React Components](https://github.com/brillout/awesome-react-components) - Catalog of React.js components potentially interesting to be wrapped into Dash components.
- [Awesome React](https://github.com/enaqx/awesome-react) - Helpful resources for developing React.js components.
- [Dash Core Components](https://github.com/plotly/dash-core-components)
- [Dash Cytoscape Component](https://dash.plot.ly/cytoscape) - Graph visualization component for creating easily customizable, high-performance, interactive, and web-based networks.
- [Dash DataTable Component](https://dash.plot.ly/datatable) - Interactive table that supports rich styling, conditional formatting, editing, sorting, filtering, and more.
- [Dash DAQ Components](https://dash.plot.ly/dash-daq) - Set of controls that make it simpler to integrate data acquisition and controls into your Dash applications.
- [Dash ECharts Components](https://github.com/mergeforward/dash_echarts) - ECharts(V5) Components for Dash.
- [Dash HTML Components](https://github.com/plotly/dash-html-components)
- [mydcc](https://github.com/jimmybow/mydcc) - Extension of Dash Core Components.
- [sd-material-ui](https://github.com/StratoDem/sd-material-ui) - StratoDem Analytics implementations of material-ui components for Dash.
- [sd-range-slider](https://github.com/StratoDem/sd-range-slider) - Range Slider Dash component.
- [dj-plotly-dash](https://github.com/pikhovkin/dj-plotly-dash) - Plotly Dash fork for Django.
- [dash-flexbox-grid](https://github.com/pikhovkin/dash-flexbox-grid) - Wrapper around react-flexbox-grid for Plotly Dash.
- [dash-color-picker](https://github.com/vivekvs1/dash-color-picker) - Wrapper around react-color.
- [dash-dual-listbox](https://github.com/vivekvs1/dash-dual-listbox) - Wrapper around react-duallist.
- [dash-bootstrap-components](https://dash-bootstrap-components.opensource.asidatascience.com/) - Layout engine, default styles and high-level components based on Bootstrap.
- [dash-uploader](https://github.com/np-8/dash-uploader) - Upload component for Dash. Supports large data files.
- [Dash Mantine Components](https://github.com/snehilvj/dash-mantine-components) - Collection of 40+ Dash components based on Mantine React Components library.
- [plotly-resampler](https://github.com/predict-idlab/plotly-resampler) - Wrapper for plotly figures that adds data downsampling (aggregating) functionality, enabling the visualization of large datasets.
- [dash-vega-components](https://github.com/altair-viz/dash-vega-components) - Dash component for Vega-Altair, Vega-Lite, and Vega charts.

## App Examples
- [Oil and Gas Explorer](https://plot.ly/dash/gallery/new-york-oil-and-gas/) - Explore oil and gas production over time and with linked visualisations. [Source Code.](https://github.com/plotly/dash-oil-and-gas-demo)
- [Uber Rides](https://plot.ly/dash/gallery/uber-rides/) - Displays all of the Uber rides in New York City in 2014. Pandas on the backend filters a 0.5gig datafile. [Source Code.](https://github.com/plotly/dash-uber-rides-demo)
- [Simple Stock Tickers](https://plot.ly/dash/gallery/stock-tickers/) - Queries data from Google Finance and displays the results as candlestick charts. [Source Code.](https://github.com/plotly/dash-stock-tickers-demo-app)
- [Volatility Surface Explorer](https://plot.ly/dash/gallery/volatility-surface) - Fetches CBOE options chain data from Yahoo Finance with Pandas Datareader and calculates the implied volatility of each option visualised in a 3D mesh chart. [Source Code.](https://github.com/plotly/dash-volatility-surface)
- [Drug Discovery](https://plot.ly/dash/gallery/drug-explorer/) - Displays a description of the drug as you hover over points in the graph. [Source Code.](https://github.com/plotly/dash-drug-discovery-demo/)
- [Live Wind Streaming](https://plot.ly/dash/gallery/live-wind-data/) - Continually queries a SQL database and displays live charts of wind speed and wind direction. [Source Code.](https://github.com/plotly/dash-sample-apps/tree/main/apps/dash-wind-streaming)
- [Recession in 255 Charts](https://plot.ly/dash/gallery/recession-report/) - Adapted from NYTimes's excellent [How the Recession Reshaped the Economy in 255 Charts](https://www.nytimes.com/interactive/2014/06/05/upshot/how-the-recession-reshaped-the-economy-in-255-charts.html). [Source Code.](https://github.com/plotly/dash-recession-report-demo)
- [3D Yield Curve](https://plot.ly/dash/gallery/yield-curve/) - Adapted from NYTimes's excellent [A 3-D View of a Chart That Predicts The Economic Future: The Yield Curve](https://www.nytimes.com/interactive/2015/03/19/upshot/3d-yield-curve-economic-growth.html). [Source Code.](https://github.com/plotly/dash-yield-curve)
- [Finding Bigfoot](https://bigfoot-sightings-dash.herokuapp.com/) - Several plots (including a map), a grid layout built with Bootstrap, interactions with an input field, and caching (See also [Tutorials](#tutorials)). [Source Code.](https://github.com/timothyrenner/bigfoot-dash-app)
- [Visualize Earthquakes with Plotly Dash](https://belle-croissant-54211.herokuapp.com/) - Great UI and usage of geospatial analytics with Dash. Includes [basic unit tests](https://github.com/jackdbd/dash-earthquakes/tree/master/tests). [Source Code.](https://github.com/jackdbd/dash-earthquakes)
- [Street Quality IDentification [SQUID]](https://squid-syracuse.herokuapp.com/) - Highlights poor quality roads with maps, data table and photos of the offending piece of road. [Source Code.](https://github.com/amyoshino/SQUID-Syracuse-Dashboard)
- [VoxelViz](http://lukas-snoek.com/voxelviz) - Competition winning Visualization tool for (f)MRI data-sets. [Source Code.](https://github.com/lukassnoek/VoxelViz)
- [Traffic Accidents UK](https://traffic-accidents-uk.herokuapp.com/) - Explore the 140,008 traffic accidents in the UK in 2015. [Source Code.](https://github.com/richard-muir/uk-car-accidents)
- [New York Taxi Rides](https://dash.vaex.io/) - A full year of the YellowCab Taxi company data from their prime, numbering well over 100 million trips. Dash + Vaex dataframe with over a 100 million rows. [Source Code.](https://github.com/vaexio/dash-120million-taxi-app)
- [GutenSearch](https://gutensearch.com/) - Look inside the books of Project Gutenberg. [Source Code.](https://github.com/cordb/gutensearch)

## Idiomatic examples
- [Dash recipes](https://github.com/plotly/dash-recipes) - A collection of scripts and examples created of the plotly team while answering questions from the greater Dash community.

## Galleries
- [Plotly App Gallery](https://plot.ly/dash/gallery) - Plotly's collection of Dash applications.
- [Dash Recipes GitHub](https://github.com/plotly/dash-recipes) - Collection of scripts and examples created while answering questions from the greater Dash community.
- [Dash Data Dashboards and Apps](https://www.dashboardom.com/) - Collection of data dashboards with real life data, for various topics, as well as a few apps for online marketing built with Dash.

## Talks
- [Dash: Data exploration web apps in pure Python](https://www.youtube.com/watch?v=eusglTlW4OA) - Chelsea Douglas, PyData DC 2018.
- [Overview of Dash](https://www.youtube.com/watch?v=sea2K4AuPOk) - Chris Parmer, creator of Dash (SciPy 2017).
- [We're Launching Dash](https://www.youtube.com/watch?v=5BAthiN0htc&t=1s) - Chris Parmer, creator of Dash, speaking about the motivations behind Dash before it was launched (Plotcon NYC 2016).
- [Plotly dash and data visualisation in Python, PyData, Berlin 2017](https://www.slideshare.net/vladimirkazantsev/plotly-dash-and-data-visualisation-in-python) - Volodymyr Kazantsev (slides only).

## Books
- [Interactive Dashboards and Data Apps with Plotly and Dash](https://www.amazon.com/Interactive-Dashboards-Data-Apps-Plotly-ebook/dp/B08XMW45VY): Harness the power of a fully fledged frontend web framework in Python – no JavaScript required.

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
[![CC0](http://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)<br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 International License</a>.
