#!/usr/bin/env python3
#
# author: Philipp Hanslovsky

import argparse
from bs4 import BeautifulSoup
import csv
import datetime
import requests
import sys

table_id            = 'ctl00_C_Schedule1_GridView1'
header_style        = 'HeaderStyle'
row_style           = 'RowStyle'
alternate_row_style = 'AlternateRowStyle'

benchapp_headers = ('Type','Game Type','Title','Home','Away','Date','Time')

def write_csv(header, rows, out_fd, delimiter=',',quotechar='"'):
    writer = csv.writer(out_fd, delimiter=delimiter, quotechar=quotechar, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(header)
    writer.writerows(rows)

def print_as_csv(header, rows):
    out_fd = sys.stdout
    write_csv(header, rows, out_fd)

def to_benchapp(dictionaries):
    rows = []
    for d in dictionaries:
        row = ('GAME', d['Game Type'].upper(), '', d['Home'], d['Away'], get_date(d['Date']), complete_as_midnight(d['Time/Status']))
        rows += [row]

    return rows

def get_date(dulles_date):
    now = datetime.datetime.now()
    return dulles_date.replace('-', ', ') + ', %d' % now.year

def complete_as_midnight(status):
    return '00:00 AM' if status.lower() == 'complete' else status

def to_dictionaries(header, rows):
    return tuple(
        {h:r for (h, r) in zip(header, row)} for row in rows
        )

if __name__ == '__main__':
    example_url = 'https://dulles-sportsplex.ezleagues.ezfacility.com/teams/2201163/Dulles-Danglers.aspx'

    parser = argparse.ArgumentParser()
    parser.add_argument('URL',                              help="URL to your team's schedule, e.g. {}.".format(example_url))
    parser.add_argument('--output',   '-o', required=False, help='If specified, write output to file instead of std out.', default=None)
    parser.add_argument('--benchapp', '-b', required=False, help='Convert to benchapp style csv', action='store_true')
    arguments = parser.parse_args()

    r       = requests.get(arguments.URL)
    data    =  r.text
    soup    = BeautifulSoup(data, 'html.parser')
    table   = soup.find('table', {'id': table_id})
    header  = table.find('tr', {'class': header_style})
    headers = tuple(h.get_text(strip=True) for h in header.findAll('th'))
    rows    = table.findAll('tr', {'class':[row_style, alternate_row_style]})

    empty_headers_indices = [i for (i, h) in enumerate(headers) if h == '']

    entries = tuple(
        tuple(r.get_text(strip=True) for r in row.findAll('td'))
        for index, row in enumerate(rows) )

    if arguments.benchapp:
        entries = to_benchapp(to_dictionaries(headers, entries))
        headers = benchapp_headers

    if arguments.output:
        with open(arguments.output, 'w') as f:
            write_csv(headers, entries, f)
    else:
        print_as_csv(headers, entries)

