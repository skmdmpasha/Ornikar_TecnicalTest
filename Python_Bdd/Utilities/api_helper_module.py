import logging
from Utilities.LogUtil import Logger
from Utilities.behave_rest import *
import time
import requests

payloadDict = {}
# log = Logger(__name__, logging.INFO)


class Request(object):
    def __init__(self):
        pass

    def send(context, method='', endpoint='', payload=''):
        context.r = getattr(requests, method.lower())(
            endpoint, headers=context.headers, data=payload)
        Request.print_status(context, payload)
        if context.r.status_code == 429:
            print(
                f'\n Too Many Requests, Please Wait ... "{context.r.headers["Retry-After"]}" seconds')
            time.sleep(int(context.r.headers["Retry-After"]))
            context.r = getattr(requests, method.lower())(
                endpoint, headers=context.headers, data=payload)
            Request.print_status(context, payload)

    def create_payload_from_table(context, req_url):
        tempUrl = req_url
        payload = {}
        payloadList = []
        tempList = []
        session = requests.Session()
        session.verify = False
        for row in context.table:
            tempUrl = req_url.replace(
                '@ID', row['@ID']) if '@ID' in context.table.headings else req_url
            tempList.append(tempUrl)
            for x in context.table.headings:
                if not x.startswith('@'):
                    payload[x] = row[x]
            tempList.append(payload.copy())
            payloadList.append(tempList)
            tempList = []
            # print(context.active_outline[0])
            if context.scenario.keyword == 'Scenario Outline':
                key = context.active_outline[0]
                if key not in payloadDict:
                    if len(payloadDict) > 0:
                        tempDict = payloadDict.copy()
                        for k, v in tempDict.items():
                            if tempDict[k] != payload.copy() and \
                                    (payload.copy() not in tempDict.values()):
                                payloadDict[key] = payload.copy()
                    else:
                        payloadDict[key] = payload.copy()
        return payloadList, payloadDict

    def func_ScenarioOutline(payloadList, payloadDict):
        tempDict = payloadDict.copy()
        for k, v in tempDict.items():
            payload = v
        return payload

    def print_status(context, payload={}):
        if context.r.status_code == 200:
            # print(f'\n\n {context.r.url} \n {payload} \n {context.r.text}')
            # print(f'\n\n {context.r.url} \n {payload} \n {context.r.json()}')
            log_full(context.r)


class ListIterator:
    def __init__(self, ls):
        self.ls = ls
        self.idx = 0

    def __iter__(self):
        return self

    def rewind(self):
        self.idx = 0

    def __next__(self):
        try:
            return self.ls[self.idx]
        except IndexError:
            raise StopIteration
        finally:
            self.idx += 1

# class Request(object):

#     def send(context, method='', endpoint='', payload=''):
#         context.r = getattr(requests, method.lower())(
#             endpoint, headers=context.headers, data=payload)
#         if context.r.status_code == 429:
#             print(
#                 f'\n Too Many Requests, Please Wait ... "{context.r.headers["Retry-After"]}" seconds')
#             time.sleep(int(context.r.headers["Retry-After"]))
#             context.r = getattr(requests, method.lower())(
#                 endpoint, headers=context.headers, data=payload)

#     def get_table_payload(context, req_url):
#         tempUrl = req_url
#         payload = {}
#         payloadList = []
#         tempList = []
#         session = requests.Session()
#         session.verify = False
#         for row in context.table:
#             tempUrl = req_url.replace(
#                 '@ID', row['@ID']) if '@ID' in context.table.headings else req_url
#             tempList.append(tempUrl)
#             for x in context.table.headings:
#                 if not x.startswith('@'):
#                     payload[x] = row[x]
#             tempList.append(payload.copy())
#             payloadList.append(tempList)
#             tempList = []
#         return payloadList

#     def print_status(context, payload=''):
#         if context.r.status_code == 200:
#             # print(f'\n\n {context.r.url} \n {payload} \n {context.r.text}')
#             print(
#                 f'\n\n {context.r.url} \n {payload} \n {context.r.json()}')
#             payload = {}



