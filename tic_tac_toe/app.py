from kivy.app import App
from kivy.lang import Builder

class TicTacToe(App):

    def on_start(self):
        
        print('starting app ...')

    def on_stop(self):
        
        print('stopping app ...')

    def build(self):

        print('building app ...')
        
        self.title = 'Tic Tac Toe'
        self.turn = 'X'

        return Builder.load_file('tic_tac_toe.kv')
    
    def presser(self, button):

        button.disabled = True

        if self.turn == 'X':
            
            button.text = 'X'
            self.turn = 'O'


        elif self.turn == 'O':
            
            button.text = 'O'
            self.turn = 'X'

        self.root.ids.score.text = '{}\'s turn'.format(self.turn)        
    
    def restart(self):

        print('restarting game ...')

        self.root.ids.score.text = 'X goes first'

        # enable buttons
        self.root.ids.upper_left.disabled = False
        self.root.ids.upper_center.disabled = False
        self.root.ids.upper_right.disabled = False

        self.root.ids.middle_left.disabled = False
        self.root.ids.middle_center.disabled = False
        self.root.ids.middle_right.disabled = False

        self.root.ids.lower_left.disabled = False
        self.root.ids.lower_center.disabled = False
        self.root.ids.lower_right.disabled = False

        # set text button to empty
        self.root.ids.upper_left.text = ''
        self.root.ids.upper_center.text = ''
        self.root.ids.upper_right.text = ''

        self.root.ids.middle_left.text = ''
        self.root.ids.middle_center.text = ''
        self.root.ids.middle_right.text = ''

        self.root.ids.lower_left.text = ''
        self.root.ids.lower_center.text = ''
        self.root.ids.lower_right.text = ''

