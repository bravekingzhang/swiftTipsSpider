# -*- coding: utf-8 -*-
import json


class MoveOutputer:
    def __init__(self):
        self.contents = []
        pass

    def collect_data(self, content):
        if content is not None:
            self.contents.append(content)

    def out_put_data(self):
        with open('data.json', 'w') as outfile:
            json.dump(self.contents[0], outfile)
