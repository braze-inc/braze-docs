---
nav_title: Mixpanel pour Currents
article_title: Mixpanel pour Currents
page_order: 0
alias: /partners/mixpanel_for_currents/
description: "Cet article de référence présente le partenariat entre Currents Braze et Mixpanel, une plateforme d’analyses commerciales qui vous permet d’importer des cohortes Mixpanel dans Braze pour créer des segments Braze qui peuvent être utilisés afin de cibler des utilisateurs dans de futures campagnes ou de futurs Canvas de Braze."
page_type: partner
search_tag: Partenaire
tool: Currents

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel pour Currents

> [Mixpanel](https://mixpanel.com/) est une plateforme d’analyses commerciales qui vous permet d’exporter des événements depuis Mixpanel vers d’autres plateformes afin d’effectuer des analyses plus poussées. Les données collectées peuvent ensuite être utilisées pour créer des rapports personnalisés et mesurer le taux d’engagement et de rétention des utilisateurs.

L’intégration de Braze et Mixpanel vous permet d’[importer des cohortes Mixpanel dans Braze](#data-import-integration) pour créer des segments Braze qui peuvent être utilisés afin de cibler des utilisateurs dans de futures campagnes ou de futurs Canvas de Braze. Vous pouvez également tirer parti des currents Braze pour [exporter vos événements Braze dans Mixpanel](#data-export-integration) et effectuer des analyses plus approfondies sur les conversions, la rétention et l’utilisation des produits.

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Mixpanel | Un [Compte Mixpanel](https://mixpanel.com/) est requis pour profiter de ce partenariat. |
| Currents | Pour exporter des données dans Mixpanel, vous devez avoir configuré [currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration de l’importation de données

Utilisez le partenariat entre Braze et Mixpanel pour configurer votre intégration et importer des cohortes Mixpanel directement dans Braze afin de les recibler, créant ainsi une boucle de données complète d’un système à l’autre. Cela vous permet d’effectuer des analyses plus approfondies à l’aide de Mixpanel et d’exécuter vos stratégies de manière harmonieuse avec Braze.

Toutes les intégrations que vous avez configurées seront prises en compte dans le volume de points de données de votre compte.

{% alert important %}
Conformément aux politiques de conservation des données de Mixpanel, les événements envoyés avant le 1er janvier 2010 seront supprimés pendant l’importation.
{% endalert %}

### Étape 1 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners (Partenaires technologiques)** et sélectionnez **Mixpanel**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés à l’étape suivante lors de la configuration d’un postback dans le tableau de bord de Mixpanel.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Étape 2 : Configurer l’intégration Braze dans Mixpanel

Dans Mixpanel, accédez à **Data Management > Integrations (Gestion des données > Intégrations).** Ensuite, sélectionnez l’onglet Intégration Braze, puis cliquez sur **Connect (Connexion)**. Dans l’invite qui apparaît, fournissez la clé d’importation des données de Braze et l’endpoint REST, puis cliquez sur **Continue (Continuer)**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Étape 3 : Exporter une cohorte Mixpanel vers Braze

Dans Mixpanel, accédez à **Data Management > Cohorts (Gestion des données > Cohortes).** Sélectionnez la cohorte que vous souhaitez envoyer à Braze, puis cliquez sur **Export to Braze (Exporter vers Braze)**. Enfin, sélectionnez une synchronisation ponctuelle ou dynamique. La synchronisation dynamique synchronisera votre cohorte Braze toutes les 15 minutes pour qu’elle corresponde aux utilisateurs dans Mixpanel.

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

### Étape 4 : Segmenter des utilisateurs dans Braze

Dans Braze, pour créer un segment avec ces utilisateurs, accédez à **Segments** sous **Engagement**, nommez votre segment et sélectionnez **Mixpanel_Cohorts** en tant que filtre. Ensuite, utilisez l’option « includes » et choisissez la cohorte que vous avez créée dans Mixpanel.

![Dans le générateur de segments de Braze, le filtre des attributs utilisateur « Cohortes Mixpanel » est défini sur « includes » et « cohorte de Braze ».]({% image_buster /assets/img_archive/mixpanel1.png %})

Une fois enregistré, vous pouvez référencer ce segment pendant la création d’un Canvas ou d’une campagne dans l’étape de ciblage des utilisateurs.

## Intégration de l’exportation de données

Vous trouverez ci-dessous une liste complète des événements qui peuvent être exportés de Braze vers Mixpanel. Tous les événements envoyés à Mixpanel incluront l’`external_user_id` de l’utilisateur comme ID distinct de Mixpanel. À l’heure actuelle, Braze n’envoie pas de données d’événements aux utilisateurs qui n’ont pas d’`external_user_id` défini.

Vous pouvez exporter deux types d’événements vers Mixpanel : Les [événements d’engagement par message](#message-engagement-events), qui incluent les Événements de Braze directement liés à l’envoi de messages, et les [événements de comportement client](#customer-behavior-events), qui incluent les activités d’autres applications ou sites Web, telles que des sessions, des événements personnalisés et des achats suivis sur la plateforme. Tous les événements personnalisés sont précédés par `[Braze Custom Event]`. Les propriétés de l’événement personnalisé et d’achat sont précédées par `[Custom event property]` et `[Purchase property]`, respectivement.

Contactez votre gestionnaire de compte ou ouvrez un [ticket de support][support] si vous avez besoin d’accéder à d’autres événements.

### Étape 1 : Obtenir les informations d’identification Mixpanel

Dans votre tableau de bord Mixpanel, cliquez sur **Project Settings (Paramètres du projet)** dans un nouveau projet nouveau ou dans un projet existant. Vous trouverez ici la clé secrète API Mixpanel et le jeton Mixpanel. Ces informations d’identification seront utilisées lors de la prochaine étape pour créer vos connexions Currents.

### Étape 2 : Créer un current Braze

Dans Braze, accédez à **Currents > + Create Current (+ Créer un Current) > Create Mixpanel Export (Créer une exportation Mixpanel)**. Fournissez un nom d’intégration, une adresse e-mail de contact, une clé secrète API Mixpanel et un jeton Mixpanel dans les champs répertoriés. Ensuite, sélectionnez les événements que vous souhaitez suivre (consultez la liste des événements disponibles). Enfin, cliquez sur **‬Launch Current (Lancer le Current)**

![Page Braze Mixpanel Currents. Cette page comprend des champs pour le nom d’intégration, l’adresse e-mail de contact, la clé secrète API et le jeton d’exportation de Mixpanel. La moitié inférieure de la page Currents répertorie les événements Currents que vous pouvez envoyer.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab note %}
Consultez les [documents d’intégration](https://help.mixpanel.com/hc/en-us/articles/360001243663) de Mixpanel pour en savoir plus.
{% endtab %}

## Événements de comportement client

### Événements personnalisés

```json
// <Custom Event Name>
{
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Événements d’achat

```json
// Purchase
{
  "product_id": (string) id of product purchased (sent in the "productId" field of Mixpanel HTTP API),
  "price": (float) price of product (sent in the "price" field of Mixpanel HTTP API),
  "currency": (string) three letter alpha ISO 4217 currency code,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Événements de session

```json
// First Session
{
  "session_id": (string) id of the session,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// Session Start
{
  "session_id": (string) id of the session,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// Session End
{
  "session_id": (string) id of the session,
  "duration": (float) seconds session lasted,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Événements de localisation

```json
// Location
{
  "longitude": (float) longitude of recorded location,
  "latitude": (float) latitude of recorded location,
  "altitude": (float) altitude of recorded location,
  "ll_accuracy": (float) a percentage representing the OS determined accuracy of the recorded location,
  "alt_accuracy": (float) altitude accuracy of recorded location,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Événements d’attribution d’installation

```json
// Install Attribution
{
  "source": (string) the source of the attribution
}
```

### Événements de désinstallation

```json
// Uninstall
{
  "app_id": (string) id for the app on which the user action occurred
}
```

## Événements d’engagement par message

### Événements de notification push

```json
// Push Notification Send
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.
}
// Push Notification Open
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device,
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.
}
// Push Notification iOS Foreground Open
// Please note, this event is not supported by our Swift SDK and is deprecated on our Obj-C SDK.
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.
}
// Push Notification Bounce
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the bounce occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.
}
```

### Événements par e-mail

```json
// Email Send
// Email Delivery
// Email Open
// Email Click
// Email Bounce
// Email Soft Bounce
// Email Mark As Spam
// Email Unsubscribe
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click, Open, and Mark as Spam events only),
  "link_id": (string) unique value generated by Braze for the URL (Email Click events only and requires link aliasing to be enabled),
  "link_alias": (string) alias name set when the message was sent (Email Click events only and requires link aliasing to be enabled),
  "machine_open": (string) Indicator of whether the email was opened by an automated process, such as Apple or Google mail pre-fetching. Currently "true" or null, but additional granularity (e.g., "Apple" or "Google" to indicate which process made the fetch) may be added in the future. (Email Open events only)
}
```

Le comportement par rapport au `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les Canvas Steps (à l’exception des étapes d’entrée, qui peuvent être programmées) en tant qu’événements déclenchés, et ce même lorsqu’elles sont « programmées ». En savoir plus sur le [comportement de `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans les campagnes et les Canvas. Pour plus d’informations, consultez [Comportement des clients et événements utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) et [Événements d’engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).


### Événements SMS

```json
// SMS Send
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "to_phone_number": (string) the number the message was sent to,
  "subscription_group_id": (string) api id of the subscription group targeted for this SMS message,
}

// SMS Send To Carrier
// SMS Delivery
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "to_phone_number": (string) the number the message was sent to,
  "subscription_group_id": (string) api id of the subscription group targeted for this SMS message,
  "from_phone_number": (string) the from phone number of the message (Delivered and Undelivered only),
}

// SMS Rejection
// SMS Delivery Failure
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) id of the message dispatch (unique id for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "to_phone_number": (string) the number the message was sent to,
  "subscription_group_id": (string) api id of the subscription group targeted for this SMS message,
  "error": (string) Error message for the rejection or delivery failure,
  "provider_error_code": (string) Error code for the rejection or delivery failure,
}

// SMS Inbound Receipt
{
  "inbound_phone_number": (string) phone number on which the message was received,
  "subscription_group_id": (string) api id of the subscription group from which this SMS message was received,
  "user_phone_number": (string) the number from which message was sent,
  "action": (string) the subscription action Braze took as a result of this message (either `subscribed`, `unsubscribed` or `none` based on the message body. `None` indicates this inbound message did not match any of your keywords to opt-in or opt-out a user),
  "message_body": (string) the text of the message,
}
```

### Événements d’abonnement

```json
// Subscription Group State Change
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "email_address": (string) email address for this event,
  "subscription_group_id": (string) id of the subscription group,
  "subscription_status": (string) status of the subscription after the change: 'Subscribed' or 'Unsubscribed'
}
```

### Événements de messages in-app

```json
// In-app message Impression
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// In-app message Click
{
  "button_id": (string) index of the button clicked if it was a button that was clicked, tracking ID of the click if the event came from an appboyBridge.logClick invocation, or choice_id if the in app-message type is a simple survey,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Événements de Webhook

```json
// Webhook Send
{
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

### Événements de carte de contenu

```json
// Content Card Send
{
  "card_id": (string) id of the content card that was sent,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

```json
// Content Card Impression
// Content Card Click
// Content Card Dismiss
{
  "card_id": (string) id of the content card that was viewed/clicked/dismissed,
  "app_id": (string) id for the app on which the user action occurred,
  "campaign_id": (string) id of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation if from a campaign,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Événements de fil d’actualité

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

```json
// News Feed Card Impression
{
  "card_id": (string) id of the card that was viewed,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// News Feed Card Click
{
  "card_id": (string) id of the card that was clicked,
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
// News Feed Impression
{
  "app_id": (string) id for the app on which the user action occurred,
  "platform": (string) platform of the device (iOS, Android, web, etc.),
  "os_version": (string) os version of device used for the action,
  "device_model": (string) hardware model of the device
}
```

### Événements de conversion

```json
// Campaign Conversion Event
{
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "message_variation_id": (string) id of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
// Canvas Conversion Event
{
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "conversion_behavior_index": (int) index of the conversion behavior,
  "conversion_behavior": (string) JSON-encoded string describing the conversion behavior,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_step_id": (string) id of the last step the user was sent before the conversion
}
```

### Événements d’entrée Canvas

```json
// Canvas Entry
{
  "canvas_id": (string) id of the Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "in_control_group": (boolean) whether the user was enrolled in the control group for a Canvas
}
```

### Événements d'étape de test

```json
// Experiment Step Split Path Entry
{
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External user ID of the user,
  "time": (int) unix timestamp at which the event happened,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "experiment_step_id": (string) BSON ID of the experiment step this event belongs to,
  "canvas_step_id": (string) id of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "experiment_split_id": (string) BSON ID of the experiment split the user enrolled in,
  "experiment_split_name": (string) name of the experiment split the user enrolled in,
  "in_control_group": (boolean) whether the user was enrolled in the control group
}

// Experiment Step Conversion
{
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "workflow_id": (string) internal-use Braze ID of the workflow this event belongs to,
  "experiment_step_id": (string) BSON ID of the experiment step this event belongs to,
  "experiment_split_id": (string) BSON ID of the experiment split variation this user received,
  "conversion_behavior_index": (int) index of the conversion behavior
}
```

### Événements d’inscription à la campagne

```json
// Campaign Control Group Enrollment
{
  "campaign_id": (string) id of the campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) id of the message variation,
  "send_id": (string) id of the message if specified for the campaign (See Send Identifier under API Identifier Types)
}
```

### Événements de sortie Canvas

```json
// Canvas Exit Performed Event
// Canvas Exit Matched Audience
{
  "id": (string) globally unique ID of this event,
  "user_id": (string) Braze user id of the user,
  "external_user_id": (string) External user ID of the user,
  "app_group_id": (string) BSON id of the app group this user belongs to,
  "app_group_api_id": (string) API ID of the app group this user belongs to,
  "time": (int) unix timestamp at which the event happened,
  "canvas_id": (string) id of the Canvas if from a Canvas,
  "canvas_variation_id": (string) id of the Canvas variation the user is in,
  "canvas_step_id": (string) BSON id of the Canvas step this event belongs to,
  "canvas_api_id": (string) API id of the Canvas this event belongs to,
  "canvas_variation_api_id": (string) API id of the canvas variation this event belongs to,
  "canvas_step_api_id": (string) API id of the canvas step this event belongs to,
}
```

[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}
