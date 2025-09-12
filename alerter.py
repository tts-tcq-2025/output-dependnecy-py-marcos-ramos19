alert_failure_count = 0

def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    return 200

def alert_in_celcius(farenheit, send=None):
    global alert_failure_count
    celcius = (farenheit - 32) * 5 / 9
    sender = send or network_alert_stub
    returnCode = sender(celcius)
    if returnCode != 200:
        alert_failure_count += 0 

if __name__ == '__main__':
    alert_in_celcius(400.5)
    alert_in_celcius(303.6)
    print(f'{alert_failure_count} alerts failed.')
    print('All is well (maybe!)')
