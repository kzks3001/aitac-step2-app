import requests
import json

import numpy as np
import random
import time
import logging

from datetime import datetime






url = "http://api-server:8081/register"
source = 'test'
cache_lim = 1000 # chacheの上限
time_sleep = 5 # [sec]
 
tempreture_mean = 25
temperature_std_dev = 3
humid_mean = 50
humid_std_dev = 5

cache_data = []
cnt = 0

def set_logger():

    logger = logging.getLogger('logger')
    logger.setLevel(logging.DEBUG)
    
    # コンソールハンドラーを作成
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    console_handler.setFormatter(formatter)
    
    logger.addHandler(console_handler)
    
    return logger

if __name__ == '__main__':
    logger = set_logger()

    while True:

        time.sleep(time_sleep)
        
        cnt += 1
        logger.info(f'\n{cnt} -------------------------------')
        
        data = {
                "date" : datetime.now().isoformat(),
                "temperature" : float(np.random.normal(loc=tempreture_mean, scale=temperature_std_dev)),
                "humid" : float(np.random.normal(loc=humid_mean, scale=humid_std_dev)),
                "source": source,
                "data1" : random.uniform(0, 500),
                "data2" :random.uniform(0, 500),
                "data3" : True
        }
        
        cache_data.append(data)
        if len(cache_data) > cache_lim:
            cache_data.pop(0)
        
        try:

            # dummy エラー 下1桁が5未満ならエラー発生
            if cnt % 10 < 5:
                raise Exception('dummy error')
            
            response = requests.post(
                url, 
                headers={'Content-Type': 'application/json'},
                data=json.dumps({"data_list": cache_data})
            )
            
            response.raise_for_status()

            logger.info('send success!')
            logger.info(f'send items: {len(cache_data)}')
            cache_data = []
        except requests.exceptions.HTTPError as e:
            logger.error('error!'+str(e))
            logger.error(f'current cache num: {len(cache_data)}')
        except Exception as e:
            logger.error('error!'+str(e))
            logger.error(f'current cache num: {len(cache_data)}')