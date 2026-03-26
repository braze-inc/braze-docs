---
nav_title: Centre de préférences des e-mails API
article_title: Centre de préférences des e-mails API
page_order: 1
description: "Cet article décrit le centre de préférences des e-mails API et explique comment le personnaliser."
channel:
  - email
---

# Centre de préférences des e-mails API

> En configurant un centre de préférences, vous offrez à vos utilisateurs un guichet unique pour modifier et gérer leurs préférences de notification pour vos [e-mails]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Cet article décrit les étapes pour créer un centre de préférences généré par API, mais vous pouvez également en créer un à l'aide de l'[éditeur par glisser-déposer]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/).

Dans le tableau de bord de Braze, rendez-vous dans **Audience** > **Centres de préférences e-mail**.

C'est ici que vous pouvez gérer et visualiser chaque groupe d'abonnement. Chaque groupe d'abonnement que vous créez est ajouté à cette liste de centres de préférences. Vous pouvez créer plusieurs centres de préférences.

{% alert important %}
Le centre de préférences est conçu pour être utilisé dans le cadre du canal e-mail de Braze. Les liens du centre de préférences sont dynamiques, propres à chaque utilisateur, et ne peuvent pas être hébergés en externe.
{% endalert %}

## Création d'un centre de préférences avec l'API

En utilisant les [endpoints Preference Center de Braze]({{site.baseurl}}/api/endpoints/preference_center), vous pouvez créer un centre de préférences, c'est-à-dire un site web hébergé par Braze, qui affiche l'état d'abonnement de vos utilisateurs et les statuts de leurs groupes d'abonnement. Votre équipe de développeurs peut créer le centre de préférences en HTML et CSS afin que le style de la page corresponde aux lignes directrices de votre marque.

Grâce à Liquid, vous pouvez récupérer les noms de vos groupes d'abonnement ainsi que le statut de chaque utilisateur. Braze stocke et récupère ces données lors du chargement de la page.

### Conditions préalables

| Condition | Description |
|---|---|
| Centre de préférences activé | Votre tableau de bord de Braze dispose des autorisations nécessaires pour utiliser la fonctionnalité de centre de préférences. |
| Espace de travail valide avec un groupe d'abonnement e-mail, SMS ou WhatsApp | Un espace de travail fonctionnel avec des utilisateurs valides et un groupe d'abonnement e-mail, SMS ou WhatsApp. |
| Utilisateur valide | Un utilisateur avec une adresse e-mail et un ID externe. |
| Clé API générée avec des autorisations de centre de préférences | Dans le tableau de bord de Braze, allez dans **Paramètres** > **Clés API** pour vérifier que vous avez accès à une clé API avec des autorisations de centre de préférences. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 1 : Utiliser l'endpoint Créer un centre de préférences

Commençons par créer un centre de préférences à l'aide de l'[endpoint Créer un centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/). Pour personnaliser votre centre de préférences, vous pouvez inclure du code HTML correspondant à votre image de marque dans les champs `preference_center_page_html` et `confirmation_page_html`.

L'[endpoint Générer l'URL du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) vous permet d'obtenir l'URL du centre de préférences pour un utilisateur spécifique en dehors d'un e-mail envoyé par Braze.

### Étape 2 : Inclure le lien dans votre campagne e-mail

{% multi_lang_include alerts/important_alerts.md alert='Preference Center warning' %}

Pour insérer un lien vers le centre de préférences dans vos e-mails, utilisez l'étiquette Liquid suivante à l'endroit souhaité, de la même manière que vous inséreriez des URL de désabonnement.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Vous pouvez également utiliser une combinaison de HTML et de Liquid. Par exemple, vous pouvez coller le code suivant en tant qu'URL dans l'éditeur HTML ou l'éditeur par glisser-déposer. Cela affichera la mise en page de base du centre de préférences, répertoriant automatiquement tous les groupes d'abonnement e-mail. Si vous utilisez l'[aliasage de lien]({{site.baseurl}}/user_guide/message_building_by_channel/email/templates/link_aliasing/), ajoutez un point d'interrogation (`?`) après l'étiquette Liquid afin que Braze puisse ajouter les paramètres de suivi.

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}?">Edit your preferences</a>
```
{%endraw%}

Le centre de préférences dispose d'une case à cocher permettant à vos utilisateurs de se désabonner de tous les e-mails. Notez que ces préférences ne pourront pas être enregistrées si le message est envoyé en tant que test.

{% alert important %}
L'étiquette Liquid ci-dessus ne fonctionne que lors du lancement d'une campagne ou d'un Canvas. L'envoi d'un e-mail de test ne génère pas de lien valide. Pour vérifier le lien du centre de préférences, lancez le message dans une campagne ciblant uniquement votre profil de test.
{% endalert %}

#### Modifier un centre de préférences

Vous pouvez modifier et mettre à jour votre centre de préférences en utilisant l'endpoint [Mettre à jour le centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/). 

#### Identifier les centres de préférences et leurs détails

Pour identifier vos centres de préférences, utilisez l'endpoint [Afficher les détails du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) afin de récupérer des informations telles que l'horodatage de la dernière mise à jour, l'ID du centre de préférences, etc.

## Personnalisation

Braze gère les mises à jour du statut d'abonnement depuis le centre de préférences, ce qui le maintient synchronisé. Cependant, vous pouvez également créer et héberger votre propre centre de préférences en utilisant les [API des groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups/) avec les options suivantes.

### Option 1 : Lien avec des paramètres de requête sous forme de chaîne de caractères

Utilisez des paires champ-valeur dans la chaîne de requête de l'URL pour transmettre l'ID de l'utilisateur et la catégorie d'e-mail à la page, afin que les utilisateurs n'aient qu'à confirmer leur choix de désabonnement. Cette option convient à ceux qui stockent un identifiant utilisateur sous forme hachée et ne disposent pas déjà d'un centre d'abonnement.

Pour cette option, chaque catégorie d'e-mail nécessite son propre lien de désabonnement :<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Il est également possible de hacher l'ID externe de l'utilisateur au moment de l'envoi à l'aide d'un filtre Liquid. Cela convertira le `user_id` en une valeur de hachage MD5, par exemple :
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Option 2 : S'authentifier avec un jeton web JSON

Utilisez un [jeton web JSON](https://auth0.com/learn/json-web-tokens/) pour authentifier les utilisateurs auprès d'une partie de votre serveur web (par exemple, les préférences de compte) qui se trouve normalement derrière une couche d'authentification telle qu'un identifiant et un mot de passe. 

Cette approche ne nécessite pas de paires champ-valeur de chaîne de requête intégrées dans l'URL, car elles peuvent être transmises dans la charge utile du jeton web JSON, par exemple :

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": "offers"
}
```

## Foire aux questions

### Je n'ai pas créé de centre de préférences. Pourquoi « PreferenceCenterBrazeDefault » s'affiche-t-il sur mon tableau de bord ?

Ceci sert à afficher le centre de préférences lorsque l'ancien Liquid {%raw%}`${preference_center_url}`{%endraw%} est utilisé, ce qui signifie que les étapes du canvas ou les modèles qui font référence à {%raw%}`${preference_center_url}` ou `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} ne fonctionneront pas. Cela s'applique également aux messages précédemment envoyés qui incluaient l'ancien Liquid ou « PreferenceCenterBrazeDefault » dans le corps du message. 

Si vous faites à nouveau référence à {%raw%}`${preference_center_url}`{%endraw%} dans un nouveau message, un centre de préférences nommé « PreferenceCenterBrazeDefault » sera recréé.

### Les centres de préférences prennent-ils en charge plusieurs langues ?

Non. Cependant, vous pouvez utiliser Liquid lorsque vous rédigez le code HTML pour les pages personnalisées d'abonnement et de désabonnement. Si vous utilisez des liens dynamiques pour gérer les désabonnements, il s'agit d'un lien unique. 

Par exemple, si vous suivez le taux de désabonnement des utilisateurs hispanophones, vous devrez soit utiliser des campagnes distinctes, soit exploiter l'analytique autour de Currents (par exemple en vérifiant quand un utilisateur se désabonne et en consultant la langue préférée de cet utilisateur).

Autre exemple : pour suivre les taux de désabonnement des utilisateurs hispanophones, vous pourriez ajouter une chaîne de caractères de paramètre de requête telle que `?Spanish=true` à l'URL de désabonnement si la langue de l'utilisateur est l'espagnol, et utiliser un lien de désabonnement classique dans le cas contraire :

{% raw %}
```liquid
{% if ${language} == 'spanish' %} "${unsubscribe_url}?spanish=true"
{% else %}
${unsubscribe_url}
{% endif %}
```
{% endraw %}

Ensuite, grâce à Currents, vous pourriez identifier les utilisateurs hispanophones et le nombre d'événements de clic sur ce lien de désabonnement.

### Les liens de désabonnement et les centres de préférences e-mail sont-ils tous deux obligatoires pour l'envoi ?

Non. Si le message « Le corps de votre e-mail ne contient pas de lien de désabonnement » s'affiche lors de la composition d'une campagne e-mail, cet avertissement est normal si votre lien de désabonnement se trouve dans un bloc de contenu.

### Comment mettre à jour l'icône par défaut du navigateur ?

Par défaut, l'icône affichée à côté du nom de l'onglet du navigateur (favicon) utilise le logo Braze. Pour ajouter une favicon personnalisée, définissez-la via l'attribut `links-tags` dans votre appel API [Créer ou Mettre à jour le centre de préférences]({{site.baseurl}}/api/endpoints/preference_center). Braze insère ensuite la balise {% raw %}`<link rel="icon" ...>`{% endraw %} dans la page hébergée pour vous.

{% raw %}
```
{
  "name": "MyPreferenceCenter",
  "preference_center_title": "Email Preferences",
  "preference_center_page_html": "<!doctype html> ...",
  "confirmation_page_html": "<!doctype html> ...",
  "state": "active",
  "options": {
    "links-tags": [
      {
        "rel": "icon",
        "type": "image/png",
        "sizes": "32x32",
        "href": "https://yourcdn.com/path/to/favicon-32x32.png"
      },
      {
        "rel": "shortcut icon",
        "type": "image/x-icon",
        "href": "https://yourcdn.com/path/to/favicon.ico"
      },
      {
        "rel": "apple-touch-icon",
        "sizes": "180x180",
        "href": "https://yourcdn.com/path/to/apple-touch-icon.png"
      }
    ]
  }
}
```
{% endraw %}