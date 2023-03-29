---
nav_title: Meilleures pratiques de collecte
article_title: Meilleures pratiques de collecte
page_order: 3.1
page_type: reference
description: "L’article suivant vous aidera à clarifier les méthodes et les meilleures pratiques de collecte de données pour les nouveaux utilisateurs et les utilisateurs existants."

---

# Meilleures pratiques de collecte de données

> Savoir quand et comment collecter les données utilisateur pour les utilisateurs connus et inconnus peut être difficile à appréhender lorsque vous envisagez le cycle de vie du profil de l'utilisateur de vos clients. L’article suivant vous aidera à clarifier les méthodes et les meilleures pratiques de collecte de données pour les nouveaux utilisateurs et les utilisateurs existants.

## Aperçu

L’exemple suivant comprend un cas d’utilisation de la collecte d’adresses e-mail, mais cette logique peut s’appliquer à de nombreux scénarios de collecte de données différents. Dans cet exemple, nous supposons que vous avez déjà intégré un formulaire d’inscription ou une autre façon de recueillir des informations sur l’utilisateur. 

Une fois qu’un utilisateur vous fournit des informations que vous pouvez enregistrer, nous vous recommandons de vérifier si les données existent déjà dans votre base de données et de créer un profil d’alias utilisateur ou de mettre à jour le profil utilisateur existant, le cas échéant. 

Si un utilisateur inconnu va sur votre site, puis revient ultérieurement pour créer un compte ou s’identifier par e-mail, la fusion de profil doit être traitée avec prudence. En fonction de la méthode dans laquelle vous fusionnez, les informations des utilisateurs avec alias uniquement, ou les données anonymes, peuvent être écrasées.

## Capture des données utilisateur via un formulaire Web

### Étape 1 : Vérifier si l’utilisateur existe

Lorsqu’un utilisateur saisit du contenu via un formulaire Web, vérifiez si un utilisateur avec cette adresse e-mail existe déjà dans votre base de données. Cela peut être fait de deux manières :

- **Vérification de la base de données interne (recommandée)**<br>Si vous avez un enregistrement ou une base de données externe contenant les informations utilisateur fournies en dehors de Braze, vérifiez-le au moment de la soumission de l’adresse e-mail ou de la création du compte pour vous assurer que cette information n’a pas encore été capturée.<br><br>
- **[Endpoint /users/export/id]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/)**<br>Exécutez l’appel suivant et vérifiez si le tableau d’utilisateurs retourné est vide ou contient une valeur :
  ```json
  --data-raw '{
    "email_address": "example@braze.com",
    "fields_to_export": ["external_id", "user_aliases"]
  }'
  ```
Il n’est pas recommandé d’utiliser intensément ce endpoint pour requêter sur un seul utilisateur ; nous avons limité ce endpoint à 2500 requêtes par minute. Pour plus d’informations sur les limites des endpoints, reportez-vous à [Limites de taux par type de demande]({{site.baseurl}}/api/api_limits/#rate-limits-by-request-type).

### Étape 2 : Enregistrer ou mettre à jour l’utilisateur

- **Si un utilisateur existe :**
  - Ne créez pas de nouveau profil.
  - Enregistrez un attribut personnalisé (par ex., `newsletter_subscribed: true`) sur le profil de l’utilisateur pour indiquer que l’utilisateur a communiqué son adresse e-mail en s’inscrivant à la newsletter. Si plusieurs profils utilisateur Braze ont la même adresse e-mail, tous les profils seront exportés.<br><br>
- **Si un utilisateur n’existe pas :**
  - Créez un profil avec alias uniquement via l’endpoint [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) de Braze. Ce endpoint accepte les objets [Alias utilisateur]({{site.baseurl}}/api/objects_filters/user_alias_object/) et crée un profil avec alias uniquement lorsque `update_existing_only` est défini sur `false`. Définissez l’adresse e-mail de l’utilisateur comme alias utilisateur pour référencer cet utilisateur à l’avenir (car l’utilisateur n’aura pas de `external_id`).

![Diagramme montrant le processus de mise à jour d’un profil utilisateur avec alias uniquement. Un utilisateur envoie son adresse e-mail et un attribut personnalisé, son code postal, sur une page de renvoi marketing. Une flèche pointant de la collection de page d’accueil vers un profil utilisateur alias uniquement affiche une demande API Braze au endpoint de suivi utilisateur, avec le corps de la requête contenant le nom d’alias de l’utilisateur, le libellé d’alias, l’e-mail et le code postal. Le profil a le libellé « utilisateur avec Alias Uniquement créé dans Braze » avec les attributs du corps de la requête pour montrer les données qui se reflètent sur le profil nouvellement créé.][3]{: style="max-width:90%;"}

## Identifier les utilisateurs avec alias uniquement

Lorsque vous identifiez les utilisateurs lors de la création du compte, ceux avec alias uniquement peuvent être identifiés et recevoir un ID externe à l’aide de l’endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) en fusionnant l’utilisateur avec alias uniquement avec le profil connu. 

Pour vérifier si un utilisateur est à alias uniquement, [vérifiez si l’utilisateur existe](#step-1-check-if-user-exists) dans votre base de données. 
- Si un enregistrement externe existe, vous pouvez appeler l’endpoint `/users/identify/`. 
- Si l’endpoint [`/users/export/id`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) renvoie un `external_id`, vous pouvez appeler l’endpoint `/users/identify/`.
- Si l’endpoint ne renvoie rien, vous ne devriez pas effectuer un appel `/users/identify/`.

## Capture des données utilisateur lorsque des informations d’utilisateurs avec alias uniquement sont déjà présentes

Lorsqu’un utilisateur crée un compte ou s’identifie en s’inscrivant pour recevoir des e-mails, il y a deux options qui permettent de fusionner les profils en fonction des données à conserver :

### Option 1 : Écraser les données alias uniquement et conserver les données anonymes

Appelez `changeUser()` avant de faire une requête API vers le endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/), puis définissez l’alias utilisateur. 

En appelant `changeUser()` avant la requête , Braze fusionnera et conservera les données de l’utilisateur anonyme (par exemple, si l’utilisateur a téléchargé l’application et enregistré des données personnalisées avant de créer un compte) dans le profil d’utilisateur identifié, mais rendra « orpheline », toutes les données associées au profil utilisateur avec alias uniquement (attributs, événements, achats, etc.).

![Diagramme montrant le processus d’écrasement des données Alias Uniquement et la conservation des données anonymes lors de l’identification d’un utilisateur. Le processus commence par un utilisateur anonyme et son identifiant Braze. L’utilisateur crée alors un compte et les données anonymes de l’utilisateur sont migrées vers un profil utilisateur identifié lorsque changeUser est appelé. L’utilisateur identifié a maintenant un ID Braze et un ID externe. Une flèche pointant de l’utilisateur identifié vers un utilisateur identifié avec un alias montre une requête d’API Braze vers le endpoint d'identification Utilisateurs, avec l’ID externe, le nom d’alias et le libellé d'alias de l’utilisateur. Pendant cette étape, les données utilisateur associées à cet utilisateur avec alias seulement sont perdues. L’étape finale montre l’utilisateur identifié avec un ID Braze, un ID externe, un nom d’alias, un libellé d'alias, mais aucun des attributs personnalisés associés au profil avec alias uniquement avant la fusion.][1]{: style="max-width:90%;"}

#### Conserver les informations de profil d’alias utilisateur
Si vous avez des événements ou des attributs que vous souhaitez conserver lorsque vous fusionnez des profils d’utilisateur, vous pouvez exporter les données d’utilisateur avec alias avant de l’identifier en utilisant le endpoint [`/users/export/ids`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/), et ensuite réassocier les attributs, événements et achats à l’utilisateur identifié.

### Option 2 : Écraser les données anonymes et conserver le profil alias uniquement

Faites une requête à l’API Braze au endpoint [`/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) pour identifier tout utilisateur correspondant à un alias utilisateur donné. Si cela est possible, Braze migrera les données d’alias utilisateur vers le profil utilisateur identifié. Pour éviter une condition de course, nous vous recommandons vivement de mettre en place un délai de 5 minutes. Ensuite, appelez `changeUser()`.

En appelant `changeUser()` après avoir touché le endpoint `/users/identify` Braze fusionnera et conservera toutes les données associées au profil alias uniquement, mais rendra « orphelines » les données de tout utilisateur anonyme.

![Diagramme montrant le processus d’écrasement des données anonymes avec conservation du profil « alias uniquement ». Le processus commence par un utilisateur anonyme et son identifiant Braze. Puis l’utilisateur crée un compte. Une flèche pointant de l’étape de création de compte vers le profil utilisateur identifié montre une requête d’API Braze vers le endpoint d’identification des utilisateurs, avec l’ID externe, le nom d’alias et le libellé d'alias. Une case au-dessus de la flèche montre que cet utilisateur avec alias-uniquement existe déjà dans Braze, et a des attributs personnalisés associés. Ces attributs personnalisés sont préservés et écrits dans le profil utilisateur identifié. La dernière étape montre l’appel changeUser , après quoi les données anonymes de l’utilisateur sont perdues.][2]{: style="max-width:90%;"}

## Ressources complémentaires
- Consultez notre article sur le [cycle de vie du profil de l'utilisateur ]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)Braze pour un contexte supplémentaire.<br>
- Documentation sur la définition des ID utilisateur et l’appel de la méthode `changeUser()` pour [Android]({{site.baseurl}}/developer_guide/platform_integration_guides/android/analytics/setting_user_ids/), [iOS]({{site.baseurl}}/developer_guide/platform_integration_guides/ios/analytics/setting_user_ids/#suggested-user-id-naming-convention), et [Web]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids/).

[1]: {% image_buster /assets/img/user_profile_process.png %}
[2]: {% image_buster /assets/img/user_profile_process2.png %}
[3]: {% image_buster /assets/img/user_profile_process3.png %}
