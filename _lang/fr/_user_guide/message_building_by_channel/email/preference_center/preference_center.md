---
nav_title: Overview
article_title: Overview du centre de préférences
page_order: 1
description: "Cet article décrit comment créer et modifier un centre de préférences en utilisant les endpoints du centre de préférences de Braze."
channel:
  - email
---

# Centre de préférence des e-mails

Le centre de préférences des e-mails est un moyen facile de gérer les utilisateurs qui reçoivent certains groupes de bulletins d’information et qui se trouvent dans le tableau de bord sous **Groupes d’abonnement**. Chaque groupe d'abonnement que vous créez est ajouté à la liste du centre de préférences. Cliquez sur le nom du centre de préférences pour avoir un aperçu interactif.

Pour placer un lien vers le centre de préférence dans vos e-mails, utilisez la balise Liquid suivante du centre de préférences et ajoutez-la à l’emplacement souhaité dans votre e-mail, de la même façon que vous insérez des [URL de désabonnement](#custom-footer).

{% raw %}
```
{{${preference_center_url}}}
```
{% endraw %}

{% alert note %}
Le centre de préférences dispose d’une case à cocher permettant à vos utilisateurs de se désabonner de tous les e-mails. Tenez compte du fait que vous ne pourrez pas sauvegarder ces préférences si elles sont envoyées en tant que message de test.
{% endalert %}

Le centre de préférences est destiné à être utilisé uniquement dans le canal e-mail lui-même. Les liens du centre de préférences sont dynamiques, basés sur chaque utilisateur et ne peuvent pas être hébergés en externe. Vous pouvez toutefois créer et héberger votre propre centre de préférences personnalisé avec les [endpoints de centre de préférence]({{site.baseurl}}/api/endpoints/preference_center/) et utiliser les [API REST du groupe d’abonnement][25] pour conserver les données en synchronisation avec Braze. Reportez-vous à la section suivante pour plus d’informations.

## Personnalisez votre centre de préférences

Vous pouvez créer et héberger sur votre serveur Web un centre de préférences HTML entièrement personnalisé et synchroniser avec Braze grâce à notre [API][28]. À ce stade, vous ne pouvez avoir qu’un seul centre de préférences qui répertorie tous vos groupes d’abonnement actuels.

**Option 1 : Lien avec paramètres de requête de chaîne de caractères**

Utilisez les paires champ-valeur de la chaîne de caractères dans le corps de l’URL pour transmettre l’ID d’utilisateur et la catégorie d’e-mail à la page, afin que les utilisateurs n’aient qu’à confirmer leur choix de désabonnement. Cette option est valable pour ceux qui stockent un identifiant utilisateur dans un format haché et n’ont pas déjà de centre d’abonnement.

Pour cette option, chaque catégorie de courrier électronique nécessitera son propre lien de désabonnement :<br>
`http://mycompany.com/query-string-form-fill?field_id=John&field_category=offers`

{% alert tip %}
Il est également possible de hacher les `external_id` utilisateur au point d’envoi à l’aide d’un filtre Liquid. Cela convertira le `user_id` à une valeur de hachage md5, par exemple :
{% raw %}
```liquid
{% assign my_string = {{${user_id}}} | md5 %}
Mon string codé est : {{my_string}}
```
{% endraw %}
{% endalert %}

**Option 2 : Jeton Web JSON**

Utilisez un [jeton Web JSON](https://auth0.com/learn/json-web-tokens/) pour authentifier les utilisateurs sur une partie de votre serveur Web (par exemple, préférences de compte) qui se trouve normalement derrière une couche d’authentification, comme la connexion par nom d'utilisateur et mot de passe. Cette approche ne nécessite pas de paires de valeur de chaîne de requête incorporées dans l’URL, car elles peuvent être transmises dans la charge utile du jeton Web JSON, par exemple :

```json
{
    “user_id”: "1234567890",
    "name": "John Doe",
    “category": offers
}
```

### Logo

Vous pouvez modifier le logo de votre centre de préférences. Cliquez sur l’engrenage, puis sur **Edit (Modifier)** dans le menu qui apparaît.

[25]: {{site.baseurl}}/developer_guide/rest_api/subscription_group_api/