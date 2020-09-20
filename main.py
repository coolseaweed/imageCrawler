#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## run
## > python main.py tag number_of_images_to_attempt_to_download extras
from flickrapi import FlickrAPI
import pandas as pd
import sys, os
import argparse
import multiprocessing as mp
import requests



FLAGS = None
key='941c8dfe45f2a1fef3aa2008604cba33'
secret='5258cb3a06d663c1'




def process(url,tag):
    try:
        resp = requests.get(url,stream=True)
        filename = os.path.basename(url)
        
        image_path = '../images/'+tag
        os.makedirs(image_path, exist_ok=True)
        #path_to_write=os.path.join(image_path,url.split("/")[-1])
        path_to_write=os.path.join(image_path,filename)
        outfile=open(path_to_write,'wb')
        outfile.write(resp.content)
        outfile.close()

    except:
        #print('[!] Error saving image', url)
        pass


    return {'file': filename, 'url': url}




n = 0
def call_back(x):
  global n, df

  if x is not False:
    df = df.append(x, ignore_index=True)

  n += 1
  sys.stdout.write('\r%s/%s' % (n, '?'))
  sys.stdout.flush()



if __name__=='__main__':

    cnt = 0
    results = []
    df = pd.DataFrame(columns=['file', 'url'])
    pool = mp.Pool(processes=mp.cpu_count())

    tag = sys.argv[1]
    MAX_NUM = int(sys.argv[2])

    # if sys.argv[3] is not None:
    #     extras = sys.argv[3]
    # else:
    #     extras = 'url_c'


    flickr = FlickrAPI(key, secret)
    photos = flickr.walk(
        text=tag,
        tag_mode='all',
        tags=tag,
        extras='url_c',
        per_page=50,
        sort='relevance'
    )


    for i, photo in enumerate(photos):
        if cnt > MAX_NUM:
            break
        
        url = photo.get('url_c')
        
        if url is None:
            continue
        
        result = pool.apply_async(process, (url,tag), callback=call_back)
        
        results.append(result)
        cnt += 1

    for r in results:
        r.wait()

    df.to_csv(os.path.join('../images',tag, 'metadata.csv'), index=False, header=False)

    print('saved %d images!' % len(df))

