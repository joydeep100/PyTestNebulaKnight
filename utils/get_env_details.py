from configs.env_data import envData

def get_env_details(request):
    env_vars = {
        'browser': request.config.getoption("--browser"),
        'env': request.config.getoption("--env"),
        'login': request.config.getoption("--login"),
        'secret': request.config.getoption("--secret"),
        'headless': request.config.getoption("--headless"),
        'testdata': request.config.getoption("--testdata"),
        'baseurl': envData[request.config.getoption("--env")]['baseurl']
    }
    return env_vars
