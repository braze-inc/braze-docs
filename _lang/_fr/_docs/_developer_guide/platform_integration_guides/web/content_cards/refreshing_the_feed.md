---
nav_title: Rafraîchissement du flux
article_title: Rétablir le flux de la carte de contenu pour le Web
page_order: 3
platform: Web
channel: cartes de contenu
page_type: Référence
description: "Cet article de référence décrit comment mettre en file d'attente une mise à jour manuelle des cartes de contenu."
---

# Rafraîchissement des cartes de contenu

 Vous pouvez mettre en file d'attente une mise à jour manuelle des Cartes de Contenu Braze à tout moment en appelant :

`requestContentCardsRefresh()`

Vous obtiendrez toutes les cartes actuellement disponibles à partir de la dernière mise à jour des cartes de contenu.

[Docs JS pour getCachedContentCards](https://js.appboycdn.com/web-sdk/latest/doc/module-appboy.html#.getCachedContentCards)

Le flux sera actualisé automatiquement lors de la nouvelle session ou lorsque le flux sera ouvert et plus de 60 secondes se seront écoulées depuis le dernier rafraîchissement.
