---
nav_title: "Cas d'utilisation de l'API"
article_title: "Cas d'utilisation de l'API"
description: "Que tu sois un développeur compétent ou un spécialiste du marketing disposant de ressources minimales en matière de développement, cet article de référence est conçu pour t'aider à comprendre comment tirer parti de la puissance de l'API REST de Braze pour accomplir diverses tâches et améliorer ta stratégie d'engagement des clients."
page_type: reference
page_order: 4.8
---

# Cas d’utilisation

> L'[API REST de Braze]({{site.baseurl}}/api/basics/) propose un large éventail de points de terminaison conçus pour t'aider à gérer et à optimiser ta stratégie d'engagement des clients. Dans cet article, nous allons explorer plusieurs cas d'utilisation pour chaque collection de points de terminaison : catalogues, listes et adresses électroniques, exportation, messages, centre de préférences, SMS, groupes d'abonnement, modèles et données utilisateur.<br><br>Chaque section présente un scénario avec un guide étape par étape, un exemple de code et le résultat attendu. À la fin de cet article, tu comprendras mieux comment utiliser l'API REST de Braze pour améliorer tes efforts d'engagement des clients.

## Suppression de plusieurs articles dans un catalogue

La nouvelle année s’accompagne de nouveaux lancements de produits chez Kitchenerie, une marque de vente au détail spécialisée dans les articles de cuisine. Dans le tableau de bord de Braze, Kitchenerie a mis en place un catalogue pour sa collection de vaisselle. Il est intitulé « Dishware ». Cette nouvelle année signifie également le retrait des produits suivants de sa collection de vaisselle.

* Plain Bisque
* Porcelaine perlée
* Pink Shimmer

Pour supprimer ces produits de son catalogue, Kitchenerie peut utiliser le [point de terminaison `/catalogs/{catalog_name}/items`]({{site.baseurl}}/api/endpoints/catalogs/catalog_items/asynchronous/delete_catalog_items_bulk/) afin de transmettre les identifiants des produits.

Voici l'exemple de demande :

```
curl --location --request DELETE 'https://rest.iad-03.braze.com/catalogs/dishware/items' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer YOUR-REST-API-KEY' \
--data-raw '{
  "items": [
    {"id": "plainbisque"},
    {"id": "pearlporcelain"},
    {"id": "pinkshimmer"}
  ]
}'
```

Après avoir envoyé cette charge utile, la réponse suivante confirme que les trois collections ont bien été supprimées du catalogue de vaisselle de Kitchenerie.

```json
{
  "message": "success"
}
```

## Retirer des e-mails de la liste des courriers indésirables de Braze

Chez MovieCanon, une entreprise de services de streaming, l'équipe de développeurs est chargée d'auditer périodiquement ses listes de courriels afin d'identifier et de conserver les utilisateurs qui sont abonnés à ses campagnes de courriels. Dans le cadre de cet audit, MovieCanon souhaite supprimer cette liste d'e-mails de sa liste de courriers indésirables :

- august.author.example.com
- betty.benson@example.com
- charlie.chase@example.com
- delilah.york@example.com
- evergreen.rebecca@example.com

Pour accomplir cette tâche, l'équipe de développeurs aura besoin d'une clé API avec l'autorisation `email.spam.remove` pour utiliser l’endpoint `/email/spam/remove`. Cet endpoint supprime les adresses e-mails de la liste des courriers indésirables de Braze et de la liste des courriers indésirables gérée par le fournisseur de messagerie de MovieCanon.

Pour envoyer cette demande, tu dois inclure soit une chaîne d'adresses électroniques, soit un tableau de 50 adresses électroniques à modifier. Comme le nombre des e-mails à supprimer est inférieur à 50, MovieCanon peut accomplir cette tâche avec le corps de requête suivant :

```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

```json
{
  "email": ["august.author.example.com","betty.benson@example.com","charlie.chase@example.com","delilah.york@example.com","evergreen.rebecca@example.com"]
}
```

Après avoir envoyé cette charge utile avec succès, cette réponse confirme que les e-mails ont été retirés de la liste des courriers indésirables de MovieCanon.

```json
{
  "message": "success"
}
```

## L'audit de toutes les toiles

Siege Valley Health est un système hospitalier qui comprend 10 hôpitaux opérationnels et des centres de recherche avec des milliers de patients. Son équipe marketing veut comparer les Canevas envoyés aux patients pour leur rappeler de prendre rendez-vous pour les vaccins contre la grippe des trois dernières années d'utilisation de Braze. L'équipe marketing de Siege Valley Health souhaite également disposer d'un moyen rapide et efficace de consulter à la fois la liste des canvas et le résumé analytique.

Plongeons dans la façon dont Siege Valley Health peut accomplir ces deux tâches en utilisant une combinaison de points de terminaison plutôt qu'en filtrant à travers le tableau de bord de Braze.

Pour la première tâche d'audit des canvas, utilisez l’[endpoint `/canvas/list`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvases/) pour exporter une liste de canvas qui comprend le nom et les étiquettes. Voici un exemple de demande :

{% details Here’s the response that the Siege Valley Health marketing team would receive. %}
```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "canvases" : [
  	{
  		"id": "canvas_identifier_1",
  		"last_edited": "2020-07-10T23:59:59",
  		"name": "PatientReminder_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "2020"
      },
  	},
  	{
  		"id": "canvas_identifier_2",
  		"last_edited": "2020-07-30T23:59:59",
  		"name": "PatientReminder2_FluShot_2020",
  		"tags": {
        "flu_shots", "patienthealth", "reminder", "2020"
      },
  	},
    ... (more Canvases)
  ],
  "message": 'success'
}
```
{% enddetails %}

Passons à la tâche suivante. Celle-ci consiste à afficher le résumé analytique du premier canvas de la liste des canvas de Siege Valley Health. Pour ce faire, nous utiliserons l’[endpoint `/canvas/data_summary`]({{site.baseurl}}/api/endpoints/export/canvas/get_canvas_analytics_summary/) avec les paramètres de requête suivants :

* `canvas_id`: "canvas_identifier_2"
* `ending_at` : 2023-07-10T23:59:59
* `starting_at` : 2020-07-10T23:59:59

Voici un exemple de demande :

```
curl --location -g --request GET 'https://rest.iad-01.braze.com/canvas/data_summary?canvas_id={{canvas_identifier_2}}&ending_at=2023-07-10T23:59:59&starting_at=2020-07-10T23:59:59&length=5&include_variant_breakdown=false&include_step_breakdown=false&include_deleted_step_data=false' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

## Vérifier les campagnes et canvas planifiés à venir

La période la plus chargée de l'année approche à grands pas pour Flash & Thread, une marque de vente au détail de vêtements et de produits de beauté en ligne et en magasin. Son équipe marketing souhaite vérifier les campagnes et les canvas à venir depuis le tableau de bord de Braze avant le 31 mars 2024 à 12 heures. Cette tâche peut être effectuée au moyen de l’[endpoint `/messages/scheduled_broadcasts`]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/get_messages_scheduled/). 

Voici l'exemple de demande :

```
curl --location --request GET 'https://rest.iad-01.braze.com/messages/scheduled_broadcasts?end_time=2024-03-31T12:00:00' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

Ce point de terminaison renvoie la liste des campagnes et des toiles à venir. À partir de là, l'équipe marketing peut confirmer sa liste de messages en se référant au champ `name` pour les campagnes et les Canvases dans la réponse.

## Affichage d'un ancien centre de préférences

PoliterWeekly est un magazine numérique dont les abonnés sont joignables par e-mail. Dans le but de mieux comprendre le parcours utilisateur de ses abonnés, l'équipe marketing souhaite examiner les détails du centre de préférences de PoliterWeekly pour vérifier quand il a été créé et mis à jour pour la dernière fois.

En utilisant l’[endpoint `/preference_center/v1/{preferenceCenterExternalID}`]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/), l'équipe marketing n'a qu'à insérer l'ID externe du centre de préférences en tant que paramètre de chemin, ce qui ressemblerait à ceci :

```
curl --location -g --request GET https://rest.iad-01.braze.com/preference_center/v1/politer_weekly_preference_center_api_id \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```

{% details Here’s the response the PoliterWeekly marketing team would receive. %}

```json
{
  "name": "PoliterWeekly Notification Preferences",
  "preference_center_api_id": "user_engage_pref_123",
  "created_at": "2021-04-03T12:00:00",
  "updated_at": "2024-08-15T15:00:00",
  "preference_center_title": "Manage Your PoliterWeekly Notification Preferences",
  "preference_center_page_html": "<!DOCTYPE html><html><head><title>Your PoliterWeekly Newsletter Preferences</title><style>body { font-family: Arial, sans-serif; margin: 0; padding: 20px; }.container { max-width: 600px; margin: auto; }h1 { color: #333; }.preference { margin-bottom: 20px; }.preference label { font-size: 16px; }.preference input[type=\"checkbox\"] { margin-right: 10px; }.submit-btn { background-color: #007bff; color: white; padding: 10px 20px; border: none; cursor: pointer; }</style></head><body><div class=\"container\"><h1>Manage your notification preferences</h1><p>Select the types of updates you wish to receive from us:</p><form id=\"preferencesForm\"><div class=\"preference\"><label><input type=\"checkbox\" name=\"newsUpdates\" checked> News Updates</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"editorialPicks\"> Editorial Picks</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"events\"> Events & Webinars</label></div><div class=\"preference\"><label><input type=\"checkbox\" name=\"specialOffers\"> Special Offers & Promotions</label></div><button type=\"submit\" class=\"submit-btn\">Save Preferences</button></form></div><script>document.getElementById('preferencesForm').addEventListener('submit', function(e) {e.preventDefault();alert('Your preferences have been saved!');});</script></body></html>",
  "confirmation_page_html": "<!DOCTYPE html><html><head><title>PoliterWeekly Preferences Updated</title></head><body><h1>You're good to go!</h1><p>Your preferences have been updated successfully.</p></body></html>",
  "redirect_page_html": null,
  "preference_center_options": {
    "meta-viewport-content": "width=device-width, initial-scale=1"
  },
  "state": "active"
}
```

À partir de cette réponse, l'équipe marketing peut voir que le centre de préférences a été créé 3 ans avant sa mise à jour la plus récente. Avec ces informations en tête, l'équipe marketing pourrait créer et lancer un nouveau centre de préférences.

{% enddetails %}

## Supprimer les numéros de téléphone non valides

Chez CashBlastr, l'objectif principal est de simplifier la façon dont les individus peuvent envoyer et recevoir des paiements rapides. En tant que société de services financiers, CashBlastr veut que la liste des numéros de téléphone de ses clients soit à jour et exacte. L'équipe de développeurs a été chargée de supprimer la liste suivante de numéros de téléphone marqués comme "non valides" afin que les messages SMS de l'équipe marketing puissent atteindre les clients CashBlastr appropriés.

- 12223135467
- 12183095514
- 14235662245
- 14324567892

Pour envoyer une demande avec le [point de terminaison`/sms/invalid_phone_numbers/remove` ]({{site.baseurl}}/api/endpoints/sms/post_remove_invalid_numbers/), les numéros de téléphone doivent être dans un tableau de chaînes au [format e.164](https://en.wikipedia.org/wiki/E.164), avec un maximum de 50 numéros de téléphone par demande. Comme la liste ne dépasse pas 50 numéros de téléphone, voici un exemple du corps de la demande que l'équipe de développeurs de CashBlastr enverrait :

```json
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "phone_numbers": ["12183095514","14255551212"]
}
```

Après avoir envoyé cette charge utile, la réponse suivante confirme que les numéros de téléphone invalides de CashBlastr ont été retirés de la liste invalide de Braze.

```json
{
  "message": "success"
}
```

## Consulter le statut du groupe d'abonnement d'un utilisateur

SandwichEmperor est une chaîne de restauration rapide aux États-Unis, et son équipe marketing souhaite vérifier les statuts des groupes d'abonnement d'une liste aléatoire de ses utilisateurs pour les SMS. En utilisant le [point de terminaison`/subscription/status/get` ]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/), SandwichEmperor peut accomplir cette tâche pour un utilisateur individuel avec l'exemple de demande suivant :

{% raw %}
```
curl --location -g --request GET 'https://rest.iad-01.braze.com/subscription/status/get?subscription_group_id={{subscription_group_id}}&phone=+11232223333' \
--header 'Authorization: Bearer YOUR-REST-API-KEY'
```
{% endraw %}

Ce point de terminaison répertorie également les statuts des groupes d'abonnement d'un utilisateur pour le courrier électronique et peut être utilisé pour voir le statut des groupes d'abonnement pour plusieurs utilisateurs.

## Vérification d'un modèle HTML pour la messagerie électronique

Chez WorkFriends, un réseau social qui aide à créer des liens entre les travailleurs de différents secteurs d'activité, son équipe de marketing est chargée d'envoyer des campagnes de courriels à ses utilisateurs. Ces campagnes comprennent souvent des rappels d'événements locaux, des bulletins d'information hebdomadaires et des mises en avant des activités du profil.

Dans ce scénario, WorkFriends a toujours utilisé un modèle HTML unique avec son ancienne marque. Dans un effort pour aligner l'identité de sa marque, WorkFriends veut vérifier s'il y a des informations utiles dans ce modèle HTML à exploiter avant de passer à un nouveau modèle.

{% details Here’s the response that the WorkFriends team would receive. %}

```json
Content-Type: application/json
Authorization: Bearer YOUR_REST_API_KEY
{
  "email_template_id": "WorkFriends_Email_Template_ID",
  "template_name": "Promo template",
  "description": "Promo template",
  "subject": "WorkFriends Weekly Newsletter",
  "preheader": "Another week, another WorkFriends update",
  "body": "<!DOCTYPE html><html><head><title>WorkFriends Weekly Newsletter</title><style>body {font-family: Arial, sans-serif; color: #333;}.container {padding: 20px;}.header {background-color: #f2f2f2; padding: 10px; text-align: center;}.content {margin-top: 20px;}.footer {margin-top: 20px; font-size: 12px; text-align: center; color: #777;}</style></head><body><div class=\"container\"><div class=\"header\"><h2>WorkFriends Weekly Newsletter</h2></div><div class=\"content\"><p>Hello WorkFriends,</p><p>Welcome to another edition of our weekly newsletter. We've got some exciting updates and promos for you this week!</p><!-- Add more content here --><p>Don't forget to check out our latest promos and updates. Stay connected, stay informed!</p></div><div class=\"footer\"><p>Thank you for being a part of WorkFriends.</p><p>Unsubscribe | Update Preferences</p></div></div></body></html>",
  "tags": "promo",
  "created_at": "2020-07-10 13:00:00.000",
  "updated_at": "2024-02-04 17:00:00.000"
}
```

{% enddetails %}

Après avoir examiné ces informations sur le modèle, WorkFriends peut également utiliser l’[endpoint `/templates/email/update`]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/) pour mettre à jour le modèle d'e-mail via l'API. Le modèle d'email dans le tableau de bord de Braze reflétera ces modifications.
