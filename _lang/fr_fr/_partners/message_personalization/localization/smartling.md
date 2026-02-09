---
nav_title: Smartling
article_title: Smartling
description: "Cet article de référence présente le partenariat entre Braze et Smartling, un logiciel de localisation basé sur le cloud. Le connecteur Braze prend en charge la traduction des modèles d'e-mail HTML, des blocs de contenu, des canevas et des messages d'e-mail de campagne."
alias: /partners/smartling/
page_type: partner
search_tag: Partner
---

# Smartling

> [Smartling](https://www.smartling.com/) est un logiciel de traduction de bout en bout basé dans le cloud pour les clients désirant automatiser la traduction de sites web, d'applications et d'expériences client.

_Cette intégration est maintenue par Smartling._

## À propos de l'intégration

Le connecteur Braze prend en charge les traductions pour les messages dans les campagnes et les Canvases (messages e-mail, push et in-app), les modèles d'e-mail et les blocs de contenu. Consultez le tableau suivant pour en savoir plus sur les canaux et les fonctionnalités pris en charge lorsque vous décidez d'utiliser le nouveau connecteur avec une prise en charge multilingue ou un flux de travail hérité.

| Chaîne/Fonctionnalité | Éditeur traditionnel (ex. HTML) | Editeur par glisser-déposer |
| --------------- | ----------------------------- | -------------------- |
| [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email) | ✅ | ✅ |
| [IAM]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message) | ✅ | ✅ |
| [Notification push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push) | ✅ | s/o |
| Modèle d’e-mail | Flux de travail hérité | Flux de travail hérité|
| Blocs de contenu |  ✅* |  ✅* |

\*Pour plus d'informations, reportez-vous à la section [Gestion des traductions pour les blocs de contenu](#managing-translations-for-content-blocks).

### Flux de travail hérité

En fonction de votre cas d'utilisation, gérez les traductions pour les blocs de contenu en utilisant soit l'ancien flux de travail de traduction, soit le flux de travail mis à jour. 

Dans le flux de travail mis à jour, en utilisant la prise en charge multilingue de Braze et les locales dans les messages, des tags de traduction sont ajoutés au bloc de contenu. Cependant, Smartling exécute les traductions au niveau du message. Le contenu n'est traduit que lorsqu'il est inclus dans une campagne ou un canvas et que les paramètres linguistiques cibles sont définis. Pour en savoir plus, consultez la section [Gestion des traductions pour les blocs de contenu](#managing-translations-for-content-blocks).

Pour les modèles d'e-mail, seul l'ancien flux de travail est pris en charge. Pour en savoir plus, consultez la section [Gérer les traductions à l'aide du flux de travail existant](#managing-translations-using-the-legacy-workflow).

## Conditions préalables

| Condition                   | Description                                                                                                                                                         |
| ----------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Compte Smartling             | Un [compte Smartling](https://dashboard.smartling.com/) est requis pour profiter de ce partenariat.                                                          |
| Projet de traduction Smartling | Pour connecter votre compte Braze à Smartling, vous devez d'abord vous connecter et [créer un projet de traduction](https://help.smartling.com/hc/en-us/articles/115003074093). |
| Clé d'API REST Braze            | Une clé API REST de Braze avec les autorisations suivantes : <br>- campaigns.translations.get<br>- campaigns.translations.update<br>- campaigns.list<br>- campaigns.details<br>- canvas.translations.get<br>- canvas.translations.update<br>- campaigns.details<br>- templates.email.create<br>- templates.email.update<br>- templates.email.list<br>- templates.email.info<br>- templates.translations.get<br>- templates.translations.update<br>- content_blocks.info<br>- content_blocks.list<br>- content_blocks.create<br>- content_blocks.update<br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres > Clés API**. |
| Endpoint REST Braze           | [L'URL de votre endpoint REST.]({{site.baseurl}}/api/basics/#endpoints) Votre endpoint dépend de l'URL Braze de votre instance.             |
| Paramètres multilingues de Braze | [Complétez les paramètres multilingues dans Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Configurer les paramètres multilingues dans Braze

Consultez [les instructions de configuration multilingue de Braze]({{site.baseurl}}/user_guide/administrative/app_settings/multi_language_settings/#prerequisites) pour configurer les locales dans Braze.

### Étape 2 : Configurez le projet Braze dans Smartling TMS

Reportez-vous à la [documentation de Smartling](https://help.smartling.com/hc/en-us/articles/13248549217435) pour plus de détails sur la configuration des connecteurs.

### Connexion de Braze à Smartling

1. Dans votre [compte Smartling](https://dashboard.smartling.com/), créez un type de projet [Braze Connector](https://help.smartling.com/hc/en-us/articles/115003074093).

![Raccordement par Braze dans le Smartling.]({% image_buster /assets/img/smartling/image1_Connecting_Braze_to_Smartling.png %})

{: start="2"}
2\. Dans ce projet, sélectionnez **Paramètres** > **Paramètres de Braze** > **Connexion à Braze**.
3\. Remplissez les champs obligatoires, comme l'URL de l'API et la clé API. Si la connexion test est réussie, enregistrez la connexion. Si le test ne réussit pas, confirmez que vous avez saisi l'URL et la clé API correctes.

![Braze la connexion dans les paramètres de l'API Smartling.]({% image_buster /assets/img/smartling/image2_API.png %})

{: start="4"}
4\. Ajouter des langues de projet supplémentaires.

![Connexion par Braze dans les langues du projet Smartling.]({% image_buster /assets/img/smartling/image3_project_languages.png %})

{: start="5"}
5\. Dans Paramètres de Braze, vérifiez que les valeurs de la colonne **Langue cible (Braze)** correspondent aux paramètres locaux configurés dans les paramètres multilingues de Braze. La convention de dénomination des paramètres régionaux doit correspondre exactement.

![Braze connection in Smartling Language Confirmation.]({% image_buster /assets/img/smartling/image4_language_confirmation.png %})

### Étape 3 : Ajoutez des tags de traduction à votre message Braze

Consultez [les instructions de Braze]({{site.baseurl}}/user_guide/message_building_by_channel/email/using_locales/?tab%3Dhtml%2520editor#prerequisites) pour savoir comment ajouter des tags de traduction à vos messages :

- [E-mail]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=email)
- [Notification push]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=push)
- [in-app Messages]({{site.baseurl}}/user_guide/engagement_tools/messaging_fundamentals/localization/locales/?tab=in-app%20message)

Voici un exemple de campagne d'e-mail HTML avec des tags de traduction.

![Braze l'e-mail avec des étiquettes de traduction.]({% image_buster /assets/img/smartling/image5_translation_tags.png %})

Vous devez enregistrer le message en tant que brouillon avant de pouvoir sélectionner les langues.

### Étape 4 : Gérer les traductions dans Smartling

Après avoir connecté et configuré le connecteur Braze, trouvez du contenu Braze dans l'onglet Braze de votre projet Smartling. Pour plus d'informations, consultez la [documentation de Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979).

Smartling fournit des fonctionnalités avancées pour rechercher et sélectionner du contenu par :
- Recherche par mot-clé
- Type de contenu Braze
- Étiquetage Braze

1. Dans cet exemple, la campagne d'e-mails de promotion du Nouvel An a été créée à l'[étape 3.](#step-3-add-translation-tags-to-your-braze-message)

![Braze l'e-mail avec des étiquettes de traduction.]({% image_buster /assets/img/smartling/image6_ny_promotion.png %})

{: start="2"}
2\. Après avoir localisé la campagne à traduire, sélectionnez le dossier, choisissez les variantes et sélectionnez **Demander une traduction.**

![Demandez des traductions.]({% image_buster /assets/img/smartling/image7_request_translation.png %})

{: start="3"}
3\. Créez un nouveau travail pour la traduction.

![Créez un nouveau travail pour la traduction.]({% image_buster /assets/img/smartling/image8_request_translation.png %})

{: start="4"}
4\. Une fois le travail autorisé, modifiez chaque traduction dans l'outil de TAO.

![Outil de TAO pour la traduction.]({% image_buster /assets/img/smartling/image9_translation_job.png %})

{: start="5"}
5\. Une fois les traductions terminées, enregistrez et soumettez votre traduction à Braze.

![Soumettre la traduction à Braze.]({% image_buster /assets/img/smartling/image10_translations.png %})

### Étape 5 : Prévisualisez le message en tant qu'utilisateur multilingue dans Braze

Dans Braze, prévisualisez votre campagne en tant qu'utilisateur multilingue pour confirmer que les traductions sont appliquées correctement.

![Aperçu utilisateur multilingue.]({% image_buster /assets/img/smartling/image11_preview.png %})

## Gestion des traductions pour les blocs de contenu

Les blocs de contenu sont gérés dans la section **Modèles et médias & ** de Braze.

### Traduction stockée dans le cadre de la composante du message

Les étiquettes de traduction ont leur place dans le bloc de contenu. Cependant, Smartling exécute les traductions au niveau du message ; le contenu n'est traduit que lorsqu'il est inclus dans une campagne ou un canvas et que la locale cible est définie.

### Considérations

- Les étiquettes de traduction doivent être ajoutées manuellement au bloc de contenu pour les éditeurs HTML et les éditeurs de blocs de contenu par glisser-déposer.
- Les langues sont sélectionnées au niveau des messages, et non au niveau des blocs de contenu eux-mêmes.
- Pour Canvas, nous vous recommandons d'utiliser les rangées pour insérer des blocs de contenu dans votre message au lieu de les ajouter manuellement avec une étiquette Liquid. Si vous faites glisser un bloc de contenu de l'aperçu vers un e-mail, vous en faites une copie locale ; les modifications apportées au bloc de contenu "parent" ne sont pas répercutées sur les autres campagnes utilisant ce bloc.
- Si vous utilisez une étiquette Liquid de bloc de contenu, veillez à inclure au moins une étiquette de traduction directement dans le corps de l'e-mail. L'ajout manuel de l'étiquette de traduction vous permet de sélectionner les langues dans le menu déroulant multilingue. Smartling récupère les étiquettes de traduction pour le bloc de contenu. Vous pouvez ajouter une étiquette `comment` pour que le texte ne soit pas visible par l'utilisateur.

## Gérer les traductions à l'aide du flux de travail existant

Si vous préférez gérer les traductions directement dans un bloc de contenu ou un modèle d'e-mail, consultez les instructions relatives à l'héritage dans la [documentation de Smartling](https://help.smartling.com/hc/en-us/articles/13248577069979-Translating-with-the-Braze-Connector). Cette méthode utilise un attribut de langue et une logique Liquid if/else pour afficher le texte dans différentes langues.

## Foire aux questions

### Les étiquettes de traduction sont-elles prises en charge par l'éditeur glisser-déposer ?

Pour l'éditeur par glisser-déposer (e-mail, bloc de contenu, message in-app), vous devez ajouter manuellement les tags de traduction en tant qu'étiquettes Liquid.

### Comment traduire un texte à l'intérieur d'une étiquette Liquid ?

Smartling reconnaît les étiquettes Liquid et en fait des variables non modifiables dans le compositeur. Tout autre texte contenu dans l'étiquette Liquid, tel que le texte par défaut ou les tags comme joindre, devient également non modifiable dans Smartling. Cependant, supprimez l'étiquette Liquid dans Smartling et recréez l'étiquette Liquid avec le texte par défaut traduit. Un avertissement apparaît lorsque vous enregistrez la traduction.
