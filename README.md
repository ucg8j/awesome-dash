# Awesome Dash  [![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)

[<img src="https://cdn.rawgit.com/plotly/dash-docs/b1178b4e/images/dash-logo-stripe.svg" align="right" width="250">](https://plot.ly/products/dash/)


A curated list of awesome Dash (plotly) resources

>[Dash](https://plot.ly/products/dash/) is a productive Python framework for building web applications.
Written on top of Flask, Plotly.js, and React.js, Dash is ideal for building data visualization apps with highly custom user interfaces in pure Python. It's particularly suited for anyone who works with data in Python.

## Contents ##
- [Tutorials](#tutorials)
- [Community](#community)
- [Talks](#talks)
- [Galleries](#galleries)
- [App Examples](#app-examples)
- [Component Libraries](#component-libraries)
- [Contributors](#contributors)

## Tutorials ##
- [Introducing Plotly Dash](https://medium.com/@plotlygraphs/introducing-dash-5ecf7191b503) - A high level introduction to Dash by Chris Parmer, the author of Dash. This essay was released as part of Dash's official launch (June 21, 2017).
- Plotly's tutorials on how to use Dash:
  - [Part 1: App Layout](https://plot.ly/dash/getting-started)
  - [Part 2: Interactivity](https://plot.ly/dash/getting-started-part-2)
  - [Part 3: Interactive Graphing](https://plot.ly/dash/interactive-graphing)
  - [Part 4: Callbacks With State](https://plot.ly/dash/state)
- [Interactive Web-Based Dashboards in Python](https://alysivji.github.io/reactive-dashboards-with-dash.html) - How the MVC model pertains to Dash and a walkthrough of building an app.
- [OPS CodeDay: Dash Plotly Map + Graph](https://radumas.info/blog/tutorial/2017/08/10/codeday.html) - How to use Jupyter notebooks in tandom with Dash to create mapping viz.
- [Creating Interactive Visualizations with Plotly’s Dash Framework](http://pbpython.com/plotly-dash-intro.html) - High level overview of how to get started with Dash.
- [Finding Bigfoot with Dash, Part 1](https://timothyrenner.github.io/datascience/2017/08/08/finding-bigfoot-with-dash-part-1.html) - Walkthrough of building a dashboard of Bigfoot sightings. [Part 2](https://timothyrenner.github.io/datascience/2017/08/09/finding-bigfoot-with-dash-part-2.html), [Part 3](https://timothyrenner.github.io/datascience/2017/08/10/finding-bigfoot-with-dash-part-3.html).
- [Visualize Earthquakes with Plotly Dash](https://www.giacomodebidda.com/visualize-earthquakes-with-plotly-dash/) - Environmental scan of alternatives to Dash followed with a tutorial.

## Community ##
- [Plotly hosted Question and Answer community](https://community.plot.ly)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/plotly-dash)

## Talks ##
- [Overview of Dash](https://www.youtube.com/watch?v=sea2K4AuPOk) - Chris Parmer, creator of Dash (SciPy 2017).
- [We're Launching Dash](https://www.youtube.com/watch?v=5BAthiN0htc&t=1s) - Chris Parmer, creator of Dash, speaking about the motivations behind Dash before it was launched (Plotcon NYC 2016).

## Galleries ##
- [Plotly App Gallery](https://plot.ly/dash/gallery) - Plotly's collection of Dash applications.
- [Dash Recipes Github](https://github.com/plotly/dash-recipes) - Collection of scripts and examples created while answering questions from the greater Dash community.

## App Examples ##
- [Oil and Gas Explorer](https://plot.ly/dash/gallery/new-york-oil-and-gas/) - Explore oil and gas production over time and with linked visualisations. [Source Code.](https://github.com/plotly/dash-oil-and-gas-demo)
- [Goldman Sachs Remake: Portfolio Report](https://plot.ly/dash/gallery/goldman-sachs-report/) - Recreates the look and feel of a Goldman Sachs report. Includes a 'print to PDF' button. [Source Code.](https://github.com/plotly/dash-goldman-sachs-report-demo)
- [Uber Rides](https://plot.ly/dash/gallery/uber-rides/) - Displays all of the Uber rides in New York City in 2014. Pandas on the backend filters a 0.5gig datafile. [Source Code.](https://github.com/plotly/dash-uber-rides-demo)
- [Simple Stock Tickers](https://plot.ly/dash/gallery/stock-tickers/) - Queries data from Google Finance and displays the results as candlestick charts. [Source Code.](https://github.com/plotly/dash-stock-tickers-demo-app)
- [Volatility Surface Explorer](https://plot.ly/dash/gallery/volatility-surface) - Fetches CBOE options chain data from Yahoo Finance with Pandas Datareader and calculates the implied volatility of each option visualised in a 3D mesh chart. [Source Code.](https://github.com/plotly/dash-volatility-surface)
- [Drug Discovery](https://plot.ly/dash/gallery/drug-explorer/) - Displays a description of the drug as you hover over points in the graph. [Source Code.](https://github.com/plotly/dash-drug-discovery-demo/)
- [Live Wind Streaming](https://plot.ly/dash/gallery/live-wind-data/) - Continually queries a SQL database and displays live charts of wind speed and wind direction. [Source Code.](https://github.com/plotly/dash-wind-streaming)
- [Recession in 255 Charts](https://plot.ly/dash/gallery/recession-report/) - Adapted from NYTimes's excellent [How the Recession Reshaped the Economy in 255 Charts](https://www.nytimes.com/interactive/2014/06/05/upshot/how-the-recession-reshaped-the-economy-in-255-charts.html). [Source Code.](https://github.com/plotly/dash-recession-report-demo)
- [3D Yield Curve](https://plot.ly/dash/gallery/yield-curve/) - Adapted from NYTimes's excellent [A 3-D View of a Chart That Predicts The Economic Future: The Yield Curve](https://www.nytimes.com/interactive/2015/03/19/upshot/3d-yield-curve-economic-growth.html). [Source Code.](https://github.com/plotly/dash-yield-curve)
- [Finding Bigfoot](https://bigfoot-sightings-dash.herokuapp.com/) - Several plots (including a map), a grid layout built with Bootstrap, interactions with an input field, and caching (See also [Tutorials](#tutorials)). [Source Code.](https://github.com/timothyrenner/bigfoot-dash-app)
- [Visualize Earthquakes with Plotly Dash](https://belle-croissant-54211.herokuapp.com/) - Great UI and usage of geospatial analytics with Dash. Includes [basic unit tests[(https://github.com/jackdbd/dash-earthquakes/tree/master/tests). [Source Code.](https://github.com/jackdbd/dash-earthquakes)
- [Street Quality IDentification [SQUID]](https://squid-syracuse.herokuapp.com/) - Highlights poor quality roads with maps, data table and photos of the offending piece of road. [Source Code.](https://github.com/amyoshino/SQUID-Syracuse-Dashboard)
- [VoxelViz](http://lukas-snoek.com/voxelviz) - Competition winning Visualization tool for (f)MRI data-sets. [Source Code.](https://github.com/lukassnoek/VoxelViz)
- [Traffic Accidents UK](https://traffic-accidents-uk.herokuapp.com/) - Explore the 140,008 traffic accidents in the UK in 2015. [Source Code.](https://github.com/richard-muir/uk-car-accidents)

## Component Libraries ##
- [Tutorial on creating custom Dash components with React.js](https://plot.ly/dash/plugins)
- [Dash Core Components](https://github.com/plotly/dash-core-components)
- [Dash HTML Components](https://github.com/plotly/dash-html-components)

## Contributors ##
- [Luke Singham](http://lukesingham.com/)
- [Aly Sivji](https://alysivji.github.io/)
- [Chris Parmer](https://github.com/chriddyp)
