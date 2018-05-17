#!/usr/bin/env python3
#
# author: Philipp Hanslovsky

import argparse
from bs4 import BeautifulSoup
import csv
import datetime
import requests
import sys

from . import convert_schedule

if __name__ == "__main__":
    convert_schedule.main()
