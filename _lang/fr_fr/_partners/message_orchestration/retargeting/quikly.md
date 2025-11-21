---
nav_title: Rapidement
article_title: Rapidement
description: "Cet article de référence présente le partenariat entre Braze et Quickly, une plateforme de marketing d'urgence, qui vous permet d'accélérer les conversions sur les événements d'un parcours client Braze."
alias: /partners/quikly/
page_type: partner
search_tag: Partner

---

# Rapidement

> [Quikly](https://www.quikly.com), plateforme de marketing d'urgence, s'appuie sur la psychologie pour motiver les consommateurs, afin que les marques puissent immédiatement augmenter la réponse autour de leurs initiatives marketing clés.

_Cette intégration est assurée par Quikly._

## À propos de l'intégration

Le partenariat entre Braze et Quikly vous permet d'accélérer les conversions sur les événements d'un parcours client Braze. Pour ce faire, Quikly utilise la psychologie de l'urgence pour motiver les consommateurs de manière ludique et instantanée. Par exemple, les marques peuvent utiliser Quikly pour acquérir immédiatement de nouveaux abonnés par e-mail et SMS directement dans Braze ou pour motiver d'autres objectifs marketing clés comme le téléchargement de votre application mobile.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Quikly | Un compte partenaire de la marque [Quikly](https://www.quikly.com) est nécessaire pour bénéficier de ce partenariat. |
| Clé d'API REST Braze | Une clé API REST de Braze avec les autorisations `users.track`, `subscription.status.set`, `users.export.ids` et `subscription.status.get`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints) Votre endpoint dépendra de l'URL de Braze pour votre instance. |
| Clé API de Quikly (facultatif) | Une clé API Quikly fournie par votre gestionnaire de réussite client (webhook uniquement). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

Quikly permet aux marques d'accélérer l'acquisition par e-mail ou SMS et incite les abonnés à fournir des données first-party directement dans Braze. Vous pouvez également utiliser Braze pour cibler les clients dont l'abonnement a expiré et leur proposer une activation Quikly qui réactivera et fidélisera cette audience. En outre, les marketeurs peuvent utiliser cette intégration pour inciter des événements personnalisés spécifiques du parcours client avec des structures de récompense uniques. 

Par exemple:
 - Créez de l'anticipation et de l'engagement au fil des jours, les consommateurs s'abonnant pour avoir une chance de remporter des récompenses excitantes avec [Quikly Hype.](https://www.quikly.com/urgency-marketing/platform/product-overview/hype) Les données first-party sont automatiquement transmises à Braze.
 - Accélérez l'acquisition de nouveaux abonnés par e-mail et par SMS en utilisant des offres uniques en temps réel basées sur la rapidité de réponse du consommateur, son classement par rapport aux autres, au hasard, ou avant que le temps ou les quantités ne soient épuisés avec [Quikly Swap.](https://www.quikly.com/urgency-marketing/platform/product-overview/swap)
 - Motivez des étapes spécifiques du parcours client avec des structures de récompense uniques à l'aide de webhooks.
 - Appliquez des attributs et des events personnalisés au profil de l'utilisateur lors de sa participation à une activation Quikly.

## Intégration

Vous trouverez ci-dessous quatre intégrations différentes : l'acquisition par e-mail, l'acquisition par SMS, les attributs personnalisés et les webhooks. L'intégration que vous choisirez dépendra de votre activation Quikly et de votre cas d'utilisation.

{% tabs %}
{% tab Acquisition d'e-mails %}

### Acquisition d'e-mails

Si vos activations Quikly collectent des adresses e-mail de clients ou des données de profil, la seule étape requise consiste à fournir à Quikly votre clé API REST et votre endpoint. Quikly configurera votre compte de marque pour qu'il transmette ces données à Braze. Si vous souhaitez inclure d'autres attributs d'utilisateur, mentionnez-le lorsque vous fournissez les informations d'identification de l'API à Quikly.

Voici un aperçu de la manière dont Quikly exécute ce flux de travail.
1. Lors de la participation à une activation Quikly, Quikly planifie une recherche d'utilisateur à l'aide de l'[API d'exportation]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour voir si un utilisateur existe avec un `email_address` donné.
2. Enregistrez ou mettez à jour l'utilisateur.
  - Si l'utilisateur existe :
    - Ne créez pas de nouveau profil.
    - Si vous le souhaitez, Quikly peut enregistrer un attribut personnalisé sur le profil de l'utilisateur pour indiquer que l'utilisateur a participé à l'activation.
  - Si l'utilisateur n'existe pas :
    - Quikly crée un profil d'alias uniquement via l'[`/users/track`endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Braze, en définissant l'e-mail de l'utilisateur comme alias de l'utilisateur pour le référencer à l'avenir (car l'utilisateur n'aura pas d'ID externe).
    - Si vous le souhaitez, Quikly peut enregistrer des événements personnalisés pour indiquer que ce profil a participé à l'activation de Quikly.

{% details /users/track request %}

#### En-têtes de requête
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Corps de la requête
```
{
  "attributes": [{
    "_update_existing_only": false,
    "user_alias:": {
      "alias_name": "email@example.com",
      "alias_label: "email"
    },
    "email": "email@example.com"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Acquisition de SMS %}

### Abonnements SMS

Les activations Quikly peuvent collecter les numéros de téléphone mobile directement auprès des clients et lancer un nouvel abonnement SMS. Pour activer cette intégration, fournissez à votre gestionnaire de succès client Quikly la valeur de paramètre `subscription_group_id`. Vous pouvez accéder au site `subscription_group_id` d'un groupe d'abonnement en accédant à la page **Groupe d'abonnement**.

Quikly effectuera une recherche d'abonnement à l'aide du numéro de téléphone du client et le créditera automatiquement lors de l'activation si un abonnement SMS existe déjà. Dans le cas contraire, un nouvel abonnement sera lancé et, après vérification de l'état de l'abonnement, le client sera crédité.

Voici le flux de travail complet lorsqu'un client fournit son numéro de mobile et son consentement via Quikly :
1. Quikly effectue une recherche d'abonnement en utilisant le [statut du groupe d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) pour voir si un `phone` donné est abonné à un `subscription_group_id`. Si un abonnement existe, créditez l'utilisateur dans l'activation Quikly. Aucune autre action n'est nécessaire.
2. Quikly effectue une recherche d'utilisateur à l'aide de l'[endpoint Exporter le profil utilisateur par identifiant]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour voir s'il existe un profil utilisateur avec un `email_address` donné. Si aucun utilisateur n'existe, créez un profil d'alias uniquement via l'[`/users/track`endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) Braze, en définissant l'e-mail de l'utilisateur comme alias de l'utilisateur pour faire référence à cet utilisateur à l'avenir (car l'utilisateur n'aura pas d'ID externe).
3. Mettez à jour l’état d'abonnement à l'aide de l' [endpoint Mettre à jour l’état du groupe d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

Pour prendre en charge les flux de travail existants d'abonnement SMS à double inscription, Quikly peut envoyer un événement personnalisé à Braze plutôt que le flux de travail ci-dessus. Dans ce cas, plutôt que de mettre à jour l'état de l'abonnement directement, l'[événement personnalisé déclenche le processus de double inscription]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/) et l'état de l'abonnement est contrôlé périodiquement pour vérifier que l'utilisateur s'est inscrit avant de le créditer dans l'activation Quikly.

{% alert important %}
Braze conseille, lors de la création de nouveaux utilisateurs via l'endpoint `/users/track`, d'attendre environ 2 minutes avant d'ajouter les utilisateurs au groupe d'abonnement concerné, afin de laisser à Braze le temps de créer entièrement le profil utilisateur.
{% endalert %}

{% details requête détaillée /subscription/status/set  %}
#### En-têtes de requête
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Corps de la requête
```
{
  "subscription_group_id": "the-id-of-the-subscription-group",
    "subscription_status": "subscribed",
    "phone": "+13135551212"
  }]
}
```

{% enddetails %}

{% endtab %}
{% tab Attributs personnalisés %}
### Attributs personnalisés

En fonction de votre mise en œuvre de Braze, vous pouvez souhaiter que les événements d'activation Quikly soient transmis à Braze pour un traitement ultérieur. Par exemple, vous pouvez souhaiter appliquer un attribut utilisateur personnalisé en fonction du niveau ou de l'incitation atteint dans l'activation Quikly, ce qui vous permet d'afficher la carte de contenu correspondante lorsqu'ils ouvrent votre application ou se connectent à votre site Web. Quikly travaillera directement avec vous pour mettre en œuvre ces intégrations.

{% endtab %}
{% tab Webhooks %}
### Webhooks
Utilisez des webhooks pour déclencher des incitations lors d'événements personnalisés dans le parcours client. Par exemple, si vous disposez d'un événement Braze pour le moment où un utilisateur se connecte à votre application, active les notifications push ou utilise votre localisateur de magasin, vous pouvez utiliser un webhook pour déclencher un événement personnalisé pour cet utilisateur en fonction de la configuration d'une activation Quikly spécifique. Parmi les exemples de tactiques, on peut citer le fait de récompenser le premier nombre X d'utilisateurs qui effectuent une action (comme se connecter à votre application) avec une offre personnalisée ou de proposer une offre dont la valeur diminue au fur et à mesure que le temps s'écoule afin de motiver une réponse immédiate.

### Créer un webhook Quikly à Braze

Pour créer un modèle de webhook Quikly pour de futures campagnes ou Canvases, naviguez vers **Modèles** > **Modèles de webhook** dans la plateforme Braze. 

Si vous souhaitez créer une campagne webhook unique de Quikly ou utiliser un modèle existant, sélectionnez **Webhook** à Braze lors de la création d'une nouvelle campagne.

Sélectionnez **Blank Template (Modèle vierge)** et saisissez les éléments suivants pour l'URL du webhook et le corps de la requête :
- **URL du webhook**: https://api.quikly.com/webhook/braze
- **Corps de la requête** : Paires clé-valeur JSON

#### En-têtes et méthode de la requête

Quikly requête une autorisation à l'adresse `HTTP Header`.

- **Méthode HTTP** : POST
- **En-tête de la requête** :
  - **Autorisation**: Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Type de contenu : application/json**

#### Corps de la requête

Sélectionnez ***Paires clé-valeur JSON*** et ajoutez les paires suivantes :
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### Prévisualisez votre requête

Prévisualisez votre requête dans le panneau **Aperçu** ou accédez à l'onglet `Test`, où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser le vôtre pour tester votre webhook.

{% alert important %}
N'oubliez pas d'enregistrer votre modèle avant de quitter la page ! <br>Les modèles de webhook mis à jour se trouvent dans la liste **Modèles de webhook enregistrés** lors de la création d'une nouvelle [campagne webhook.]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/)
{% endalert %}

{% endtab %}
{% endtabs %}

## Assistance
Contactez votre gestionnaire de succès client chez Quikly pour toute question.


