---
nav_title: Notifications enrichies
article_title: Notifications push enrichies pour iOS
platform: iOS
page_order: 3
description: "Cet article de référence couvre les notifications push enrichies dans votre application iOS."
channel:
  - Notification push

---

# Notifications enrichies iOS 10

iOS 10 offre la possibilité d’envoyer des notifications push avec des images, des GIF et des vidéos. Pour activer cette fonctionnalité, les clients doivent créer un `Service Extension`, un nouveau type d’extension qui permet la modification d’une charge utile de notification push avant qu’elle ne soit affichée.

## Création d’une extension de service

Pour créer un [`Notification Service Extension`][23], naviguez jusqu’à **File > New > Target** (Fichier > Nouveau > Cible) dans Xcode et sélectionnez **Notification Service Extension** (Extension du service de notification).

![][26]{: style="max-width:90%"}

Assurez-vous que **Embed In Application** (Intégré dans l’application) est défini pour intégrer l’extension dans votre application.

## Configuration de l’extension de service

Une `Notification Service Extension` est son propre binaire fourni avec votre application. Il doit être configuré dans le [Portail Développeur Apple][27] avec son propre identifiant d’application et son profil de provisionnement.

L’ID de lot `Notification Service Extension` doit être différent de l’ID de lot de la cible de votre application principale. Par exemple, si l’ID de lot de votre application est `com.company.appname`, vous pouvez utiliser `com.company.appname.AppNameServiceExtension` pour votre extension de service.

### Configuration de l’extension de service pour travailler avec Braze

Braze envoie une charge utile de pièce jointe dans la charge utile APN sous la clé `ab` que nous utilisons pour configurer, télécharger et afficher du contenu enrichi. Par exemple :

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

Les valeurs de charges utiles pertinentes sont les suivantes :

```objc
// The Braze dictionary key
static NSString *const AppboyAPNSDictionaryKey = @"ab";

// The attachment dictionary
static NSString *const AppboyAPNSDictionaryAttachmentKey = @"att";

// The attachment URL
static NSString *const AppboyAPNSDictionaryAttachmentURLKey = @"url";

// The type of the attachment - a suffix for the file you save
static NSString *const AppboyAPNSDictionaryAttachmentTypeKey = @"type";
```

Pour afficher manuellement la notification push avec une charge utile Braze, téléchargez le contenu de la valeur `AppboyAPNSDictionaryAttachmentURLKey`, enregistrez-le comme fichier avec le type de fichier stocké sous `AppboyAPNSDictionaryAttachmentTypeKey` et ajoutez-le aux pièces jointes de notification.

### Exemple de code

Vous pouvez écrire l’extension de service dans Objective-C ou Swift.

Pour utiliser notre échantillon de code Objectif-C, remplacez le contenu de votre cible `Notification Service Extension` autogénérée `NotificationService.m` avec le contenu de l’Appboy [`NotificationService.m`][1].

Pour utiliser notre échantillon de code Swift, remplacez le contenu de votre cible `Notification Service Extension` autogénérée `NotificationService.swift` avec le contenu de l’Appboy [`NotificationService.swift`][2].

## Créer une notification enrichie dans votre tableau de bord

Pour créer une notification enrichie dans votre tableau de bord de Braze, créez une notification push iOS, mettez en pièce jointe une image ou GIF, ou indiquez une URL qui héberge une image, GIF ou vidéo. Notez que les ressources sont téléchargées à la réception des notifications push, vous devez donc prévoir des pics importants et synchrones de demandes si vous hébergez votre contenu.

Consultez [`unnotificationattachment`][28] pour obtenir une liste des types et tailles de fichiers pris en charge.

[1]: https://github.com/Appboy/appboy-ios-sdk/blob/master/Example/StopwatchNotificationService/NotificationService.m
[2]: https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftNotificationExtension/NotificationService.swift
[23]: https://developer.apple.com/reference/usernotifications/unnotificationserviceextension
[26]: {% image_buster /assets/img_archive/ios10_se_at.png %}
[27]: https://developer.apple.com
[28]: https://developer.apple.com/reference/usernotifications/unnotificationattachment
