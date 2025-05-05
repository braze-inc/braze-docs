---
nav_title: Fehlersuche
article_title: Fehlerbehebung für Unity
platform: 
  - Unity
  - iOS
  - Android
page_order: 3
description: "Dieser referenzierte Artikel behandelt Themen zur Fehlerbehebung für die Unity-Plattform."

---

# Fehlersuche

> Dieser Artikel enthält mehrere Szenarien zur Fehlerbehebung in Unity.

## "Datei konnte nicht gelesen werden" Fehler

Fehler wie die folgenden können Sie getrost ignorieren. Apple-Software verwendet eine proprietäre PNG-Erweiterung namens CgBI, die von Unity nicht erkannt wird. Diese Fehler haben keinen Einfluss auf Ihr iOS-Build oder die korrekte Anzeige der zugehörigen Bilder im Braze-Bundle.

```
Could not create texture from Assets/Plugins/iOS/AppboyKit/Appboy.bundle/...png: File could not be read
```
