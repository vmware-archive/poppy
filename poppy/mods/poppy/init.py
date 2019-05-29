def new(hub):
    # Lets start by pulling in a config
    # When you make a hub, it comes loaded up with the tools subsystem
    # Inside tools there is a fully fledged config loading system called conf
    # Calling tools.conf.integrate allows you to load configs from multiple projects
    # Just go to the config.py file and add options to the config dicts
    hub.tools.conf.integrate('poppy', cli='poppy', roots=True)
    # Now lets add a new plugin subsystem that we will use later
    # This is a library pattern subsystem, this subsystem is made to allow
    # for multiple arbitrary functions to be made available to an interface.
    # In this case the interface will be used to expose RPC calls
    hub.tools.sub.add('rpc', pypath='poppy.mods.rpc')
    # Now we will start up the rpc server. When you make a subsystem the
    # pattern should be defined in the init.py file of the subsystem.

    # Now we should start up an asyncio loop. You can call asyncio
    # Directly, but pop comes with some tools to extend asyncio
    # So we will use the loop module in tools to start up the loop.
    hub.tools.loop.start(hub.rpc.init.start(), hold=True)

    # Now the RPC server defined in in the rpc subsystem has started up!
