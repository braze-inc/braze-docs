---
nav_title: Adobe
article_title: Adobe
description: "Cette page présente le partenariat entre Braze et Adobe, une plateforme de données client, qui permet aux marques de connecter et de mapper leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel. Les marques peuvent ensuite agir sur ces données, en proposant des expériences personnalisées et ciblées à ces utilisateurs."
page_type: partner
page_order: 1
search_tag: Partner

---

# Adobe

> Créée sur Adobe Experience Platform, la plateforme de données client en temps réel d'Adobe rassemble des données connues et anonymes provenant de plusieurs sources d'entreprise pour créer des profils de clients. Ces profils peuvent ensuite être utilisés pour offrir des expériences personnalisées sur tous les canaux et appareils en temps réel.

L'intégration Braze et Adobe CDP connecte et mappe les données Adobe de votre marque (attributs et segments personnalisés) à Braze en temps réel. Vous pouvez ensuite agir sur ces données, en proposant des expériences personnalisées et ciblées à vos utilisateurs. Avec Adobe, l'intégration est intuitive. Il suffit de prendre n'importe quelle [identité](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en) Adobe, de la mapper à un ID externe Braze et de l'envoyer à la plateforme Braze. Toutes les données envoyées seront accessibles dans Braze grâce à un nouvel attribut `AdobeExperiencePlatformSegments`.

{% alert important %}
L'intégration d'Adobe Experience Platform ne prend actuellement pas en charge l'adhésion dynamique des audiences. Cela signifie qu'il ne peut qu'ajouter des valeurs aux profils utilisateurs, et non les supprimer.
{% endalert %}

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Adobe | Un [compte Adobe](https://account.adobe.com/) est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Instance de Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire onboarding Braze ou sur la [page d'aperçu de l'API]({{site.baseurl}}/api/basics/#endpoints). |
| Endpoint REST de Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
L'envoi d'attributs personnalisés supplémentaires augmentera votre consommation de points données. Nous vous conseillons de vous adresser à votre gestionnaire de satisfaction client pour mieux comprendre cette augmentation potentielle des points données.
{% endalert %}

## Intégration

### Étape 1 : Configurer la destination de Braze

Dans la page **Paramètres** Adobe, sélectionnez **Destinations** sous **Collections.** À partir de là, localisez la tuile **Braze** et sélectionnez **Configurer.** 

![]({% image_buster /assets/img/adobe/braze-destination-configure.png %})

{% alert note %}
Si une connexion avec Braze existe déjà, vous verrez un bouton **Activer** sur la carte de destination. Pour plus d'informations sur la différence entre activer et configurer la destination, reportez-vous à la section du catalogue [de la documentation](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog) de l’espace de travail de destination Adobe.
{% endalert %}

### Étape 2 : Fournir un jeton Braze

À l'étape **Compte**, indiquez votre clé API Braze et sélectionnez **Se connecter à la destination**.

![]({% image_buster /assets/img/adobe/braze-destination-account.png %}){: style="max-width:60%"}

### Étape 3 : Authentification

Ensuite, à l'étape **Authentification**, saisissez vos données de connexion à Braze :
- **Nom**: Saisissez le nom sous lequel vous souhaitez reconnaître cette destination à l'avenir.
- **Destination** : Saisissez une description qui vous aidera à identifier cette destination.
- **L'instance de l'endpoint**: Saisissez votre instance d'endpoint Braze.
- **Cas d'utilisation marketing** : Les cas d'utilisation marketing indiquent l'intention pour laquelle les données seront exportées vers la destination. Vous pouvez choisir parmi les cas d'utilisation marketing définis par Adobe ou créer votre propre cas d'utilisation marketing. Pour en savoir plus sur les cas d'utilisation marketing d'Adobe, consultez la page [Gouvernance des données dans Adobe Experience Platform](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![]({% image_buster /assets/img/adobe/braze-destination-authentication.png %}){: style="max-width:60%;"}

### Étape 4 : Créer une destination
Sélectionnez **Créer une destination**. Votre destination a été créée. Vous pouvez sélectionner **Enregistrer et quitter** pour activer les segments ultérieurement ou **Suivant** pour poursuivre le flux de travail et sélectionner les segments à activer. 

### Étape 5 : Activer les segmentations
Activez les données figurant dans la plateforme de données clients en temps réel d'Adobe en mappant les segments vers la destination Braze.

La liste suivante met en évidence les étapes générales nécessaires à l'activation d'un segment. Pour obtenir des informations détaillées sur les segments Adobe et le processus d'activation des segments, consultez le site [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites).

1. Sélectionnez et activez la destination Braze.
2. Sélectionnez les segments applicables.
4. Configurez la planification et les noms de fichiers pour chaque segment que vous exportez.
5. Sélectionnez les attributs à envoyer à Braze.
6. Examinez et vérifiez l'activation.

### Étape 6 : Mappage des champs

Pour envoyer correctement vos données d'audience d'Adobe Experience Platform vers Braze, vous devez mapper les champs. Le mappage crée un lien entre les champs du modèle de données Adobe Experience et les champs correspondants de la plateforme Braze.

1. À l'étape du mappage, sélectionnez **Ajouter un nouveau mappage**.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping.png %}){: style="max-width:50%;"}<br><br>
2. Dans la section du champ source, sélectionnez le bouton fléché à côté du champ vide pour ouvrir la fenêtre de sélection du champ source.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-source.png %})<br><br>
3. Dans la fenêtre, sélectionnez les attributs Adobe à mapper à vos attributs Braze. <br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %}){: style="max-width:70%;"}<br><br>Sélectionnez ensuite l'espace de noms de l'identité. Cette option permet de mapper un espace de noms d'identité de plateforme à un espace de noms de Braze.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %}){: style="max-width:80%;"}<br> Choisissez vos champs source, puis sélectionnez **Sélectionner.**<br><br>
4. Dans la section du champ cible, sélectionnez l'icône de mappage à côté du champ.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target.png %}){: style="max-width:90%;"} <br><br>
5. Dans la fenêtre de sélection du champ cible, vous pouvez choisir entre trois catégories de champs cibles :<br><br>- **Sélectionnez l'espace de noms d'identité** : Utilisez cette option pour mapper les espaces de noms d'identité de Platform aux espaces de noms d'identité de Braze.<br>- **Sélectionnez les attributs personnalisés** : Utilisez cette option pour mapper les attributs Adobe XDM aux attributs Braze personnalisés que vous avez définis dans votre compte Braze. <br><br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %}){: style="max-width:60%;"}<br><br>**Vous pouvez également utiliser cette option pour renommer des attributs XDM existants dans Braze.** Par exemple, le mappage d'un attribut XDM `lastname` à un attribut personnalisé `Last_Name` dans Braze créera l'attribut `Last_Name` dans Braze s'il n'existe pas déjà, et mappera l'attribut XDM `lastname` à cet attribut. <br><br> Choisissez vos champs de ciblage, puis sélectionnez **Sélectionner.**<br><br>
6. Votre mappage de champ devrait apparaître dans la liste.<br>![]({% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %})<br><br>
7. Pour ajouter d'autres mappages, répétez les étapes 1 à 6, si nécessaire. 

## Cas d'utilisation

Supposons que votre schéma de profil XDM et votre instance Braze contiennent les attributs et identités suivants :

|     | Schéma du profil XDM | Instance de Braze |
| --- | ------------------ | -------------- |
| Attributs | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identités | - `Email`<br>\- ID Google Ad (`GAID`)<br>\- Apple ID pour les annonceurs (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Le mappage correct serait le suivant :

![Mappages de destination : IdentityMap:IDFA mappé à IdentityMap:external_id, IdentityMap:GAID mappé à IdentityMap:external_id, IdentityMap:Email mappé à IdentityMap:external_id, xdm :mobilePhone.number mappé à CustomAttribute:PhoneNumber, xdm :person.name.lastName mappé à CustomAtrribute:LastName, xdm :person.name.firstName mappé à CustomAttribute:FirstName]({% image_buster /assets/img/adobe/braze-destination-mapping-example.png %})

## Données exportées
Pour vérifier si les données ont été exportées avec succès vers Braze, consultez votre compte Braze. Les segments Adobe Experience Platform sont exportés vers Braze sous l'attribut `AdobeExperiencePlatformSegments`.

## Utilisation des données et gouvernance
Toutes les destinations d'Adobe Experience Platform sont conformes aux politiques d'utilisation des données lorsqu'elles traitent vos données. Consultez la rubrique [CDP de gouvernance des données en temps réel](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) pour obtenir des informations détaillées sur la manière dont Adobe Experience Platform applique la gouvernance des données. 

