

from flickr.crawler import flickrCrawler
from config import FLAGS




def getData():

    if FLAGS.name == 'FLICKR':
        
        crawler = flickrCrawler(FLAGS.tags, FLAGS.max_num, FLAGS.num_core)

        crawler.grabImages()



    else:
        return None




if __name__=='__main__':


    getData()


