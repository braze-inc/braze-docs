---
nav_title: Punchh
article_title: Punchh
page_order: 5
description: "Cet article décrit le partenariat entre Braze et Punchh, une plateforme de fidélité et d'engagement, vous permettant de synchroniser les données sur les deux plateformes. Les données publiées à Braze seront disponibles pour la segmentation et pourront à nouveau synchroniser les données utilisateur avec Punchh via la configuration des modèles de webhook au Brésil."
alias: /fr/partners/punchh/
page_type: partenaire
search_tag: Partenaire
---

# Punchh

> [Punchh](https://punchh.com/) est une plateforme de fidélisation et d'engagement leader dans l'industrie qui permet aux marques de fournir des programmes de fidélisation omnichannel de la clientèle tant en magasin qu'en numérique.

L'intégration de Braze et Punchh vous permet de synchroniser les données à des fins de don et de loyauté sur les deux plateformes. Les données publiées à Braze seront disponibles pour la segmentation et pourront synchroniser les données de l'utilisateur à Punchh via les webhooks de Braze.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte Punchh                   | Vous avez besoin d'un compte Punchh actif pour profiter de ce partenariat.                                                                                                                                   |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Point de terminaison REST Braze | [Votre REST Endpoint URL][6]. Votre point de terminaison dépend de l'URL de Braze pour votre instance.                                                                                                       |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

Punchh offre plusieurs terminaux disponibles aux clients de Braze pour aider à ajouter des identifiants externes à la plateforme Punchh en utilisant les terminaux de l'API Punchh ci-dessous. Une fois que les identifiants externes ont été ajoutés, créez un adaptateur dans Punchh, fournissez vos identifiants Braze et sélectionnez quels événements vous souhaitez synchroniser. Ensuite, vous pouvez prendre l'ID de segment Punchh et l'utiliser pour construire un webhook Punchh pour déclencher la synchronisation des clients dans un voyage sur Canvas .

### Événements disponibles à synchroniser {#available-events-to-sync}
1. Invité
2. Check-in de fidélité
3. Check-in cadeau
4. Rédemption
5. Récompenses
6. Notifications de transaction
7. Notifications marketing

{% alert note %}
Reportez-vous à la documentation Punchh sur les exemples de charges disponibles pour ces événements.
{% endalert %}

### Étape 1 : Mettre en place des terminaux d'ingestion d'ID externe

Les identifiants externes de Braze peuvent être ajoutés en utilisant les points de terminaison suivants pour les nouveaux utilisateurs et les utilisateurs existants de Punchh.

{% alert important %}
Les valeurs du champ `external_source` et `external_source_id` doivent être uniques à Punchh et non associées à des profils existants.
{% endalert %}

1. Nouveaux utilisateurs Punchh<br> Créez de nouveaux utilisateurs dans Punchh avec un point de terminaison d'inscription Punchh en utilisant les champs `external_source` et `external_source_id`. Punchh permet d'envoyer des identifiants externes avec un profil utilisateur via l'un des points de terminaison d'inscription suivants :
- [API d'inscription mobile](https://developers.punchh.com/mobile-apis/users/mobile-sign-up)
- [SSO Inscription API](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-signup)<br><br>
2. Utilisateurs Punchh existants <br> Mettre à jour `external_source_id` pour les utilisateurs Punchh existants. Punchh permet d'ajouter des identifiants externes à un profil via un point de terminaison de mise à jour de l'API utilisateur:
- [Mise à jour de l'utilisateur mobile](https://developers.punchh.com/mobile-apis/users/mobile-update-user-profile)
- [Mise à jour de l'utilisateur SSO](https://developers.punchh.com/sso-online-apis/single-sign-on/sso-update-user-information)
- [Mise à jour de l'utilisateur du tableau de bord](https://developers.punchh.com/platform-functions-apis/users/dashboard-users-update) <br><br>
{% tabs %}
{% tab User signup API example %}
Cet exemple vous permet d'envoyer des identifiants externes avec un profil utilisateur au moment de l'inscription. Ceci est fait ci-dessous en envoyant `external_source` comme « customer_id » et `external_source_id` comme « 556644557788334412 » comme type de données de chaîne de caractères.

```json
curl --location --request POST 'https://sandbox.punchh. om/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'x-pch-digest: eac5b04cbf7362c5359a4c259cf8fc18941646bf2e11bfe46be0031ffaa1100b' \
--header 'Accept-Timezone: Etc/UTC' \
--header 'Accept: application/json' \
--header 'Accept-Language: fr' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4a0e0024ae0d30b",
    "user" : {
      "email": "example@braze. om",
      "mot de passe": "p@ssw0rd",
      "prénom":"Amit",
      "nom_du_famille":"K",
      "terms_and_conditions":"true",
      "anniversaire":"2014-02-02-02",
      "zip_code":"94497",
      "anniversaire":"2004-02-02",
      "external_source":"customer_id",
      "external_source_id":"556644557788334412"
      }
}'
```
{% endtab %}
{% tab User update API example %}
Cet exemple vous permet de mettre à jour les identifiants externes avec un profil utilisateur. Ceci est fait ci-dessous en envoyant `external_source` comme « customer_id » et `external_source_id` comme « 556644557788334412 » comme type de données de chaîne de caractères.

```json
curl --location --request PUT 'https://sandbox.punchh. om/api2/mobile/users' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'Accept-Language: fr' \
--header 'x-pch-digest: 953d896eebfdb5a84aacb9d1b8eaae1fa0cd710b68bcd3b2324415ac40fee99c' \
--header 'Authorization: Bearer c90b819bf962db9882eac6993b57c0a22816ecad0e5229b27320d63' \
--data-raw '{
    "client":"1533b61caecafea4303aa1f4bad8321d6d8e7a843593e4
    "user": {
        "external_source":"customer_id",
        "external_source_id":"556644557788334412"
    }
}'
```
{% endtab %}
{% endtabs %}

{% alert note %}
Configuration de la plateforme : afin d'activer les identifiants externes dans Punchh, depuis le tableau de bord Punchh, Naviguez vers __Cockpit -> Tableau de bord -> Identifiant utilisateur externe__.
{% endalert %}

### Étape 2 : Configuration de l'adaptateur Braze à Punchh

Pour mettre en place l'intégration Braze et Punchh :

1. Dans le tableau de bord Punchh, Naviguez vers __Cockpit -> Tableau de bord -> Fonctionnalités majeures -> Activez la gestion de Webhook__ et activez __Activer la gestion de Webhook__.<br><br>
2. Ensuite, activez les adaptateurs en naviguant dans __Paramètres -> Gestionnaire de Webhooks -> Configurations -> Afficher l'onglet des adaptateurs__ et activer/désactiver __Afficher l'onglet des adaptateurs__.<br><br>
3. Naviguez vers __Gestionnaire de Webhooks__ sous l'onglet __Paramètres__ , sélectionnez l'onglet __Adaptateurs__ et cliquez sur __Créer Adaptateur__. <br><br>!\[Punch Platform\]\[1\]<br><br>
5. Remplissez le nom de l'adaptateur, la description et l'e-mail de l'admin. Sélectionnez __Braze__ comme adaptateur et fournissez votre point de terminaison API Braze REST et votre clé API Braze.<br><br>
6. Ensuite, sélectionnez les événements disponibles que vous souhaitez activer. Une liste de ces événements peut être trouvée dans [Événements disponibles pour synchroniser](#available-events-to-sync) ci-dessus.<br><br>!\[Plate-forme Punch\]\[3\]<br><br>
7. Cliquez sur __Soumettre__ pour activer le webhook. virgule
### Étape 3 : Créez un webhook Punchh dans Braze

L'intégration de Braze et Punchh vous permet de tirer parti des fonctionnalités de Braze Webhook pour créer des segments Punchh :

1. Créez un segment personnalisé dans Punchh et notez le `custom_segment_id` présent dans l'URL du tableau de bord du segment Punchh. <br><br>Par exemple, la page ci-dessous est située à `www.dashboard.punchhtest.com/segments/11646`. Le numéro "11646" à la fin de ce lien est le `custom_segment_id`.<br><br>!\[Punch Platform\]\[5\]<br><br>
2. Ensuite, naviguez vers __Modèles de Webhook__ dans Braze et sélectionnez le modèle Punchh. Ici, vous pouvez fournir les paires `custom_segment_id` et `user_id` comme valeur clé.<br><br>!\[Punch Platform\]\[4\]<br><br>
3. Une fois le webhook enregistré, il peut être déclenché dans Canvas pour synchroniser les utilisateurs comme indiqué ci-dessous :<br><br>!\[Punch Platform\]\[7\]

Pour plus d'informations sur la façon dont les webhooks sont utilisés au Brésil, consultez [Créer un webhook]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/creating_a_webhook/).
[1]: {% image_buster /assets/img/punchh/punchh1.png %} [2]: {% image_buster /assets/img/punchh/punchh2.png %} [3]: {% image_buster /assets/img/punchh/punchh3. ng %} [4]: {% image_buster /assets/img/punchh/punchh4.png %} [5]: {% image_buster /assets/img/punchh/punchh5. ng %} [7]: {% image_buster /assets/img/punchh/punchh6.png %}

[6]: {{site.baseurl}}/api/basics?redirected=true#endpoints