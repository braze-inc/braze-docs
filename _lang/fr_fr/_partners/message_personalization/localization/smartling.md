---
nav_title: Smartling
article_title: Smartling
description: "Cet article de référence présente le partenariat entre Braze et Smartling, un logiciel de localisation basé sur le cloud. Le connecteur Braze prend en charge la traduction des modèles d'e-mail HTML, des blocs de contenu, des canevas et des messages d'e-mail de campagne."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling][5] est un logiciel de traduction de bout en bout basé dans le cloud pour les clients désirant automatiser la traduction de sites web, d'applications et d'expériences client.

_Cette intégration est maintenue par Smartling._

## À propos de l'intégration

Le connecteur Braze prend en charge la traduction des modèles d'e-mail HTML, des blocs de contenu, des canevas et des messages d'e-mail de campagne. Les traductions sont demandées à Smartling, et le contenu traduit est automatiquement envoyé à Braze.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Smartling | Un [compte Smartling][2] est requis pour profiter de ce partenariat. |
| Projet de traduction Smartling | Pour connecter votre compte Braze à Smartling, vous devez d'abord vous connecter et [créer un projet de traduction][6]. |
| Clé d'API REST Braze | Une clé API REST Braze avec toutes les autorisations de modèles et de blocs de contenu. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

L'intégration de Smartling Braze vous permet de traduire des modèles d'e-mail HTML, des blocs de contenu, des canevas et des messages d'e-mail de campagne. Notez les détails suivants en fonction de ce que vous traduisez :

**Modèles d'e-mail**
* Seuls les modèles d'e-mail en HTML sont pris en charge.
* Vous devrez décider de la manière dont vos e-mails traduits sont transmis à Braze par le connecteur :
  * **Un e-mail pour toutes les langues :** Le connecteur délivre toutes les langues dans le même e-mail que la source.
  * **Un e-mail par langue :** Le connecteur crée un nouvel e-mail pour chaque langue dans Braze.

**Blocs de contenu**
* Tous les blocs de contenu sont pris en charge.
* Les blocs de contenu contiennent les versions originale et traduite.
* Le script liquid détermine la langue correcte à afficher en fonction de la préférence linguistique du destinataire.

**Campagnes et canvas**
* Assurez-vous d'avoir ajouté vos langues cibles dans les paramètres de **prise en charge multilingue** de Braze.
* Reportez-vous à la [documentation de Smartling][3] pour plus de détails sur la configuration des connecteurs.

## Intégration

### Étape 1 : Configurez le projet Braze dans Smartling TMS

#### Connexion de Braze à Smartling

1. Dans [Smartling][2], créez un type de projet [connecteur Braze][6] dans votre compte Smartling.
  - Assurez-vous que toutes les langues cibles requises sont ajoutées au projet.
2. Dans ce projet, sélectionnez **Paramètres** > **Paramètres de Braze** > **Connexion à Braze**.
3. Entrez votre URL API Braze et votre clé API Braze.
4. Sélectionnez **Enregistrer**.

#### Configuration complète du connecteur Braze

Reportez-vous à la [documentation][3] de Smartling pour plus de détails sur la configuration du connecteur.

1. Sélectionnez comment vous souhaitez automatiser les requêtes de traduction précédentes.
2. Configurez les langues source et cible dans **Configuration de la langue**. Le connecteur l'utilisera pour ingérer du contenu dans Smartling TMS et fournir des traductions en retour à Braze.

![Configuration de la langue du connecteur.][8]

### Étape 2 : Envoyer le contenu à Smartling

Une fois que le connecteur Braze a été connecté et configuré, vous trouverez le contenu Braze dans l'onglet **Braze** de votre projet Smartling. Consultez la [documentation][7] de Smartling pour en savoir plus.

Smartling fournit des fonctionnalités avancées pour rechercher et sélectionner du contenu par :

* Recherche par mot-clé
* Type de contenu Braze
* Étiquetage Braze

![Liste des blocs de contenu.][9]

### Étape 3 : Ajoutez des traductions à Braze

Au fur et à mesure que les traductions sont complétées sur la plateforme Smartling, elles sont automatiquement envoyées à Braze—pas besoin de synchroniser manuellement le contenu entre Smartling et Braze.


[1]: {{site.baseurl}}/api/basics/#endpoints
[2]: https://dashboard.smartling.com/
[3]: https://help.smartling.com/hc/en-us/articles/13248549217435
[4]: https://help.smartling.com/hc/article_attachments/13347533624347
[5]: https://www.smartling.com/
[6]: https://help.smartling.com/hc/en-us/articles/115003074093
[7]: https://help.smartling.com/hc/en-us/articles/13248577069979
[8]: {% image_buster /assets/img/smartling/smartling-braze-settings.png %}
[9]: {% image_buster /assets/img/smartling/smartling-content-blocks-list.png %}