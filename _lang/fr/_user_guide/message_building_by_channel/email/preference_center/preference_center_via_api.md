---
nav_title: Centre de préférences via API
article_title: Centre de préférences via API
page_order: 5
description: "Cet article décrit comment créer et modifier un centre de préférence en utilisant les endpoints du centre de préférence de Braze."
channel:
  - e-mail
---

# Centre de préférences via API

> Définir un centre de préférence fournit un guichet unique pour que vos utilisateurs puissent éditer leurs préférences de notifications pour vos [envois de messages par e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/). En utilisant les endpoints de [centre de préférence de Braze]({{site.baseurl}}/api/endpoints/preference_center), vous pouvez modifier directement le code HTML de votre centre de préférence pour l’aligner sur votre marque et comprendre les préférences de vos utilisateurs.

## Conditions préalables

| Condition | Description |
|---|---|
| Activer un centre de préférence | Votre tableau de bord de Braze possède des permissions pour utiliser la fonctionnalité de centre de préférence. |
| Groupe d’apps valide avec un groupe d’abonnement par e-mail, SMS, ou WhatsApp | Un groupe d’apps fonctionnel avec des utilisateurs valides et un groupe d’abonnement par e-mail, SMS, ou WhatsApp. |
| Utilisateur valide | Un utilisateur avec une adresse e-mail et un ID externe. |
| Clé API générale avec des permissions de centre de préférence | Dans le Tableau de bord de Braze, rendez-vous dans **Developer Console** > **Paramètres API** pour confirmer que vous avez accès à une clé API avec les permissions du centre de préférences. |
{: .reset-td-br-1 .reset-td-br-2}

## Étape 1 : Créer un centre de préférences par API

{% raw %}
Commençons à créer un centre de préférence en utilisant l’[endpoint `/preference_center/v1`][1]. Pour paramétrer votre centre de préférences, vous pouvez ajouter du code HTML qui s’aligne sur votre marque pour les champs `preference_center_page_html` et `confirmation_page_html`.

L’[endpoint `/preference_center/v1/{preferenceCenterExternalId}/url/{userId}`][2] vous permet de récupérer l’URL du centre de préférences pour un utilisateur donné en dehors d’un e-mail envoyé par Braze.

## Étape 2 : Inclure dans la campagne par e-mail

Ajoutez ensuite votre centre de préférence dans votre campagne par e-mail en collant un ensemble de code HTML comprenant du Liquid. Vous pouvez par exemple copier ce qui suit en tant qu’URL de lien, soit dans le code HTML, soit dans l’éditeur Drag & Drop.  

```html
<a href="{{preference_center.${preference_center_name_example}}}">Edit your preferences</a>
```
{%endraw%}

{% alert important %}
La balise Liquid ci-dessus ne marchera que lors du lancement d’une campagne ou d’un Canvas. Envoyer un e-mail de test n’affichera pas un lien valide.
{% endalert %}

## Modifier un centre de préférence

Vous pouvez éditer et mettre à jour votre centre de préférences en utilisant l’endpoint [`/preference_center/v1/{preferenceCenterExternalId}`][3]. 

## Identifier les centres de préférences et leurs détails

Pour identifier vos centres de préférence, utilisez l’[endpoint `/preference_center/v1/{preferenceCenterExternalId}`][4] pour renvoyer les informations liées, telles que le dernier timestamp mis à jour, l’ID du centre de préférences et plus encore.

[1]: {{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/
[2]: {{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/
[3]: {{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/
[4]: {{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/ 
