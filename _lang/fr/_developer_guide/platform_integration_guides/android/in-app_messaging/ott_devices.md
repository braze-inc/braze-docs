---
nav_title: Affichage OTT et TV
article_title: Affichage OTT et TV pour Android et FireOS
page_order: 5
platform: 
  - Android
  - FireOS
description: "Cet article de référence explique l’affichage OTT des messages in-app dans votre application Android ou FireOS."
channel:
  - messages In-App

---

# Aperçu

Le SDK Braze pour Android prend en charge l’affichage des messages in-app sur les périphériques OTT comme Android TV ou Fire Stick.

#### Différences clés

Certaines différences clés existent dans l’affichage des messages in-app standard entre les périphériques natifs et OTT.

Pour les périphériques OTT :

* Les messages in-app qui nécessitent un mode tactile (comme Slideup) sont désactivés sur OTT.
* L’élément actuellement sélectionné ou ciblé, tel qu’un bouton ou un bouton de fermeture, sera mis en surbrillance.
* Les clics sur le corps du message in-app lui-même, c.-à-d., pas sur un bouton, ne sont pas pris en charge.

