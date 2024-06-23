def is_context_manager(obj):
    return '__exit__' in obj.__dir__ and '__enter__' in obj.__dir__