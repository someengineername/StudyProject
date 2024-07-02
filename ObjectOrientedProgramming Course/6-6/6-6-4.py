from contextlib import contextmanager


@contextmanager
def safe_open(filename, mode='r'):
    # try to open file - make context
    yielding_obj = ()
    success_flag = False

    try:
        test_file = open(filename, mode=mode)
        yielding_obj = (test_file, None)
        success_flag = True
    except Exception as e:
        yielding_obj = (None, e)

    # yield filewrapperIO - operation inside a context

    yield yielding_obj

    # close file - end context

    if success_flag:
        test_file.close()
