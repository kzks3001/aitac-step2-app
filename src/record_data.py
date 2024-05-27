import numpy as np
import random
import time

from orm.setting import session
from orm.model import Data
from datetime import datetime

tempreture_mean = 25
temperature_std_dev = 3

humid_mean = 50
humid_std_dev = 5

try:
    time.sleep(1)
    data = Data()
    data.create_data_record(
        date = datetime.now(),
        temperature = np.random.normal(loc=tempreture_mean, scale=temperature_std_dev),
        humid = np.random.normal(loc=humid_mean, scale=humid_std_dev),
        data1 = random.uniform(0, 500),
        data2 = random.uniform(0, 500),
        data3 = True
    )
    session.add(data)
    session.commit()
    print('コミットしたよ')
except Exception as e:
    raise(e)