---
nav_title: Segment pour les courants
article_title: Segment pour les courants
page_order: 1.2
alias: /fr/partners/segment_for_currents/
description: "Cet article décrit le partenariat entre Braze Currents et Segment, une plateforme de données client qui collecte et achemine des informations entre les sources de votre pile marketing."
page_type: partenaire
tool: Courants
search_tag: Partenaire
---

# Segment pour les courants

{% include video.html id="RfOHfZ34hYM" align="right" %}

> [Segment](https://segment.com) est une plate-forme de données client qui collecte et achemine des informations à partir de sources multiples vers une variété d'autres emplacements de votre pile marketing.

## Détails de l'intégration

### Étape 1 : Obtenir une clé d'écriture de segment

1. Pour commencer, trouvez la __Segment Write Key__ dans votre tableau de bord de segment.
2. Sur le tableau de bord de Braze, accédez à __courants__ sous __Intégrations__ et créez un __Export de données de segments__.
3. Ajouter la clé d'écriture du segment dans le champ __clé API__.

!\[Segment\]\[1\]

{% alert warning %}
Il est important de garder votre clé API de segment à jour. Si les identifiants de votre connecteur expirent, le connecteur arrêtera d'envoyer des événements. Si cela persiste plus de **48 heures**, les événements du connecteur seront supprimés et les données seront définitivement perdues.
{% endalert %}

### Étape 2 : Exporter les événements d'engagement de messages

Ensuite, sélectionnez les événements d'engagement de message que vous souhaitez exporter. Référez-vous à la table des événements d'exportation et des propriétés listée ci-dessous. Tous les événements envoyés au segment incluront le `external_user_id de l'utilisateur` en tant que `userId`. En ce moment, Braze n'envoie pas de données d'événement pour les utilisateurs qui n'ont pas leur `external_user_id`.

Enfin, sélectionnez __Lancer le__.

{% alert warning %}
Si vous avez l'intention de créer plus d'un des mêmes connecteurs de courant (par exemple, deux connecteurs d'événements d'engagement de messages), ils doivent être dans différents groupes d'applications. Parce que l'intégration des courants de segment de Braze ne peut pas isoler les événements par différentes applications dans un seul groupe d'applications, si vous ne le faites pas, cela entraînera une perte inutile de données et une perte de données.
{% endalert %}

!\[Segment\]\[2\]

Pour en savoir plus, visitez la documentation [Segments](https://segment.com/docs/sources/cloud-apps/appboy/).

## Configuration des données

{% tabs %}
{% tab Export Events %}

Vous pouvez exporter les données suivantes de Braze vers Segment:

| Nom de l'événement                   | Libellé                                                                                                                                                                                                                                          |
| ------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Notification envoyée                 | Une notification push a été envoyée avec succès.                                                                                                                                                                                                 |
| Notification push tapée              | L'utilisateur a ouvert une notification push.                                                                                                                                                                                                    |
| Notification Push rebondie           | Braze n'a pas pu envoyer de notification push à cet utilisateur.                                                                                                                                                                                 |
| Push de premier plan iOS ouvert      | L'utilisateur a reçu une notification push sur iOS pendant que l'application était ouverte.                                                                                                                                                      |
| Courriel envoyé                      | Un e-mail a été envoyé avec succès.                                                                                                                                                                                                              |
| Courriel envoyé                      | Un e-mail a été envoyé avec succès au serveur de messagerie d'un utilisateur.                                                                                                                                                                    |
| Courriel ouvert                      | L'utilisateur a ouvert un e-mail.                                                                                                                                                                                                                |
| Lien de courriel cliqué              | L'utilisateur a cliqué sur un lien dans un e-mail. Le suivi des clics par e-mail doit être activé.                                                                                                                                               |
| E-mail rebondi                       | Braze a tenté d'envoyer un courriel, mais le serveur de réception de l'utilisateur ne l'a pas accepté.                                                                                                                                           |
| Courriel Soft Bounce                 | Braze a tenté d'envoyer un e-mail, mais l'utilisateur reçoit un serveur de courrier temporairement rebondi. <br> <br> (Les raisons peuvent inclure une boîte de réception complète ou un serveur mis en panne, entre autres choses.) |
| Courriel marqué comme spam           | L'utilisateur a marqué un e-mail comme spam.                                                                                                                                                                                                     |
| E-mail désabonné                     | L'utilisateur a cliqué sur le lien de désinscription dans un e-mail.                                                                                                                                                                             |
| SMS envoyé                           | Un SMS a été envoyé.                                                                                                                                                                                                                             |
| SMS envoyé à l'opérateur             | Un SMS a été envoyé au Transporteur pour livraison.                                                                                                                                                                                              |
| SMS envoyé                           | Un SMS a été envoyé avec succès.                                                                                                                                                                                                                 |
| Échec de l'envoi du SMS              | Impossible d'envoyer un SMS avec succès.                                                                                                                                                                                                         |
| SMS Rejeté                           | Un SMS a été rejeté.                                                                                                                                                                                                                             |
| SMS entrants reçus                   | Un SMS entrant a été reçu.                                                                                                                                                                                                                       |
| Etat du Groupe d'Abonnement Changé   | L'état du groupe d'abonnement de l'utilisateur est passé à 'Abonné' ou 'Désabonné'.                                                                                                                                                              |
| Message In-App consulté              | L'utilisateur a consulté un message dans l'application.                                                                                                                                                                                          |
| Message In-App cliqué                | L'utilisateur a appuyé ou cliqué sur un bouton dans un message In-App.                                                                                                                                                                           |
| Carte de contenu envoyée             | Une carte de contenu a été envoyée à l'appareil d'un utilisateur.                                                                                                                                                                                |
| Carte de contenu vue                 | L'utilisateur a consulté une fiche de contenu.                                                                                                                                                                                                   |
| Carte de contenu cliquée             | L'utilisateur a cliqué sur une fiche de contenu.                                                                                                                                                                                                 |
| Carte de contenu rejetée             | L'utilisateur a rejeté une carte de contenu.                                                                                                                                                                                                     |
| Flux d'actualité consulté            | L'utilisateur a consulté le flux natif des nouvelles de Braze.                                                                                                                                                                                   |
| Fil d'actualité consulté             | L'utilisateur a consulté une carte dans le flux de nouvelles natif de Braze.                                                                                                                                                                     |
| Carte de flux d'actualités cliquée   | L'utilisateur a cliqué sur une carte dans le flux natif Braze News Feed.                                                                                                                                                                         |
| Webhook envoyé                       | Un message de webhook a été envoyé.                                                                                                                                                                                                              |
| Campagne convertie                   | L'utilisateur a effectué un événement de conversion pour une campagne dans sa fenêtre de conversion.                                                                                                                                             |
| Toile convertie                      | L'utilisateur a effectué un événement de conversion pour un Canvas dans sa fenêtre de conversion.                                                                                                                                                |
| Toile entrée                         | L'utilisateur a été entré dans un Canvas.                                                                                                                                                                                                        |
| Groupe de contrôle de campagne entré | L'utilisateur a été inscrit dans un groupe de contrôle de campagne.                                                                                                                                                                              |
| Application désinstallée             | L'utilisateur a désinstallé l'application.                                                                                                                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Export Properties %}

Les propriétés suivantes seront incluses avec tous les événements Braze envoyés à Segment:

| Nom de la propriété            | Type de texte          | Libellé                                                                                                                                                                                                                                                                                          |
| ------------------------------ | ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `app_id`                       | `Chaîne de caractères` | L'identifiant API de l'application sur laquelle un utilisateur a reçu un message ou a effectué une action, le cas échéant.                                                                                                                                                                       |
| `id_expéditeur`                | `Chaîne de caractères` | L'id du message si spécifié pour la campagne, le cas échéant.                                                                                                                                                                                                                                    |
| `format@@0 dispatch_id`        | `Chaîne de caractères` | L'id de l'envoi de message (id unique pour chaque 'transmission' envoyée depuis la plateforme Braze). Les utilisateurs qui reçoivent un message de planification reçoivent le même dispatch_id. Les messages basés sur l'action ou sur l'API obtiennent un dispatch_id unique par utilisateur. |
| `campaign_id`                  | `Chaîne de caractères` | L'identifiant API de la campagne associée à l'événement, le cas échéant.                                                                                                                                                                                                                         |
| `nom_campagne`                 | `Chaîne de caractères` | Le nom de la campagne associée à l'événement, le cas échéant.                                                                                                                                                                                                                                    |
| `Id de la variante du message` | `Chaîne de caractères` | L'identifiant API de la variante de message pour la campagne associée à l'événement, le cas échéant.                                                                                                                                                                                             |
| `id_toile`                     | `Chaîne de caractères` | L'identifiant API du Canvas associé à l'événement, le cas échéant.                                                                                                                                                                                                                               |
| `nom_de_toile`                 | `Chaîne de caractères` | Le nom de la toile associée à l'événement, le cas échéant.                                                                                                                                                                                                                                       |
| `id de variation_de la toile`  | `Chaîne de caractères` | L'identifiant API de la Variation Canvas associée à l'événement, le cas échéant.                                                                                                                                                                                                                 |
| `canas_step_id`                | `Chaîne de caractères` | L'identifiant API de l'étape Canvas associée à l'événement, le cas échéant.                                                                                                                                                                                                                      |
| `Groupe in_contrôle_in_`       | `Chaîne de caractères` | Pour les événements Canvas Entré , que l'utilisateur soit inscrit ou non dans le groupe de contrôle - toujours `true` ou `false`                                                                                                                                                                 |
| `Caractéristiques du contexte` | `Chaîne de caractères` | Pour les événements de courriel, l'adresse e-mail à laquelle l'e-mail a été envoyé.                                                                                                                                                                                                              |
| `URL du lien`                  | `Chaîne de caractères` | Pour les événements Courriel cliqués, l'URL du lien sur lequel l'utilisateur a cliqué.                                                                                                                                                                                                           |
| `ID du bouton`                 | `Chaîne de caractères` | Pour le message In-App Clicked events, l'index du bouton sur lequel l'utilisateur a cliqué.                                                                                                                                                                                                      |
| `id de la carte`               | `Chaîne de caractères` | Pour les événements de la carte de flux d'actualité et de la carte de contenu, l'identifiant API de la carte.                                                                                                                                                                                    |
| `ID de groupe d'abonnement`    | `Chaîne de caractères` | Pour les événements de changement d'état du groupe d'abonnement, l'identifiant de l'API du groupe d'abonnement.                                                                                                                                                                                  |
| `Statut de l'abonnement`       | `Chaîne de caractères` | Pour les événements changés d'état de groupe d'abonnement, le statut de l'utilisateur a été modifié, soit "abonné", soit "désabonné".                                                                                                                                                            |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}


{% endtab %}
{% endtabs %}
[1]: {% image_buster /assets/img_archive/currents-segment-edit.png %} [2]: {% image_buster /assets/img/segment/segment_currents.png %}
