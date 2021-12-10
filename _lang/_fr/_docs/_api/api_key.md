---
nav_title: "Aperçu de la clé API"
article_title: Aperçu de la clé API REST
page_order: 2.1
description: "Cet article de référence couvre le concept de clés d'API, ce pour quoi elles sont utilisées et comment elles sont utilisées."
page_type: Référence
---

# Aperçu de la clé API REST

> Cet article de référence couvre deux des trois principaux types de clés que vous verrez au Brésil, la clé d'API REST ou la clé API de groupe d'applications, appelée `api_key`, et la clé d'identification de l'application, connue sous le nom de `app_id`, ainsi que ce que sont ces clés, comment ils sont utilisés au Brésil, leurs permissions et comment les garder en sécurité.

En plus de ces clés, il existe également un troisième type de clé appelée Clefs d'identification qui peut être utilisé pour référencer des choses spécifiques comme des modèles, Canvases, campagnes, Cartes de Contenu et segments de l'API. Les informations sur ces types/clés d'identification API peuvent être trouvées [ici][2].

## Qu'est-ce qu'une clé API de groupe d'API REST API ?

Une clé d'interface de programmation d'application REST (clé d'API REST) est un code unique qui est transmis dans une API pour authentifier l'appel API et identifier l'application ou l'utilisateur appelant. L'accès à l'API est fait à l'aide de requêtes web HTTPS vers le point de terminaison de l'API REST de votre entreprise. Nous utilisons des clés d'API REST à Braze en tandem avec nos clés d'identification pour suivre, accéder, envoyer, exporter, et analysez les données pour vous assurer que tout fonctionne en douceur à la fois sur votre côté et sur celui de notre côté.

Les groupes d'applications et les clés API vont de pair au Brésil. Les groupes d'applications sont conçus pour héberger des versions de la même application sur plusieurs plateformes. De nombreux clients utilisent également des groupes d'applications pour contenir des versions gratuites et premium de leurs applications sur la même plateforme. Comme vous pouvez le remarquer, ces groupes d'applications utilisent également l'API REST et ont leurs propres clés d'API REST. Ces clés peuvent être individuellement étendues pour inclure l'accès à des terminaux spécifiques sur l'API. Chaque appel à l'API doit inclure une clé avec accès au point de terminaison.

Nous nous référons à la fois à la clé d'API REST et à la clé d'API de groupe d'applications comme la `api_key`. La `api_key` est incluse dans chaque requête comme un en-tête de requête et agit comme une clé d'authentification qui vous permet d'utiliser nos API REST. Ces API REST sont utilisées pour suivre les utilisateurs, envoyer des messages, exporter des données utilisateur et plus encore.  Lorsque vous créez une nouvelle clé d'API REST, vous devrez lui donner accès à des terminaux spécifiques. En assignant des permissions spécifiques à une clé API, vous pouvez limiter exactement quels appels une clé API peut s'authentifier.

### Où puis-je le trouver?

Vos clés API peuvent toujours être trouvées dans le tableau de bord de Braze dans la **Console développeur** dans **Réglages**. En haut de cette nouvelle page, vous trouverez la section **clés API REST**. Ici vous pouvez voir toutes vos clés API REST API/App Group API disponibles et créer de nouvelles clés API.

### Comment puis-je l'utiliser ?

Avant avril 2020, les clés API seraient incluses dans le corps de la requête API ou dans l'URL de la requête en tant que paramètre. Braze a maintenant mis à jour la façon dont nous lisons les clés de l'API. Les clés API sont maintenant définies avec l'en-tête de requête d'autorisation HTTP, ce qui rend vos clés API plus sécurisées.

Tandis que l'ancienne façon de passer des clés API continue de fonctionner, après une période de temps, cela sera définitivement supprimé et nous exhortons donc les utilisateurs à mettre à jour les appels API en conséquence.

{% alert important %}
__Vous cherchez le paramètre `api_key` dans vos points de terminaison Braze ? _<br> Depuis mai 2020, Braze a changé la façon dont nous lisons les clés API pour être plus sécurisés. Les clés API doivent maintenant être passées en tant qu'en-tête de requête, veuillez consulter VOTRE REST-API-KEY dans chaque exemple de requête de point d'extrémité. <br><br> Braze continuera à supporter la `api_key` en passant par le corps de la requête et les paramètres de l'URL, mais finira par être couché au soleil. Veuillez mettre à jour vos appels API en conséquence.
{% endalert %}

### Autorisations de la clé REST API

Les permissions de la clé API sont des autorisations que vous pouvez assigner à un utilisateur ou à un groupe pour limiter leur accès à certains appels API.

{% tabs %}
{% tab User Data %}

| Permission                            | Libellé                                                                                                                      |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| `Suivre les utilisateurs`             | Enregistrer les attributs des utilisateurs, les événements personnalisés et les achats                                       |
| `Supprimer les utilisateurs`          | Supprimer n'importe quel utilisateur.                                                                                        |
| `Nouvel alias`                        | Créer un nouvel alias pour un utilisateur existant.                                                                          |
| `Identifier les utilisateurs`         | Requête d'informations de profil utilisateur par ID d'utilisateur.                                                           |
| `Exporter les identifiants`           | Requête pour les informations de profil utilisateur par identificateur, par exemple device_id, email_address, external_id. |
| `Exporter les utilisateurs`           | Requête pour les informations de profil utilisateur par segment.                                                             |
| `Renommer les identifiants externes`  | Renommer l'ID externe existant d'un utilisateur.                                                                             |
| `supprimer les identifiants externes` | Supprimer l'ID externe obsolète d'un utilisateur.                                                                            |
{: .reset-td-br-1 .reset-td-br-2}

 {% endtab %}
 {% tab Email %}

| Nom                                     | Libellé                                                        |
| --------------------------------------- | -------------------------------------------------------------- |
| `Se désabonner`                         | Requête pour les adresses e-mail désabonnées.                  |
| `email.status`                          | Changer le statut de l'adresse e-mail.                         |
| `Vous avez bouncé votre adresse e-mail` | Requête pour les adresses e-mail rebondissantes.               |
| `Retirer l'e-mail`                      | Retirer les adresses e-mail de votre liste de rebondissements. |
| `Supprimer le spam`                     | Retirer les adresses e-mail de votre liste de spams.           |
| `Liste noire`                           | Liste noire des adresses e-mail.                               |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Messages %}

| Nom                           | Libellé                                                               |
| ----------------------------- | --------------------------------------------------------------------- |
| `envoyer des messages`        | Envoyez un message immédiat et ad hoc à des utilisateurs spécifiques. |
| `Créer un calendrier`         | Planifier un message à envoyer à une heure précise.                   |
| `Mettre à jour le calendrier` | Mettre à jour un message planifié.                                    |
| `Supprimer le planning`       | Supprimer un message programmé.                                       |
| `Programmer les diffusions`   | Interroger tous les messages de diffusion programmés.                 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Campaigns %}

| Nom                         | Libellé                                                                        |
| --------------------------- | ------------------------------------------------------------------------------ |
| `envoyer`                   | Déclencher l'envoi d'une campagne existante.                                   |
| `Créer un planning`         | Planifier un futur envoi d'une campagne avec une livraison déclenchée par API. |
| `Mettre à jour le planning` | Mettre à jour une campagne planifiée avec une livraison déclenchée par l'API.  |
| `Supprimer le planning`     | Supprimer une campagne planifiée avec une livraison déclenchée par l'API       |
| `campagnes.liste`           | Requête pour une liste de campagnes.                                           |
| `Séries de données`         | Requête pour les analyses de campagne sur une période donnée.                  |
| `Détails des campagnes`     | Requêtes pour les détails d'une campagne spécifique.                           |
| `Séries de données`         | Requête pour l'envoi de messages analytiques sur une période donnée.           |
| `Créer un id`               | Créer un ID d'envoi pour le suivi des diffusions de messages.                  |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Canvas %}

| Nom                            | Libellé                                                                       |
| ------------------------------ | ----------------------------------------------------------------------------- |
| `Envoyer`                      | Déclencher l'envoi d'un Canvas existant.                                      |
| `Créer un planning`            | Planifiez un futur envoi d'un Canvas avec une livraison déclenchée par l'API. |
| `Planifier la mise à jour`     | Mettre à jour une Canvas planifiée avec une livraison déclenchée par API.     |
| `Supprimer le planning`        | Supprimer une Canvas planifiée avec une livraison déclenchée par l'API.       |
| `Liste de toiles`              | Requête pour une liste de Canvases.                                           |
| `Séries de données`            | Requête d'analyses de Canvas sur une période donnée.                          |
| `Détails de la page d'accueil` | Demander des détails sur une toile spécifique.                                |
| `Récapitulatif des données`    | Requête de rollups de Canvas analytics sur une période donnée.                |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Segments %}

| Nom                   | Libellé                                              |
| --------------------- | ---------------------------------------------------- |
| `segments.list`       | Requête pour une liste de Segments.                  |
| `Segments de données` | Requête d'analyse de segment sur une période donnée. |
| `détails`             | Requête pour les détails d'un segment spécifique.    |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Purchases %}

| Nom                          | Libellé                                                                                      |
| ---------------------------- | -------------------------------------------------------------------------------------------- |
| `Liste des produits achetés` | Requête pour une liste de produits achetés dans votre application.                           |
| `Revenus en série`           | Requête de l'argent total dépensé par jour dans votre application sur une période donnée.    |
| `Quantité d'achat`           | Requête sur le nombre total d’achats par jour dans votre application sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Events %}

| Nom                                | Libellé                                                                           |
| ---------------------------------- | --------------------------------------------------------------------------------- |
| `liste des événements`             | Requête pour une liste d'événements personnalisés.                                |
| `Données de la série d'événements` | Interrogation des occurrences d'un événement personnalisé sur une période donnée. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab News Feed %}

| Nom                   | Libellé                                                         |
| --------------------- | --------------------------------------------------------------- |
| `Liste`               | Requête pour une liste des cartes de flux d'actualités.         |
| `Données de la série` | Requête d'analyses de flux d'actualités sur une période donnée. |
| `Détails du flux`     | Requête pour les détails d'un fil d'actualités spécifique.      |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Sessions %}

| Nom                 | Libellé                                                |
| ------------------- | ------------------------------------------------------ |
| `Séries de données` | Demander des sessions par jour sur une plage de temps. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab KPIs %}

| Nom                                     | Libellé                                                                                                          |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------- |
| `Kpi.mau.série de données`              | Requête pour les utilisateurs actifs totaux uniques sur une fenêtre roulante de 30 jours sur une plage de temps. |
| `Kpi.dau.série de données`              | Requête pour les utilisateurs actifs uniques par jour sur une plage de temps.                                    |
| `Nouvelle série de données utilisateur` | Requête pour les nouveaux utilisateurs par jour sur une plage de temps.                                          |
| `kpi.uninstalls.uninstall.data_series`  | Requête de désinstallation d'applications par jour sur une période donnée.                                       |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Templates %}

| Nom                            | Libellé                                                         |
| ------------------------------ | --------------------------------------------------------------- |
| `Créer un modèle d'e-mail`     | Créer un nouveau modèle d'e-mail sur le tableau de bord.        |
| `Mise à jour des modèles`      | Mettre à jour un modèle d'e-mail stocké sur le tableau de bord. |
| `Informations sur les modèles` | Requête pour les informations d'un modèle spécifique.           |
| `Liste des modèles`            | Requête pour une liste de modèles de courriels.                 |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab SSO %}

| Nom              | Libellé                                                                                                            |
| ---------------- | ------------------------------------------------------------------------------------------------------------------ |
| `Sso.saml.login` | Configurer la connexion initiée par le fournisseur d'identité. Lisez notre documentation pour plus d'informations. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Content Blocks %}

| Nom                                     | Libellé                                                  |
| --------------------------------------- | -------------------------------------------------------- |
| `Informations sur le contenu des blocs` | Requête pour les informations d'un modèle spécifique.    |
| `Liste des blocs de contenu`            | Requête pour une liste de blocs de contenu.              |
| `Créer des blocs de contenu`            | Créer un nouveau bloc de contenu sur le tableau de bord. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% tab Subscription %}

| Nom                 | Libellé                                                                                                                 |
| ------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| `Définir un statut` | Définir le statut du groupe d'abonnement.                                                                               |
| `Obtenir le statut` | Obtenir le statut du groupe d'abonnement.                                                                               |
| `Obtenir`           | Obtenir le statut des groupes d'abonnement auxquels des utilisateurs spécifiques sont explicitement abonnés/désabonnés. |
{: .reset-td-br-1 .reset-td-br-2}

{% endtab %}
{% endtabs %}

Veuillez consulter notre site de [documentation de Braze][5] ou notre [documentation de Braze Postman][6] pour une description complète de ces points de terminaison de l'API.

{% alert important %}
Une fois que vous avez créé une nouvelle clé d'API, vous ne pouvez pas modifier la portée des permissions ou les adresses IP en liste blanche. Cette limitation est en place pour des raisons de sécurité. Si vous avez besoin de changer la portée d'une clé, créer une nouvelle clé avec les permissions mises à jour et implémenter cette clé à la place de l'ancienne clé. Une fois que vous avez terminé votre implémentation, continuez et supprimez l'ancienne clé.
{% endalert %}

## La clé API de l'App Identifier

La clé API de l'App Identifier ou `app_id` est un paramètre associant l'activité à une application spécifique dans votre groupe d'applications. Il désigne l'application avec laquelle vous interagissez dans le groupe d'applications. Par exemple, vous trouverez que vous aurez un `app_id` pour votre application iOS, un `app_id` pour votre application android et un `app_id` pour votre intégration web. Chez Braze, vous pourriez trouver que vous avez plusieurs applications pour la même plate-forme à travers les différents types de plates-formes supportés par Braze.

Les identifiants d'application à Braze sont utilisés lors de l'intégration du SDK et sont également utilisés pour référencer une application spécifique dans les appels à l'API REST. Avec `app_id` vous pouvez faire beaucoup de choses comme extraire des données pour un événement personnalisé qui s'est produit pour une application particulière, récupérer les statistiques de désinstallation, les nouvelles statistiques d'utilisateur, les statistiques DAU et les statistiques de démarrage de session pour une application particulière.

Parfois, vous pouvez trouver qu'on vous demande un `app_id` mais vous ne travaillez pas avec une application, parce que c'est un champ hérité spécifique à une plate-forme spécifique, vous pouvez « omettre » ce champ en incluant n'importe quelle chaîne de caractères comme espace réservé pour ce paramètre obligatoire.

### Où puis-je le trouver?

Il y a deux façons de localiser votre `app_id`:

1. Vous pouvez trouver cet identifiant `app_id` ou application dans la **Console développeur** dans **Paramètres**. Sur cette nouvelle page, sous **Identification**, vous pourrez voir chaque `app_id` qui existe pour vos applications.

2. Allez à **Gérer les paramètres** sous **Paramètres**. À partir de cette nouvelle page, dans l'onglet **Paramètres** , Au milieu de la page vous trouverez une "clé API pour __NOM APP__ sur __PLATEFORM__" (e. "API Key for Ice Cream on iOS). Cette clé API est votre identifiant d'application.

### Plusieurs clés API d'identification de l'application

Lors de la configuration du SDK, le cas d'utilisation le plus courant pour plusieurs clés API d'identification d'applications est de séparer ces clés pour le débogage et de publier les variantes de compilation. Pour basculer facilement entre plusieurs clés API d'identification d'applications dans vos builds, nous vous recommandons de créer un frein `séparé. ml` fichier pour chaque [version pertinente][3]. Une variante de construction est une combinaison de type de construction et de saveur de produit. Notez que par défaut, [un nouveau projet Android est configuré avec `debug` et `version` types de build][8] et aucune saveur de produit.

Pour chaque variante de compilation pertinente, créez un nouveau `braze.xml` dans `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_appboy_api_key">REPLACE_WITH_YOUR_BUILD_VARIANT_API_KEY</string>
</resources>
```
Quand la variante de compilation est compilée, elle utilisera la nouvelle clé API.

## Sécurité de la clé API REST

La sécurité est de la plus haute importance au Brésil. Étant donné que les clés d'API REST permettent d'accéder à des terminaux REST API potentiellement sensibles, veuillez sécuriser ces clés et ne les partager qu'avec des partenaires de confiance. Ils ne devraient jamais être exposés au public. Par exemple, n'utilisez pas cette clé pour passer des appels AJAX à partir de votre site Web ou pour l'exposer d'une autre manière publique.

Une bonne pratique de sécurité est d'assigner un utilisateur seulement autant d'accès que nécessaire pour terminer son travail : ce principe peut également être appliqué aux clés API en assignant des permissions à chaque clé. Ces autorisations vous donnent une meilleure sécurité et un meilleur contrôle sur les différentes zones de votre compte.

Avec les identifiants de l'application, l' `app_id` est assigné par Braze et les autorisations ne peuvent pas être assignées ou révoquées. En raison de la nature de la relation entre `app_id` et le SDK, garder cet identifiant sécurisé est __crucial__ dans la sécurité de votre application.


[2]: {{site.baseurl}}/api/identifier_types/
[3]: https://developer.android.com/studio/build/build-variants.html
[5]: {{site.baseurl}}/api/basics/
[6]: https://documenter.getpostman.com/view/4689407/SVYrsdsG?version=latest#intro
[8]: http://tools.android.com/tech-docs/new-build-system/user-guide#TOC-Build-Types
