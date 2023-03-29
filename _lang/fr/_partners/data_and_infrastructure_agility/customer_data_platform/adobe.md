---
nav_title: Adobe
article_title: Adobe
alias: /partners/adobe/
description: "Cet article de référence décrit le partenariat entre Braze et Adobe, une plateforme de données client qui permet aux marques de connecter et de mapper leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel. Les marques peuvent ensuite se servir de ces données pour offrir des expériences personnalisées et ciblées à ces utilisateurs."
page_type: partner
page_order: 2.1
search_tag: Partenaire

---

# Adobe

> Reposant sur Adobe Experience Platform, la plateforme de données client en temps réel d’Adobe aide les entreprises à rassembler des données connues et anonymes provenant de diverses sources d’entreprise pour créer des profils clients. Ces profils peuvent ensuite être utilisés pour offrir des expériences personnalisées en temps réel sur tous les canaux et appareils.

L’intégration entre Braze et Adobe CDP permet aux marques de connecter et de mapper leurs données Adobe (segments et attributs personnalisés) vers Braze en temps réel. Les marques peuvent ensuite se servir de ces données pour offrir des expériences personnalisées et ciblées à ces utilisateurs. Avec Adobe, l’intégration est intuitive. Munissez-vous d’une [identité](https://experienceleague.adobe.com/docs/experience-platform/identity/namespaces.html?lang=en) Adobe, mappez-la à un ID externe Braze et envoyez-la à la plateforme Braze. Toutes les données envoyées seront accessibles dans Braze via un nouvel attribut `AdobeExperiencePlatformSegments`.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Adobe | Un compte [Adobe](https://account.adobe.com/) est requis pour profiter de ce partenariat. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
| Instance de Braze | Votre instance Braze peut être obtenue auprès de votre gestionnaire d’onboarding Braze ou est disponible sur la [page API overview]({{site.baseurl}}/api/basics/#endpoints). |
| Endpoint REST de Braze  | URL de votre endpoint REST. Votre endpoint dépendra de l’[URL Braze pour votre instance]({{site.baseurl}}/api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2}

{% alert important %}
Notez que le fait d’envoyer des attributs personnalisés supplémentaires peut entraîner des problèmes au niveau des points de données. Nous vous conseillons d’en parler à votre gestionnaire pour mieux comprendre cette augmentation potentielle de vos points de données.
{% endalert %}

## Intégration

### Étape 1 : Configurer la destination Braze

Sur la page **Settings (Paramètres)** d’Adobe, sélectionnez **Destinations** sous **Collections**. À cet endroit, cherchez la mosaïque **Braze** et cliquez sur **Configure (Configurer)**. 

![][1]

{% alert note %}
Si une connexion Braze existe déjà, vous verrez un bouton **Activate (Activer)** sur la carte de destination. Pour plus d’informations sur la différence entre l’activation et la configuration, reportez-vous à la section Catalogue de la [documentation](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/destinations/destinations-interface/destinations-workspace.html?lang=en#catalog) sur l’espace de travail de destination Adobe.
{% endalert %}

### Étape 2 : Fournir un jeton Braze

À l’étape **Account (Compte)**, fournissez votre clé API Braze et cliquez sur **Connect to destination (Se connecter à la destination)**.

![][3]{: style="max-width:60%"}

### Étape 3 : Authentification

Ensuite, à l’étape **Authentication (Authentification)**, renseignez les détails de la connexion Braze :
- **Name** : Saisissez un nom avec lequel vous souhaitez reconnaître cette destination à l’avenir.
- **Destination** : Saisissez une description qui vous aidera à identifier la destination.
- **Instance d’endpoint** : Saisissez votre instance d’endpoint Braze.
- **Cas d’utilisation marketing** : Les cas d’utilisation marketing indiquent l’intention pour laquelle les données seront exportées vers la destination. Vous pouvez choisir l’un des cas d’utilisation marketing définis par Adobe ou créer votre propre cas d’utilisation marketing. Pour en savoir plus sur les cas d’utilisation marketing d’Adobe, consultez la page [Data governance in Adobe Experience Platform (Gouvernance des données dans Adobe Experience Platform)](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en#destinations).

![][4]{: style="max-width:60%;"}

### Étape 4 : Créer une destination
Cliquez sur **Create destination (Créer une destination)**. Votre destination a maintenant été créée. Vous pouvez cliquer sur **Save & Exit (Enregistrer et quitter)** pour activer les segments plus tard ou sur **Next (Suivant)** pour continuer le flux de travail et sélectionner des segments à activer. 

### Étape 5 : Activer des segments
Activez les données que vous avez dans le CDP en temps réel d’Adobe en mappant les segments vers la destination Braze.

La liste ci-dessous met en évidence les principales étapes à suivre pour activer un segment. Rendez-vous sur le site Web [Adobe](https://experienceleague.adobe.com/docs/experience-platform/destinations/ui/activate-destinations.html?lang=en#prerequisites) pour obtenir des conseils détaillés sur les segments Adobe et le flux de travail d’activation des segments.

1. Sélectionnez et activez la destination Braze.
2. Sélectionnez les segments applicables.
4. Configurez la planification et les noms de fichier pour chaque segment que vous exportez.
5. Sélectionnez les attributs à envoyer à Braze.
6. Vérifiez l’activation.

### Étape 6 : Mappage des champs

Pour envoyer correctement vos données d’audience depuis la plateforme Adobe Experience Platform vers Braze, vous devez terminer l’étape de mappage de champs. Le mappage crée un lien entre les champs de modèle de données d’Adobe Experience et les champs de la plateforme Braze correspondants.

1. À l’étape du mappage, cliquez sur **Add new mapping (Ajouter un nouveau mappage)**.<br>![][5]{: style="max-width:50%;"}<br><br>
2. Dans la section champ source, cliquez sur la flèche à côté du champ vide ; cela ouvrira la fenêtre du champ source sélectionné.<br>![][6]<br><br>
3. Dans cette fenêtre, vous devez sélectionner les attributs Adobe que vous souhaitez mapper à vos attributs Braze.  <br>![][7]{: style="max-width:70%;"}<br><br>Ensuite, vous devez sélectionner l’espace de noms d’identité. Cette option permet de mapper un espace de noms d’identité Adobe Experience Platform à un espace de noms Braze.<br>![][8]{: style="max-width:80%;"}<br> Choisissez vos champs sources, puis cliquez sur **Select (Sélectionner)**.<br><br>
4. Dans la section champ cible, cliquez sur l’icône de mappage à côté du champ.<br>![][9]{: style="max-width:90%;"} <br><br>
5. Dans la fenêtre de champ cible sélectionnée, vous pouvez choisir entre trois catégories de champs cibles :<br><br>• **Select identity namespace (Sélectionner un espace de noms d’identité)** : Utilisez cette option pour mapper des espaces de noms d’identité Adobe Experience Platform à des espaces de noms d’identité Braze.<br>• **Select custom attributes (Sélectionner des attributs personnalisés)** : Utilisez cette option pour mapper des attributs Adobe XDM à des attributs personnalisés de Braze que vous avez définis sur votre compte Braze.  <br><br>![][10]{: style="max-width:60%;"}<br><br>**Vous pouvez également utiliser cette option pour renommer les attributs XDM existants dans Braze.** Par exemple, le fait de mapper un attribut `lastname` XDM à un attribut `Last_Name` personnalisé de Braze créera un attribut `Last_Name` dans Braze s’il n’existe pas déjà et y mappera l’attribut `lastname` XDM. <br><br> Choisissez vos champs cibles, puis cliquez sur **Select (Sélectionner)**.<br><br>
6. Vous devriez maintenant voir votre mappage de champs dans la liste.<br>![][11]<br><br>
7. Pour ajouter d’autres mappages, répétez les étapes 1 à 6, si nécessaire. 

## Exemple

Supposons que votre schéma de profil XDM et votre instance Braze contiennent les attributs et identités suivants :

|     | Schéma de profil XDM | Instance de Braze |
| --- | ------------------ | -------------- |
| Attributs | - `person.name.firstname`<br>- `person.name.lastname`<br>- `mobilePhone.number`| - `FirstName`<br>- `LastName`<br>- `PhoneNumber`|
| Identités | - `Email`<br>- ID Google Ad (`GAID`)<br>- ID Apple pour les annonceurs (`IDFA`) | - `external_id` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Le mappage correct ressemble à ceci :

![Mappages des destinations : IdentityMap:IDFA mappé vers IdentityMap:external_id, IdentityMap:GAID mappé vers IdentityMap:external_id, IdentityMap:Email mappé vers IdentityMap:external_id, xdm:mobilePhone.number mappé vers CustomAttribute:PhoneNumber, xdm:person.name.lastName mappé vers CustomAtrribute:LastName, xdm:person.name.firstName mappé vers CustomAttribute:FirstName][12]

## Données exportées
Accédez à votre compte Braze pour vérifier si les données ont bien été exportées dans Braze. Les segments Adobe Experience Platform sont exportés vers Braze sous l’attribut `AdobeExperiencePlatformSegments`.

## Utilisation et gouvernance des données
Toutes les destinations Adobe Experience Platform gèrent vos données conformément aux politiques d’utilisation des données. Consultez [CDP de gouvernance des données en temps réel](https://experienceleague.adobe.com/docs/experience-platform/rtcdp/privacy/data-governance-overview.html?lang=en) pour obtenir des informations détaillées sur la façon dont Adobe Experience Platform applique la gouvernance des données. 

[1]: {% image_buster /assets/img/adobe/braze-destination-configure.png %} 
[3]: {% image_buster /assets/img/adobe/braze-destination-account.png %}
[4]: {% image_buster /assets/img/adobe/braze-destination-authentication.png %}
[5]: {% image_buster /assets/img/adobe/braze-destination-mapping.png %} 
[6]: {% image_buster /assets/img/adobe/braze-destination-mapping-source.png %} 
[7]: {% image_buster /assets/img/adobe/braze-destination-mapping-attributes.png %} 
[8]: {% image_buster /assets/img/adobe/braze-destination-mapping-namespaces.png %} 
[9]: {% image_buster /assets/img/adobe/braze-destination-mapping-target.png %} 
[10]: {% image_buster /assets/img/adobe/braze-destination-mapping-target-fields.png %} 
[11]: {% image_buster /assets/img/adobe/braze-destination-mapping-complete.png %} 
[12]: {% image_buster /assets/img/adobe/braze-destination-mapping-example.png %} 