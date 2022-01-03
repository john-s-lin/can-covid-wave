# Waving Goodbye to Subsequent COVID-19 Waves

## Using data from the Government of Canada on daily cases and vaccination rate to model the end of the pandemic in Canada

**Disclaimer**: Please note that this project is for my personal learning and is just for fun. Although the data is publicly accessible, these analyses should **not** be used to guide real-world decisions. Models used an idealized input and are not adequate representations of human behaviour.

#### Update: 2022-01-03

Playing around with the [COVID-19 Outbreak Analysis](https://covidpredictions.mit.edu/) tool from MIT has allowed me to figure out that they implemented the dashboard using `plotly` and `dash`. Moreover, it seems like their prediction model stems from a mixture of multiple gaussians of different amplitudes summed together into one lineplot. If I were to implement a prediction model for Canada based on this, it would be _relatively_ simple to perform a fourier transform to decompose the waves into individual peaks. So let's set that as a first step and once we're there, we can think about adding complexity such as vaccination rate, mask mandates, lockdown measures, etc.

- [ ] Generate a dashboard for front-end interactive web app using `dash` using `plotly`

#### Update: 2021-12-07

**TODO**: A weaker model looks only at the shape of the curve to generate a forecast. I don't want to do that since pandemic wave modeling depends on a plethora of external factors such as vaccination rates, mask mandates, travel restrictions, distance learning, remote work, etc. The [COVID-19 Outbreak Analysis](https://covidpredictions.mit.edu/) from MIT acts as inspiration for this project.

After speaking to my Machine Learning professor, he recommended I do the following to get started before I make the leap to a real-world dataset.

- [ ] Make a synthetic dataset with a known function and sample from it to train prediction model as a sanity check
- [ ] Look into Facebook Prophet API for forecasting algorithms
- [ ] Look into other forecasting models done by other universities
