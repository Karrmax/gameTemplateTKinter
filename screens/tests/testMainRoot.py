import unittest
from unittest.mock import patch, MagicMock

from screens.mainRoot import MainRoot

class TestMainRoot(unittest.TestCase):

    @patch('screens.mainRoot.os')
    @patch('screens.mainRoot.importlib')
    def test_init_screens(self, mock_importlib, mock_os):
        # Mock the os.listdir method
        mock_os.listdir.return_value = ['lobby.py', 'leaderboard.py', 'game.py', 'mainRoot.py']
        
        # Mock the importlib.import_module method
        mock_module = MagicMock()
        mock_importlib.import_module.return_value = mock_module
        
        # Mock the screen classes
        LobbyScreen = MagicMock()
        LeaderboardScreen = MagicMock()
        GameScreen = MagicMock()
        mock_module.Lobby = LobbyScreen
        mock_module.Leaderboard = LeaderboardScreen
        mock_module.Game = GameScreen
        
        # Create an instance of the class containing init_screens
        instance = MainRoot()
        instance.root = MagicMock()
        instance.switch_screen = MagicMock()
        instance.loadManager = MagicMock()
        
        # Call the init_screens method
        instance.init_screens()
        
        # Check if the screens dictionary is populated correctly
        self.assertIn('lobby', instance.screens)
        self.assertIn('leaderboard', instance.screens)
        self.assertIn('game', instance.screens)
        
        # Check if the switch_screen method is called with 'lobby'
        instance.switch_screen.assert_called_with('lobby')

    @patch('screens.mainRoot.tk')
    def test_switch_screen(self, mock_tk):
        # Create mock screen instances
        mock_lobby_screen = MagicMock()
        mock_leaderboard_screen = MagicMock()
        mock_game_screen = MagicMock()
        
        # Create an instance of the class containing switch_screen
        instance = MainRoot()
        instance.screens = {
            'lobby': mock_lobby_screen,
            'leaderboard': mock_leaderboard_screen,
            'game': mock_game_screen
        }
        instance.currentScreen = None
        
        # Call the switch_screen method
        instance.switch_screen('lobby')
        
        # Check if the current screen is set correctly
        self.assertEqual(instance.currentScreen, mock_lobby_screen)
        mock_lobby_screen.pack.assert_called_with(fill=mock_tk.BOTH, expand=True)
        
        # Call the switch_screen method again
        instance.switch_screen('leaderboard')
        
        # Check if the previous screen is packed away and the new screen is set correctly
        mock_lobby_screen.pack_forget.assert_called_once()
        self.assertEqual(instance.currentScreen, mock_leaderboard_screen)
        mock_leaderboard_screen.pack.assert_called_with(fill=mock_tk.BOTH, expand=True)

if __name__ == '__main__':
    unittest.main()