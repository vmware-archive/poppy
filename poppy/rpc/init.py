# poppy/rpc/init.py

from aiohttp import web

def __init__(hub):
    app = web.Application()
    routes = [
            web.get('/', hub.rpc.init.router),
    ]
    app.add_routes(routes)
    web.run_app(app,
                host=hub.OPT['poppy']['addr'],
                port=hub.OPT['poppy']['port'])


async def router(hub, request):
    try:
        data = await request.json()
    except:
        data = {}
    if 'ref' in data:
        result = {}
        result['ref'] = await getattr(hub.rpc, data['ref'])(**data.get('kwargs'))
        return web.json_response(result)
    default_text = """example: curl -X GET http://{0}:{1} -d '{{"ref": "math.fib", "kwargs": {{"num": "11"}}}}'\n""".format(
            hub.OPT['poppy']['addr'],
            hub.OPT['poppy']['port']
            )
    return web.Response(text=default_text)
