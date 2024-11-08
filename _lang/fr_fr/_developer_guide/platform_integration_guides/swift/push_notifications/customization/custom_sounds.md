---
nav_title: Sons personnalisés
article_title: Sons de notification Push personnalisés pour iOS
platform: Swift
page_order: 3
description: "Cet article traite de l’implémentation des sons personnalisés iOS dans le SDK Swift."
channel:
  - push

---

# Sons personnalisés

## Étape 1 : Héberger les sons dans l’application

Les sons de notification push personnalisés doivent être hébergés localement dans le bundle principal de votre application. Les formats de données audio suivants sont acceptés :

- Linear PCM
- MA4
- µLaw
- aLaw

Vous pouvez regrouper les données audio dans un fichier AIFF, WAV ou CAF. Dans Xcode, ajoutez le fichier audio à votre projet comme ressource non localisée du lot d’applications.

{% alert note %}
Les sons personnalisés doivent durer moins de 30 secondes lorsqu’ils sont joués. Si un son personnalisé dépasse cette limite, le son système par défaut est joué à la place.
{% endalert %}

### Conversion de fichiers audio

Vous pouvez utiliser l'outil afconvert pour convertir les sons. Par exemple, pour convertir le système PCM linéaire 16 bits Submarine.aiff en audio IMA4 dans un fichier CAF, utilisez la commande suivante dans le terminal :

```bash
afconvert /System/Library/Sounds/Submarine.aiff ~/Desktop/sub.caf -d ima4 -f caff -v
```

{% alert tip %}
Vous pouvez inspecter un son pour déterminer son format de données en l'ouvrant dans QuickTime Player et en choisissant **Afficher l'inspecteur de film** dans le menu **Film.**
{% endalert %}

## Étape 2 : Fournir une URL de protocole pour le son

Vous devez spécifier une URL de protocole qui dirige vers l'emplacement/localisation du fichier son dans votre application. Il existe deux méthodes pour ce faire :

* Utilisez le paramètre `sound` de l'[objet Apple push]({{site.baseurl}}/api/objects_filters/messaging/apple_object#apple-push-object) pour transmettre l'URL à Braze.
* Spécifiez l'URL dans le tableau de bord. Dans le [compositeur push]({{site.baseurl}}/user_guide/message_building_by_channel/push/creating_a_push_message/#step-3-select-notification-type-ios-and-android), sélectionnez **Paramètres** et saisissez l'URL du protocole dans le champ **Son.**  

![Le compositeur poussé dans le tableau de bord de Braze]({% image_buster /assets/img_archive/sound_push_ios.png %})

Si le fichier son spécifié n’existe pas ou si le mot-clé « default » est saisi, Braze utilisera le son d’alerte par défaut du appareil. En dehors de notre tableau de bord, le son peut également être configuré via notre [API d’envoi de messages][12].

Pour plus d'informations, consultez la documentation du développeur Apple concernant [la préparation de sons d'alerte personnalisés](https://developer.apple.com/library/content/documentation/NetworkingInternet/Conceptual/RemoteNotificationsPG/SupportingNotificationsinYourApp.html).

