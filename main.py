# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import httpx
import uvicorn
from fastapi import FastAPI, BackgroundTasks
from reasoner_pydantic import Query as PDQuery, AsyncQuery as PDAsyncQuery, Response as PDResponse
import json
import aiofiles

APP = FastAPI()


async def get_answer(request: PDQuery):
    message = request.dict()
    call_back = message.get('callback')
    print("Incoming message: ", message)
    async with aiofiles.open('./a.0_RHOBTB2_direct_output.json', 'r') as stream:
        ao_ = json.loads(await stream.read())
    ao_query = ao_['message']['query_graph']
    message_q = message['message']['query_graph']
    if ao_query == message_q:
        print(f'received a0 like request with: {call_back}')
        return ao_
    else:
        async with aiofiles.open('./c3_output.json', 'r') as stream:
            print(f'received c3 like request with {call_back}')
            c3_ = json.loads(await stream.read())
            return c3_


@APP.post('/query', tags=["Strider Mock"], response_model=PDResponse, response_model_exclude_none=True, status_code=200)
async def sync_query_handler(request: PDQuery):
    return await get_answer(request)


async def call_callback(request: PDQuery):
    call_back_url = request.dict()['callback']
    print(f"started bg task for call_back {call_back_url}")
    answer = await get_answer(request)
    print(f"done reading answer for callback {call_back_url}")
    async with httpx.AsyncClient(timeout=600) as client:
        print(f"preparing to send to {call_back_url}")
        await client.post(call_back_url, json=answer)
        print(f"done sending to {call_back_url}")


@APP.post('/asyncquery', tags=["Strider Mock"], response_model_exclude_none=True, status_code=200)
async def async_query_handler(request: PDQuery, background_tasks: BackgroundTasks):
    call_back_url = request.dict()['callback']
    print(f'starting background task for callback {call_back_url}')
    background_tasks.add_task(call_callback, request)
    return {"status": "success"}


if __name__ == '__main__':
    uvicorn.run(APP, host="0.0.0.0", port=5001, log_level="trace")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
