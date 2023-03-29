---
nav_title: Aperçu
article_title: Overview du centre de préférences
page_order: 1
description: "Cet article décrit comment créer et modifier un centre de préférence en utilisant les endpoints du centre de préférence de Braze."
channel:
  - e-mail
---

# Centre de préférence des e-mails

Le centre de préférences des e-mails est un moyen facile de gérer les utilisateurs qui reçoivent certains groupes de bulletins d’information et qui se trouvent dans le tableau de bord sous **Subscription Groups (Groupes d’abonnement)**. Chaque groupe d’abonnement que vous créez est ajouté à la liste du centre de préférences. Cliquez sur le nom du centre de préférence pour voir un aperçu interactif.

Pour placer un lien vers le centre de préférence dans vos e-mails, utilisez la balise Liquid suivante et ajoutez-la à l’emplacement souhaité dans votre e-mail, de la même façon que vous insérez des [URL de désabonnement](#custom-footer).

{% raw %}
```
{{${preference_center_url}}}
```
{% endraw %}

Ceci affichera la mise en page de base du centre de préférence répertoriant automatiquement tous les groupes d'abonnement.

{% alert note %}
Le centre de préférences dispose d’une case à cocher permettant à vos utilisateurs de se désabonner de tous les e-mails. Tenez compte du fait que vous ne pourrez pas sauvegarder ces préférences si elles sont envoyées en tant que message de test.
{% endalert %}

Le centre de préférences est destiné à être utilisé dans le canal e-mail. Les liens du centre de préférences sont dynamiques, basés sur chaque utilisateur et ne peuvent pas être hébergés en externe.

## Personnalisez votre centre de préférences

Avec les [endpoints de centre de préférence]({{site.baseurl}}/api/endpoints/preference_center/), vous pouvez utiliser du code HTML pour mettre à jour le centre de préférences qui est hébergé par Braze. Vous pouvez créer plusieurs centres de préférence. Braze gère les mises à jour du statut d’abonnement depuis le centre de préférences, ce qui le garde synchronisé. Cependant, vous pouvez également créer et héberger votre propre centre de préférence en utilisant les [API de groupes d’abonnement]({{site.baseurl}}/developer_guide/rest_api/subscription_group_api/) avec les options suivantes.

**Option 1 : Lien avec paramètres de requête de chaîne de caractères**

Utilisez les paires champ-valeur de la chaîne de caractères dans le corps de l’URL pour transmettre l’ID d’utilisateur et la catégorie d’e-mail à la page, afin que les utilisateurs n’aient qu’à confirmer leur choix de désabonnement. Cette option est valable pour ceux qui stockent un identifiant utilisateur dans un format haché et n’ont pas déjà de centre d’abonnement.

Pour cette option, chaque catégorie de courrier électronique nécessitera son propre lien de désabonnement :<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Il est également possible de hacher les `external_id` utilisateur au point d’envoi à l’aide d’un filtre Liquid. Cela convertira le `user_id` à une valeur de hachage MD5, par exemple :
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
My encoded string is: {{my_string}}
```
{% endraw %}
{% endalert %}

**Option 2 : Jeton Web JSON**

Utilisez un [jeton Web JSON](https://auth0.com/learn/json-web-tokens/) pour authentifier les utilisateurs sur une partie de votre serveur Web (par exemple, préférences de compte) qui se trouve normalement derrière une couche d’authentification, comme la connexion par nom d'utilisateur et mot de passe. Cette approche ne nécessite pas de paires de valeur de chaîne de requête incorporées dans l’URL, car elles peuvent être transmises dans la charge utile du jeton Web JSON, par exemple :

```json
{
    "user_id": "1234567890",
    "name": "John Doe",
    "category": offers
}
```

### Logo

Pour éditer le logo dans votre centre de préférences e-mail, sélectionnez l’icône d’engrenage <i class="fas fa-cog"></i> et cliquez sur **Edit (Éditer)**.
