'''
MIT License

Copyright (c) 2020 James Ma

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

import multiprocessing
import requests
import time
from links import links_to_views

def view( link, views ):
    print
    start_time = time.time()
    for i in range(views):
        r = requests.get(link)

    print ("     {} completed!".format(link))
    print ("     {} views in :".format(views))
    view_time = float(time.time() - start_time)
    print ("     Time      : " + " %s sec" % view_time)
    view_rate = float(views / view_time)
    print ("     View rate : " +  " %s views/sec" % view_rate)
    print ()

    # todo : proxy support

def intro( links_to_views_dict ):
    print ("\n --------------------------------------------")
    print (" viewbot v.2.0.0")
    print (" --------------------------------------------\n")
    # Listing the links and views
    print (" Links ({}) :\n".format(len(links_to_views_dict)))
    for link, views in links_to_views_dict.items():
        print(" - {} - {} views".format(link, views))

def view_all( links_to_views_dict ):
    print ("\n --------------------------------------------")
    print (" Watching ... ")
    print (" Do not close this window. \n")

    jobs = []

    # making the multiprocessing jobs
    for link, views in links_to_views_dict.items():
        jobs.append(multiprocessing.Process(target=view, args=(link, views, )))

    # doing the multiprocessing jobs
    start_time = time.time()
    for job in jobs:
        job.start()

    # wait for all jobs to finish
    for job in jobs:
        job.join()

    total_views = 0

    for views in links_to_views_dict.values():
        total_views += views

    print (" Tasks completed! ")
    total_view_time = float(time.time() - start_time)
    print (" Total time : " + " %s sec" % total_view_time)
    view_rate = float(total_views / total_view_time)
    print (" View rate  : " +  " %s views/sec" % view_rate)
    print
    print

if __name__ == '__main__':
  intro( links_to_views )
  view_all( links_to_views )
