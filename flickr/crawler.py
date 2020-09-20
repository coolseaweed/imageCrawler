

from flickrapi import FlickrAPI
import pandas as pd
import sys, os
import multiprocessing as mp
import requests



FLAGS = None
key='941c8dfe45f2a1fef3aa2008604cba33'
secret='5258cb3a06d663c1'



class flickrCrawler():

    def __init__(self, tags, max_num, num_core):
        
        self.tags = tags
        self.max_num = max_num
        self.num_core = num_core
        self.flickr = FlickrAPI(key, secret)
        
        print(f'Using flickr API\nTargets: {self.tags}\nMax num of image: {self.max_num}')



    def process(self, url, tag):

        try:
            resp = requests.get(url,stream=True)
            filename = os.path.basename(url)
            
            image_path = './images/'+tag
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



    def call_back(self, x):


      if x is not False:
        self.df = self.df.append(x, ignore_index=True)

      self.n += 1
      sys.stdout.write('\r%s/%s' % (self.n, '?'))
      sys.stdout.flush()


    def grabImages(self):


        for tag in self.tags:

            self.n = 0
            cnt = 0

            photos = self.flickr.walk(
                text=tag,
                tag_mode='all',
                tags=tag,
                extras='url_c',
                per_page=50,
                sort='relevance'
            )

            results = []
            self.df = pd.DataFrame(columns=['file', 'url'])

            pool = mp.Pool(processes=self.num_core)
            #pool = mp.Pool(processes=mp.cpu_count())


            for i, photo in enumerate(photos):

                if cnt > self.max_num: break
                
                url = photo.get('url_c')
                
                if url is None: continue
                
                result = pool.apply_async(self.process, (url,tag), callback=self.call_back)
                
                results.append(result)
                cnt += 1

            for r in results:
                r.wait()

            self.df.to_csv(os.path.join('./images',tag, 'metadata.csv'), index=False, header=False)

            print('saved %d images!' % len(self.df))


