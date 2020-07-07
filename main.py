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
