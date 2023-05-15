# Modeling COVID-19 Waves in Canada and Generating Predictions using FB Prophet

## Using data from the Government of Canada on daily cases and to model the end of the pandemic in Canada

### Data extraction and exploratory analysis

Data is extracted from Health Canada's website and explored in `src/exploration.ipynb`.

### Modeling

The data is modeled using Facebook's Prophet library in `src/model.ipynb`. The prediction plots are modeled with a `PERIOD = 30` days using `prophet`'s plotting function. As you can see, there's not much seasonality that can be modeled, since at the beginning of 2021 vaccines were made available in Canada.

![Predictions](/docs/assets/predict_plot.png)

### Next Steps and Further Questions

Using vaccination data, is it possible to finetune the models or would a more "complex" model be required to better predict COVID-19 cases in a longer time frame?

---

**Disclaimer**: Please note that this project is for my personal learning and is just for fun. Although the data is publicly accessible, these analyses should **not** be used to guide real-world decisions. Models used an idealized input and are not adequate representations of human behaviour.
