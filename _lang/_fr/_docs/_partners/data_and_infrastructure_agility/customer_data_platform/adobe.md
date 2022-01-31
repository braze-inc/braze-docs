---
nav_title: Argile
article_title: Argile
alias: /fr/partners/adobe/
description: "L'intégration de Braze et Adobe CDP permet aux marques de se connecter et de cartographier leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel. Les marques peuvent alors agir sur ces données, en fournissant des expériences personnalisées et ciblées à ces utilisateurs."
page_type: partenaire
page_order: 2.1
search_tag: Partenaire
---

# Argile

> Construit sur la plateforme Adobe Experience, La plate-forme de données client en temps réel d'Adobe aide les entreprises à rassembler des données connues et anonymes provenant de plusieurs sources d'entreprise pour créer des profils de clients. Ces profils peuvent ensuite être utilisés pour fournir des expériences personnalisées sur tous les canaux et appareils en temps réel.

L'intégration de Braze et Adobe CDP permet aux marques de se connecter et de cartographier leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel. Les marques peuvent alors agir sur ces données, en fournissant des expériences personnalisées et ciblées à ces utilisateurs. Avec Adobe, l'intégration est intuitive. Prenez simplement n'importe quelle identité [d'Adobe](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en), associez-la à un ID externe Braze et envoyez-la sur la plateforme Braze. Toutes les données envoyées seront accessibles à Braze via un nouvel attribut `AdobeExperiencePlatformSegments`.

## Pré-requis

| Exigences                       | Libellé                                                                                                                                                                                                      |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Compte Adobe                    | Un [compte Adobe](https://account.adobe.com/) est requis pour profiter de ce partenariat.                                                                                                                    |
| Braze clé API REST              | Une clé API Braze REST avec les permissions `users.track`. <br><br> Ceci peut être créé dans le **tableau de bord de Braze > Console développeur > Clé d'API REST > Créer une nouvelle clé API** |
| Instance Braze                  | Votre instance Braze peut être obtenue auprès de votre gestionnaire d'intégration Braze ou peut être trouvée sur la page [Aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints).                          |
| Point de terminaison REST Braze | Votre URL de terminaison REST. Votre point de terminaison dépendra de l'URL [Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints).                                                             |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Veuillez noter que l'envoi d'attributs personnalisés supplémentaires peut causer des problèmes de points de données. Nous vous conseillons de parler avec votre représentant respectif pour mieux comprendre cette augmentation potentielle des données.
{% endalert %}

## Intégration

### Étape 1 : Configurer la destination de Braze

Dans la page Adobe **Paramètres** , sélectionnez **Destinations** sous **Collections**. À partir de là, localisez la tuile **Braze** et sélectionnez **Configurer**.

!\[Connect\]\[1\]

{% alert note %}
Si une connexion avec Braze existe déjà, vous verrez un bouton **Activer** sur la carte de destination. Pour plus d'informations sur la différence entre l'activation et la configuration, reportez-vous à la section catalogue de l'espace de travail de destination d'Adobe [documentation](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog).
{% endalert %}

### Étape 2 : Fournir un jeton Braze

Dans l'étape **Compte** fournissez votre clé API Braze et cliquez sur **Se connecter à la destination**.

!\[Token\]\[3\]{: style="max-width:60%"}


### Étape 3 : Authentification

Ensuite, à l'étape  **Authentification** vous devez entrer vos données de connexion Braze :
- **Name**: Entrez le nom par lequel vous souhaitez reconnaître cette destination dans le futur.
- **Destination**: Entrez une description qui vous aidera à identifier cette destination.
- **Instance de point d'extrémité**: Entrez dans votre instance de point de terminaison Braze.
- **Cas d'utilisation marketing**: Les cas d'utilisation marketing indiquent l'intention pour laquelle les données seront exportées vers la destination. Vous pouvez sélectionner des cas d'utilisation marketing définis par Adobe ou créer votre propre cas d'utilisation marketing. Pour en savoir plus sur les cas d'utilisation du marketing d'Adobe, visitez [la gouvernance des données dans la plate-forme Adobe Experience](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

!\[Authentication\]\[4\]{: style="max-width:60%;"}

### Étape 4 : Créer une destination
Cliquez sur **Créer une destination**. Votre destination a été créée. Vous pouvez cliquer sur **Enregistrer & Quitter** pour activer les segments plus tard ou **Suivant** pour continuer le workflow et sélectionner les segments à activer.

### Étape 5 : Activer les segments
Activez les données que vous avez dans le CDP en temps réel Adobe en associant les segments à la destination de Braze.

Voici la liste des étapes générales requises pour activer un segment. Pour obtenir des conseils détaillés sur les segments Adobe et le flux de travail d'activation du segment, visitez [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Sélectionnez et activez la destination de Braze.
2. Sélectionnez les segments applicables.
4. Configurer la planification et les noms de fichiers pour chaque segment que vous exportez.
5. Sélectionnez les attributs à envoyer à Braze.
6. Revoir et vérifier l'activation.

### Étape 6 : mapping des champs

Pour envoyer correctement les données de votre auditoire de la plate-forme Adobe Experience à Braze, vous devez compléter l'étape de cartographie du champ. La cartographie crée un lien entre les champs du modèle de données Adobe Experience et les champs de la plateforme Braze correspondants.

1. Dans l'étape de mappage, cliquez sur **Ajouter un nouveau mapping**!<br>!\[Mapping\]\[5\]{: style="max-width:50%;"}<br><br>
2. Dans la section du champ source, cliquez sur le bouton de la flèche à côté du champ vide; cela ouvrira la fenêtre de champ source de sélection.<br>!\[Source\]\[6\]<br><br>
3. Dans cette fenêtre, vous devez sélectionner les attributs Adobe à associer à vos attributs Braze. <br>!\[Field\]\[7\]{: style="max-width:70%;"}<br><br>Ensuite, vous devez sélectionner l'espace de noms d'identité. Cette option est utilisée pour associer un espace de noms d'identité à un espace de noms Braze.<br>!\[Identity\]\[8\]{: style="max-width:80%;"}<br> Choisissez vos champs source, puis cliquez sur **Sélectionnez**.<br><br>
4. Dans la section du champ cible, cliquez sur l'icône de mapping à droite du champ.<br>!\[Tagret\]\[9\]{: style="max-width:90%;"} <br><br>
5. Dans la fenêtre de sélection du champ cible, vous pouvez choisir entre trois catégories de champs cibles :<br><br>• **Sélectionnez les attributs**: Utilisez cette option pour associer vos attributs Adobe XDM aux attributs standard de Braze.<br>• **Sélectionnez l'espace de noms d'identité**: Utilisez cette option pour associer les espaces de noms d'identité de la plateforme à Braze espaces de noms d'identité.<br>• **Sélectionnez les attributs personnalisés**: Utilisez cette option pour associer les attributs Adobe XDM aux attributs personnalisés de Braze que vous avez définis dans votre compte Braze. <br><br>!\[Attributes\]\[10\]{: style="max-width:60%;"}<br><br>**Vous pouvez également utiliser cette option pour renommer les attributs XDM existants en Braze.** Par exemple, associer un attribut XDM à un `nom de famille` à un attribut personnalisé `Last_Name` en Brésil, créera l'attribut `Last_Name` dans Braze s'il n'existe pas déjà, et mapper l'attribut `nom` XDM. <br><br> Choisissez vos champs cibles, cliquez sur **Sélectionner**.<br><br>
6. Vous devriez maintenant voir votre mapping de champ dans la liste.<br>!\[List\]\[11\]<br><br>
7. Pour ajouter plus de mappages, répétez les étapes 1 à 6, si nécessaire.

## Exemple

Disons que votre schéma de profil XDM et votre instance Braze contiennent les attributs et identités suivants :

|           | Schéma de profil XDM                                                                        | Instance Braze                                               |
| --------- | ------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| Attributs | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number` | - `Prénom`<br>- `Nom`<br>- `Numéro de téléphone` |
| Identités | - `Email`<br>- `Google Ad ID (GAID)`<br>- `Apple ID pour les annonceurs (IDFA)` | - `external_id`                                              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Le mapping correct ressemblerait à ceci :

!\[Mappage correct\]\[12\]

## Données exportées
Pour vérifier si les données ont été exportées avec succès vers Braze, vérifiez votre compte Braze. Les segments de plateforme Adobe Experience sont exportés vers Braze sous l'attribut `AdobeExperiencePlatformSegments`.

## Consommation et gouvernance des données
Toutes les destinations Adobe Experience Platform sont conformes aux politiques d'utilisation des données lors du traitement de vos données. Voir [la gouvernance des données en temps réel CDP](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) pour des informations détaillées sur la manière dont la plate-forme Adobe Experience applique la gouvernance des données.
[1]: {% image_buster /assets/img/adobe/braze-destination-configure.png %} [3]: {% image_buster /assets/img/adobe/braze-destination-account.png %} [4]: {% image_buster /assets/img/adobe/braze-destination-authentication. ng %} [5]: {% image_buster /assets/img/adobe/braze-destination-mapping.png %} [6]: {% image_buster /assets/img/adobe/braze-destination-mapping-source. ng %} [7]: {% image_buster /assets/img/adobe/braze-destination-mapping-attributes. ng %} [8]: {% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %} [9]: {% image_buster /assets/img/adobe/braze-destination-mapping-target. ng %} [10]: {% image_buster /assets/img/adobe/braze-destination-mapping-target-field. ng %} [11]: {% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %} [12]: {% image_buster /assets/img/adobe/braze-destination-mapping-example.png %} 