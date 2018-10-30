# Sportsplex Utilities

This repository provides a set of utlities to make life easier for hockey team managers at [Dulles Sportsplex](http://dullessportsplex.com/). You can run any of the available tools on the command line via
```bash
<tool-name> <tool-options>
```
All tools provide a help message that you can display via the `-h`, `--help` flags:
```bash
<tool-name> --help
```
See below for a list of all available tools.

## Installation
The easiest way to get access to these tools is via conda. 
### Conda
If you are not familiar with conda, or do not have it yet, download and install [Miniconda with Python 3 for your operating system](https://conda.io/miniconda.html). 

#### Linux/macOS
During the command line installation you can decide to add `/conda/installation/directory/bin` to your `PATH`. If you choose not to, make sure that conda is on your `PATH` before you install this package or run any of the tools.

#### Windows
For Windows users, a conda-specific *Anaconda Prompt* is provided that sets all required environment variables. You can start this prompt from the start menu.

### Sportsplex Utilities
After successful installation of conda, start a terminal (Linux/macOS) or the Anaconda Prompt (Windows). Install the sportsplex utilities by typing
```bash
conda install -c hanslovsky sportsplex-utilities
```

## Available Tools

### convert-schedule
`convert-schedule` extracts the schedule of a team from its website on the [Dulles Sportsplex website](https://dulles-sportsplex.com). It can print the schedule to standard out or write to a file (`--output`, `-o` flags). The `--benchapp`, `-b` flags convert the output into a [benchapp](https://benchapp.com) compatible csv format. You can export to google calendar from benchapp. Use the `--help`,`-h` flags to show a more detailed help message.

#### Usage example
As an example I extract the [May 2018 schedule for my silver team (Dulles Danglers)](https://dulles-sportsplex.ezleagues.ezfacility.com/teams/2201163/Dulles-Danglers.aspx) as benchapp csv:
```bash
convert-schedule --benchapp https://dulles-sportsplex.ezleagues.ezfacility.com/teams/2201163/Dulles-Danglers.aspx
```
Expected output:
```
Type,Game Type,Title,Home,Away,Date,Time
GAME,REGULAR,,Dulles Danglers,Unjust Guinjas,"Tue, May 1, 2018",00:00 AM
GAME,REGULAR,,Dulles Danglers,Flying Whales,"Tue, May 8, 2018",00:00 AM
GAME,REGULAR,,Dulles Danglers,Make Santa Jolly Again,"Tue, May 15, 2018",00:00 AM
GAME,REGULAR,,Dulles Danglers,Unjust Guinjas,"Tue, May 22, 2018",7:00 PM
GAME,REGULAR,,Dulles Danglers,Flying Whales,"Tue, May 29, 2018",11:00 PM
GAME,REGULAR,,Dulles Danglers,Make Santa Jolly Again,"Sun, Jun 3, 2018",3:00 PM
GAME,REGULAR,,Dulles Danglers,Unjust Guinjas,"Tue, Jun 5, 2018",8:00 PM
GAME,REGULAR,,Dulles Danglers,Flying Whales,"Tue, Jun 12, 2018",10:00 PM
GAME,REGULAR,,Dulles Danglers,Make Santa Jolly Again,"Tue, Jun 19, 2018",8:00 PM
GAME,REGULAR,,Dulles Danglers,Unjust Guinjas,"Sun, Jun 24, 2018",4:00 PM
GAME,REGULAR,,Dulles Danglers,Flying Whales,"Sun, Jul 1, 2018",6:00 PM
GAME,REGULAR,,Dulles Danglers,Make Santa Jolly Again,"Tue, Jul 10, 2018",7:00 PM
```

If you prefer to save the output in a file, run
```bash
convert-schedule --output=<output> --benchapp https://dulles-sportsplex.ezleagues.ezfacility.com/teams/2201163/Dulles-Danglers.aspx
```

Replace `<output>` with the path at which you would like to store your team's schedule, e.g. `stanley-cup-champions-schedule.csv`, `C:\Users\smooth-hands\schedule.csv` (Windows only), or `/home/hockey-gods/schedule.csv` (Linux/macOS only). You can then import the schedule into benchapp from the file located at `<output>`.
