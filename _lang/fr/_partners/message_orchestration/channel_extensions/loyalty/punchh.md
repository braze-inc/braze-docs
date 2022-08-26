---
nav_title: Punchh
article_title: Punchh
page_order: 5
description: "Cet article présente le partenariat entre Braze et Punchh, une plateforme de fidélité et d’engagement, qui vous permet de synchroniser les données sur les deux plateformes. Les données publiées dans Braze seront disponibles pour la segmentation et peuvent synchroniser les données des utilisateurs dans Punchh via des modèles de webhooks configurés dans Braze. "
alias: /partners/punchh/
page_type: partner
search_tag: Partenaire

---

# Punchh

> [Punchh](https://punchh.com/) est une plateforme de fidélité et d’engagement leader du secteur qui permet aux marques de proposer des programmes de fidélité omnicanal à la fois en magasin et en ligne. 

L’intégration de Braze et de Punchh vous permet de synchroniser les données à des fins de cadeaux et de fidélisation sur les deux plateformes. Les données publiées dans Braze seront disponibles pour la segmentation et peuvent synchroniser les données des utilisateurs dans Punchh via des webhooks dans Braze.

## Conditions préalables

| Configuration requise | Description |
|---|---|
| Compte Punchh | Un compte Punchh est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br>
<br>
 Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][6]. Votre endpoint dépend de l’URL Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Punchh propose plusieurs endpoints aux clients de Braze pour les aider à ajouter des ID externes dans la plateforme Punchh en utilisant les endpoints d’API Punchh suivants. Une fois les ID externes ajoutés, créez un adaptateur dans Punchh, fournissez vos identifiants Braze et sélectionnez les événements que vous souhaitez synchroniser. Ensuite, vous pouvez prendre l’ID de segment Punchh et l’utiliser pour créer un webhook Punchh pour déclencher la synchronisation du client dans un parcours Canvas.

### Événements disponibles à synchroniser {#available-events-to-sync}
1. Invité
2. Enregistrement fidélité
3. Enregistrement cadeau
4. Échange de points
5. Récompenses
6. Notifications de transaction
7. Notifications marketing

{% alert note %}
Consultez la documentation de Punchh sur les exemples de charges utiles pour ces événements disponibles. 
{% endalert %}

### Étape 1 : Configurer les endpoints externes d’ingestion d’ID

Des ID externes de Braze peuvent être ajoutés en utilisant les critères d’évaluation suivants pour les utilisateurs de Punchh nouveaux et existants.

{% alert important %}
Les valeurs des champs `external_source` et `external_source_id` doivent être uniques dans Punchh et ne pas être associées à des profils existants.
{% endalert %}

1. Nouveaux utilisateurs de Punchh<br>

Créez de nouveaux utilisateurs dans Punchh avec un endpoint d’inscription à Punchh en utilisant les champs `external_source` et `external_source_id`. Punchh permet d’envoyer des identifiants externes avec un profil utilisateur via l’un des endpoints suivants :
- [API d’inscription mobile](https://developers.punchh.com/mobile-apis/users/mobile-sign-up)
- [API d’inscription SSO](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-signup)<br>
<br>

2. Utilisateurs Punchh existants <br>

Mettez à jour `external_source_id` pour les utilisateurs Punchh existants. Punchh permet d’ajouter des identifiants externes à un profil via un endpoint de mise à jour de l’API utilisateur : 
- [Mise à jour de l’utilisateur mobile](https://developers.punchh.com/mobile-apis/users/mobile-update-user-profile)
- [Mise à jour de l’utilisateur SSO](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-update-user-information)
- [Mise à jour de l’utilisateur de tableau de bord](https://developers.punchh.com/platform-functions-apis/users/dashboard-users-update)
<br><br>
{% tabs %}
{% tab User signup API example %}
Cet exemple vous permet d’envoyer des identifiants externes avec un profil d’utilisateur au moment de l’inscription. Ceci est fait en envoyant `external_source` comme « customer_id » et `external_source_id` comme « 556644557788334412 » comme type de données de chaîne de caractères.

```json
curl --location --request POST 'https://sandbox.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: eac5b04cbf7362c5359a4c259cf8fc18941646bf2e11bfe46be0031ffaa1100b' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4a0e0024ae0d30b",
    "user" : {
      "email": "example@braze.com",
      "password": "p@ssw0rd",
      "first_name":"Amit",
      "last_name":"K",
      "terms_and_conditions":"true",
      "anniversary":"2014-02-02",
      "zip_code":"94497",
      "birthday":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"556644557788334412"
      }
}'
```
{% endtab %}
{% tab User update API example %}
Cet exemple vous permet d’envoyer des identifiants externes avec un profil d’utilisateur. Ceci est fait en envoyant `external_source` comme « customer_id » et `external_source_id` comme « 556644557788334412 » comme type de données de chaîne de caractères.

```json
curl --location --request PUT 'https://sandbox.punchh.com/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: en' \
--header 'x-pch-digest: 953d896eebfdb5a84aacb9d1b8eaae1fa0cd710b68bcd3b2324415ac40fee99c' \
--header 'Authorization: Bearer c90b819bf962db9882eeac6993b57c0a22816ecad0e5229b27320d63' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4a0e0024ae0d30b",
    "user": {
        "external_source":"customer_id",
        "external_source_id":"556644557788334412"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
Configuration de la plateforme : Pour activer les identifiants externes dans Punchh, dans le tableau de bord Punchh, accédez à **Cockpit > Dashboard (Tableau de bord) > External User Identifier (Identifiant utilisateur externe)**.
{% endalert %}

### Étape 2 : Configuration de l’adaptateur Braze dans Punchh

Pour configurer l’intégration Punchh à Braze :

1. Dans le tableau de bord Punchh, accédez à **Cockpit > Dashboard (Tableau de bord) > Major Features (Fonctionnalités principales) > Enable Webhook Management (Activer la gestion du webhook)** et basculez à **Enable Webhook Management (Activer la gestion du webhook)**.<br>
<br>

2. Ensuite, activez les adaptateurs en accédant à **Settings (Paramètres) > Webhooks Manager (Gestionnaire des webhooks) > Configurations > Show Adapters Tab (Afficher l’onglet Adaptateurs) ** et basculez à **Show Adapters Tab (Afficher l’onglet Adaptateurs)**.<br>
<br>

3. Accédez à **Webhooks Manager** (Gestionnaire des webhooks) sous l’onglet **Settings** (Paramètres) sélectionnez l’onglet **Adapters** (Adaptateurs) et cliquez sur **Create Adapter** (Créer un adaptateur). <br>
<br>
![][1]<br>
<br>

4. Indiquez le nom de l’adaptateur, la description et l’e-mail d’administration. Sélectionnez **Braze** comme adaptateur et fournissez votre endpoint d’API REST et la clé d’API REST de Braze.<br>
<br>

5. Ensuite, sélectionnez les événements disponibles que vous souhaitez activer. Une liste de ces événements est disponible dans [Événements disponibles à synchroniser](#available-events-to-sync).<br>
<br>
![][3]<br>
<br>

6. Cliquez sur **Submit** (Envoyer) pour activer le webhook.

### Étape 3 : Créer un webhook Punchh dans Braze

L’intégration de Braze et de Punchh permet de tirer parti des capacités de webhook de Braze pour créer des segments Punchh :

1. Créez un segment personnalisé dans Punchh et notez le `custom_segment_id` présent dans l’URL du tableau de bord de segment Punchh. <br>
<br>
Par exemple, la page suivante est située sur `www.dashboard.punchhtest.com/segments/11646`. Le numéro « 11646 » à la fin de ce lien est le `custom_segment_id`.<br>
<br>
![][5]<br>
<br>

2. Créez une campagne de webhook dans Braze en utilisant l’endpoint Punchh pour ajouter un utilisateur à un segment personnalisé comme URL du webhook. Vous pouvez fournir `custom_segment_id` et `user_id` comme paires clé-valeur.<br>
<br>
![][4]<br>
<br>

3. Une fois le webhook enregistré, il peut être déclenché dans Canvas pour synchroniser les utilisateurs, comme le montre l’image suivante :<br>
<br>
![Exemple de synchronisation des utilisateurs à l’aide du webhook enregistré suite à l’intégration de Braze et Punchh.][7]

Pour plus d’informations sur la façon dont les webhooks sont utilisés chez Braze, consultez la rubrique [Creating a webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/) (Créer un webhook). 

[1]: {% image_buster /assets/img/punchh/punchh1.png %}
[2]: {% image_buster /assets/img/punchh/punchh2.png %}
[3]: {% image_buster /assets/img/punchh/punchh3.png %}
[4]: {% image_buster /assets/img/punchh/punchh4.png %}
[5]: {% image_buster /assets/img/punchh/punchh5.png %}
[7]: {% image_buster /assets/img/punchh/punchh6.png %}
[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints