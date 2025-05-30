from kivy.uix.screenmanager import Screen
from kivy.properties import StringProperty, BooleanProperty
from kivy.core.clipboard import Clipboard
from kivy.uix.popup import Popup
from kivy.uix.label import Label

from utils.android_id import get_android_id
from utils.license_checker import verifier_licence, enregistrer_licence_localement

class SubscriptionScreen(Screen):
    android_id = StringProperty('')
    code_licence = StringProperty('')
    licence_valide = BooleanProperty(False)

    def on_enter(self):
        # Affiche l'Android ID à l'entrée de l'écran
        self.android_id = get_android_id()

    def copier_android_id(self):
        Clipboard.copy(self.android_id)
        self.popup_info("ID copié dans le presse-papier.")

    def valider_licence(self):
        if not self.code_licence:
            self.popup_info("Veuillez entrer un code de licence.")
            return

        # Vérifie la validité de la licence
        resultat = verifier_licence(self.android_id, self.code_licence)

        if resultat['valide']:
            enregistrer_licence_localement(self.code_licence)
            self.licence_valide = True
            self.popup_info("Licence activée avec succès.")
            self.manager.current = "home"
        else:
            self.popup_info("Licence invalide ou expirée.")

    def contacter_admin(self):
        import webbrowser
        webbrowser.open("https://wa.me/243997105634")

    def popup_info(self, message):
        popup = Popup(title='Information',
                      content=Label(text=message),
                      size_hint=(0.8, 0.3))
        popup.open()
