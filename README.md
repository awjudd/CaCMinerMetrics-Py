# CaCMinerMetrics

## Notes
This is still in active development. For any issues or feature requests, please open an issue on the repo and it will be evaluated.

## Pre-Requisites
- Python 3.9.2+
- Selenium
- Gecko Driver installed and accessible in path

## CloudAtCocks Website
Some turds on the internet created a website to track cost over time for CaC miners historically. As part of this, a function was created to automatically post to their website form for tracking purposes. If you want to do this you will need to visit https://mining.cloudatcocks.com/ and create an account. You will then need to create your miners prior to running this script. Fill in the necessary information in the config.json file and flip the field to enabled. After this, every time this script runs, you will post your output to their form for tracking.
