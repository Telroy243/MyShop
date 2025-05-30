from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, NumericProperty
from kivy.clock import Clock
from datetime import datetime, timedelta
import random


class StatsScreen(Screen):
    ventes_par_semaine = ListProperty([])
    produits_populaires = ListProperty([])
    revenu_total = NumericProperty(0.0)

    def on_enter(self):
        # Charge les statistiques simulées à l'entrée sur l'écran
        Clock.schedule_once(self.charger_stats, 0.5)

    def charger_stats(self, *args):
        # Simuler des ventes des 7 derniers jours
        aujourd_hui = datetime.now()
        self.ventes_par_semaine = [
            {
                'date': (aujourd_hui - timedelta(days=i)).strftime('%d/%m'),
                'montant': random.randint(10000, 50000)
            }
            for i in reversed(range(7))
        ]

        # Simuler les produits les plus vendus
        self.produits_populaires = [
            {'nom': 'Savon Lux', 'quantite': 35},
            {'nom': 'Riz 25kg', 'quantite': 27},
            {'nom': 'Huile 1L', 'quantite': 21}
        ]

        # Calcul du revenu total
        self.revenu_total = sum(jour['montant'] for jour in self.ventes_par_semaine)
