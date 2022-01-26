---
nav_title: mParticule pour les courants
article_title: mParticule pour les courants
page_order: 0.5
alias: /fr/partners/mparticle_for_currents/
description: "Cet article décrit le partenariat entre Braze Currents et mParticle, une plateforme de données client qui collecte et achemine des informations entre les sources dans votre pile de marketing."
page_type: partenaire
tool: Courants
search_tag: Partenaire
---

# mParticule pour les courants

> [mParticle](https://www.mparticle.com) est une plate-forme de données client qui collecte et achemine des informations à partir de sources multiples vers une variété d'autres emplacements de votre pile marketing.

L'intégration de Braze et mParticle vous permet de contrôler de façon transparente le flux d'informations entre les deux systèmes. Avec les courants, vous pouvez également connecter des données à mParticle pour le rendre utilisable sur toute la pile de croissance.

## Pré-requis

| Exigences                                                                       | Libellé                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| compte mParticule                                                               | Un [compte mParticle](https://app.mparticle.com/login) est requis pour profiter de ce partenariat.                                                                                                                                                       |
| Courants                                                                        | Afin d'exporter les données vers Mixpanel, vous devez avoir [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) configuré pour votre compte.                                                                |
| mParticle server à la clé de serveur<br><br>mParticle server secret | Celles-ci peuvent être obtenues en naviguant sur votre tableau de bord mParticle et en créant les [flux nécessaires](#step-1-create-feeds) qui permettent à mParticle de recevoir des données d'interaction Braze pour iOS, Android, et plateformes Web. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Créer des flux

Depuis votre compte administrateur mParticle, accédez à __Configuration > Entrées__. Trouvez __Braze__ dans le répertoire mParticule ____ et ajoutez l'intégration du flux.

L'intégration du flux de Braze prend en charge quatre flux distincts : iOS, Android, Web et Unbound. Le flux non lié peut être utilisé pour des événements tels que les e-mails qui ne sont pas connectés à une plate-forme. Vous devrez créer une entrée pour chaque flux principal de la plateforme. Vous pouvez créer des entrées supplémentaires à partir de __Configuration > Entrées__, dans l'onglet __Configurations de flux__.

!\[mParticle Settings\]\[1\]

Pour chaque flux, sous __Act as Platform__ sélectionnez la plate-forme correspondante dans la liste. Si vous ne voyez pas d'option pour sélectionner un flux __act-as__ , les données seront traitées comme non liées, mais peuvent toujours être transmises aux sorties d'entrepôt de données.

!\[mParticle Settings\]\[2\]{: style="max-width:40%;"} !\[mParticle Settings\]\[3\]{: style="max-width:37%;"}

Lors de la création de chaque entrée, mParticle vous fournira une clé et un secret. Copiez ces identifiants, en vous assurant de savoir à quel flux chaque paire d’identifiants est utilisée.

### Étape 2 : Créer un courant

En Brésil, accédez à **courants > + Créer Courant > Créer Exportation mParticule**. Fournissez un nom d'intégration, un courriel de contact et la clé API mParticle et une clé secrète mParticle pour chaque plateforme. Ensuite, sélectionnez les événements que vous souhaitez suivre. Une liste des événements disponibles est fournie ci-dessous. Enfin, cliquez sur **Lancer le**

![mParticule]({% image_buster /assets/img_archive/currents-mparticle-edit.png %})

{% alert important %}
Il est important de garder votre clé API mParticle et mParticle Secret Key à jour ; si les identifiants de votre connecteur expirent, le connecteur arrêtera l'envoi d'événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

Tous les événements envoyés à mParticle incluront le `external_user_id de l'utilisateur` en tant que `customerid`. En ce moment, Braze n'envoie pas de données d'événement pour les utilisateurs qui n'ont pas leur `external_user_id`.

## Détails de l'intégration

Vous pouvez exporter les données suivantes de Braze vers mParticle:

{% tabs %}
{% tab Platform-Specific %}
| Nom de l'événement                        | Type de flux                    | Libellé                                                                      | Propriétés des courants                                                                    |
| ----------------------------------------- | ------------------------------- | ---------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| Envoi de la notification push             | Flux spécifique à la plateforme | Une notification push a été envoyée à un utilisateur avec succès.            | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`              |
| La notification Push s'ouvre              | Flux spécifique à la plateforme | L'utilisateur a ouvert une notification push.                                | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`              |
| Bounces de notification push              | Flux spécifique à la plateforme | Braze n'a pas pu envoyer de notification push à cet utilisateur.             | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`              |
| Impressions de message dans l'application | Flux spécifique à la plateforme | L'utilisateur a consulté un message dans l'application.                      | `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`              |
| Clics de message dans l'application       | Flux spécifique à la plateforme | L'utilisateur a appuyé ou cliqué sur un bouton dans un message In-App.       | `button_id`, `app_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id` |
| Carte de contenu envoyée                  | Flux spécifique à la plateforme | Une carte de contenu a été envoyée à l'appareil d'un utilisateur             | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`   |
| Carte de contenu vue                      | Flux spécifique à la plateforme | L'utilisateur a consulté une carte de contenu                                | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`   |
| Carte de contenu cliquée                  | Flux spécifique à la plateforme | L'utilisateur a cliqué sur une carte de contenu                              | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`   |
| Carte de contenu rejetée                  | Flux spécifique à la plateforme | L'utilisateur a rejeté une carte de contenu                                  | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`   |
| Vues du fil d'actualité                   | Flux spécifique à la plateforme | L'utilisateur a consulté le flux natif des nouvelles de Braze.               | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`   |
| Vues des fiches d'actualités              | Flux spécifique à la plateforme | L'utilisateur a consulté une carte dans le flux de nouvelles natif de Braze. | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`   |
| Clics de carte de flux d'actualités       | Flux spécifique à la plateforme | L'utilisateur a cliqué sur une carte dans le flux natif Braze News Feed.     | `app_id`, `card_id`, `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`   |
| Application désinstallée                  | Flux spécifique à la plateforme | L'utilisateur a désinstallé l'application.                                   | `app_id`                                                                                   |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% tab Unbound %}
| Nom de l'événement                             | Type de flux | Libellé                                                                                                       | Propriétés des courants                                                                                                                                                                                                                          |
| ---------------------------------------------- | ------------ | ------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Envois par e-mail                              | Flux non lié | Un e-mail a été envoyé avec succès.                                                                           | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                                                                                                                                                                              |
| Livraisons de courrier électronique            | Flux non lié | Un e-mail a été envoyé avec succès au serveur de messagerie d'un utilisateur.                                 | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                                                                                                                                                                              |
| Ouverture de l'e-mail                          | Flux non lié | L'utilisateur a ouvert un e-mail.                                                                             | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`, `user_agent`, `machine_open`                                                                                                                                                |
| Clics par e-mail                               | Flux non lié | L'utilisateur a cliqué sur un lien dans un e-mail. Le suivi des clics par e-mail doit être activé.            | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`, `link_id`, `link_alias`, `user_agent`                                                                                                                                       |
| Envoyer les Bounces                            | Flux non lié | Braze a tenté d’envoyer un courriel, mais le serveur de messagerie de l’utilisateur ne l’a pas accepté.       | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                                                                                                                                                                              |
| Marques par e-mail comme spam                  | Flux non lié | L'utilisateur a marqué un e-mail comme spam.                                                                  | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`, `user_agent`                                                                                                                                                                |
| Se désabonner par e-mail                       | Flux non lié | L'utilisateur a cliqué sur le lien de désinscription dans un e-mail.                                          | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                                                                                                                                                                              |
| Envoi de SMS                                   | Flux non lié | Un SMS a été envoyé à un utilisateur.                                                                         | `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`                                                      |
| Envoyé par l'opérateur SMS                     | Flux non lié | Un SMS a été défini sur un opérateur.                                                                         | `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number`                                 |
| Livraisons de SMS                              | Flux non lié | Un SMS a été envoyé avec succès.                                                                              | `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number`                                 |
| Échec de l'envoi de SMS                        | Flux non lié | Impossible d'envoyer un SMS avec succès.                                                                      | `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number`, `error`, `provider_error_code` |
| Rejets SMS                                     | Flux non lié | Un SMS a été rejeté.                                                                                          | `campaign_id`, `campaign_name`, `message_variation_id`, `canvas_step_id`, `canvas_step_name`, `canvas_id`, `canvas_name`, `canvas_variation_id`, `canvas_variation_name`, `to_phone_number`, `from_phone_number`, `error`, `provider_error_code` |
| SMS entrants reçus                             | Flux non lié | Un SMS entrant a été reçu.                                                                                    | `inbound_phone_number`, `action`, `message_body`                                                                                                                                                                                                 |
| Changement d'état du Groupe d'Abonnement       | Flux non lié | L'état du groupe d'abonnement de l'utilisateur est passé à 'Abonné' ou 'Désabonné'                            | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                                                                                                                                                                              |
| Envoi de Webhook                               | Flux non lié | Un message de webhook a été envoyé au nom d'un utilisateur.                                                   | `campaign_id`, `canvas_step_id`, `canvas_id`, `canvas_variation_id`                                                                                                                                                                              |
| Conversions de campagne                        | Flux non lié | L'utilisateur a effectué l'événement de conversion principal pour une campagne dans sa fenêtre de conversion. | `campaign_id`                                                                                                                                                                                                                                    |
| Inscriptions de groupe de contrôle de campagne | Flux non lié | L'utilisateur a été inscrit dans un groupe de contrôle de campagne.                                           | `campaign_id`                                                                                                                                                                                                                                    |
| Conversions de Canvas                          | Flux non lié | L'utilisateur a effectué l'événement principal de conversion pour un Canvas dans sa fenêtre de conversion.    | `canvas_step_id`, `canvas_id`, `canvas_variation_id`                                                                                                                                                                                             |
| Entrées de la toile                            | Flux non lié | L'utilisateur a été entré dans un Canvas.                                                                     | `in_control_group`, `canvas_id`, `canvas_variation_id`                                                                                                                                                                                           |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3  .reset-td-br-4}
{% endtab %}
{% endtabs %}

Pour en savoir plus sur l'intégration de mParticle, visitez leur documentation [ici](http://docs.mparticle.com/integrations/braze/feed).
[1]: {% image_buster /assets/img/braze-feed-inputs.png %} [2]: {% image_buster /assets/img/braze-feed-act1.png %} [3]: {% image_buster /assets/img/braze-feed-act2.png %}
