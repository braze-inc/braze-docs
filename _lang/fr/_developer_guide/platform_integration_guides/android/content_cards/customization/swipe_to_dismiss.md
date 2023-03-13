---
nav_title: Fermeture de carte de contenu
article_title: Fermeture de carte de contenu pour Android et FireOS
page_order: 4.5
platform: 
  - Android
  - FireOS
description: "Cet article couvre les options de personnalisation pour vos cartes de contenu dans votre application Android ou FireOS."
channel:
  - cartes de contenu

---

# Fermeture de carte de contenu

La désactivation de la fonctionnalité « glisser pour fermer » est effectuée sur la base d’une seule carte via la méthode [`card.setIsDismissibleByUser()`][48]. Les cartes peuvent être interceptées avant l’affichage en utilisant la méthode [`ContentCardsFragment.setContentCardUpdateHandler()`][45].

[45]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze.ui.contentcards/-content-cards-fragment/set-content-card-update-handler.html
[48]: https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.appboy.enums/-card-key/index.html#285743463%2FClasslikes%2F-1725759721
