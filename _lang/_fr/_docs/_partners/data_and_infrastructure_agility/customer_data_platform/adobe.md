---
nav_title: Argile
article_title: Argile
alias: /fr/partners/adobe/
description: "L'intégration de Braze et Adobe CDP permet aux marques de se connecter et de cartographier leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel. Les marques peuvent alors agir sur ces données, en fournissant des expériences personnalisées ciblées à ces utilisateurs."
page_type: partenaire
page_order: 2.1
search_tag: Partenaire
---

# Argile

> Construit sur la plateforme Adobe Experience, La plateforme de données client en temps réel d'Adobe (CDP en temps réel) aide les entreprises à rassembler des données connues et anonymes provenant de plusieurs sources d'entreprise afin de créer des profils clients qui peuvent être utilisés pour fournir des expériences clients personnalisées sur tous les canaux et appareils en temps réel.

L'intégration de Braze et Adobe CDP permet aux marques de se connecter et de cartographier leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel. Les marques peuvent alors agir sur ces données, en fournissant des expériences personnalisées ciblées à ces utilisateurs. Avec Adobe, l'intégration est intuitive. Prenez simplement n'importe quelle identité [d'Adobe](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en), associez-la à un ID externe Braze et envoyez-la sur la plateforme Braze. Toutes les données envoyées seront accessibles à Braze via un nouvel attribut `AdobeExperiencePlatformSegments`.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte Adobe                    | Vous devez avoir un compte Adobe actif pour utiliser leurs services avec Braze                                                                                                                               |
| Clé d'API REST Braze            | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le __tableau de bord Braze -> Console développeur -> Clé d'API REST -> Créer une nouvelle clé API__ |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL de Braze pour votre instance.                                                                                                    |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Veuillez noter que l'envoi d'attributs personnalisés supplémentaires peut causer des problèmes de points de données. Nous vous conseillons de parler avec votre représentant respectif pour une meilleure compréhension de cette augmentation potentielle des données.
{% endalert %}

## Aperçu de l'intégration

### Étape 1 : Connectez le compte Adobe à la destination de Braze

À partir de la page des paramètres d'Adobe, sélectionnez __Destinations__ sous __Collections__. À partir de là, localisez la tuile Braze et sélectionnez __Configurer__.

!\[Connect\]\[1\]

{% alert note %}
Si une connexion avec Braze existe déjà, vous verrez un bouton Activer sur la carte de destination. Pour plus d'informations sur la différence entre l'activation et la configuration, reportez-vous à la section Catalogue de l'espace de travail de destination d'Adobe [documentation](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog).
{% endalert %}

### Étape 2 : Fournir un jeton Braze
!\[Token\]\[3\]{: style="float:right;max-width:40%;margin-left:15px;"} Dans l'étape de compte, fournissez votre clé API de compte Braze. Pour plus d'informations sur la façon d'obtenir votre clé API dans l'aperçu de la clé [REST API Braze]({{site.baseurl}}/api/api_key/). Entrez cette clé et cliquez sur __Se connecter à la destination__.

### Étape 3 : Authentification

Ensuite, vous serez présenté avec l'étape d'authentification. Ici, vous devez entrer vos informations de connexion Braze :
- __Name__: Entrez le nom par lequel vous souhaitez reconnaître cette destination dans le futur.
- __Destination__: Entrez une description qui vous aidera à identifier cette destination.
- __Instance de point de terminaison__: Veuillez contacter votre représentant Braze pour savoir quelle instance de terminaison vous devez utiliser.
- __Cas d'utilisation marketing__: Les cas d'utilisation marketing indiquent l'intention pour laquelle les données seront exportées vers la destination. Vous pouvez sélectionner des cas d'utilisation marketing définis par Adobe ou vous pouvez créer votre propre cas d'utilisation marketing. Pour en savoir plus sur les cas d'utilisation du marketing d'Adobe, visitez leur documentation sur la [gouvernance des données dans la plate-forme Adobe Expérience](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

!\[Authentication\]\[4\]{: style="max-width:60%;"}

### Étape 4 : Créer une destination
Enfin, cliquez sur __Créer une destination__. Votre destination a été créée. Vous pouvez cliquer sur __Enregistrer & Quitter__ si vous voulez activer les segments plus tard, ou vous pouvez sélectionner __Suivant__ pour continuer le workflow et sélectionner les segments à activer.

### Étape 5 : Activer les segments
Activez les données que vous avez dans le CDP Adobe Real-Time en associant les segments à la destination de Braze.

Voici la liste des étapes générales requises pour activer un segment. Pour obtenir des conseils détaillés sur les segments Adobe et le flux de travail d'activation du segment, visitez leur [Documentation du segment](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Sélectionnez et activez la destination de Braze.
2. Sélectionnez les segments applicables.
4. Configurer la planification et les noms de fichiers pour chaque segment que vous exportez.
5. Sélectionnez les attributs à envoyer à Braze.
6. Revoir et vérifier l'activation.

### Étape 6 : mapping des champs

Pour envoyer correctement les données de votre auditoire depuis Adobe Experience Platform à Braze, vous devez compléter l'étape de cartographie du champ. La cartographie consiste à créer un lien entre les champs Adobe Experience Data Model et les champs Braze Platform correspondants.

1. Dans l'étape de mappage, cliquez sur __Ajouter un nouveau mapping__!<br>!\[Mapping\]\[5\]{: style="max-width:50%;"}<br><br>
2. Dans la Section de champ Source, cliquez sur le bouton flèche à côté du champ vide, cela ouvrira la fenêtre de champ Sélectionner le champ source.<br>!\[Source\]\[6\]<br><br>
3. Dans la fenêtre Sélectionner le champ source, vous devez sélectionner les attributs Adobe à associer à vos attributs de Braze. <br>!\[Field\]\[7\]{: style="max-width:70%;"}<br><br>Ensuite, vous devez sélectionner l'espace de noms d'identité. Cette option est utilisée pour associer un espace de noms d'identité de la plateforme à un espace de noms Braze.<br>!\[Identity\]\[8\]{: style="max-width:80%;"}<br> Choisissez vos champs source, puis cliquez sur __Sélectionnez__.<br><br>
4. Dans la section Champ cible, cliquez sur l'icône de mapping à droite du champ.<br>!\[Tagret\]\[9\]{: style="max-width:90%;"} <br><br>
5. Dans la fenêtre Sélectionner le champ cible, vous pouvez choisir entre trois catégories de champs cibles :<br><br>• __Sélectionnez les attributs__: Utilisez cette option pour associer vos attributs Adobe XDM aux attributs standard de Braze.<br>• __Sélectionnez l'espace de noms d'identité__: Utilisez cette option pour associer les espaces de noms d'identité de la plateforme à Braze espaces de noms d'identité.<br>• __Sélectionnez les attributs personnalisés__: Utilisez cette option pour associer les attributs Adobe XDM aux attributs personnalisés de Braze que vous avez définis dans votre compte Braze. <br><br>!\[Attributes\]\[10\]{: style="max-width:60%;"}<br><br>__You can also use this option to rename existing XDM attributes into Braze.__ For example, mapping a `lastname` XDM attribute to a custom `Last_Name` attribute in Braze, will create the `Last_Name` attribute in Braze if it doesn't already exist, and map the `lastname` XDM attribute to it. <br><br> Choisissez vos champs cibles, cliquez sur __Sélectionner__.<br><br>
6. Vous devriez maintenant voir votre mapping de champ dans la liste.<br>!\[List\]\[11\]<br><br>
7. Pour ajouter plus de mappages, répétez les étapes 1 à 6 si nécessaire.

## Exemple

Disons que votre schéma de profil XDM et votre instance Braze contiennent les attributs et identités suivants :

|           | Schéma de profil XDM                                                                        | Instance de Braze                                            |
| --------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Attributs | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number` | - `Prénom`<br>- `Nom`<br>- `Numéro de téléphone` |
| Identités | - `Email`<br>- `Google Ad ID (GAID)`<br>- `Apple ID pour les annonceurs (IDFA)` | - `external_id`                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Le mapping correct ressemblerait à ceci :

!\[Correct\]\[12\]

## Données exportées
Pour vérifier si les données ont été exportées avec succès vers Braze, vérifiez votre compte Braze. Les segments de plateforme Adobe Experience sont exportés vers Braze sous l'attribut `AdobeExperiencePlatformSegments`.

## Consommation et gouvernance des données
Toutes les destinations Adobe Experience Platform sont conformes aux politiques d'utilisation des données lors du traitement de vos données. Pour des informations détaillées sur la manière dont la plateforme Adobe Experience applique la gouvernance des données, consultez la documentation d'Adobe sur la [gouvernance des données en temps réel CDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en).
[1]: {% image_buster /assets/img/adobe/braze-destination-configure.png %} [3]: {% image_buster /assets/img/adobe/braze-destination-account.png %} [4]: {% image_buster /assets/img/adobe/braze-destination-authentication. ng %} [5]: {% image_buster /assets/img/adobe/braze-destination-mapping.png %} [6]: {% image_buster /assets/img/adobe/braze-destination-mapping-source. ng %} [7]: {% image_buster /assets/img/adobe/braze-destination-mapping-attributes. ng %} [8]: {% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %} [9]: {% image_buster /assets/img/adobe/braze-destination-mapping-target. ng %} [10]: {% image_buster /assets/img/adobe/braze-destination-mapping-target-field. ng %} [11]: {% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %} [12]: {% image_buster /assets/img/adobe/braze-destination-mapping-example.png %} 
