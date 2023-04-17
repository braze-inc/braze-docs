---
nav_title: Rafraîchir le flux
article_title: Actualisation du flux de carte de contenu pour le Web
page_order: 2
platform: Web
channel: cartes de contenu
page_type: reference
description: "Cet article de référence décrit comment mettre en file d’attente une actualisation manuelle de vos cartes de contenu pour votre application Web."

---

# Rafraîchir le flux

> Cet article de référence décrit comment mettre en file d’attente une actualisation manuelle de vos cartes de contenu pour votre application Web.

Vous pouvez mettre en file d’attente un rafraîchissement manuel des cartes de contenu Braze à tout moment en appelant [`requestContentCardsRefresh()`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestcontentcardsrefresh). 

Vous pouvez également appeler [`getCachedContentCards`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#getcachedcontentcards) pour obtenir toutes les cartes actuellement disponibles depuis le dernier rafraîchissement de cartes de contenu. 

Le flux se rafraîchit automatiquement sur la nouvelle session ou lorsqu’il est ouvert et que plus de 60 secondes se sont écoulées depuis la dernière actualisation.
