# network-experiments

Repo for various network experiments, initially focused on python stdlib functionality.

## Docker Compose commands

The client and server modules are intended to be run separately, but can be
built simultaneously.
```docker-compose build```

The modules can be built and run individually with:
```docker-compose up --build <module-name>```

Or, run without rebuilding with:
``` docker-compose run --rm <module-name>```

**Note:** When using the docker-compose run command the server module should be
assigned the name "server" in the manner:
```docker-compose run --rm --name server server```
