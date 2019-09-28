import PySimpleGUI as sg 
#sg.ChangeLookAndFeel('Dark') # change style

filename = None

# string varables to shorten loop and menu code
file_new = 'New............(CTRL+N)'
file_open = 'Open..........(CTRL+O)'
file_save = 'Save............(CTRL+S)'

menu_layout = [['File',[file_new, file_open, file_save,'Save As','---','Exit']],
               ['Tools',['Word Count']],
               ['Help',['About']]]
layout = [[sg.Menu(menu_layout)],
          [sg.Text('/New file/', size=(500,1), font=('Consolas',10), key='_INFO_')],
          [sg.Multiline(font=('Consolas',12), size=(500,100), key='_BODY_')]]
window = sg.Window('Notepad', layout=layout, margins=(0,0), size=(1000,600), resizable=True, return_keyboard_events=True)

def new_file():
    window['_BODY_'].update(value=None)

def open_file():
    ''' open file and update the infobar '''
    filename = sg.popup_get_file('Open File', no_window=True)
    if filename == None:
        return
    else:
        with open(filename, 'r') as f:
            window['_BODY_'].update(value=f.read())
        window['_INFO_'].update(value=filename)
    return filename

def save_file(filename):
    ''' save file instantly if already open; otherwise use `save-as` popup '''
    if filename is None:
        filename = sg.popup_get_file('Save File', save_as=True, default_path=filename, no_window=True)
        window['_INFO_'].update(value=filename)
    else:
        with open(filename,'w') as f:
            f.write(values.get('_BODY_'))
        window['_INFO_'].update(value=filename)

def save_file_as():
    ''' save new file or save existing file with another name '''
    filename = sg.popup_get_file('Save File', save_as=True, no_window=True)
    with open(filename,'w') as f:
        f.write(values.get('_BODY_'))
    window['_INFO_'].update(value=filename)

def word_count():
    ''' display estimated word count '''
    words = values.get('_BODY_').split(' ')
    words_clean = [w for w in words if w!='\n']
    word_count = len(words_clean)
    sg.PopupQuick(f'Word Count: {word_count:,d}', auto_close=False)

def about_me():
    sg.PopupQuick('What did you expect? This is a tutorial program I made for learning how to use PySimpleGUI', auto_close=False)

while True:
    event, values = window.read()
    if event is None or event == 'Exit':
        break
    if event in [file_new,'n:78']:
        new_file()
        filename = None
    if event in [file_open,'o:79']:
        filename = open_file()
    if event in [file_save,'s:83']:
        save_file(filename)
    if event == 'Save As':
        save_file_as()   
    if event == 'Word Count':
        word_count() 
    if event == 'About':
        about_me()  