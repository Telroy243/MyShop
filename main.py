from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.lang import Builder
from kivy.core.window import Window
from utils.license_checker import is_license_valid
from screens.home import HomeScreen
from screens.inventory import InventoryScreen
from screens.stats import StatsScreen
from screens.subscription import SubscriptionScreen

# Charger les fichiers .kv
Builder.load_file("ui/home.kv")
Builder.load_file("ui/inventory.kv")
Builder.load_file("ui/stats.kv")
Builder.load_file("ui/subscription.kv")

# Définir la taille de fenêtre pour le développement (supprime cette ligne pour Android)
Window.size = (360, 640)


class RootWidget(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.screen_manager = ScreenManager(transition=NoTransition())

        # Ajouter les écrans
        self.screen_manager.add_widget(HomeScreen(name='home'))
        self.screen_manager.add_widget(InventoryScreen(name='inventory'))
        self.screen_manager.add_widget(StatsScreen(name='stats'))
        self.screen_manager.add_widget(SubscriptionScreen(name='subscription'))

        self.add_widget(self.screen_manager)

        # Ajouter la barre de navigation
        from kivy.uix.boxlayout import BoxLayout
        from kivy.uix.button import Button

        nav = BoxLayout(size_hint_y=0.1)

        self.buttons = {
            'home': Button(text='Accueil', on_release=lambda x: self.change_screen('home')),
            'inventory': Button(text='Inventaire', on_release=lambda x: self.change_screen('inventory')),
            'stats': Button(text='Statistiques', on_release=lambda x: self.change_screen('stats')),
            'subscription': Button(text='Abonnement', on_release=lambda x: self.change_screen('subscription')),
        }

        for btn in self.buttons.values():
            nav.add_widget(btn)

        self.add_widget(nav)

        # Initialisation selon licence
        if is_license_valid():
            self.change_screen('home')
        else:
            self.disable_all_except_subscription()
            self.change_screen('subscription')

    def change_screen(self, screen_name):
        self.screen_manager.current = screen_name

    def disable_all_except_subscription(self):
        for key in self.buttons:
            self.buttons[key].disabled = (key != 'subscription')


class MyShopApp(App):
    def build(self):
        self.title = "MyShop"
        return RootWidget()


if __name__ == '__main__':
    MyShopApp().run()
