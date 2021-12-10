---
nav_title: Notifications riches
article_title: Notifications Rich Push pour iOS
platform: iOS
page_order: 3
description: "Cet article couvre la façon d'implémenter des notifications de push riches dans votre application iOS."
channel:
  - Pousser
---

# Notifications riches iOS 10

iOS 10 introduit la possibilité d'envoyer des notifications push avec des images, des gifs et des vidéos. Pour activer cette fonctionnalité, les clients doivent créer une `Extension de service`, un nouveau type d'extension qui permet de modifier un bloc push avant qu'il ne soit affiché.

## Création d'une extension de service
Pour créer une [Extension de service de notification][23], accédez à `Fichier > Nouvelle > Cible` et sélectionnez `Extension du service de notification`.

!\[Ajout d'une extension de service\]\[26\]

Assurez-vous que `Intégrer l'application` est configuré pour intégrer l'extension dans votre application.

## Mise en place de l'extension de service
Une `Extension de service de notification` est son propre binaire qui est fourni avec votre application. En tant que tel, il doit être configuré dans le [Apple Developer Portal][27] avec son propre ID d'application et son propre Provisioning Profile.

### Configuration de l'extension du service pour qu'il fonctionne avec Braze
Braze envoie une charge utile de pièces jointes dans le bloc APN sous la clé `ab` que nous utilisons pour configurer, télécharger et afficher le contenu riche. Par exemple :

```json
{
  "ab" :
    {
...

    "att" :
      {
       "url" : "http://mysite.com/myimage.jpg",
       "type" : "jpg"
       }
    },
  "aps" :
    {
    ...
    }
}
```

Les valeurs de charge utile sont :

```objc
// La clé de dictionnaire de Braze
NSString statique *const AppboyAPNSDictionaryKey = @"ab";

// Le dictionnaire d'attachement
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// L'URL de la pièce jointe
NSString statique *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// Le type de la pièce jointe - un suffixe pour le fichier que vous économisez
NSString statique *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

Pour afficher manuellement une push avec un bloc Braze, téléchargez le contenu de la valeur sous `AppboyAPNSDictionaryAttachmentURLKey`, enregistrez-le en tant que fichier avec le type de fichier stocké sous la touche `AppboyAPNSDictionaryAttachmentTypeKey` et ajoutez-le aux pièces jointes de notification.

### Exemple de code

Vous pouvez écrire l'extension de service dans Objective-C ou Swift.

Pour utiliser notre exemple de code Objective-C, remplacez le contenu de votre `Extension de service de notification` cible générée automatiquement `NotificationService.` avec le contenu de [ce fichier][1].

Pour utiliser notre exemple de code Swift, remplacez le contenu de votre `Extension de service de notification` cible générée automatiquement `NotificationService. wift` avec le contenu de [ce fichier][2].

## Créer une notification enrichie dans votre tableau de bord

Pour créer une notification enrichie dans votre tableau de bord Braze, créez simplement un push iOS et attachez une image ou un gif, ou fournissez une URL qui héberge une image, un gif ou une vidéo.  Notez que les ressources sont téléchargées sur la réception des notifications push, donc vous devriez planifier pour les grands, pics synchrones dans les requêtes si vous hébergez votre contenu.

Notez également les types et tailles de fichiers pris en charge, listés [ici][28].
[26]: {% image_buster /assets/img_archive/ios10_se_at.png %}

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m
[2]: https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift
[23]: https://developer.apple.com/reference/usernotifications/unnotificationserviceextension
[27]: https://developer.apple.com
[28]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
