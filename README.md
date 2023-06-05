
* This code is Based on https://git.ligo.org/daniel.wysocki/bayesian-parametric-population-models/-/blob/master/src/pop_models/powerlaw/mcmc.py
* We modified this code to add the eccentircity parameter in the power law model.
* Example: You may want to look at the example of this code but without eccentricity paramter. https://gitlab.com/dwysocki/pop-models-examples

# How to run this code to get the population inference

* First, build the appropriate vt_m1_m2.hdf5
```
python vt.py 10 50 100 4 vt_m1_m2.hdf5
```
* First, you need a data containing three colums: m1_source , m2_source, ecc.
* You may make a fake data to check that if code actually works or not. For sample, fake.dat is given in repo.
* You can also generate a desired population by using the directory **population-genrator**. Please follow the steps written in README.md in that directory.
* Once you have the fake/synthetic/real data, you can tun this code as follows to get the parameters values.
* 
* Once you have the data and vt.hdf5 file, you can run the script **run-10-20-1000.sh**. By default in this script, we have set the number of input files = 10, number of walker for mcmc method equal to 20, and number of steps for each walker equal to 1000. But you may change these as you like in the script.
* The run time will take hours to days depends on data, walker, and steps.
* Once the run is done, you will get the myout.hdf5 file which will contain the PE for each parameters and you can make plots as you need for your analysis.

* Keep in mind that our power law model has the three random variables (m1,m2,ecc) which we provide to the model thorugh the real data or synthetic data.
* Then this model gives us the inference for the five paramters of the model : log rate, alpha, m_min, m_max, sigma_ecc.
* Lastly, if you want to run the code without eccentricity and want to comapre the results with and without ecccentricity, then you may go into the **original-pop-code** direcotry and run this code in the similar method defined above. But keep in mind that this code requires data without ecccentricity. You can get this data by just simly removing the eccentricity column in the used data. or you may use the scaling method in **pop-genrator** directory to get the scaled data without eccentricity.
