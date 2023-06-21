# F-Prediction

This project is focused on predicting a driver's likelihood of winning their forthcoming race in both Formula 1 and
Formula E.

## Data Sources

Data for this project will be collected from various sources.

### Official Websites:

- [Formula 1](https://www.formula1.com/)
- [Formula E](https://www.fiaformulae.com/)

### APIs:

- [Ergast MRD](http://ergast.com/mrd/): This API offers a historical record of motor racing data for non-commercial use,
  providing data for the Formula One series since its inception in 1950.

### Datasets:

- [Racing Reference Standings](https://www.racing-reference.info/standings/2022/F/)
- [Pitwall Races](https://pitwall.app/races)
- [Racing Statistics](https://www.racing-statistics.com/en/)

### Potential Additional Data Source:

- [Formula 1 Lap Charts](https://github.com/davidor/formula1-lap-charts)

## Data Processing

The data collected will undergo a series of processing steps: parsing, cleaning, and got processing, to create a predictive
model for Formula 1 and Formula E race outcomes. These steps will be executed for
each race.

## Factors Incorporated

The project intends to incorporate a comprehensive range of factors into the model, not only focusing on driver
performance data but also considering environmental variables. These include weather conditions (rain, snow, or sunny),
temperature, humidity, time of year, wind speed, light levels (morning, afternoon, evening, night), and track
conditions (poor, moderate, good). Furthermore, driver-specific data such as age, nationality, years of experience, past
teams, and win history will also be factored in.

## Prediction Goals

Currently, the project is considering two main avenues for predictive modeling:

1. Predicting a driver's likelihood of winning the upcoming or current race.
2. A more complex task of predicting the likelihood of a driver and which team will win a race.

The project's concept is still under development,, and the above goals might be refined or expanded upon as the
project progresses.

### Classification algorithm


----
* Criar um model com é sem grid

* Tem que fazer a transformações das categorias de position:
  * integer (finishing position)
  * “R” (retired)
  * “D” (disqualified)
  * “E” (excluded)
  * “W” (withdrawn)
  * “F” (failed to qualify)
  * “N” (not classified)

* parse miliseconds

### Columns

- num_of_podiums_in_circuit
- num_of_wins_in_circuit
- driver_made_fp ?
- 

Based on the date of each date calculate te cumulative, WIN,PODIUM,POLE,LAPS,LED,POINTS, RANK, AVST, AVFN, RAF, LLF, DNQ, WD.

Pole - Poles won (won in qualifying only)
Laps - Laps completed
Led - Laps led
Earnings - Total money won for the season (includes bonuses)
Rank - Points rank at the end of the season
AvSt - Average starting position
AvFn - Average finishing position
RAF - Number of times Running At Finish (DNFs = Races - RAF)
Miles - Miles raced
LLF - Lead lap finishes
DNQ - Races for which the driver Did Not Qualify
WD - Withdrew
