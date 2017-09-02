import requests
import webbrowser

def logon():

    try:

        with requests.Session() as c :

            url = 'http://phc.prontonetworks.com/cgi-bin/authlogin?'

            # enter your username instead of '16BCB0088'
            USERNAME = '16BCB0088'
            # enter your password instead of 'NoWayThisIsMyPwd6969'
            PASSWORD = 'NoWayThisIsMyPwd6969'

            print('Starting ...')
            c.get(url)
            login_data = dict(userId = USERNAME, password = PASSWORD, serviceName = 'ProntoAuthentication', Submit22 = 'Login')
            c.post(url, data = login_data)

            print('Your credentials has been posted ...')
            page = c.get('http://phc.prontonetworks.com/cgi-bin/authlogin?URI=http://go.microsoft.com/fwlink/').text

            print('Successfully Logged in.')
            print('Opening Github profile ...')

            # Set your favorite page instead of 'https://github.com/greed2411'
            webbrowser.open_new('https://github.com/greed2411')

    except Exception:

        print('Sorry couldn\'t connect with your Wi-Fi, make sure you are connected.')


if __name__ == '__main__':

    logon()
    quit()
