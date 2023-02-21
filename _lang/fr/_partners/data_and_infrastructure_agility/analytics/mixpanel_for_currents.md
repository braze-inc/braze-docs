---
nav_title: Mixpanel pour Currents
article_title: Mixpanel pour Currents
page_order: 0
alias: /partners/mixpanel_for_currents/
description: "Cet article présente le partenariat entre Braze Currents et Mixpanel, une plateforme d’analyse commerciale."
page_type: partner
search_tag: Partenaire
tool: Currents

---
 
# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/mixpanel-integration-with-braze/339085/scorm/2u7y2e6qrldh2){: style="float:right;width:120px;border:0;" class="noimgborder"}Mixpanel pour Currents

> [Mixpanel](https://mixpanel.com/) est une plateforme d’analyse commerciale qui vous permet d’exporter des événements depuis Mixpanel vers d’autres plateformes afin d’effectuer des analyses plus poussées. Les données collectées peuvent ensuite être utilisées pour créer des rapports personnalisés et mesurer le taux d’engagement et de rétention des utilisateurs.

L’intégration de Braze et Mixpanel vous permet d’[importer des cohortes Mixpanel dans Braze](#data-import-integration) pour créer des segments Braze qui peuvent être utilisés afin de cibler des utilisateurs dans de futures campagnes ou de futurs Canvas de Braze. Vous pouvez également tirer parti des Currents de Braze pour [exporter vos événements Braze dans Mixpanel](#data-export-integration) et effectuer des analyses plus approfondies sur les conversions, la rétention et l’utilisation des produits. 

## Conditions préalables

| Condition | Description |
|---|---|
| Compte Mixpanel | Un [Compte Mixpanel](https://mixpanel.com/) est requis pour profiter de ce partenariat. |
| Currents | Pour exporter des données dans Mixpanel, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2} 

## Intégration de l’importation de données

Utilisez le partenariat entre Braze et Mixpanel pour configurer votre intégration et importer des cohortes Mixpanel directement dans Braze afin de les recibler, créant ainsi une boucle de données complète d’un système à l’autre. Cela vous permet d’effectuer des analyses plus approfondies à l’aide de Mixpanel et d’exécuter vos stratégies de manière harmonieuse avec Braze.

Toutes les intégrations que vous avez configurées seront prises en compte dans le volume de points de données de votre compte.

{% alert important %}
Conformément aux politiques de conservation des données de Mixpanel, les événements envoyés avant le 1er janvier 2010 seront supprimés pendant l’importation.
{% endalert %}

### Étape 1 : Obtenir la clé d’importation des données Braze

Dans Braze, accédez à **Technology Partners** et sélectionnez **Mixpanel**. Ici, vous trouverez l’endpoint REST pour générer votre clé d’importation des données Braze. Une fois la clé générée, vous pouvez créer une nouvelle clé ou invalider une clé existante. La clé d’importation des données et l’endpoint REST sont utilisés à l’étape suivante lors de la configuration d’un postback dans le tableau de bord de Mixpanel.<br><br>![]({% image_buster /assets/img_archive/currents-mixpanel-edit.png %})

### Étape 2 : Configurer l’intégration Braze dans Mixpanel

Dans Mixpanel, accédez à **Gestion des données > Intégrations.** Ensuite, sélectionnez l’onglet Intégration Braze, puis cliquez sur **Connexion**. Dans l’invite qui apparaît, fournissez la clé d’importation des données de Braze et l’endpoint REST, puis cliquez sur **Continuer**.

![]({% image_buster /assets/img_archive/mixpanel2.png %}){: style="max-width:50%;"}

### Étape 3 : Exporter une cohorte Mixpanel vers Braze

Dans Mixpanel, accédez à **Gestion des données > Cohortes.** Sélectionnez la cohorte que vous souhaitez envoyer à Braze, puis cliquez sur **Exporter vers Braze**. Enfin, sélectionnez une synchronisation ponctuelle ou dynamique. La synchronisation dynamique synchronisera votre cohorte Braze toutes les 15 minutes pour qu’elle corresponde aux utilisateurs dans Mixpanel. 

![]({% image_buster /assets/img_archive/mixpanel3.png %}){: style="max-width:50%;"}

### Étape 4 : Segmenter des utilisateurs dans Braze

Dans Braze, pour créer un segment avec ces utilisateurs, accédez à **Segments** sous **Engagement**, nommez votre segment et sélectionnez **Mixpanel_Cohorts** en tant que filtre. Ensuite, utilisez l’option « includes » et choisissez la cohorte que vous avez créée dans Mixpanel. 

![Dans le générateur de segments de Braze, le filtre des attributs utilisateur « Cohortes Mixpanel » est défini sur « includes » et « cohorte de Braze ».]({% image_buster /assets/img_archive/mixpanel1.png %})

Une fois enregistré, vous pouvez référencer ce segment pendant la création d’un Canvas ou d’une campagne dans l’étape de ciblage des utilisateurs.

## Intégration de l’exportation de données

Vous trouverez ci-dessous une liste complète des événements qui peuvent être exportés de Braze vers Mixpanel. Tous les événements envoyés à Mixpanel incluront l’`external_user_id` de l’utilisateur comme ID distinct de Mixpanel. À l’heure actuelle, Braze n’envoie pas de données d’événements aux utilisateurs qui n’ont pas d’`external_user_id` défini.

Vous pouvez exporter deux types d’événements vers Mixpanel : Les [événements d’engagement par message](#message-engagement-events), qui incluent les Événements de Braze directement liés à l’envoi de messages, et les [événements de comportement client](#customer-behavior-events), qui incluent les activités d’autres applications ou sites Web, telles que des sessions, des événements personnalisés et des achats suivis sur la plateforme. Tous les événements personnalisés sont précédés d’`[Événement personnalisé Braze]`. Les propriétés de l’événement personnalisé et de l’événement d’achat sont précédées de `[Propriétés de l’événement personnalisé]` et `[Propriété d’achat]`, respectivement.

Contactez votre gestionnaire de compte ou ouvrez un [cas d’assistance][support] si vous avez besoin d’accéder à des droits d’événement supplémentaires.

### Étape 1 : Obtenir les informations d’identification Mixpanel

Dans votre tableau de bord Mixpanel, cliquez sur **Paramètres du projet** dans un nouveau projet nouveau ou dans un projet existant. Vous trouverez ici la clé secrète API Mixpanel et le jeton Mixpanel. Ces informations d’identification seront utilisées lors de la prochaine étape pour créer vos connexions Currents. 

### Étape 2 : Créer un Braze Current

Dans Braze, accédez à **Currents > + Créer un Current > Créer une exportation Mixpanel**. Fournissez un nom d’intégration, une adresse e-mail de contact, une clé secrète API Mixpanel et un jeton Mixpanel dans les champs répertoriés. Ensuite, sélectionnez les événements que vous souhaitez suivre (consultez la liste des événements disponibles). Enfin, cliquez sur **‬Launch Current (Lancer le Current)**

![Page Braze Mixpanel Currents. Cette page comprend des champs pour le nom d’intégration, l’adresse e-mail de contact, la clé secrète API et le jeton d’exportation de Mixpanel. La moitié inférieure de la page Currents répertorie les événements Currents que vous pouvez envoyer.]({% image_buster /assets/img_archive/mixpanel4.png %}){: style="max-width:80%;"}

{% tab remarque %}
Consultez les [documents d’intégration](https://help.mixpanel.com/hc/en-us/articles/360001243663) de Mixpanel pour en savoir plus. 
{% endtab %}

## Événements de comportement client

### Événements personnalisés

```json
// <Custom Event Name>
{
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements d’achat

```json
// Achat
{
  "product_id": (string) ID du produit acheté (envoyé dans le champ « productId » de l’API HTTP Mixpanel),
  "price": (float) prix du produit (envoyé dans le champ « price » (prix) de l’API HTTP Mixpanel),
  "currency": (string) code de devise ISO 4217 alphabétique à trois lettres,
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de session

```json
// Première session
{
  "session_id": (string) ID de la session,
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Démarrage de la session
{
  "session_id": (string) ID de la session,
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Fin de la session
{
  "session_id": (string) ID de la session,
  "duration": (float) durée de la session en secondes,
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de localisation

```json
// Position
{
  "longitude": (float) longitude du lieu enregistré,
  "latitude": (float) latitude du lieu enregistré,
  "altitude": (float) altitude du lieu enregistré,
  "ll_accuracy": (float) un pourcentage représentant la précision déterminée par le système d’exploitation de l’emplacement enregistré,
  "alt_accuracy": (float) précision de l’altitude du lieu enregistré,
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements d’attribution d’installation

```json
// Attribution d’installation
{
  "source": (string) la source de l’attribution
}
```

### Événements de désinstallation

```json
// Désinstallation
{
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite
}
```

## Événements d’engagement par message

### Événements de notification push

```json
// Notification push envoyée
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur.
}
// Notification push ouverte
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil,
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur.
}
// Notification Push iOS ouverte en premier plan
// Veuillez noter que cet événement n’est pas pris en charge par notre SDK Swift et est obsolète sur notre SDK Obj-C.
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur.
}
// Notification push renvoyée
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "app_id": (string) ID de l’application sur laquelle le renvoi s’est produit,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur.
}
```

### Événements par e-mail

```json
// E-mail envoyé
// Livraison des e-mails
// Ouverture des e-mails
// Clics sur les e-mails
// Renvoi d’e-mail
// Soft bounce d’e-mail
// E-mails marqués comme spam
// Désinscription des e-mails
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "email_address": (string) adresse e-mail pour cet événement,
  "url": (string) l’URL qui a été cliquée (événements e-mail cliqué uniquement),
  "user_agent": (string) description du système et du navigateur de l’utilisateur pour l’événement (événements e-mail cliqué, ouvert et marqué comme courrier indésirable uniquement),
  "link_id": (string) valeur unique générée par Braze pour l’URL (événements e-mail cliqué uniquement et nécessite l’activation de l’aliasage de lien),
  "link_alias": (string) nom d’alias défini lors de l’envoi du message (événements e-mail cliqué uniquement et nécessite l’activation de l’aliasage de lien),
  "machine_open": (string) Indicateur permettant de savoir si l’e-mail a été ouvert par un processus automatisé, comme la fonction de pré-récupération des e-mails d’Apple ou de Google. Actuellement « true » ou nul, mais une granularité supplémentaire pourrait être ajoutée à l’avenir (par ex., « Apple » ou « Google » pour indiquer quel processus a récupéré l’e-mail). (Événements e-mail ouverts uniquement)
}
```

Le comportement par rapport au `dispatch_id` diffère entre Canvas et les campagnes, car Braze traite les Canvas Steps (à l’exception des étapes d’entrée, qui peuvent être programmées) en tant qu’événements déclenchés, et ce même lorsqu’elles sont « programmées ». En savoir plus sur le[ comportement de `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) dans les campagnes et les Canvas. Pour plus d’informations, consultez [Comportement des clients et événements utilisateur]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events/) et [Événements d’engagement par message]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events/).


### Événements SMS

```json
// SMS envoyé
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string)ID de l’API du groupe d’abonnement ciblé pour ce message SMS,
}

// SMS envoyé à l’opérateur
// Envoi SMS
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string)ID de l’API du groupe d’abonnement ciblé pour ce message SMS,
  "from_phone_number": (string) le numéro de téléphone de l’expéditeur du message (remis et non remis uniquement),
}

// Rejet de SMS
// Échec de livraison SMS
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "dispatch_id": (string) ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur,
  "to_phone_number": (string) le numéro auquel le message a été envoyé,
  "subscription_group_id": (string)ID de l’API du groupe d’abonnement ciblé pour ce message SMS,
  "error": (string) Message d’erreur pour le rejet ou l’échec de livraison,
  "provider_error_code": (string) Code d’erreur pour le rejet ou l’échec de livraison,
}

// Réception d’un SMS entrant
{
  "inbound_phone_number": (string) numéro de téléphone sur lequel le message a été reçu,
  "subscription_group_id": (string) ID API du groupe d’abonnement à partir duquel ce message SMS a été reçu,
  "user_phone_number": (string) le numéro à partir duquel le message a été envoyé,
  "action": (string) l’action d’inscription prise par Braze à la suite de ce message (`subscribed` (abonné), `unsubscribed` (désabonné) ou `none` (aucun) sur la base du corps du message. `None` (Aucun) indique que ce message entrant ne correspond à aucun de vos mots-clés pour l’abonnement ou le désabonnement d’un utilisateur),
  "message_body": (string) le texte du message,
}
```

### Événements d’abonnement

```json
// Changement de statut du groupe d’abonnement
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "email_address": (string) adresse e-mail pour cet événement,
  "subscription_group_id": (string) ID du groupe d’abonnement,
  "subscription_status": (string) statut de l’abonnement après le changement : 'Abonné' ou 'Désabonné'
}
```

### Événements de messages in-app

```json
// Impression des messages in-app
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Clics des messages in-app
{
  "button_id": (string) index du bouton cliqué, s’il s’agit d’un bouton cliqué, ou ID de suivi du clic, si l’événement provient d’un appel appboyBridge.logClick, ou choice_id si le type de message in-app est un simple sondage.,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de Webhook

```json
// Webhook envoyé
{
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API)
}
```

### Événements de carte de contenu

```json
// Carte de contenu envoyée
{
  "card_id": (string) ID de la carte de contenu qui a été envoyée,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API)
}
```

```json
// Impression de la carte de contenu
// Carte de contenu cliquée
// Carte de contenu rejetée
{
  "card_id": (string) ID de la carte de contenu qui a été visualisée/clicked/dismissed,
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "campaign_id": (string) ID de la campagne si provenant d’une campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message si provenant d’une campagne,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API),
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de fil d’actualité

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

```json
// Impression de la carte de fil d’actualité
{
  "card_id": (string) ID de la carte qui a été visualisée,
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Clics sur la carte de fil d’actualité
{
  "card_id": (string) ID de la carte qui a été cliquée,
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
// Impression du fil d’actualité
{
  "app_id": (string) ID de l’application sur laquelle l’action de l’utilisateur s’est produite,
  "platform": (string) plateforme de l’appareil (iOS, Android, Web, etc.),
  "os_version": (string) version du système d’exploitation de l’appareil utilisé pour l’action,
  "device_model": (string) modèle matériel de l’appareil
}
```

### Événements de conversion

```json
// Événements de conversion de campagne
{
  "campaign_id": (string) ID de la campagne,
  "campaign_name": (string) nom de la campagne,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne de caractères encodée en JSON décrivant le comportement de conversion,
  "message_variation_id": (string) ID de la variation du message,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API)
}
// Événements de conversion Canvas
{
  "canvas_id": (string) ID du Canvas,
  "canvas_name": (string) nom du Canvas,
  "conversion_behavior_index": (int) index du comportement de conversion,
  "conversion_behavior": (string) chaîne de caractères encodée en JSON décrivant le comportement de conversion,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "canvas_step_id": (string) ID de la dernière étape à laquelle l’utilisateur a été envoyé avant la conversion
}
```

### Événements d’entrée Canvas

```json
// Entrée Canvas
{
  "canvas_id": (string) ID du Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "in_control_group": (boolean) si l’utilisateur était inscrit dans le groupe de contrôle pour un Canvas
}
```

### Événements d'étape de test

```json
// Entrée de direction fractionnée de l’étape expérimentale
{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_name": (string) nom du Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "canvas_variation_name": (string) nom de la variation Canvas dans laquelle se trouve l’utilisateur s’il provient d’un Canvas,
  "experiment_step_id": (string) ID BSON de l’étape d’expérience à laquelle appartient cet événement,
  "canvas_step_id": (string) ID de l’étape pour ce message s’il provient d’un Canvas,
  "canvas_step_name": (string) nom de l’étape pour ce message s’il provient d’un Canvas,
  "experiment_split_id": (string) ID BSON de la division d’expérience à laquelle l’utilisateur s’est inscrit,
  "experiment_split_name": (string) nom de la division d’expérience à laquelle l’utilisateur s’est inscrit,
  "in_control_group": (boolean) si l’utilisateur était inscrit dans le groupe de contrôle
}

// Conversion d’étape de test
{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "app_group_id": (string) ID BSON du groupe d’apps auquel appartient cet utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "workflow_id": (string) ID Braze à usage interne du flux de travail auquel cet événement appartient,
  "experiment_step_id": (string) ID BSON de l’étape d’expérience à laquelle appartient cet événement,
  "experiment_split_id": (string) ID BSON de la variation de répartition du test reçue par cet utilisateur,
  "conversion_behavior_index": (int) index du comportement de conversion
}
```

### Événements d’inscription à la campagne

```json
// Inscription au groupe de contrôle de campagne
{
  "campaign_id": (string) ID de la campagne,
  "campaign_name": (string) nom de la campagne,
  "message_variation_id": (string) ID de la variation du message,
  "send_id": (string) ID du message si spécifié pour la campagne (voir Envoyer un identifiant sous Types d’identifiant API)
}
```

### Événements de sortie Canvas

```json
// Sortie du Canvas ayant effectué un événement
// Sortie du Canvas par correspondance à une audience
{
  "id": (string) ID global unique de cet événement,
  "user_id": (string) ID utilisateur Braze de l’utilisateur, 
  "external_user_id": (string) ID utilisateur externe de l’utilisateur,
  "app_group_id": (string) ID BSON du groupe d’apps auquel appartient cet utilisateur,
  "app_group_api_id": (string) ID API du groupe d’apps auquel appartient cet utilisateur,
  "time": (int) horodatage Unix de l’événement,
  "canvas_id": (string) ID du Canvas s’il provient d’un Canvas,
  "canvas_variation_id": (string) ID de la variation Canvas dans laquelle se trouve l’utilisateur,
  "canvas_step_id": (string) ID BSON de Canvas Step à laquelle appartient cet événement,
  "canvas_api_id": (string) ID API du Canvas auquel appartient cet événement,
  "canvas_variation_api_id": (string) ID API de la variation de Canvas auquel appartient cet événement,
  "canvas_step_api_id": (string) ID API de Canvas Step à laquelle appartient cet événement,
}
```

[support]: {{site.baseurl}}/braze_support/
[1]: {% image_buster /assets/img_archive/mixpanel1.png %}
[2]: {% image_buster /assets/img_archive/mixpanel2.png %}
[3]: {% image_buster /assets/img_archive/mixpanel3.png %}
[4]: {% image_buster /assets/img_archive/mixpanel4.png %}
