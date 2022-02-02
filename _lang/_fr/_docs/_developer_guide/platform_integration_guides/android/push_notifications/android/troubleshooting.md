---
nav_title: Dépannage
article_title: Dépannage des notifications push pour Android
platform: Android
page_order: 16
description: "Cet article couvre les sujets potentiels de dépannage pour votre implémentation de push Android."
channel:
  - Pousser
---

# Dépannage

## Comprendre le workflow Braze
Le service Firebase Cloud Messaging (FCM) est l’infrastructure de Google pour les notifications push envoyées aux applications Android. Voici la structure simplifiée de la façon dont les notifications push sont activées pour les appareils de vos utilisateurs et comment Braze peut leur envoyer des notifications push :

### Étape 1 : Configuration de votre clé API Google Cloud
Dans le développement de votre application, vous devrez fournir au SDK Braze Android votre identifiant Firebase Sender ID. De plus, vous devrez fournir une clé API pour les applications serveur sur le tableau de bord de Braze. Braze utilisera cette clé API lorsque nous tenterons d'envoyer des messages à vos appareils. Vous devrez vous assurer que le service FCM est également activé dans la console du développeur Google. __Remarque__: Une erreur courante dans cette étape est l'utilisation d'une clé API pour les applications Android. Il s'agit d'une clé API différente et incompatible pour le type d'accès dont Braze a besoin.

### Étape 2 : Les appareils s'enregistrent pour FCM et fournissent à Braze des jetons push
Dans les intégrations typiques, le Braze Android SDK gérera le processus d'enregistrement des périphériques pour la capacité FCM. Cela se produira généralement immédiatement après l'ouverture de l'application pour la première fois. Après l’enregistrement, Braze recevra un ID d’enregistrement FCM, qui est utilisé pour envoyer des messages à cet appareil précisément. Nous stockerons l'ID d'enregistrement pour cet utilisateur et cet utilisateur deviendra "Enregistré" s'il n'avait pas de jeton push pour l'une de vos applications.

### Étape 3 : Lancement d'une campagne Braze push
Lorsqu'une campagne de push est lancée, Braze fera des demandes à FCM pour envoyer votre message. Braze utilisera la clé API copiée dans le tableau de bord pour s'authentifier et vérifier que nous sommes autorisés à envoyer des notifications push aux jetons de push fournis.

### Étape 4 : Suppression des jetons invalides
Si FCM nous informe que l'un des jetons de push que nous tentions d'envoyer est invalide, nous retirons ces jetons des profils d'utilisateurs auxquels ils ont été associés. Si cet utilisateur n'a pas d'autre jeton push, il n'apparaîtra plus comme "Pousser Enregistré" sous la page Segments.

Google a plus de détails sur la FCM sur sa page [Développeurs][6].

## Utilisation des logs d'erreur push
Braze fournit un journal des erreurs de notification Push dans le journal d'activité des messages. Ce journal d'erreurs fournit une variété d'avertissements qui peuvent être très utiles pour identifier pourquoi vos campagnes ne fonctionnent pas comme prévu.  Cliquer sur un message d’erreur vous redirigera vers la documentation pertinente pour vous aider à résoudre un incident particulier.

!\[Journal d'erreur\]\[11\]

## Dépannage des scénarios

### Aucun utilisateur "push registred" ne s'affiche dans le tableau de bord de Braze (avant d'envoyer des messages)

Assurez-vous que votre application est correctement configurée pour autoriser les notifications push. Les points d'échec communs à vérifier incluent :

#### ID de l'expéditeur incorrect

Assurez-vous que l'ID FCM Sender correct est inclus dans le fichier `braze.xml`. Un ID Sender incorrect conduira à `erreurs MismatchSenderID` signalées dans le journal d'activité des messages du tableau de bord.

#### L'enregistrement de Braze n'a pas lieu

Étant donné que l'enregistrement FCM est géré en dehors du Brésil, l'absence d'enregistrement ne peut se produire que dans deux endroits :

1. Lors de l'inscription à la FCM
2. Lors de la transmission du jeton push généré par FCM à Braze

Nous vous recommandons de définir un point d'arrêt ou une journalisation pour vous assurer que le jeton de push généré par FCM est envoyé à Braze. Si un jeton n'est pas généré correctement ou du tout, nous vous recommandons de consulter la [documentation FCM][1].

#### Les services Google Play ne sont pas présents

Pour que la FCM puisse fonctionner, les Services Google Play doivent être présents sur l'appareil. Si les Services Google Play ne sont pas sur un appareil, l'enregistrement push ne se produira pas.

__Remarque :__ les services Google Play ne sont pas installés sur les émulateurs Android sans API Google.

#### Appareil non connecté à internet

Assurez-vous que votre appareil possède une bonne connexion Internet et qu'il n'envoie pas de trafic réseau via un proxy.

### Taper sur la notification push n'ouvre pas l'application

Vérifier si `com_braze_handle_push_deep_links_automatically` est défini à `true` ou `false`. Pour activer Braze pour ouvrir automatiquement l'application et tous les liens profonds quand une notification push est activée, mettez `com_braze_handle_push_deep_links_automatically` à `true` dans votre `braze. ML` fichier.

Si `com_braze_handle_push_deep_links_automatically` est défini à sa valeur par défaut `false`, vous devez alors créer un récepteur de diffusion pour écouter et gérer les intentions reçues et ouvertes.

### Notifications push bounce

Si une notification push n'est pas envoyée, assurez-vous qu'elle n'a pas rebondi en regardant dans la [console développeur][2]. Voici les descriptions des erreurs courantes qui peuvent être enregistrées dans la console du développeur :

#### Erreur: MismatchSenderID

`MismatchSenderID` indique un échec d'authentification. Assurez-vous que votre Firebase Sender ID et votre clé API FCM sont corrects. Consultez notre section sur [inscription push de débogage][3] pour plus d'informations.

#### Erreur: Inscription incorrecte

`Invalidation de l'enregistrement` peut être causée par un jeton push malformé.

1. Assurez-vous de passer un jeton de push valide à Braze depuis Firebase Cloud Messaging [selon leur documentation][21].

#### Erreur: Non enregistré

1. `Non enregistré` se produit généralement lorsqu'une application a été supprimée d'un appareil. Braze utilise `NotRegistered` en interne comme signal qu'une application a été désinstallée d'un appareil.

2. `Non enregistré` peut également se produire lorsque de multiples enregistrements se produisent et qu'une seconde inscription invalide le premier jeton.

### Notifications envoyées mais non affichées sur les appareils des utilisateurs

Il y a quelques raisons pour lesquelles cela pourrait se produire:

#### L'application a été forcée de quitter

Si vous forcez l'arrêt de votre application par le biais des paramètres de votre système, vos notifications push ne seront pas envoyées. Lancer à nouveau l'application réactivera votre appareil pour recevoir des notifications push.

#### AppboyFirebaseMessagingService non enregistré

Le AppboyFirebaseMessagingService doit être enregistré correctement dans `AndroidManifest.xml` pour que les notifications push apparaissent :

```xml
<service android:name="com.braze.BrazeFirebaseMessagingService"
  android:exported="false">
  <intent-filter>
    <action android:name="com.google.firebase.MESSAGING_EVENT" />
  </intent-filter>
</service>
```

#### Le pare-feu bloque le push

Si vous testez push via Wi-Fi, votre pare-feu peut bloquer les ports nécessaires à la réception de messages par FCM. Veuillez vous assurer que les ports 5228, 5229 et 5230 sont ouverts. De plus, puisque FCM ne spécifie pas ses IPs, vous devez également autoriser votre pare-feu à accepter les connexions sortantes à toutes les adresses IP contenues dans les blocs IP listés dans l'ASN de Google de 15169.

#### Usine de notification personnalisée renvoyant NULL

Si vous avez implémenté une [usine de notification personnalisée][16], assurez-vous qu'elle ne retourne pas `null`. Cela fera que les notifications ne seront pas affichées.

### Les utilisateurs "Push registered" ne sont plus activés après l'envoi de messages

Il y a quelques raisons pour lesquelles cela pourrait se produire:

#### L'application a été désinstallée

Les utilisateurs ont désinstallé l'application. Cela invalidera leur jeton push FCM.

#### Clé de serveur de messagerie Firebase Cloud invalide

La clé Firebase Cloud Messaging Server fournie dans le tableau de bord de Braze n'est pas valide. L'ID Sender fourni devrait correspondre à celui référencé dans le fichier `braze.xml` de votre application. La clé du serveur et l'identifiant de l'expéditeur se trouvent ici dans votre Console Firebase:

!\[FirebaseServerKey\]\[20\]

### Les clics push ne sont pas enregistrés

Les logs de Braze poussent les clics automatiquement, donc ce scénario devrait être comparativement rare.

Si les clics push ne sont pas enregistrés, il est possible que les données des clics push n'aient pas encore été vidées sur les serveurs de Brase. Le brasage limite la fréquence de ses pannes en fonction de la puissance de la connexion au réseau. Avec une bonne connexion réseau, les données des clics push doivent arriver au serveur en une minute dans la plupart des cas.

### Les liens profonds ne fonctionnent pas

#### Vérifier la configuration des liens profonds

Les liens profonds peuvent être [testés avec ADB][17]. Nous vous recommandons de tester votre lien profond avec la commande suivante :

`adb shell am start -W -a android.intent.action.VIEW -d "THE_DEEP_LINK" THE_PACKAGE_NAME`

Si le lien profond ne fonctionne pas, il se peut que le lien profond soit mal configuré. Un lien profond mal configuré ne fonctionnera pas quand il sera envoyé par Braze push.

#### Vérifier la logique de gestion personnalisée

Si le lien profond [fonctionne correctement avec ADB][17] mais ne fonctionne pas à partir de Braze push, vérifier si une [gestion de push open personnalisée][18] a été implémentée. Si c'est le cas, vérifiez que le code de gestion personnalisé gère correctement le lien profond entrant.

#### Désactiver le comportement de la pile arrière

Si le lien profond [fonctionne correctement avec ADB][17] mais ne fonctionne pas depuis Braze push, essayez de désactiver [la pile arrière][22]. Pour ce faire, mettez à jour votre fichier **braze.xml** pour inclure :

```xml
<bool name="com_braze_push_deep_link_back_stack_activity_enabled">faux</bool>
```
[11]: {% image_buster /assets/img_archive/message_activity_log.png %} [20]: {% image_buster /assets/img_archive/finding_firebase_server_key.png %} "FirebaseServerKey"

[1]: https://firebase.google.com/docs/cloud-messaging/android/client
[2]: #utilizing-the-push-error-log
[3]: #scenario-1-no-push-registered-users-showing-in-the-appboy-dashboard-prior-to-sending-messages
[6]: https://firebase.google.com/docs/cloud-messaging/
[16]: #custom-displaying-notifications
[17]: https://developer.android.com/training/app-indexing/deep-linking.html#testing-filters
[17]: https://developer.android.com/training/app-indexing/deep-linking.html#testing-filters
[18]: #custom-handling-push-receipts-and-opens
[21]: https://firebase.google.com/docs/cloud-messaging/android/client#retrieve-the-current-registration-token
[22]: https://developer.android.com/guide/components/activities/tasks-and-back-stack
