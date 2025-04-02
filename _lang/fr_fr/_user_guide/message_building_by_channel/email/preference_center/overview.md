---
nav_title: Aperçu
article_title: Overview du centre de préférences
page_order: 1
description: "Cet article décrit le centre de préférences des e-mails et comment le personnaliser."
channel:
  - email
---

# Aperçu du centre de préférences

> En gérant les paramètres d'un centre de préférences, vous offrez à vos utilisateurs un guichet unique où ils peuvent modifier et gérer leurs préférences en matière d'envoi [de messages e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/). Cet article comprend des étapes pour créer un centre de préférences généré par l'API, mais vous pouvez également créer un centre de préférences à l'aide de l'[éditeur par glisser-déposer]({{site.baseurl}}/user_guide/message_building_by_channel/email/preference_center/dnd_preference_center/).

Dans le tableau de bord de Braze, allez dans **Audience** > **Abonnements** > **Centre de préférences e-mail.**

{% alert note %}
Si vous utilisez l' [ancienne navigation]({{site.baseurl}}/navigation), cette page est située dans **Utilisateurs** > **Groupes d'abonnement** > **Centre de préférences e-mail.**
{% endalert %}

C'est ici que vous pouvez gérer et visualiser chaque groupe d'abonnements. Chaque groupe d'abonnement que vous créez est ajouté à cette liste de centres de préférences. Vous pouvez créer plusieurs centres de préférence.

{% alert important %}
Le centre de préférences est destiné à être utilisé dans le cadre du canal d'e-mail de Braze. Les liens du centre de préférences sont dynamiques, basés sur chaque utilisateur et ne peuvent pas être hébergés en externe.
{% endalert %}

## Créer un centre de préférences avec l'API

En utilisant les [endpoints Preference Center Braze]({{site.baseurl}}/api/endpoints/preference_center), vous pouvez créer un centre de préférences, un site web hébergé par Braze, qui peut afficher l'état de l'abonnement de votre utilisateur et les statuts du groupe d'abonnement. Votre équipe de développeurs peut créer le centre de préférences à l'aide de HTML et de CSS afin que le style de la page corresponde aux lignes directrices de votre marque.

L'utilisation de Liquid vous permet de retrouver les noms de vos groupes d'abonnement et le statut de chaque utilisateur. De cette manière, Braze stocke et récupère ces données lors du chargement de la page.

### Conditions préalables

| Condition | Description |
|---|---|
| Activer un centre de préférence | Votre tableau de bord de Braze possède des permissions pour utiliser la fonctionnalité de centre de préférence. |
| Espace de travail valide avec un groupe d'abonnement e-mail, SMS ou WhatsApp. | Un espace de travail avec des utilisateurs valides et un groupe d'abonnement par e-mail, SMS ou WhatsApp. |
| Utilisateur valide | Un utilisateur avec une adresse e-mail et un ID externe. |
| Clé API générale avec des permissions de centre de préférence | Dans le tableau de bord de Braze, allez dans **Paramètres** > **Clés API** pour confirmer que vous avez accès à une clé API avec des autorisations de centre de préférences. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Si vous utilisez l'[ancienne navigation]({{site.baseurl}}/navigation), vous pouvez créer une clé API à partir de la **console de développement** > **Paramètres API.**
{% endalert %}

### Étape 1 : Utilisez l'endpoint Créer un centre de préférences

Commençons par créer un centre de préférences à l'aide de l' [endpoint Créer un centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/post_create_preference_center/). Pour personnaliser votre centre de préférences, vous pouvez inclure du code HTML correspondant à votre image de marque dans les champs `preference_center_page_html` et `confirmation_page_html`.

L'[endpoint Générer l'URL du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/get_create_url_preference_center/) vous permet d'obtenir l'URL du centre de préférences pour un utilisateur spécifique en dehors d'un e-mail envoyé par Braze.

### Étape 2 : Inclure dans votre campagne d'e-mailing

{% multi_lang_include preference_center_warning.md %}

Pour placer un lien vers le centre de préférences dans vos e-mails, utilisez l'étiquette Liquid suivante à l'endroit souhaité dans votre e-mail, de la même manière que vous inséreriez des URL de désabonnement.

{% raw %}
```liquid
{{preference_center.${kitchenerie_preference_center_example}}}
```
{%endraw%}

Vous pouvez également utiliser une combinaison de HTML qui inclut Liquid. Par exemple, vous pouvez coller l'URL suivante dans l'éditeur HTML ou l'éditeur par glisser-déposer. Ceci affichera la mise en page de base du centre de préférence répertoriant automatiquement tous les groupes d'abonnement. 

{% raw %}
```html
<a href="{{preference_center.${kitchenerie_preference_center_example}}}">Edit your preferences</a>
```
{%endraw%}

Le centre de préférences dispose d’une case à cocher permettant à vos utilisateurs de se désabonner de tous les e-mails. Tenez compte du fait que vous ne pourrez pas sauvegarder ces préférences si elles sont envoyées en tant que message de test.

{% alert important %}
L'étiquette Liquid ci-dessus ne fonctionnera que lors du lancement d'une campagne ou d'un Canvas. L'envoi d'un e-mail de test ne génère pas de lien valide.
{% endalert %}

#### Modifier un centre de préférence

Vous pouvez modifier et mettre à jour votre centre de préférences en utilisant l'endpoint [Mettre à jour le centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/put_update_preference_center/). 

#### Identifier les centres de préférences et leurs détails

Pour identifier vos centres de préférences, utilisez le [point de terminaison Afficher les détails du centre de préférences]({{site.baseurl}}/api/endpoints/preference_center/get_view_details_preference_center/) pour renvoyer des informations connexes telles que l'horodatage de la dernière mise à jour, l'ID du centre de préférences, etc.

## Personnalisation

Braze gère les mises à jour du statut d’abonnement depuis le centre de préférences, ce qui le garde synchronisé. Cependant, vous pouvez également créer et héberger votre propre centre de préférences en utilisant les [API des groupes d'abonnement]({{site.baseurl}}/api/endpoints/subscription_groups/) avec les options suivantes.

### Option 1 : Lien avec des paramètres de requête sous forme de chaîne de caractères

Utilisez les paires champ-valeur de la chaîne de caractères dans le corps de l’URL pour transmettre l’ID d’utilisateur et la catégorie d’e-mail à la page, afin que les utilisateurs n’aient qu’à confirmer leur choix de désabonnement. Cette option est valable pour ceux qui stockent un identifiant utilisateur dans un format haché et n’ont pas déjà de centre d’abonnement.

Pour cette option, chaque catégorie de courrier électronique nécessitera son propre lien de désabonnement :<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Il est également possible de hacher l'ID externe de l'utilisateur au point d'envoi à l'aide d'un filtre Liquid. Cela convertira le `user_id` à une valeur de hachage MD5, par exemple :
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

### Option 2 : S'authentifier avec un jeton web JSON

Utilisez un [jeton web JSON](https://auth0.com/learn/json-web-tokens/) pour authentifier les utilisateurs auprès d'une partie de votre serveur web (par exemple, les préférences de compte) qui se trouve normalement derrière une couche d'authentification telle que l'identification par nom d'utilisateur et mot de passe. 

Cette approche ne nécessite pas de paires de valeur de chaîne de requête incorporées dans l’URL, car elles peuvent être transmises dans la charge utile du jeton Web JSON, par exemple :

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```

## Foire aux questions

### Je n'ai pas créé de centre de préférences. Pourquoi mon tableau de bord affiche-t-il "PreferenceCenterBrazeDefault" ?

Il est utilisé pour afficher le centre de préférences lorsque l'ancien Liquid {%raw%}`${preference_center_url}`{%endraw%} est utilisé, ce qui signifie que les étapes du canvas ou les modèles qui font référence à {%raw%}`${preference_center_url}` ou `preference_center.${PreferenceCenterBrazeDefault}`{%endraw%} ne fonctionneront pas. Ceci s'applique également aux messages envoyés précédemment qui comprenaient l'ancien Liquid ou "PreferenceCenterBrazeDefault" dans le message. 

Si vous faites à nouveau référence à {%raw%}`${preference_center_url}`{%endraw%} dans un nouveau message, un centre de préférences nommé "PreferenceCenterBrazeDefault" sera à nouveau créé.