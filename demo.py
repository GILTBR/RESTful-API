import LogTrace

if __name__ == '__main__':
    for i in range(5):
        LogTrace.log_trace('Customer', f'{i}', 200, 'test1', 'req', 'res')
