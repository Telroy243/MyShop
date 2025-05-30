import base64
import hashlib
import os
from datetime import datetime
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from kivy.storage.jsonstore import JsonStore
from .android_id import get_android_id

# Clé secrète connue uniquement de l'administrateur
SECRET_KEY = "VictorTes!a@Key2024"  # NE PAS PARTAGER
LICENSE_FILE = os.path.join(os.path.expanduser("~"), ".myshop_license.json")

class LicenseManager:
    def __init__(self):
        self.android_id = get_android_id()
        self.store = JsonStore(LICENSE_FILE)

    def is_trial_active(self):
        if not self.store.exists("trial"):
            start_date = datetime.now().strftime("%Y-%m-%d")
            self.store.put("trial", start=start_date)
            return True
        else:
            start = datetime.strptime(self.store.get("trial")["start"], "%Y-%m-%d")
            now = datetime.now()
            return (now - start).days < 7

    def save_license(self, code):
        self.store.put("license", code=code)

    def is_license_valid(self):
        if not self.store.exists("license"):
            return False

        code = self.store.get("license")["code"]

        try:
            # Déchiffrement
            key = hashlib.sha256(SECRET_KEY.encode()).digest()
            cipher = AES.new(key, AES.MODE_ECB)
            decrypted = unpad(cipher.decrypt(base64.b64decode(code)), AES.block_size)

            # Décodage
            data = decrypted.decode().split("|")
            if len(data) != 3:
                return False

            license_android_id, start_date, end_date = data
            if license_android_id != self.android_id:
                return False

            today = datetime.now().date()
            start = datetime.strptime(start_date, "%Y-%m-%d").date()
            end = datetime.strptime(end_date, "%Y-%m-%d").date()
            return start <= today <= end

        except Exception as e:
            print("Erreur de validation de licence :", e)
            return False

    def is_app_authorized(self):
        return self.is_license_valid() or self.is_trial_active()

    def get_license_dates(self):
        if not self.store.exists("license"):
            return None
        try:
            code = self.store.get("license")["code"]
            key = hashlib.sha256(SECRET_KEY.encode()).digest()
            cipher = AES.new(key, AES.MODE_ECB)
            decrypted = unpad(cipher.decrypt(base64.b64decode(code)), AES.block_size)
            license_android_id, start_date, end_date = decrypted.decode().split("|")
            return start_date, end_date
        except:
            return None
