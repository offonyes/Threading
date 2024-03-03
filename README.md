# Multithreaded JSON Fetcher

## Description

This project demonstrates a multithreaded approach to efficiently fetch JSON data from an API using Python. It employs the PyQt5 library for the graphical user interface, requests library for making HTTP requests, and the json module for handling JSON data.

## Features

- **Multithreaded Fetching:** The application spawns multiple threads, each responsible for fetching JSON data for a specific object ID concurrently, enhancing performance.

- **Dynamic Resource Selection:** Users can dynamically select the resource to fetch data from using a dropdown menu, providing flexibility.

- **Thread Control:** Users can choose to enable or disable multithreading, allowing for experimentation with different fetching strategies.

- **Progress Tracking:** Although not implemented in the provided code, the application has the potential to include a progress bar to track the completion status of the fetching process.

## Prerequisites

- Python 3.x
- PyQt5
- requests

## Installation

1. Clone or download the project repository.
2. Install the required dependencies using the provided requirements.txt file:

```py
pip install -r requirements.txt
```
3. After installing the dependencies, run the run.py file to start the Figure calculator app.
```py
python run.py
```