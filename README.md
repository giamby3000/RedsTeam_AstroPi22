# RedsTeam_AstroPi22

*"Gravitation is not responsible for people falling in love"        Albert Einstein*






This is a collection of material used by our team to analyse data captured on the ISS during the AstroPi challenge 2021-2022 about the zero-gravity effect.

Through Pandas and MathPlotLib Python libraries, we analysed data we captured on the ISS on Monday 18 April 2022.

Our script edited a csv file with 50808 samples of the acceleration along the three-axis.

We analysed:
a) the acceleration profile (see AstropiAnalisys.ipynb and AstropiAnalisys.py)
b) the ISS Elevation profile through Skyfield tool (see ElevationProfile.ipynb and Elevation.py)
c) the PIR sensor activation (see MotionPlot.py)

As the point a), from all the samples, we isolated only the peaks in the intensity of the acceleration profile in order to study the cause of these peaks (vibrations, re,-boosting of the ISS and so on).

As the point b) we observed two complete revolution period of the ISS around the world; in the report we calculated the revolution period from the Universal Gravitation Law, verifing the result with ISS published data.

As the PIR sensor, we observed many activations (please zoom the graph), but their reason aren't so clear, because analysing data we see short duration of these activations, uncorrelated with a human presence near the sensor.







RedsTeam
