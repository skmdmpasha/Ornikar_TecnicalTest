from Utilities.api_helper_module import Request
from Utilities.behave_rest import *
from behave import *


@then("I want to print it")
def step_impl(context):
    print_star = ''.join('*' for i in range(len(context.base_url)))
    print(print_star)
    print(context.base_url)
    print(print_star)
    print(context.r.json())


@step('I send a "{method}" request to "{endpoint}" employee')
def request_step(context, method, endpoint):
    req_url = context.base_url + '/' + endpoint
    if bool(context.table):
        payloadList, payloadDict = Request.create_payload_from_table(
            context, req_url)
        if context.scenario.keyword == 'Scenario Outline':
            payload = Request.func_ScenarioOutline(payloadList, payloadDict)
            kwargs = {"method": method,
                      "endpoint": req_url, "payload": payload}
            Request.send(context, **kwargs)
        else:
            for p in payloadList:
                req_url = p[0]
                payload = p[1]
                kwargs = {"method": method,
                          "endpoint": req_url, "payload": payload}
                Request.send(context, **kwargs)
                context.execute_steps(u"""
                    Then the response status code should be among "200, 201"
                    """)
    else:
        kwargs = {"method": method, "endpoint": req_url, "payload": {}}
        Request.send(context, **kwargs)
