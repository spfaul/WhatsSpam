import pyperclip

def get_user_choices():
    print('\nCopy the text you want to spam into your clipboard.')

    while True:
        print('\nText Detected In Clipboard:')
        clip = pyperclip.waitForPaste()
        print(f'{clip}\n')

        is_correct_message = input('Do you want to spam this text? (y/n) >> ')
        if is_correct_message == 'y':
            break
        elif is_correct_message == 'n':
            print('Cancelled!')
        else:
            print('Enter \'y\' for yes or \'n\' for no.')

    while True:
        times = input('Number of times to spam >> ')
        try:
            times = int(times)
            break
        except ValueError:
            print('Invalid Number! Try Something Like \'10\'.')

    return clip, times

