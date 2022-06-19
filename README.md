# RedsTeam_AstroPi_2021_2022

*"Gravitation is not responsible for people falling in love"    -    Albert Einstein*

This is a collection of material used by our team to analyse data captured on the ISS during the AstroPi challenge 2021-2022 about the zero-gravity effect.

Through Pandas and MathPlotLib Python libraries, we analysed data we captured on the ISS on Monday 18 April 2022.

Our script edited a csv file with 50808 samples of the acceleration along the three-axis (see *RedsTeamDataLogSamplesOriginal.csv*).

Each sample consists of different data

1) date and time of capture

2) accelerometer value on axis x,y,z

3) Total g = vectorial sum of the 3 axis accelerations

4) ISS Elevation (Skyfield)

5) Mean Value of the previous 5 samples (except the first ones - buffer has to be filled by the first five samples); a value greater than this mean value triggers the fast mode sampling

6) Motion detection - PIR activations (true = activated; false = not activated); we can correlate a variation in the acceleration value with a human presence

7) Fast mode enable: if True the Fast mode sampling rate is on (1 sample every 80ms instead 240ms of normal mode)

8) fast mode counter: a counter for 4 seconds fast mode duration 



We analysed:

a) the acceleration profile (see AstropiAnalisys.ipynb and AstropiAnalisys.py)

b) the ISS Elevation profile through Skyfield tool (see ElevationProfile.ipynb and Elevation.py)

c) the PIR sensor activation (see MotionPlot.py)


As the point a), from all the samples, we isolated only the peaks in the intensity of the acceleration profile in order to study the cause of these peaks (vibrations, re,-boosting of the ISS and so on). Pandas library helped us to select the sample we need, i.e. the samples greater than the mean value of the acceleration profile.

We analysed the spikes in the acceleration value (see Astropi_RedsTeam_Data_Analysis.png):
a)	they are low in intensity and with a short duration, so they aren’t related with the ISS re-boosting;
b)	they aren’t correlated with the PIR sensor motion detection (no astronaut detected);
We suppose that they are little vibrations in the structure.




As the point b) we observed two complete revolution period of the ISS around the world; in the report we calculated the revolution period from the Universal Gravitation Law, verifing the result with ISS published data.


As the PIR sensor, we noticed frequent detections that can’t be comparable with human presence (they are short - max 320 ms). We suppose that there are some InfraRed sources in the module or some space particles that can activate it.











See below the objective of the experiment and the script structure we created.


## Python Script running on the ISS
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************
 
           --------------------------------------------------------------------------------    
           -                                                                              -
           -    RedsTeam Python Script for AstroPI Challenge - Life in Space 2021/2022    -
           -                                                                              -
           --------------------------------------------------------------------------------
 
          OBJECT OF THE EXPERIMENT 
 
          We want to study the acceleration profile in the ISS Columbus module
          during its free fall or its orbit adjustment, answering these questions:
          
            1) Is gravity acceleration equal to 0 in free fall or not?
 
            2) If gravity acceleration is equal to 0, how is it possible and why? We will
               analize the force diagram applying the third Newton Law (action and reaction)
               
            3) Try calculating the actual gravity acceleration at the ISS elevation and the
               speed of ISS throught Skyfield and the Universal Gravity Law (Newton);
 
            4) We expect a great variation of the g value if ISS orbit is corrected during 
               re boosting on higher orbit; in this case, if it happens, we will analize 
               and study this variation (stop of the free fall and altitude change)
 
            5) Detection of vibrations on ISS module by fast sample mode (if there is
               a derivative pattern on the module of gravity acceleration or there is 
               a motion detection in front of the RaspberyPi board, we start a fast 
               sampling mode.
 
          This script will help us to answer these questions sampling data from the 
          accelerometer on the SENSE HAT module.
 
------------------------------------------------------------------------------------------------------------
          SCRIPT DESCRIPTION
 
          1) File requirements and output:
 
             This script needs to iss.tle file and generates the RedsTeamDataLogSamples.csv file,
             that contains all the samples from the accelerometer and the events.log file
 
          2) Hardware requirements:
             accelerometer and IR sensor for motion detection
          
          3) Python structure:
             It is a single-thread script.
 
          4) The main loop consists of 3 parts:
 
            a)Initialization: the START... string is displayed for ten seconds;
 
            b)Main loop: for 2 hours and 57 minutes the core runs executing the main
              tasks, such as accelerometer sampling time with saving data and display
              update;
 
            c)Deinitialization: for 20 seconds the SHUTTING DOWN... string is displayed
              and then the Python script stops.
 
 
          As the b) point, we have organized it as following (measuring by the 
          oscilloscope, with two test points):
 
            1) A single main loop is 80 ms long;
 
            2) Every 240 ms we capture a single accelerometer data and we save it into
               the .csv file (in normal sample mode): it corresponds to a sample every
               4 main loops;
 
            3) If a motion detection is signaled by the IR sensor or there is a change 
               in the g value compared to the mean value of the last 5 samples of g
               a fast mode sampling of 80 ms is implemented: it corresponds to a sample 
               every a single main loop. If motion detection or vibrations conditions
               stops, fast sampling mode automatically stops after 4 seconds (50 main
               loops);
 
            4) The display update duration is only 2 ms long; on the led matrix a countdown 
               string is displayed with a scrolling red led cursor. We calculate the next 
               position draw without using the lib function in order to be more efficient
               and without using threads;
 
  
 
*************************************************************************************************************
*************************************************************************************************************
*************************************************************************************************************











RedsTeam - June 2022
