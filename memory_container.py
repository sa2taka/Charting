from container import Container
from pandas import DataFrame

class MemoryContainer(Container):
    _data = DataFrame()

    # classmethodなpropertyが面倒なやり方でしか実装できなかったため
    @classmethod
    def get_data(self):
        return self._data

    @classmethod
    def append(self, item):
        new_df = DataFrame({ 'ask': [float(item['ask'])] ,
                             'bid': [float(item['bid'])] }, 
                             [item['timestamp']])

        self._data = self._data.append(new_df)
