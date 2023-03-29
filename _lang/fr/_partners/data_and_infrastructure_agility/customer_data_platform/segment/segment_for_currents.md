---
nav_title: Segment.io pour Currents
article_title: Segment.io pour Currents
page_order: 1.2
alias: /partners/segment_for_currents/
description: "Cet article de référence présente le partenariat entre Currents Braze et Segment.io, une plateforme de données client qui recueille et transfère des informations entre les différentes sources de votre pile marketing."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# Segment.io pour Currents  

> [Segment.io](https://segment.com) est une plateforme de données client qui vous aide à collecter, nettoyer et activer vos données client. Cet article de référence présente un aperçu de la connexion entre Currents Braze et Segment et décrit les exigences et les processus nécessaires pour assurer une mise en œuvre et une utilisation adaptées.

L’intégration de Braze et Segment.io vous permet de tirer parti de Currents Braze pour exporter vos événements Braze dans Segment.io et effectuer des analyses plus avancées sur les conversions, la rétention et l’utilisation des produits. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Segment.io | Un [compte Segment.io](https://app.segment.com/login) est requis pour profiter de ce partenariat. |
| Utiliser Braze en tant que destination | Vous devez avoir déjà [configuré Braze en tant que destination]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings/) dans votre intégration Segment.io.<br><br>Vous devez également avoir fourni le bon centre de données Braze et la bonne clé API REST dans vos [paramètres de connexion]({{site.baseurl}}/partners/data_and_infrastructure_agility/customer_data_platform/segment/segment/#connection-settings). |
| Currents | Pour réexporter des données dans Segment.io, vous devez avoir configuré [Currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Obtenir la clé d’écriture Segment.io

1. Dans votre tableau de bord Segment.io, sélectionnez votre source Segment.io. Ensuite, accédez à **Settings > API keys (Paramètres > Clés API)**. Vous trouverez ici la **clé d’écriture Segment.io**.
2. Dans Braze, accédez à **Currents > + Create Currents > Create Segment.io Export (Currents > + Créer des Currents > Créer une exportation Segment.io)**.
3. Ensuite, fournissez un nom d’intégration, une adresse e-mail de contact, une clé d’écriture et la région Segment.io.

![La page Currents Segment.io dans Braze. Ici, vous pouvez trouver des champs pour le nom de l’intégration, l’adresse e-mail de contact, la région Segment et la clé API.][3]

{% alert warning %}
Il est important de garder votre clé d’écriture Segment.io à jour. Le connecteur arrêtera d’envoyer des événements si les informations d’identification de votre connecteur expirent. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}

### Étape 2 : Exporter des événements d’engagement par message 

Ensuite, sélectionnez les événements d’engagement par message que vous souhaitez exporter. Reportez-vous aux événements d’exportation et au tableau des propriétés ci-dessous. Tous les événements envoyés à Segment.io incluront l’`external_user_id` de l’utilisateur en tant que `userId`. À l’heure actuelle, Braze n’envoie pas de données d’événements aux utilisateurs qui n’ont pas d’`external_user_id` défini.

![Liste de tous les événements d’engagement par message disponibles sur la page Currents Segment.io de Braze.][2]

Enfin, cliquez sur **Lancer Current**.

{% alert warning %}
Si vous avez l’intention de créer plusieurs connecteurs Currents identiques (par exemple, deux connecteurs d’événement d’engagement par message), ces connecteurs doivent faire partie de différents groupes d’apps. L’intégration Currents Segment.io dans Braze ne permet pas d’isoler des événements de différentes applications dans un seul groupe d’apps, le non-respect de cette consigne entraînera des dédoublements et des pertes de données. 
{% endalert %}

Pour en savoir plus, consultez la [documentation](https://segment.com/docs/sources/cloud-apps/appboy/) de Segment.io.

## Configuration des données

{% tabs %}
{% tab Export events %}

Vous pouvez exporter les données suivantes de Braze à Segment.io :

| Nom de l’événement | Description |
| ----- | ----- |
| Notification push envoyée         | Une notification push a été envoyée avec succès. |
| Notification push ouverte       | L’utilisateur a ouvert une notification push. |
| Notification push renvoyée      | Braze n’a pas pu envoyer une notification push à cet utilisateur. |
| Notification push ouverte en premier plan sur iOS     | L’utilisateur a reçu une notification push sur iOS pendant que l’application était ouverte. <br> (Veuillez noter que cet événement est déprécié sur notre SDK Obj-C et n'est pas supporté par notre [SDK Swift](https://github.com/braze-inc/braze-swift-sdk)).|
| E-mail envoyé                     | Un e-mail a été envoyé avec succès. |
| E-mail livré                | Un e-mail a été envoyé avec succès au serveur de messagerie d’un utilisateur. |
| E-mail ouvert                   | L’utilisateur a ouvert un e-mail. |
| Lien de l’e-mail cliqué             | L’utilisateur a cliqué sur un lien dans un e-mail. Le suivi des clics des e-mails doit être activé. |
| Hard bounce d’e-mail                  | Braze a tenté d’envoyer un e-mail, mais le serveur de messagerie de l’utilisateur n’a pas accepté l’e-mail. |
| Soft bounce d’e-mail             | Braze a tenté d’envoyer un e-mail, mais le serveur de messagerie de l’utilisateur a temporairement rejeté l’e-mail. <br> <br> (Cela peut être dû à une boîte de réception pleine ou un serveur indisponible, entre autres raisons.) |
| E-mail désigné comme spam           | L’utilisateur a désigné un e-mail comme étant du spam. |
| Désinscription e-mail             | L’utilisateur a cliqué sur le lien de désinscription d’un e-mail. |
| SMS envoyé                       | Un SMS a été envoyé. |
| SMS envoyé à l’opérateur            | Un SMS a été envoyé à l’opérateur pour être livré. |
| SMS livré                  | Un SMS a été livré avec succès. |
| Échec de livraison SMS            | Un SMS n’a pas pu être livré avec succès. |
| SMS rejeté                   | Un SMS a été rejeté. |
| SMS reçu           | Un SMS a été reçu. |
| Changement de statut du groupe d’abonnement | Le statut du groupe d’abonnement de l’utilisateur est passé à « Abonné » ou « Désinscrit ». |
| Message in-app consulté          | L’utilisateur a consulté un message in-app. |
| Message in-app cliqué         | L’utilisateur a appuyé ou cliqué sur un bouton dans un message in-app. |
| Carte de contenu envoyée              | Une carte de contenu a été envoyée à l’appareil d’un utilisateur. |
| Carte de contenu consultée            | L’utilisateur a consulté une carte de contenu. |
| Carte de contenu cliquée           | L’utilisateur a cliqué sur une carte de contenu. |
| Carte de contenu rejetée         | L’utilisateur a rejeté une carte de contenu. |
| Fil d’actualité consulté               | L’utilisateur a vu le fil d’actualité natif de Braze. |
| Carte de fil d’actualité visionnée          | L’utilisateur a vu une carte du fil d’actualité natif de Braze. |
| Carte de fil d’actualité cliquée         | L’utilisateur a cliqué sur une carte du fil d’actualité natif de Braze. |
| Webhook envoyé                   | Un message Webhook a été envoyé. |
| Campagne convertie             | L’utilisateur a effectué un événement de conversion pour une campagne dans sa fenêtre de conversion. |
| Canvas converti               | L’utilisateur a effectué un événement de conversion pour un Canvas dans sa fenêtre de conversion. |
| Entré dans un Canvas                 | L’utilisateur a été entré dans un Canvas. |
| Inscrit dans un groupe de contrôle de campagne | L’utilisateur a été inscrit dans un groupe de contrôle de campagne. |
| Application désinstallée        | L’utilisateur a désinstallé l’application. |
| Expérimenter les conversions | Conversion de l'utilisateur pour une étape Canvas Experiment. |
| Expérimenter les entrées fractionnées | L'utilisateur saisit une adresse d'étape Canvas Experiment. |
| Sortie du Canvas | L’utilisateur a quitté un Canvas en effectuant un événement ou en correspondant à une audience. | 
{: .reset-td-br-1 .reset-td-br-2}

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

{% endtab %}
{% tab Export properties %}

Les propriétés suivantes seront incluses avec tous les événements Braze envoyés à Segment.io :

| Nom de la propriété          | Type     | Description |
| ---------------------- | -------- | ----        |
| `app_id`               | `String` | L’identificateur d’API de l’application sur laquelle un utilisateur a reçu un message ou effectué une action, le cas échéant. |
| `send_id`              | `String` | L’ID du message si indiqué pour la campagne, le cas échéant. |
| `dispatch_id`          | `String` | L’ID de distribution du message (ID unique pour chaque « transmission » envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message planifié reçoivent le même dispatch_id. Les messages basés sur des actions ou les messages déclenchés par API reçoivent un dispatch_id unique pour chaque utilisateur. |
| `campaign_id`          | `String` | L’identificateur d’API de la campagne associée à l’événement, le cas échéant. |
| `campaign_name`        | `String` | Le nom de la campagne associée à l’événement, le cas échéant. |
| `message_variation_id` | `String` | L’identificateur d’API de la variante du message pour la campagne associée à l’événement, le cas échéant. |
| `canvas_id`            | `String` | L’identificateur d’API du Canvas associé à l’événement, le cas échéant. |
| `canvas_name`          | `String` | Le nom du Canvas associé à l’événement, le cas échéant. |
| `canvas_variation_id`  | `String` | L’identificateur d’API de la variante du Canvas associée à l’événement, le cas échéant.                           |
| `canvas_step_id`       | `String` | L’identificateur d’API du Canvas Step associé à l’événement, le cas échéant. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Les propriétés suivantes seront incluses avec certains événements Braze envoyés à Segment.io :

| Nom de la propriété               | Type     | Description                                                                                                                                                                                                                                                                                |
|-----------------------------| -------- |--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `in_control_group`          | `String` | Pour les événements Entré dans un Canvas, que l’utilisateur soit inclus ou non dans le groupe de contrôle : toujours `true` soit `false`                                                                                                                                                                     |
| `context.traits.email`      | `String` | Pour les événements E-mail, l’adresse e-mail à laquelle l’e-mail a été envoyé.                                                                                                                                                                                                                            |
| `link_url`                  | `String` | Pour les événements E-mail cliqué, l’URL du lien sur lequel l’utilisateur a cliqué.                                                                                                                                                                                                                    |
| `button_id`                 | `String` | Pour les événements Message in-app cliqué, l’index du bouton sur lequel l’utilisateur a cliqué.                                                                                                                                                                                                            |
| `card_id`                   | `String` | Pour les événements Carte de fil d’actualité et Carte de contenu, l’Identificateur d’API de la carte.                                                                                                                                                                                                                |
| `subscription_group_id`     | `String` | Pour les événements Changement de statut du groupe d’abonnement, l’identificateur d’API du groupe d’abonnement.                                                                                                                                                                                                 |
| `subscription_status`       | `String` | Pour les événements Changement de statut du groupe d’abonnement, le nouveau statut de l’utilisateur : `Subscribed` ou `Unsubscribed`.                                                                                                                                                                        |
| `user_agent`                | `String` | Pour les événements E-mail cliqué et E-mail ouvert, événements marqués comme spam, la description du système et le navigateur de l’utilisateur pour l’événement.                                                                                                                                                                        |
| `link_id`                   | `String` | Pour les événements E-mail cliqué, la valeur unique générée par Braze pour l’URL. Nul, sauf si la fonction d’aliasage de lien est activée.                                                                                                                                                                                 |
| `link_alias`                | `String` | Pour les événements E-mail cliqué, l’alias défini lorsque le message a été envoyé. Nul, sauf si la fonction d’aliasage de lien est activée.                                                                                                                                                                                    |
| `machine_open`              | `String` | Pour les événements E-mail ouvert, un indicateur permettant de savoir si l’e-mail a été ouvert par un processus automatisé, comme la fonction de pré-récupération des e-mails d’Apple ou de Google. Actuellement `true` ou nul, mais une granularité supplémentaire pourrait être ajoutée à l’avenir (par ex., « Apple » ou « Google » pour indiquer quel processus a récupéré l’e-mail). |
| `conversion_behavior_index` | `Int`    | Pour les conversions de Canvas, les campagnes de conversion et événements de conversion d'étape d'expérience, index du comportement de conversion.                                                                                                                                                                   |
| `conversion_behavior`       | `String` | Pour les conversions Canvas, les campagnes de conversion et événements de conversion d'étape d'expérience, une chaîne de caractères codée en JSON décrivant le comportement de conversion.                                                                                                                                               |
| `experiment_step_id`        | `String` | Pour les événements de conversion d'étape d'expérience et de saisie de fractionnement d'étape d'expérience, l'identifiant API de l'étape d'expérience à laquelle appartient cet événement.                                                                                                                                                             |
| `experiment_split_id`       | `String` | Pour les événements de conversion d'étape d'expérience et de saisie de fractionnement d'étape d'expérience, l'identifiant API du fractionnement d'expérience auquel l'utilisateur s'est inscrit.                                                                                                                                                            |
| `experiment_split_name`     | `String` | Pour les événements de conversion d'étape d'expérience et de saisie de fractionnement d'étape d'expérience, le nom du fractionnement de l'expérience.                                                                                                                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

{% endtab %}
{% endtabs %}

[1]: {% image_buster /assets/img/segment/segment_currents1.png %}
[2]: {% image_buster /assets/img/segment/segment_currents.png %}
[3]: {% image_buster /assets/img/segment/segment.png %}
