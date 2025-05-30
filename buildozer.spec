[app]
title = MyShop
package.name = myshop
package.domain = com.victor
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0
requirements = python3,kivy,kivymd,pillow,plyer,cryptography
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 23b
android.archs = arm64-v8a,armeabi-v7a
android.private_storage = True
android.logcat_filters = *:S python:D
presplash.filename = ./assets/logo.png
icon.filename = ./assets/logo.png
copy_libs = 1

[buildozer]
log_level = 2
warn_on_root = 1

[python]
# Options spécifiques à l'interpréteur
