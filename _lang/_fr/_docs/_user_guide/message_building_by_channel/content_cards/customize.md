---
nav_title: Personnaliser
article_title: Personnaliser
page_order: 2
layout: en vedette
guide_top_header: "Personnaliser vos cartes de contenu"
guide_top_text: "La personnalisation des cartes de contenu et du flux dans lequel elles seront installées ne peut pas être effectuée pendant le processus de création de la campagne - vous devez travailler avec vos ingénieurs et vos développeurs pour construire et personnaliser vos cartes. C'est facile et entièrement personnalisable de cette manière!"
description: "La personnalisation des cartes de contenu et du flux dans lequel elles seront installées doit être faite avec vos ingénieurs et vos développeurs. Cet article couvrira où cette information peut être trouvée dans la documentation de Braze."
guide_featured_title: "Personnaliser les cartes de contenu pour..."
guide_featured_list:
  - 
    name: Android
    link: /fr/docs/developer_guide/platform_integration_guides/android/content_cards/customization/
    fa_icon: fab fa-android
  - 
    name: iOS
    link: /fr/docs/developer_guide/platform_integration_guides/ios/content_cards/customization/
    fa_icon: fa-pomme fab
  - 
    name: Web
    link: /fr/docs/developer_guide/platform_integration_guides/web/content_cards/customization/
    fa_icon: fas fa-globe
channel:
  - cartes de contenu
---

<br>

## Changer la langue du flux vide

Vous pouvez changer la langue qui apparaît automatiquement dans les flux de la carte de contenu vide en [redéfinissant les chaînes de caractères traduisables](https://github.com/Appboy/appboy-ios-sdk/blob/3cca65b06f66085f5bc7c8e1ad267bf8bb1f0da7/AppboyUI/ABKContentCards/Resources/en.lproj/AppboyContentCardsLocalizable.strings) dans le fichier de chaînes localisables de votre application :
```
"Appboy.content-cards.no-card.text" = "Aucune carte!!!!";
"Appboy.content-cards.done-button.title" = "Terminé";
"Appboy.content-cards.no-card.text" = "Nous n'avons pas de mises à jour.\nVeuillez vérifier plus tard. ;
"Appboy.content-cards.no-connection.title" = "Erreur de connexion";
"Appboy.content-cards.no-connection.message" = "Impossible d'établir la connexion au réseau.title"\nVeuillez réessayer plus tard.";
```
{% alert note %}
Si vous voulez le mettre à jour pour différentes langues, trouver la langue correspondante dans [la structure du dossier Ressources](https://github.com/Appboy/appboy-ios-sdk/tree/3cca65b06f66085f5bc7c8e1ad267bf8bb1f0da7/AppboyUI/ABKContentCards/Resources) avec la même chaîne `Appboy. ontent-cards.no-card.text`.
{% endalert %}

<br>
