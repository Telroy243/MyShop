from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, DictProperty
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout


class InventoryScreen(Screen):
    articles = ListProperty([])

    def on_enter(self):
        self.charger_articles()

    def charger_articles(self):
        # Exemple de données simulées
        self.articles = [
            {
                'nom': 'Savon Lux',
                'categorie': 'Hygiène',
                'quantite': 40,
                'achat': 500,
                'vente': 700,
            },
            {
                'nom': 'Riz 25kg',
                'categorie': 'Alimentaire',
                'quantite': 20,
                'achat': 18000,
                'vente': 22000,
            }
        ]

    def ajouter_article(self, article):
        self.articles.append(article)
        self.ids.rv_articles.data = self.articles

    def modifier_article(self, index, nouvel_article):
        self.articles[index] = nouvel_article
        self.ids.rv_articles.data = self.articles

    def supprimer_article(self, index):
        del self.articles[index]
        self.ids.rv_articles.data = self.articles


# Optionnel : Exemple de Popup pour ajouter ou modifier un article
class ArticleForm(BoxLayout):
    def __init__(self, on_save, article=None, index=None, **kwargs):
        super().__init__(**kwargs)
        self.on_save = on_save
        self.article = article
        self.index = index
        if article:
            self.ids.nom.text = article['nom']
            self.ids.categorie.text = article['categorie']
            self.ids.quantite.text = str(article['quantite'])
            self.ids.achat.text = str(article['achat'])
            self.ids.vente.text = str(article['vente'])

    def enregistrer(self):
        article = {
            'nom': self.ids.nom.text,
            'categorie': self.ids.categorie.text,
            'quantite': int(self.ids.quantite.text),
            'achat': float(self.ids.achat.text),
            'vente': float(self.ids.vente.text),
        }
        self.on_save(article, self.index)
        self.parent.parent.dismiss()


class ArticlePopup(Popup):
    def __init__(self, on_save, article=None, index=None, **kwargs):
        super().__init__(**kwargs)
        self.title = "Ajouter / Modifier un article"
        self.content = ArticleForm(on_save, article, index)
        self.size_hint = (0.9, 0.8)
