---
nav_title: Notifications push
article_title: Notifications push pour Windows Universal
platform: Windows Universal
page_order: 1
description: "Cet article couvre les instructions d’intégration des notifications push pour la plateforme Windows Universal."
channel: push 
hidden: true
---

# Intégration de notifications Push
{% multi_lang_include archive/windows_deprecation.md %}

![Exemple de notification push pour Windows Universal.][10]{: style="float:right;max-width:40%;margin-left:15px;"}

Une notification push est une alerte hors application qui apparaît sur l’écran de l’utilisateur lorsqu’une mise à jour importante se produit. Les notifications push constituent un moyen précieux de fournir à vos utilisateurs un contenu urgent et pertinent, ou de les réengager dans votre application.

Pour connaître d’autres bonnes pratiques, consultez notre [documentation][9].

## Étape 1 : Configurer votre application pour les notifications push

Assurez-vous que les paramètres suivants sont configurés dans votre fichier `Package.appxmanifest` :

Dans l'onglet **Application**, assurez-vous que `Toast Capable` est défini sur `YES`.

## Étape 2 : Configurer le tableau de bord de Braze

1. [Trouvez votre SID et votre secret client][4]
2. Dans la page **Paramètres** du tableau de bord de Braze, ajoutez le SID et le Secret client dans vos paramètres.<br>![][6]

## Étape 3 : Mettre à jour pour l’enregistrement ouvert en arrière-plan

Dans votre méthode `OnLaunched` une fois que vous avez appelé `OpenSession` ajoutez l’extrait de code suivant.

```
string campaignId = e.Arguments.Split(new[] { "_ab_pn_cid" }, StringSplitOptions.None)[0];
if (!string.IsNullOrEmpty(campaignId))
{
Appboy.SharedInstance.PushManager.LogPushNotificationOpened(campaignId);          
}
```

## Étape 4 : Créer des gestionnaires d’événements

Pour écouter des événements qui sont déclenchés lorsqu’une notification push est reçue et activée (l’utilisateur a cliqué dessus), créez des gestionnaires d’événements et ajoutez-les aux événements `PushManager` :

- `Appboy.SharedInstance.PushManager.PushReceivedEvent += YourPushReceivedEventHandler;`
- `Appboy.SharedInstance.PushManager.ToastActivatedEvent += YourToastActivatedEventHandler;`

Vos gestionnaires d’événement devraient avoir les signatures suivantes :

- `void YourPushReceivedEventHandler(PushNotificationChannel sender, AppboyPushNotificationReceivedEventArgs args);`
- `void YourToastActivatedEventHandler(ToastNotification sender, AppboyToastActivatedEventArgs args);`

## Étape 5 : Créer des liens profonds entre la notification push et l’application

### Partie 1 : Créer des liens profonds pour votre application

Les liens profonds sont utilisés pour diriger les utilisateurs extérieurs à votre application directement vers un écran ou une page de votre celle-ci. Généralement, cela se fait en enregistrant un schéma d'URL (par exemple, myapp://mypage) auprès d'un système d'exploitation et en enregistrant votre application pour gérer ce schéma ; lorsque le système d'exploitation est invité à ouvrir un URL de ce format, il transfère le contrôle à votre application.

La prise en charge de liens profonds WNS est différente en ce qu’elle lance votre application avec des données portant sur l’endroit où envoyer l’utilisateur. Lorsque la notification push WNS est créée, elle peut inclure une chaîne de caractères de lancement transmise à l’application `OnLaunched` quand vous cliquez sur la notification push et que votre application est ouverte. Nous utilisons déjà cette chaîne de caractères de lancement pour réaliser le suivi de campagne et nous donnons aux utilisateurs la possibilité d’ajouter leurs propres données qui peuvent être analysées et utilisées pour diriger l’utilisateur lorsque l’application est lancée.

Si vous spécifiez une chaîne de caractères de lancement supplémentaire dans le tableau de bord ou l’API REST, elle sera ajoutée à la fin de celle que nous créons, après la clé « abextras= ». Par exemple, un exemple de chaîne de caractères de lancement peut ressembler à `ab_cn_id=_trackingid_abextras=page=settings`, dans laquelle vous avez spécifié `page=settings` dans le paramètre de chaîne de caractères de lancement supplémentaire pour que vous puissiez l’analyser et diriger l’utilisateur vers la page des paramètres.

### Partie 2 : Créer des liens profonds via le tableau de bord

Spécifiez la chaîne de caractères à ajouter à la chaîne de caractères de lancement dans le champ « Additional Launch String Configuration (Configuration de la chaîne de caractères de lancement supplémentaire) » au sein des paramètres de notification push.

![][15]

### Partie 3 : Créer des liens profonds via l’API REST

Braze permet également d'envoyer des liens profonds via l'API REST. Les [objets de notification push pour Windows Universal][13] acceptent un paramètre `extra_launch_string` facultatif.

[4]: http://msdn.microsoft.com/en-us/library/windows/apps/hh465407.aspx
[6]: {% image_buster /assets/img_archive/windows_sid.png %} "Tableau de bord Windows SID"
[9]: {{site.baseurl}}/user_guide/message_building_by_ (en anglais)channel/push/best_practices/
[10]: {% image_buster /assets/img_archive/windows_uni_push_sample.png %}
[13]: {{site.baseurl}}/api/objects_filters/messaging/windows_objects/
[15]: {% image_buster /assets/img_archive/windows_deep_link_click_action.png %} "Action de clic sur les liens profonds"
