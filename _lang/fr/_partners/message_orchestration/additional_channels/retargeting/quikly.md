---
nav_title: Quikly
article_title: Quikly
description: "Quickly, une plateforme de marketing d'urgence, vous permet d'accélérer les conversions sur les événements du parcours client Braze."
alias: /partners/quikly/
page_type: partner
search_tag: Partenaire

---

# Quikly

> [Quikly][1], une plateforme de marketing d’urgence, s’appuie sur la psychologie pour motiver les consommateurs, de sorte que les marques peuvent immédiatement augmenter la réponse autour de leurs initiatives marketing clés.

Le partenariat Braze et Quikly vous permet d’accélérer les conversions sur les événements au sein d’un parcours client Braze. Pour ce faire, Quikly utilise la psychologie de l'urgence pour motiver les consommateurs de manière amusante et instantanée. Par exemple, les marques peuvent utiliser Quikly pour acquérir immédiatement de nouveaux utilisateurs abonnés par e-mail et SMS directement dans Braze ou pour motiver d'autres objectifs marketing clés comme le téléchargement de votre application mobile.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Quikly | Un compte partenaire de la marque [Quikly][1] est nécessaire pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][2]. Votre endpoint dépendra de l’URL Braze pour votre instance. |
| Clé API Quikly | (Facultatif) Une clé API Quikly fournie par votre gestionnaire de la réussite client (webhook seulement) |
{: .reset-td-br-1 .reset-td-br-2}

## Cas d’utilisation

Quikly permet aux marques d'accélérer l'acquisition par e-mail ou SMS et incite les utilisateurs abonnés à fournir des données first-party directement dans Braze. Vous pouvez également utiliser Braze pour cibler les anciens clients avec une activation Quikly qui réactivera et conservera cette audience. De plus, les marketeurs peuvent utiliser cette intégration pour inciter des événements spécifiques du parcours client avec des structures de récompense uniques. 

Par exemple :
 - Construisez l’anticipation et l’engagement au fil des jours alors que les consommateurs optent pour une chance de réclamer des récompenses intéressantes avec [Quikly Hype][3]. Les données first-party sont automatiquement transmises à Braze.
 - Accélérez l’acquisition de nouveaux utilisateurs abonnés par e-mail et SMS en utilisant des offres uniques en temps réel basées sur la vitesse de réponse du consommateur, son classement par rapport aux autres, le hasard, ou avant que le temps ou les quantités ne soient épuisés avec [Quikly Swap][4].
 - Motivez des étapes spécifiques du parcours client avec des structures de récompense uniques en utilisant des webhooks.
 - Appliquez des événements ou des attributs personnalisés au profil utilisateur lors de sa participation à une activation Quikly.

## Intégration

Vous trouverez ci-dessous quatre intégrations différentes : acquisition par e-mail, acquisition par SMS, attributs personnalisés et webhooks. L'intégration que vous choisirez dépendra de votre activation Quikly et de votre cas d'utilisation.

{% tabs %}
{% tab Email Acquisition %}

### Acquisition d'e-mails

Si vos activations Quikly collectent les adresses e-mail ou les données de profil des clients, la seule étape requise est de fournir à Quikly votre clé API REST et votre endpoint. Quikly configurera le compte de votre marque pour transmettre ces données à Braze. Si vous souhaitez inclure d'autres attributs d'utilisateur, mentionnez-le lorsque vous fournissez les informations d'identification de l'API à Quikly.

Voici un aperçu de la manière dont Quikly exécute ce flux de travail.
1. Lors de la participation à une activation Quikly, Quikly planifie une recherche d'utilisateur à l'aide de [l'API d'exportation]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour voir si un utilisateur existe avec une `email_address` donnée.
2. Enregistrer ou mettre à jour l’utilisateur
  - Si l’utilisateur existe :
    - Ne créez pas de nouveau profil.
    - Si vous le souhaitez, Quikly peut enregistrer un attribut personnalisé sur le profil utilisateur pour indiquer que l'utilisateur a participé à l'activation.
  - Si l’utilisateur n’existe pas :
    - Quikly crée un profil d'alias uniquement via l’endpoint [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze, en définissant l'e-mail de l'utilisateur comme alias d'utilisateur pour le référencer à l'avenir (puisque l'utilisateur n'aura pas de `external_id`).
    - Si vous le souhaitez, Quikly peut enregistrer des événements personnalisés pour indiquer que ce profil a participé à l'activation de Quikly.

{% details /users/track request %}

#### En-têtes de demande
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Corps de la demande
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
{% tab SMS Acquisition %}

### Abonnements aux SMS

Les activations Quikly permettent de collecter les numéros de téléphone mobile directement auprès des clients et de lancer un nouvel abonnement par SMS. Pour activer cette intégration, fournissez à votre gestionnaire de la réussite client de Quikly le `subscription_group_id`. Vous pouvez accéder à un groupe d’abonnement `subscription_group_id` en accédant à la page **Groupe d’abonnements**.

Quikly effectuera une recherche d'abonnement à l'aide du numéro de téléphone du client et le créditera automatiquement lors de l'activation si un abonnement par SMS existe déjà. Sinon, un nouvel abonnement sera initié et, une fois le statut de l'abonnement vérifié, le client sera crédité.

Voici le flux de travail complet lorsqu'un client fournit son numéro de mobile et son consentement via Quikly :
1. Quikly effectue une recherche d'abonnement en utilisant le [statut du groupe d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status/) pour voir si un `phone` donné est abonnée à un `subscription_group_id`. Si un abonnement existe, créditez l'utilisateur dans l'activation Quikly. Aucune autre action n'est nécessaire.
2. Quikly effectue une recherche d'utilisateur à l'aide de [l'API d'exportation]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) pour voir si un profil d'utilisateur existe avec une `email_address`. Si aucun utilisateur n’existe, créez un profil d'alias uniquement via l’endpoint [/users/track]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze, en définissant l'e-mail de l'utilisateur comme alias d'utilisateur pour le référencer à l'avenir (puisque l'utilisateur n'aura pas de `external_id`).
3. Mettez à jour l'état de l'abonnement en utilisant l’endpoint de [mise à jour du statut du groupe d'abonnement de l'utilisateur]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/).

Pour prendre en charge les flux de travail d'abonnement SMS en double existants, Quikly peut envoyer un événement personnalisé à Braze au lieu du flux de travail ci-dessus. Dans ce cas, plutôt que de mettre directement à jour l'état de l'abonnement, [l'événement personnalisé déclenche le processus de double abonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms/non_native/double_opt_in/) et l'état de l'abonnement est contrôlé périodiquement pour vérifier que l'utilisateur s’est pleinement abonné avant de le créditer dans l'activation Quikly.

{% alert important %}
Braze conseille, lors de la création de nouveaux utilisateurs via l’endpoint /users/track, de prévoir un délai d'environ 2 minutes avant d'ajouter les utilisateurs au groupe d'abonnement concerné, afin de laisser à Braze le temps de créer entièrement le profil utilisateur.
{% endalert %}

{% details Demande /subscription/status/set détaillée %}
#### En-têtes de demande
```
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
```

#### Corps de la demande
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
{% tab Custom Attributes %}
### Attributs personnalisés

En fonction de votre implémentation Braze, vous pouvez désirer que les événements de l'activation Quikly soient traités en cascade par Braze. Par exemple, vous pouvez souhaiter appliquer un attribut utilisateur personnalisé basé sur le niveau ou l'incitation atteint dans l'activation Quikly, ce qui vous permet d'afficher la carte de contenu correspondante lorsqu'ils ouvrent votre application ou se connectent à votre site Web. Quikly travaillera directement avec vous pour mettre en œuvre ces intégrations.

{% endtab %}
{% tab Webhooks %}
### Webhooks
Utilisez des webhooks pour déclencher des incitations lors d'événements spécifiques du parcours client. Par exemple, si vous disposez d'un événement Braze lorsqu’un utilisateur se connecte à votre application, active les notifications push ou utilise votre localisateur de magasin, vous pouvez utiliser un webhook pour déclencher une offre personnalisée pour cet utilisateur en fonction de la configuration d'une activation Quikly spécifique. Parmi les exemples de stratégies, citons le fait de récompenser les premiers X utilisateurs qui effectuent une action (par exemple, se connecter à votre application) avec une offre personnalisée ou de proposer une offre dont la valeur diminue au fur et à mesure que le temps s'écoule afin de motiver une réponse immédiate.

### Créer un Quikly webhook dans Braze

Pour créer un Quikly webhook Remerge à utiliser dans les campagnes ou les Canvas futurs, accédez à la section **Templates & Media** (Modèles et médias) dans la plateforme Braze. Si vous souhaitez créer une campagne de webhook Quikly unique ou utiliser un modèle existant, sélectionnez **Webhook** dans Braze lors de la création d’une nouvelle campagne.

Sélectionnez **Blank Template** (Modèle vierge), et saisissez les éléments suivants pour l'URL du webhook et le corps de la demande :
- **URL du webhook** : https://api.quikly.com/webhook/braze
- **Corps de la demande** : Paire clé-valeur JSON

#### En-têtes et méthode de demande

Quikly requiert un `en-têteHTTP` pour l’autorisation.

- **Méthode HTTP** : POST
- **En-tête de demande** :
  - **Autorisation** : Bearer [PARTNER_AUTHORIZATION_HEADER]
  - **Corps de la demande** : application/json

#### Corps de la demande

Sélectionnez ***JSON key/value pairs (Paire clé-valeur JSON)*** et ajoutez les paires suivantes :
{% raw %}
```
"q_scope": "your-activations-scope-id"
"event": "your-event-identifier"
"email": {{${email_address}}
```
{% endraw %}

### Prévisualiser votre demande

Prévisualisez votre demande dans le volet **Preview (Prévisualiser)** ou accédez à l’onglet `Test` où vous pouvez sélectionner un utilisateur aléatoire, un utilisateur existant ou personnaliser votre propre test pour tester votre webhook.

{% alert important %}
N’oubliez pas d’enregistrer votre modèle avant de quitter la page ! <br>Des modèles de webhook mis à jour sont disponibles dans la liste **Saved Webhook Templates (Modèles de webhooks enregistrés)** lorsque vous créez une nouvelle [campagne de webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
{% endalert %}

{% endtab %}
{% endtabs %}

## Assistance
Pour toute question, contactez votre gestionnaire de la réussite client chez Quikly.

[1]: https://www.quikly.com
[2]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[3]: https://www.quikly.com/urgency-marketing/platform/product-overview/hype
[4]: https://www.quikly.com/urgency-marketing/platform/product-overview/swap
