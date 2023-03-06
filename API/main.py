from fastapi import FastAPI, Path
from uvicorn import Server, Config
from fastapi.staticfiles import StaticFiles
from endpoints import pages
from settings import Settings, main_settings
from api_loggers.log import main_logger

app = FastAPI()
app.include_router(pages.router)
app.mount("/static", StaticFiles(directory="static"), name="static")


def server_setup(settings: Settings = main_settings):
    main_logger.infolog.info('Logger is ready!')

    outer_port = settings.API_PORT or 8000

    debug_mode = settings.DEBUG_MODE
    container_enviroment = settings.DOCKER

    if container_enviroment:
        host = "0.0.0.0"
        port = 8000
    else:
        debug_mode = True
        host = 'localhost'
        port = outer_port

    if debug_mode:
        main_logger.infolog.info(f'[S] API ROOT http://localhost:{outer_port}')
        main_logger.infolog.info(f'[S] API DOCS http://localhost:{outer_port}/docs')
        log_level = 'warning'
        reload_policy = False if container_enviroment else True  # Известная проблема см. README (1)
    else:
        main_logger.infolog.info(f'API WIIL BE STARTED IN PRODUCTION MODE AT PORT :{outer_port}')
        log_level = 'info'
        reload_policy = False

    return Server(config=Config('main:app', host=host, port=port, log_level=log_level, reload=reload_policy))


if __name__ == "__main__":
    server = server_setup()
    server.run()
