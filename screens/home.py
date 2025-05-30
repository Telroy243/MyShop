from kivy.uix.screenmanager import Screen
from kivy.properties import NumericProperty, ListProperty, StringProperty
from kivy.clock import Clock


class HomeScreen(Screen):
    total_articles = NumericProperty(0)
    revenu_total = NumericProperty(0.0)
    produits_populaires = ListProperty([])

    def on_enter(self):
        # Simuler des données pour le moment, à remplacer par ta logique réelle
        Clock.schedule_once(self.update_stats, 0.5)

    def update_stats(self, *args):
        # Exemple statique — à remplacer par une récupération réelle depuis un stockage local
        self.total_articles = 125
        self.revenu_total = 150000.0
        self.produits_populaires = ["Savon Lux", "Dentifrice Colgate", "Riz 25kg"]
