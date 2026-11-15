[app]
title = SuperApp
package.name = superapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = VIBRATE

# Собираем только под современные 64-битные телефоны (это обходит ту ошибку)
android.archs = arm64-v8a
android.api = 30
android.minapi = 21

# Отключаем лишние логи, чтобы не забивать память при сборке
android.logcat_filters = *:S python:D
