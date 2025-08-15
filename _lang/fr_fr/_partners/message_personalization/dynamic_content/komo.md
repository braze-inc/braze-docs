---
nav_title: Komo
article_title: Komo
description: "Cet article de référence décrit le partenariat entre Braze et Komo, une plateforme d'engagement client spécialisée dans la gamification, le contenu interactif, les compétitions, les prix et la fidélité. Grâce à cette intégration, les données first-party et zero-party capturées dans Komo peuvent être publiées dans Braze."
alias: /partners/komo/
page_type: partner
search_tag: Partner

---

# Komo

> Komo][7] est une plateforme d'engagement client spécialisée dans la gamification, le contenu interactif, les compétitions, les prix et les programmes de fidélité.

_Cette intégration est maintenue par Komo._

## À propos de l'intégration

L'intégration de Braze et Komo vous permet de recueillir des données first-party et zero-party via les Komo Engagement Hubs. Ces hubs sont des microsites dynamiques qui offrent du contenu interactif et des fonctionnalités de gamification. Les données utilisateur collectées à partir de ces hubs sont ensuite transmises à l'API Braze.

- Intégrez en temps réel dans Braze des données utilisateur de première et de zéro-partie collectées dans Komo
- Ingérez des données d’études de marché et les préférences des utilisateurs qui répondent à des enquêtes, des sondages et des quiz
- Créez progressivement des profils utilisateurs dans Braze à mesure que l'utilisateur continue de s'engager et de partager plus de données le concernant
- Standardiser l'apparence et la convivialité des e-mails transactionnels envoyés via Braze

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Komo | Vous aurez besoin d'un compte Komo actif pour profiter de ce partenariat. Visitez [Komo][7] pour commencer un essai maintenant. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance.<br><br>Par exemple, cela devrait ressembler à ceci : https://rest.iad-03.braze.com |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Cas d'utilisation

{% tabs local %}
{% tab Saisie des données - Soumission des formulaires %}

Lorsqu'un utilisateur soumet un formulaire de capture de données personnalisable dans Komo, les champs Komo mappés dans l'intégration Braze seront transmis à Braze via l'appel d’API `/users/track/`.

Les formulaires de capture de données existent soit au début, soit à la fin des cartes.

{% endtab %}
{% tab Études de marché - Prochainement %}

Bientôt, Komo ajoutera la possibilité de transmettre les données d'étude de marché capturées lorsqu'un utilisateur répond à une question de quiz, un sondage, un test de personnalité, un curseur interactif, etc. Ces données vous permettront d'améliorer le profil d'un utilisateur au-delà des données capturées dans les soumissions de formulaires.

{% endtab %}
{% endtabs %}

## Intégration

### Étape 1 : Publier un hub d'engagement Komo et une carte

Vous devrez publier un Komo Engagement Hub avec au moins une carte contenant un formulaire de capture de donnée. Une fois publié, vous pouvez tester l'expérience utilisateur de bout en bout et vérifier que l'intégration fonctionne correctement.

![][2]

### Étape 2 : Ajoutez l'intégration Braze

Dans Komo, allez à l’onglet **Paramètres du hub** et sélectionnez la section **Intégrations**. Ensuite, trouvez l'intégration Braze dans la liste, et sélectionnez le bouton **Connecter** pour activer l'intégration.

![][3]

![][4]

#### Configurer le mappage utilisateur

La première chose que vous devrez configurer est la façon dont vous allez mapper les utilisateurs capturés dans Komo aux utilisateurs dans Braze. Si vous capturez le `braze_id` ou le `external_id` à l’aide d’un champ dans Komo, vous pouvez alors sélectionner la clé appropriée ; sinon, sélectionnez l'option la plus courante qui sera un alias d'utilisateur d'e-mail ou de téléphone.

![][5]{: style="max-width:65%;"}

Ensuite, vous devrez définir une carte des champs Komo que vous souhaitez transférer dans les attributs Braze. Komo capture une grande quantité de données, donc seuls les champs mappés dans l'intégration Braze seront envoyés à Braze.

![][6]{: style="max-width:65%;"}

Enfin, ajoutez votre clé API et l'URL de l'endpoint REST et cliquez sur **Enregistrer** pour activer l'intégration.

## En utilisant l'intégration

Une fois votre intégration terminée, vous pouvez utiliser les données Komo envoyées à Braze pour créer des segments de ciblage.


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {% image_buster /assets/img/komo/komo_hub_publish.png %}
[3]: {% image_buster /assets/img/komo/komo_hub_settings_integrations.png %}
[4]: {% image_buster /assets/img/komo/komo_hub_settings_braze_connect.png %}
[5]: {% image_buster /assets/img/komo/komo_hub_settings_braze_key.png %}
[6]: {% image_buster /assets/img/komo/komo_hub_settings_braze_settings.png %}
Il y a [7]: https://komo.tech/