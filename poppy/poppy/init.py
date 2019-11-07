def __init__(hub):
    hub.pop.conf.integrate(['poppy'], loader='yaml', cli='poppy', roots=True)
    hub.pop.sub.add(pypath='poppy.rpc')
