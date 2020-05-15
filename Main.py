from Model import App
import argparse

ap = argparse.ArgumentParser()
ap.add_argument("-u", "--url", required=False,
	help="Input url that will be summarize")
args = vars(ap.parse_args())

url = 'https://en.wikipedia.org/wiki/Ice_cream'

if args['url']:
    url = args['url']

print(App.fit(url))