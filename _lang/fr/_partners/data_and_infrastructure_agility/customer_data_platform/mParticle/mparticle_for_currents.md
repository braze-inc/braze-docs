---
nav_title: mParticle pour Currents
article_title: mParticle pour Currents
page_order: 0.5
alias: /partners/mparticle_for_currents/
description: "Cet article présente le partenariat entre currents Braze et mParticle, une plateforme de données client qui recueille et achemine des informations entre les différentes sources de votre pile marketing."
page_type: partner
tool: Currents
search_tag: Partenaire

---

# mParticle pour Currents

> [mParticle](https://www.mparticle.com) est une plateforme de données client qui collecte et transfère des informations issues de plusieurs sources vers divers emplacements de votre pile marketing.

L’intégration de Braze et de mParticle permet de contrôler de manière harmonieuse le flux d’informations entre les deux systèmes. Avec Currents, vous pouvez également connecter des données à mParticle pour les rendre utilisables sur tout le jeu d'outils de croissance. 

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte mParticle | Un [compte mParticle](https://app.mparticle.com/login) est requis pour profiter de ce partenariat. |
| Currents | Pour réexporter des données dans mParticle, vous devez avoir configuré [currents Braze]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
| Clé de serveur à serveur mParticle<br><br>Clé secrète de serveur à serveur mParticle | Vous pouvez obtenir ces clés en accédant à votre tableau de bord de mParticle et en créant les [flux nécessaires](#step-1-create-feeds) qui permettent à mParticle de recevoir des données d’interaction Braze pour les plateformes iOS, Android et Web.|
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer des flux

À partir de votre compte administrateur mParticle, accédez à **Configuration > Entrées**. Recherchez **Braze** dans le **Directory (Répertoire)** mParticle et ajoutez l’intégration de flux.

L’intégration de flux Braze prend en charge quatre flux distincts : iOS, Android, Web et indépendant. Le flux indépendant peut être utilisé pour des événements, tels que des e-mails qui ne sont pas connectés à une plateforme. Vous devrez créer une entrée pour chaque flux de plateforme principal. Vous pouvez créer des entrées supplémentaires à partir de **Configuration > Entrées**, sur l’onglet **Feed Configurations (Configurations des flux)**.

![][1]

Pour chaque flux, sélectionnez la plateforme correspondante dans la liste sous **Agir en tant que plateforme**. Si vous ne voyez pas d’option pour sélectionner un flux **agir en tant que**, les données seront traitées comme indépendantes, mais pourront toujours être transmises aux sorties d’entrepôt de données.

![La première boîte de dialogue d’intégration vous invite à nommer la configuration, à déterminer un statut de flux et à sélectionner une plateforme « agir en tant que ».][2]{: style="max-width:40%;"}  ![La deuxième boîte de dialogue d’intégration affichant la clé serveur à serveur et la clé secrète serveur à serveur.][3]{: style="max-width:37%;"}

mParticle vous fournira une clé et une clé secrète au moment où vous créerez chaque entrée. Copiez ces informations d’identification en faisant attention à bien noter le flux auquel correspond chaque paire d’identifiants.

### Étape 2 : Créer un Current

Dans Braze, accédez à **Currents > + Create Current (+ Créer un Current) > Create mParticle Export (Créer une exportation mParticle)**. Fournissez un nom d’intégration, une adresse e-mail de contact, la clé API mParticle et la clé secrète mParticle pour chaque plateforme. Ensuite, sélectionnez les événements que vous souhaitez suivre (consultez la liste des événements disponibles). Enfin, cliquez sur **‬Launch Current (Lancer le Current)**

![La page mParticle Currents dans Braze. Ici, vous pouvez trouver des champs pour le nom de l’intégration, l’adresse e-mail de contact, la clé API et la clé secrète.]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Il est important de garder votre clé API mParticle et votre clé secrète mParticle à jour : si les informations d’identification de votre connecteur expirent, le connecteur cessera d’envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront perdues définitivement.
{% endalert %}

Tous les événements envoyés à mParticle incluront l’`external_user_id` de l’utilisateur en tant que `customerid`. À l’heure actuelle, Braze n’envoie pas de données d’événements aux utilisateurs qui n’ont pas d’`external_user_id` défini.

## Détails de l’intégration

Vous pouvez exporter les données suivantes de Braze à mParticle :

{% tabs %}
{% tab Platform-Specific %}

| Nom de l’événement| Type de fil d’actualité| Description| Propriétés de Currents |
| --------- | -------- | ---------- | ------------------- |
| Notifications push envoyées| Fil spécifique à la plateforme | Une notification push a été envoyée avec succès à un utilisateur.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Notifications push ouvertes| Fil spécifique à la plateforme | L’utilisateur a ouvert une notification push.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Rebonds de notifications push| Fil spécifique à la plateforme | Braze n’a pas pu envoyer une notification push à cet utilisateur.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Impressions des messages in-app| Fil spécifique à la plateforme | L’utilisateur a consulté un message in-app.| `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Clics des messages in-app| Fil spécifique à la plateforme | L’utilisateur a appuyé ou cliqué sur un bouton dans un message in-app.| `button_id`, `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
| Carte de contenu envoyée| Fil spécifique à la plateforme | Une carte de contenu a été envoyée à l’appareil d’un utilisateur                                                | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Carte de contenu consultée| Fil spécifique à la plateforme | L’utilisateur a consulté une carte de contenu| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Carte de contenu cliquée| Fil spécifique à la plateforme | L’utilisateur a cliqué sur une carte de contenu| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Carte de contenu rejetée| Fil spécifique à la plateforme | L’utilisateur a rejeté une carte de contenu| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Vues du Fil d’actualité| Fil spécifique à la plateforme | L’utilisateur a vu le fil d’actualité natif de Braze.| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Vues de la carte de fil d’actualité| Fil spécifique à la plateforme | L’utilisateur a vu une carte du fil d’actualité natif de Braze.| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Clics sur la carte de fil d’actualité| Fil spécifique à la plateforme | L’utilisateur a cliqué sur une carte du fil d’actualité natif de Braze.| `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`  |
| Application désinstallée| Fil spécifique à la plateforme | L’utilisateur a désinstallé l’application.| `app_id`|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

{% alert note %}
Le Fil d’actualité est obsolète. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu - il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

{% endtab %}
{% tab Unbound %}

| Nom de l’événement| Type de fil d’actualité| Description| Propriétés de Currents |
| --------- | -------- | ---------- | ------------------- |
| E-mail envoyé| Flux indépendant| Un e-mail a été envoyé avec succès.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Livraisons par e-mail| Flux indépendant| Un e-mail a été envoyé avec succès au serveur de messagerie d’un utilisateur.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| E-mails ouverts| Flux indépendant| L’utilisateur a ouvert un e-mail.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`, `user_agent`, `machine_open`|
| Clics des e-mails| Flux indépendant| L’utilisateur a cliqué sur un lien dans un e-mail. Le suivi des clics des e-mails doit être activé. L’ID de lien et l’alias nécessitent que l’aliasage de lien soit activé | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`, `link_id`, `link_alias`, `user_agent`|
| E-mails renvoyés| Flux indépendant| Braze a tenté d’envoyer un e-mail, mais le serveur de messagerie de l’utilisateur n’a pas accepté l’e-mail. | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| E-mails désignés comme spam| Flux indépendant| L’utilisateur a désigné un e-mail comme étant du spam.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`, `user_agent`|
| E-mail Soft bounce| Flux indépendant| Braze a tenté d’envoyer un e-mail, mais le serveur de messagerie de l’utilisateur a temporairement rejeté l’e-mail. <br> <br> (Cela peut être dû à une boîte de réception pleine ou un serveur indisponible, entre autres raisons.) | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Désinscription aux e-mails| Flux indépendant| L’utilisateur a cliqué sur le lien de désinscription d’un e-mail.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| SMS envoyé| Flux indépendant| Un SMS a été envoyé à un utilisateur.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`&#42; |
| SMS envoyé à l’opérateur| Flux indépendant| Un SMS a été envoyé à l’opérateur.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`&#42; , `from_phone_number` |
| SMS livré| Flux indépendant| Un SMS a été livré avec succès.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`&#42; , `from_phone_number` |
| Échecs de livraison SMS| Flux indépendant| Un SMS qui n’a pas pu être livré avec succès.                                               | `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`&#42; , `from_phone_number`, `error`, `provider_error_code` |
| Rejets SMS| Flux indépendant| Un SMS a été rejeté.| `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`&#42; , `from_phone_number`, `error`, `provider_error_code` |
| SMS reçu| Flux indépendant| Un SMS a été reçu.| `inbound_phone_number`, `action`, `message_body` |
| Changement de statut du groupe d’abonnement| Flux indépendant| Le statut du groupe d’abonnement de l’utilisateur est passé à « Abonné » ou « Désinscrit »| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Webhook envoyé| Flux indépendant| Un message Webhook a été envoyé au nom d’un utilisateur.| `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Conversions de campagne| Flux indépendant| L’utilisateur a effectué l’événement de conversion primaire pour une campagne dans sa fenêtre de conversion.  | `campaign_id`|
| Inscriptions au groupe de contrôle de campagne | Flux indépendant| L’utilisateur a été inscrit dans un groupe de contrôle de campagne.| `campaign_id`|
| Conversions de Canvas| Flux indépendant| L’utilisateur a effectué l’événement de conversion primaire pour un Canvas dans sa fenêtre de conversion.| `canvas_step_id`, `canvas_id`, `canvas_variation_id`|
| Entrées dans le Canvas| Flux indépendant | L’utilisateur a été entré dans un Canvas.| `in_control_group`, `canvas_id`, `canvas_variation_id`|
| Expérimenter les conversions | Flux indépendant | Conversion de l'utilisateur pour une étape Canvas Experiment. | `time`, `workflow_id`, `experiment_step_id`, `experiment_split_id` `conversion_behavior_index` |
| Expérimenter les entrées fractionnées | Flux indépendant | L'utilisateur saisit une adresse d'étape Canvas Experiment. | `time`, `workflow_id`, `experiment_split_id`, `experiment_split_name`, `experiment_step_id`, `in_control_group` |
| Sortie du Canvas | Flux indépendant | L’utilisateur a quitté un Canvas en effectuant un événement ou en correspondant à une audience | `time`, `canvas_step_id`, `canvas_variation_id`, `canvas_step_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}

&#42; L’attribut [`$mobile` de mParticle](https://docs.mparticle.com/developers/server/json-reference/#user_attributes) est utilisé comme numéro de téléphone de destination (`to_phone_number`) dans mParticle.
{% endtab %}
{% endtabs %}

Pour en savoir plus sur l’intégration de mParticle, consultez la documentation de mParticle [ici](http://docs.mparticle.com/integrations/braze/feed).

[1]: {% image_buster /assets/img/braze-feed-inputs.png %}
[2]: {% image_buster /assets/img/braze-feed-act1.png %}
[3]: {% image_buster /assets/img/braze-feed-act2.png %}
