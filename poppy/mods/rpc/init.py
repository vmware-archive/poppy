# Import python libs
import json
# Import third party libs
import aiohttp


async def start(hub):
    '''
    Start up the rpc server
    '''
    app = aiohttp.web.Application()
    app.add_routes([web.get('/', hub.rpc.init.handle)])
    # TODO: Run this from within a loop
    web.run_app()


async def handle(hub, request):
    '''
    Take the requests and wrap them in a top level handler
    '''
    data = await request.json()
    ref = data.get('ref', None)
    kwargs = data.get('kwargs', {})
    func = hub.pop.ref.last(ref)
    if func:
        ret = await func(**kwargs)
    else:
        ret = {}
    return web.json_response(data)
