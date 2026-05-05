import time

'''
Author: João Senger
github.com/joaosenger

Co-author: Felipe Cerquiare
github.com/Felipinalves
'''


def sleep_in_ms(milliseconds: float) -> bool:
    '''
    Await a period of time in milliseconds.

    Args:
        milliseconds: the amount of time in milliseconds

    Returns:
        True if success, False if non success
    '''
    try:
        if isinstance(milliseconds, (int, float)):
            result = milliseconds / 1000
            time.sleep(result)
            return True
        else:
            print('[ERROR]: param must be in float or integer type.')
            return False
    except Exception as err:
        print(f'[ERROR]: {err}')
        return False
