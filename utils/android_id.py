# utils/android_id.py

from kivy.utils import platform

def get_android_id():
    """
    Retourne l'Android ID si sur Android, sinon un ID de test.
    """
    if platform == 'android':
        from jnius import autoclass
        SettingsSecure = autoclass('android.provider.Settings$Secure')
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        content_resolver = PythonActivity.mActivity.getContentResolver()
        android_id = SettingsSecure.getString(content_resolver, SettingsSecure.ANDROID_ID)
        return str(android_id)
    else:
        # ID fictif pour le développement (à remplacer pour les tests)
        return "DEV-1234567890"
