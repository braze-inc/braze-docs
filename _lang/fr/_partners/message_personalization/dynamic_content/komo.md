---
nav_title: Komo
article_title: Komo
description: "Cet article de référence décrit le partenariat entre Braze et Komo, une plateforme d’engagement client spécialisée dans la gamification, le contenu interactif, les concours, les remises de prix et la fidélité. Grâce à cette intégration, les données zero et first-party capturées dans Komo peuvent être publiées sur Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partenaire

---

# Komo

> [Komo][7] est une plateforme d’engagement client spécialisée dans la gamification, le contenu interactif, les concours, les remises de prix et la fidélité.

L’intégration de Braze et Komo vous permet de collecter des données zero et first-party via les hubs d’engagement Komo. Ces hubs sont des microsites dynamiques qui proposent un contenu interactif et des fonctionnalités de gamification. Les données utilisateur collectées à partir de ces hubs sont ensuite transmises à l’API Braze.

- Ingérez en temps réel de données utilisateur zero et first-party collectées depuis Komo vers Braze
- Ingérez des données d’études de marché et de préférences utilisateurs lorsqu’ils répondent à des enquêtes, des sondages et des questionnaires
- Construisez progressivement des profils d’utilisateur dans Braze, car l’utilisateur continue à s’engager et à partager plus de données sur lui-même
- Standardisez l’aspect et la convivialité des e-mails transactionnels envoyés par Braze

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Komo | Un compte Komo est requis pour profiter de ce partenariat. Rendez-vous dès maintenant sur [Komo][7] pour commencer un essai. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Endpoint REST de Braze | [URL de votre endpoint REST][1]. Votre endpoint dépendra de l’URL Braze pour votre instance.<br><br>Par exemple, il devrait ressembler à : https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

## Cas d’utilisation

{% tabs local %}
{% tab Data Capture (Form Submission) %}

Lorsqu’un utilisateur soumet un formulaire de capture de données personnalisable dans Komo, les champs Komo mappés dans l’intégration Braze seront transmis à Braze via l’appel API `/users/track/`.

Les formulaires de saisie de données existent au début ou à la fin des cartes.

{% endtab %}
{% tab Market Research (Coming soon) %}

Bientôt disponible, Komo ajoutera la possibilité de transmettre les données d’études de marché capturées lorsqu’un utilisateur répond à une question, un sondage, un test de personnalité, un lecteur, etc. Ces données vous permettront d’améliorer le profil d’un utilisateur au-delà des données obtenues lors des soumissions de formulaires.

{% endtab %}
{% endtabs %}

## Intégration

### Étape 1 : Publier un hub d’engagement Komo et une carte

Vous devrez publier un hub d’engagement Komo avec au moins une carte contenant un formulaire de capture de données. Une fois publié, vous pouvez tester l’expérience utilisateur de bout en bout et vérifier que l’intégration fonctionne correctement.

![][2]

### Étape 2 : Ajouter l’intégration Braze

Dans Komo, accédez à l’onglet **Hub Settings (Paramètres du Hub)** et sélectionnez la section **Intégrations**. Ensuite, recherchez l’intégration Braze dans la liste et sélectionnez le bouton **Connect (Connecter)** pour activer l’intégration.

![][3]

![][4]

#### Configurer le mappage d’utilisateur

La première chose que vous devrez configurer est la façon dont vous allez mapper les utilisateurs capturés dans Komo vers des utilisateurs dans Braze. Si vous capturez le `braze_id` ou l’`external_id` par un champ dans Komo, vous pouvez sélectionner la clé appropriée ; sinon, sélectionnez l’option la plus courante qui sera un alias d’utilisateur d’e-mail ou de téléphone.

![][5]{: style="max-width:65%;"}

Ensuite, vous devrez définir un mappage des champs Komo que vous souhaitez transférer dans les attributs Braze. Komo capture une grande quantité de données, de sorte que seuls les champs mappés dans l’intégration Braze seront envoyés à Braze.

![][6]{: style="max-width:65%;"}

Enfin, ajoutez votre clé API et l’URL de l’endpoint REST et appuyez sur **Save (Enregistrer)** pour activer l’intégration.

## Comment utiliser l’intégration

Une fois votre intégration terminée, vous pouvez utiliser les données Komo envoyées à Braze pour créer des segments à cibler.

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/komo/komo_hub_publish.png %}
[3]: {% image_buster /assets/img/komo/komo_hub_settings_integrations.png %}
[4]: {% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %}
[5]: {% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}
[6]: {% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}
[7]: https://komo.tech/