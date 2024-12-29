def initialize_dependencies():
    """
    This method is called before fast API server starts and initializes the services prior to app start
    ensuring requests aren't made before the application starts
    """
    #TODO: initialize the db
    #TODO: initialize the logger
    #TODO: initialize any caches

def close_dependencies():
    """
    This method is called when the server receives a signal to shutdown (i.e. SIGINT or SIGTERM)
    All dependent services will be closed first and the server will shutdown gracefully
    """
    #TODO:Close Connection to the DB
    #TODO: Stop asynchronous workers/threads
    #TODO: add logs to indicate the server has been closed


