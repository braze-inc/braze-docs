---
nav_title: Smartling
article_title: Smartling
description: "Cet article de référence présente le partenariat entre Braze et Smartling, un logiciel de localisation basé sur le cloud. Cette intégration vous permet de traduire des modèles d'e-mail et des blocs de contenu dans Braze."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling][2] est un logiciel de traduction de bout en bout basé dans le cloud pour les clients désirant automatiser la traduction de sites web, d'applications et d'expériences client.

L'intégration de Braze et Smartling vous permet de traduire des modèles d'e-mail et des blocs de contenu. Smartling permet aux linguistes de voir le contexte pendant la traduction afin de réduire les erreurs et garantir une traduction de qualité.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Smartling | Un [compte Smartling][2] est requis pour profiter de ce partenariat. |
| Projet de traduction Smartling | Pour connecter votre compte Braze à Smartling, vous devez d'abord vous inscrire et [créer un projet de traduction][3]. |
| Clé API REST de Braze | Une clé API REST Braze avec toutes les autorisations de modèles et de blocs de contenu. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

L'intégration Smartling Braze vous permettra de traduire des modèles d'e-mail et des blocs de contenu. 

Modèles d'e-mail : 
* Seuls les e-mails de l'éditeur HTML sont pris en charge. 
* Chaque traduction sera stockée comme son propre modèle d'e-mail. 

Blocs de contenu : 
* Tous les blocs de contenu sont pris en charge. 
* Les blocs de contenu contiennent les versions originale et traduite.
* Le script liquid détermine la langue correcte à afficher en fonction de la préférence linguistique du destinataire.

### Étape 1 : Configurez le projet Braze dans Smartling TMS

#### Connexion de Braze à Smartling

1. Dans [Smartling][2], créez un type de projet [connecteur Braze][6] dans votre compte Smartling. 
  - Assurez-vous que toutes les langues cibles requises sont ajoutées au projet.
2. Depuis ce projet, cliquez sur **Paramètres** > **Paramètres Braze** > **Se connecter à Braze**.
3. Entrez votre URL API Braze et votre clé API Braze.
4. Cliquez sur **enregistrer**.

#### Configuration complète du connecteur Braze

Reportez-vous à la [documentation][3] de Smartling pour plus de détails sur la configuration du connecteur.

Sélectionnez comment vous souhaitez automatiser les requêtes de traduction précédentes.

Configurez les langues source et cible dans **Configuration de la langue**. Ces informations seront utilisées par le connecteur pour ingérer du contenu dans Smartling TMS et renvoyer les traductions à Braze.

![][8]

### Étape 2 : Envoyer le contenu à Smartling

Une fois que le connecteur Braze a été connecté et configuré, vous trouverez le contenu Braze dans l'onglet **Braze** de votre projet Smartling. Consultez la [documentation][7] de Smartling pour en savoir plus.

Smartling fournit des fonctionnalités avancées pour rechercher et sélectionner du contenu par :
* Recherche par mot-clé
* Type de contenu Braze
* Étiquetage Braze

![][9]

### Étape 3 : Ajoutez des traductions à Braze

Au fur et à mesure que les traductions sont complétées sur la plateforme Smartling, elles sont automatiquement envoyées à Braze—pas besoin de synchroniser manuellement le contenu entre Smartling et Braze.

[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://help.smartling.com/hc/article_attachments/13946813331739
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}