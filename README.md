# 🌐 Atlas

**Atlas** es una herramienta diseñada
para realizar búsquedas rápidas de información pública como **IP
lookups** y **búsqueda de números telefónicos**

Está pensada para ser **simple**, **extensible** y **eficiente**, con
una interfaz limpia 🖥️.

------------------------------------------------------------------------

## ✨ Características

-   🌐 IP lookup (país, región, ciudad, ISP, ASN, coordenadas)
-   📞 Phone lookup
-   🧼 Interfaz CLI limpia y minimalista
-   🧩 Arquitectura modular (`commands/`)
-   ➕ Fácil de extender con nuevos comandos
------------------------------------------------------------------------

## 🧰 Requisitos

-   🐍 Python **3.9+**
-   📦 Dependencias:
    -   `requests`
    -   `colorama`
    -   `phonenumbers`

------------------------------------------------------------------------

## 🚀 Uso

Ejecuta Atlas haciendo doble click en el archivo
ini.bat


------------------------------------------------------------------------

## 🧭 Comandos disponibles

### 🌐 IP Lookup

    IP <address>

### 📞 Phone Lookup

    Phone <number>


### ⚙️ Sistema

    Clear   Limpia la pantalla
    Help    Muestra el menú completo
    Exit    Cierra Atlas

------------------------------------------------------------------------

## 📂 Estructura

    Atlas/
    ├── main.py
    ├── commands/
    │   ├── ip.py
    │   ├── phone.py
    │   ├── user.py
    │   └── utils.py
    └── README.md

------------------------------------------------------------------------

## ⚖️ Aviso

Atlas es una herramienta educativa. El uso indebido es responsabilidad
del usuario.
