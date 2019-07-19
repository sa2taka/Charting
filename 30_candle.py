import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pandas as pd
import requests
import json
import time
from datetime import datetime

from coin_info_loader import CoinInfoLoader

rate = CoinInfoLoader.rate()['data'][0]

rate_data_frame = pd.DataFrame({ 'ask': [float(rate['ask'])] ,
                                 'bid': [float(rate['bid'])] },
                                 [rate['timestamp']])

fig = plt.figure()
ax = plt.subplot()
ax.grid()
plt.tick_params()
plt.tight_layout()

while True:
    time.sleep(0.5)
    plt.cla()
    
    rate = CoinInfoLoader.rate()['data'][0]

    new_df = pd.DataFrame({ 'ask': [float(rate['ask'])] ,
                            'bid': [float(rate['bid'])] }, 
                          [rate['timestamp']])

    rate_data_frame = rate_data_frame.append(new_df)
    fig.autofmt_xdate() #x軸のオートフォーマット
    
    rate_data_frame.bid.plot()


ani = animation.FuncAnimation(fig, add_and_plot, interval=10, repeat=True)
plt.show()
