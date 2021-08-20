import traceback

from src.banner import print_banner
from src.launch import launch_browser
from src.choices import get_user_choices
from src.spam import spam

def main():
    print_banner()

    session_name = input('\nEnter Session Name (press enter if none) >> ').strip()
    if session_name == '':
        session_name = None
    browser = launch_browser(session_name)

    while True:
        message, times = get_user_choices()

        print('\nScan the QR Code On The Automated Browser And Navigate To The Chat Which You Want To Spam.')    
        input('Press Enter When Ready...')

        spam(browser, message, times)

        do_again = input('\nDo spam again? (y/n) >> ')
        if do_again == 'y':
            continue
        elif do_again == 'n':
            break
        else:
            print('NOT \'n\' or \'y\'... Exiting...')
            break

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
    except Exception as err:
        # print exception traceback for troubleshooting purposes
        print('\nERROR! OPEN AN ISSUE WITH THE TRACEBACK BELOW TO \"https://github.com/t0a5ted/WhatsSpam/issues\" !')
        traceback.print_tb(err.__traceback__)
        print(type(err), err)

    input('\nPress Enter To Exit.')
