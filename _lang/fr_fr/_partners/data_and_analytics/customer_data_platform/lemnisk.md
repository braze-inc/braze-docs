---
nav_title: Lemnisk
article_title: Intégrer Lemnisk à Braze
description: "Cet article de référence détaille le partenariat entre Braze et Lemnisk, une plateforme d'automatisation du marketing basée sur l'intelligence artificielle des données clients, vous permettant de transmettre en continu à Braze les données personnalisées collectées chez Lemnisk à partir de diverses sources, afin de les activer sur différents canaux et destinations à l'aide des outils de Braze."
alias: /partners/lemnisk/
page_type: partner
search_tag: Partner

---

# Lemnisk

> [Lemnisk](https://www.lemnisk.co/), est une plateforme de données client (CDP) alimentée par l'intelligence artificielle et une solution d'automatisation du marketing qui permet de capturer, d'unifier et d'activer en temps réel les données client provenant de sources diverses et cloisonnées. Elle fournit de façon fluide/sans heurts ces données unifiées sur diverses plateformes MarTech et commerciales, tout en offrant des analyses/analytiques robustes et en temps réel pour suivre chaque étape du cycle de vie des données client. 

_Cette intégration est maintenue par Lemnisk._

## À propos de l'intégration

L'intégration de Lemnisk et de Braze permet aux marques et aux entreprises de libérer tout le potentiel de Braze en agissant comme une couche d'intelligence pilotée par CDP qui unifie les données des utilisateurs à travers les plateformes en temps réel, et en envoyant les informations et les comportements de l'utilisateur collectés à Braze en temps réel. Lemnisk fournit des profils de clients enrichis directement dans Braze en combinant des signaux comportementaux et des attributs personnels qui vous permettent de personnaliser votre envoi de messages avec un contexte plus approfondi.

## Conditions préalables

| Condition | Description |
| --- | --- |
| Comptes Lemnisk | Un compte [Lemnisk](https://www.lemnisk.co/) est nécessaire pour bénéficier de ce partenariat. |
| API externe à Lemnisk | Contactez votre CSM Lemnisk pour activer l'**API externe** pour votre compte. |
| Clé d'API REST Braze | Une clé API REST Braze avec l'autorisation `users.track`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre compte]({{site.baseurl}}/user_guide/administrative/access_braze/sdk_endpoints#api-and-sdk-endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Intégration de Lemnisk

### Étape 1 : Créer une API externe de Braze {#create-a-braze-external-api}

Dans Lemnisk, accédez au canal API externe. Sélectionnez **Ajouter une nouvelle API externe.** Nous allons maintenant configurer l'endpoint " [Suivi des utilisateurs"]({{site.baseurl}}/api/endpoints/user_data/post_user_track) en tant qu'API externe.

![Démarrer le processus de création d'une API externe dans Lemnisk]({% image_buster /assets/img/lemnisk/open_external_api.png %})

Sous **Détails de base**, entrez un nom, une description, un canal et un identifiant de canal.

![Entrer les détails de la configuration de base pour une nouvelle API externe dans Lemnisk]({% image_buster /assets/img/lemnisk/ext_api_basic_details.png %})

Sous **Détails de l'API externe**, entrez les détails pertinents pour votre endpoint `users.track`. Vous pouvez définir plusieurs champs au niveau de l'engagement à l'aide de {% raw %}`{{}}`{% endraw %}, ce qui vous permet de définir des valeurs différentes pour différentes campagnes.

![Remplir les détails de l'endpoint et du payload de l'API externe]({% image_buster /assets/img/lemnisk/ext_api_ext_api_details.png %})

Pour terminer la configuration des utilisateurs de la piste, sélectionnez **Enregistrer.** Vous serez automatiquement redirigé vers la page de l **'API de test.** 

### Étape 2 : Testez la configuration

Sur la page **Test API**, saisissez quelques valeurs de test pour les paramètres API dans votre arborescence JSON, puis sélectionnez **Test Configuration.**

Si vos informations d'identification et les définitions de l'API sont correctes, Braze renvoie une réponse positive.

![Test d'une configuration d'API externe avec un exemple de charge utile et de réponse positive]({% image_buster /assets/img/lemnisk/test_ext_api.png %})

Ensuite, vous vérifierez que vos événements sont bien envoyés à Braze. Dans le tableau de bord de Braze, accédez à **Audience** > **Rechercher des utilisateurs**, puis saisissez l'un des identifiants de votre configuration API externe (par exemple, l'adresse e-mail d'un utilisateur). Si tout fonctionne correctement, le profil qui a reçu votre déclencheur API de test sera répertorié.

![Consulter le profil d'un utilisateur et l'aperçu de ses activités dans Braze]({% image_buster /assets/img/lemnisk/braze_cov.png %})

### Étape 3 : Déclencher des événements utilisateur dans Braze

1. Sur Lemnisk, créez un nouveau segment. Par exemple, vous pouvez créer un segment qui envoie des informations à Braze dès que les utilisateurs soumettent un formulaire de prospect.
2. Dans votre nouveau segment, allez dans **API externe** > **Ajouter un engagement.**
3. Sous **Création d'engagement**, entrez les détails de base et sélectionnez la configuration [que vous avez créée précédemment.](#create-a-braze-external-api)
4. Sous **Configure Parameters**, vous trouverez les entrées pour les paramètres de Braze que vous avez choisi d'exposer au niveau de l'engagement. Dans l'exemple suivant, elle affiche le _nom de l'utilisateur_, l'_ID du produit_ et l'_heure de l'événement._
    ![Création d'un engagement pour envoyer les données de l'utilisateur à Braze.]({% image_buster /assets/img/lemnisk/create_an_engagement.png %})
5. Saisissez les variables de personnalisation pertinentes pour les paramètres que nous avons choisis, puis sélectionnez **Enregistrer.**
6. Lorsque vous avez terminé, activez l'engagement.
