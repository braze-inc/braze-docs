---
nav_title: Notifications push
article_title: Notifications Push pour Windows Universal
platform: Univers Windows
page_order: 1
description: "Cet article couvre les instructions d'intégration des notifications push pour la plate-forme universelle Windows."
channel: Pousser
---

# Intégration des notifications push

!\[Sample Push\]\[10\]{: style="float:right;max-width:40%;margin-left:15px;"}

Une notification push est une alerte hors application qui apparaît à l'écran de l'utilisateur lorsqu'une mise à jour importante se produit. Les notifications push sont un moyen précieux de fournir à vos utilisateurs un contenu sensible au temps et pertinent ou de les réengager avec votre application.

Visitez notre [documentation][9] pour obtenir des pratiques exemplaires supplémentaires.

## Étape 1 : Configurez votre application pour push

Assurez-vous que dans votre fichier `Package.appxmanifest` , les paramètres suivants sont configurés comme indiqué ci-dessous:

Dans l’onglet __Application__ , assurez-vous que `Toast Capable` est réglé sur `OUI`.

## Étape 2 : Configurer le tableau de bord Braze

1. Trouvez votre SID et votre Secret Client - [Instructions étape par étape][4]
2. Dans la page __Paramètres__ du tableau de bord Braze, ajoutez le SID et le Secret Client dans vos paramètres.

## Étape 3 : Mettre à jour pour les logs ouverts en arrière-plan

Dans votre méthode `OnLaunched` , après avoir appelé `OpenSession` ajouter le code snippet.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);          
}
```

!\[Tableau de bord SID Windows \]\[6\]

## Étape 4 : Créer des gestionnaires d'événements

Pour écouter les événements qui sont déclenchés lorsque le push est reçu et activé (cliqué par l'utilisateur), créez des gestionnaires d'événements et ajoutez-les aux événements `PushManager`:

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += VotrePushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += VotreToastActivatedEventHandler;`

Vos gestionnaires d'événements devraient avoir les signatures :

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## Étape 5 : En profondeur la liaison depuis push vers votre application

### Partie 1 : Création de liens profonds pour votre application

Les liens profonds sont utilisés pour naviguer les utilisateurs de l'extérieur de votre application directement vers un certain écran ou une page dans votre application. Généralement, cela se fait en enregistrant un schéma d'URL (par ex. myapp://mypage) avec un système d'exploitation et enregistrer votre application pour gérer ce schéma ; quand il est demandé à l'OS d'ouvrir une URL de ce format, il transfère le contrôle à votre application.

Le support des liens profonds WNS diffère de cela au moment où il lance votre application avec des données sur où envoyer l'utilisateur. Lorsque WNS push est créé, il peut inclure une chaîne de lancement qui est transmise à votre application `OnLaunched` lorsque le push est cliqué et que votre application est ouverte. Nous utilisons déjà cette chaîne de lancement pour faire le suivi des campagnes, et nous donnons aux utilisateurs la possibilité d'ajouter leurs propres données qui peuvent être analysées et utilisées pour naviguer dans l'utilisateur lorsque l'application est lancée.

Si vous spécifiez une chaîne de lancement supplémentaire dans le tableau de bord ou dans l'API REST, il sera ajouté à la fin de la chaîne de lancement que nous créons, après la touche "abextras=". Ainsi, un exemple de chaîne de lancement peut ressembler à `ab_cn_id=_trackingid_abextras=page=settings`, dans lequel vous avez spécifié `page=settings` dans le paramètre de chaîne de lancement supplémentaire pour que vous puissiez l'analyser et naviguer vers la page des paramètres.

### Partie 2 : Liaison profonde à travers le tableau de bord

Spécifiez la chaîne à ajouter à la chaîne de lancement dans le champ « Configuration de chaîne de lancement supplémentaire » dans les paramètres de notification push.

!\[Deep_Link_Dash_Example\]\[15\]

### Partie 3 : Liens profonds à travers l'API REST

Braze permet également d'envoyer des liens profonds à travers l'API REST. Les objets Push Universal de Windows acceptent un paramètre facultatif `extra_launch_string`. Voir l’exemple [d’objet Push Universal de Windows.][13]
[6]: {% image_buster /assets/img_archive/windows_sid.png %} "Windows SID Dashboard" [10]: {% image_buster /assets/img_archive/windows_uni_push_sample. ng %} [15]: {% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Action du lien profond"

[4]: http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx
[9]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/
[13]: {{site.baseurl}}/api/objects_filters/messaging/windows_objects/