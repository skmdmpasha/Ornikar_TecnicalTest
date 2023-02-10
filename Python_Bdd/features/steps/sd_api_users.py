# from __future__ import unicode_literals
from behave import *
import requests
from nose.tools import assert_equal
from pprint import pprint  # prettyprint


@When('I send a "{method}" request to "{endpoint}" by "{ID}"')
def step_impl(context, method, endpoint, ID):
    req_url = context.base_url + '/' + endpoint +  '/' + ID
    # context.r = requests.get(req_url, headers=context.headers)
    context.r = getattr(requests, method.lower())(req_url, headers=context.headers)
    print(f'\n\n {context.r.url} \n {context.r.text}')


@then("I want to print it")
def step_impl(context):
    print_star = ''.join('*' for i in range(len(context.base_url)))
    print(print_star)
    print(context.base_url)
    print(print_star)
    print(context.r.json())


@when('I send a "{method}" request to "{endpoint}" employee')
def request_step(context, method, endpoint):
    context.req_url = context.base_url + '/' + endpoint
    print(f"*______URI End point______: {context.req_url}\n")
    match method:
        case 'GET':
            context.r = requests.get(context.req_url)
        case 'POST'|'PUT':
            req_url = context.req_url
            payload = {}
            session = requests.Session()
            session.verify = False

            for row in context.table:
                req_url = req_url.replace('@ID', row['@ID']) if '@ID' in context.table.headings else req_url
                for x in context.table.headings:
                    if not x.startswith('@'):
                        payload[x] = row[x]
                        # req_url = req_url.replace('@ID', row['@ID'])

                context.r = getattr(requests, method.lower())(
                    req_url, headers=context.headers, data=payload)                    
                # context.r = requests.post(
                #     req_url, headers=context.headers, data=payload)

                print(f'\n\n {context.r.url} \n {payload} \n {context.r.text}')
                payload = {}
                req_url = context.req_url
        case 'DELETE':
            req_url = context.req_url
            # save in 'context' variable
            context.r = getattr(requests, method.lower())(
                req_url, headers=context.headers)
            print(f'\n {context.r.url} \n {context.r.json()}')
            print(f'\n {context.r.url} \n {context.r.text}')
