import requests
import json
import argparse

bart_api_key = "&key=MW9S-E7SL-26DU-VV8V"
json_yes = "&json=y"

bart_urls = {
    'bsa': 'http://api.bart.gov/api/bsa.aspx?',
    'etd': 'http://api.bart.gov/api/etd.aspx?',
    'route': 'http://api.bart.gov/api/route.aspx?',
    'schedule': 'http://api.bart.gov/api/sched.aspx?',
    'stations': 'http://api.bart.gov/api/stn.aspx?',
    'version': 'http://api.bart.gov/api/version.aspx'
}

commands = {
    'bsa': ['help', 'bsa', 'count', 'elev'],
    'etd': ['help', 'etd'],
    'route': ['help', 'routeinfo', 'routes'],
    'schedule': ['help', 'arrive', 'depart', 'fare', 'holiday', 'routesched', 'scheds', 'special', 'stnsched'],
    'stations': ['help', 'stnaccess', 'stninfo', 'stns']
}


def parse_args():
    parser = argparse.ArgumentParser(
        description='BART API on command line!!',
        epilog='BART API - a free API giving BART train details!!',
        prog='bart.py'
    )

    parser.add_argument('--bsa', choices=commands['bsa'], help='bsa command')
    parser.add_argument('--etd', choices=commands['etd'], dest='etd', help='etc command')
    parser.add_argument('--origin', dest='origin', help='Origin Station Abbreviation')
    parser.add_argument('--dest', dest='dest', help='Destination Station Abbreviation')
    parser.add_argument('--route', choices=commands['route'], dest='route', help='route command')
    parser.add_argument(
        '--schedule', choices=commands['schedule'], dest='sched', help='sched command')
    parser.add_argument('--station', choices=commands['stations'], dest='stn', help='stn command')
    parser.add_argument('--version', dest='version', help='display BART API version info')
    args = parser.parse_args()
    return args


def listStns():
    r = requests.get(bart_urls['stations'] + "cmd=" +
                     commands['stations'][3] + bart_api_key + json_yes)
    stns = json.loads(r.text)
    for i in range(len(stns['root']['stations']['station'])):
        stn_name = stns['root']['stations']['station'][i]['name']
        stn_abbr = stns['root']['stations']['station'][i]['abbr']
        print("Station Name = ", stn_name, end=' ')
        print("\t AND \t Station Abbr = ", stn_abbr)


def etd(orig):
    origin = '&orig=' + orig
    r = requests.get(bart_urls['etd'] + "cmd=" + commands['etd']
                     [1] + origin + bart_api_key + json_yes)
    etd = json.loads(r.text)
    for i in range(len(etd['root']['station'][0]['etd'][0]['estimate'])):
        print("AT STATION " + orig + " - Train in = ",
              etd['root']['station'][0]['etd'][0]['estimate'][i]['minutes'], " Mins")


def bsa():
    r = requests.get(bart_urls['bsa'] + "cmd=" + commands['bsa'][1] + bart_api_key + json_yes)
    bsa = json.loads(r.text)
    print(bsa)


def train_count():
    r = requests.get(bart_urls['bsa'] + "cmd=" + commands['bsa'][2] + bart_api_key + json_yes)
    train_count = json.loads(r.text)
    print("Train Count = " + train_count['root']['traincount'])


def elev_maint():
    r = requests.get(bart_urls['bsa'] + "cmd=" + commands['bsa'][3] + bart_api_key + json_yes)
    elev_maint = json.loads(r.text)
    if len(elev_maint['root']['bsa']) > 0:
        for i in range(len(elev_maint['root']['bsa'])):
            print(elev_maint['root']['bsa'][i]['sms_text']['#cdata-section'])


if __name__ == "__main__":
    arguments = parse_args()
    if arguments.bsa:
        if arguments.bsa == 'bsa':
            bsa()
        elif arguments.bsa == 'count':
            train_count()
        elif arguments.bsa == 'elev':
            elev_maint()
    if arguments.etd:
        if arguments.etd == 'etd':
            if arguments.origin:
                etd(arguments.origin)
    if arguments.stn:
        if arguments.stn == 'stns':
            listStns()
