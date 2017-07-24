# ir-plot

A Python script to plot infrared pulse/space data as logged by a tool like [mode2](http://www.lirc.org/html/mode2.html) from [LIRC](http://www.lirc.org/).

## Installation

Install `matplotlib` from your package manager and then clone this repository.

## Usage

ir-plot reads data from STDIN. So you should fist capture your desired data via `mode2` and then save it to a file.

`cat sample/tower | ./ir-plot`
