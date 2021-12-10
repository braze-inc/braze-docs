---
nav_title: Sons personnalisés
article_title: Sons de notification Push personnalisés pour iOS
platform: iOS
page_order: 2
description: "Cet article couvre la façon d'implémenter des sons personnalisés dans vos notifications push iOS."
channel:
  - Pousser
---

# Sons personnalisés

## Étape 1 : Héberger le son dans l'application

Les sons de notification push personnalisés doivent être hébergés localement dans le lot principal de l'application client. Les formats de données audio suivants sont acceptés :

- PCM linéaire
- MA4
- μLoi
- aLaw

Vous pouvez empaqueter les données audio dans un fichier aiff, onde ou caf. Puis, dans Xcode, ajoutez le fichier son à votre projet en tant que ressource non localisée du lot d'applications.

Vous pouvez utiliser l'outil afconvert pour convertir des sons. Par exemple, pour convertir le son PCM linéaire 16 bits sous-marine. iff à l'audio IMA4 dans un fichier CAF, utilisez la commande suivante dans l'application Terminal :

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

Vous pouvez inspecter un son pour déterminer son format de données en l'ouvrant dans QuickTime Player et en choisissant Show Movie Inspector dans le menu Films.

Les sons personnalisés doivent être inférieurs à 30 secondes lors de la lecture. Si un son personnalisé dépasse cette limite, le son système par défaut est joué à la place.

## Étape 2 : Fournissez au tableau de bord une URL de protocole pour le son

Votre son doit être hébergé localement dans l'application. Vous devez spécifier une URL de protocole qui dirige vers l'emplacement du fichier de son dans l'application dans le champ "Sound" du compositeur push. Spécifier « default » dans ce champ jouera le son de notification par défaut sur l'appareil. Ceci peut être spécifié via notre [API de messagerie][25] ou notre tableau de bord sous « Paramètres avancés » dans l'assistant du compositeur push comme illustré ci-dessous :

!\[Son de Notification Push\]\[8\]

Si le fichier son spécifié n'existe pas ou si le mot clé « default » est saisi, Braze utilisera le son d'alerte par défaut. Outre notre tableau de bord, le son peut également être configuré via notre [API de messagerie][12]. Pour plus d'informations, voir la documentation du développeur Apple concernant ["Préparation des sons d'alerte personnalisés"][9].
[8]: {% image_buster /assets/img_archive/sound_push_ios.png %}

[9]: https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html
[25]: {{site.baseurl}}/api/endpoints/messaging/
