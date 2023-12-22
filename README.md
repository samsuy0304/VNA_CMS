# VNA Data Visualization: CMS Differeantial Pair Cables

This repository contains Python code designed to read and visualize data acquired from Vector Network Analyzers (VNAs) during quality and reliability testing of multi-channel differential pair cables utilized in the CMS (Compact Muon Solenoid) upgrade.

## Purpose
The primary objective of this repository is to analyze, visualize, and assess the quality and reliability of differential pair cables. The VNA data obtained through testing these cables provides valuable insights into their performance characteristics across various frequencies, aiding in determining their suitability for the CMS upgrade project.


## Visualizations
The generated plots from the VNA data include insights into the differential pair cables' performance such as:

* Frequency Domain Analysis
* Time Domain Analysis
* Smith charts
* Impedance Parameters


## Dependencies
Ensure the following libraries are installed:
* `numpy`
* `matplotlib`
* `scikit-rf`


## Usage
### Data Preparation:
Place the VNA data files under Data/_Cable_ID_.

### Visualization:
Execut `main.py`. When working with data from a new cable, make sure to enter all the prompted information. This information will be shelved.

Visualizations depicting cable characteristics and performance will be saved in the Data/_Cable_ID_/plots directory.

