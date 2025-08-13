---
nav_title: Adobe pour Currents
article_title: Adobe pour Currents
alias: /partners/adobe_for_currents/
description: "Cet article de référence présente le partenariat entre Braze Currents et Adobe, une plateforme de données client qui permet aux marques de connecter et de mapper leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel."
page_type: partner
tool: Currents
search_tag: Partner
---

# Adobe pour Currents

> [Adobe](https://www.adobe.com/) est une plateforme de données client qui permet aux marques de connecter et de mapper leurs données Adobe (attributs et segments personnalisés) à Braze en temps réel.

L'intégration de Braze et d'Adobe vous permet de contrôler de façon fluide/sans heurts/de façon homogène le flux d'informations entre les deux systèmes. Avec [Currents]({{site.baseurl}}/user_guide/data/braze_currents/), vous pouvez également connecter les données à Adobe pour les rendre exploitables dans l'ensemble des outils de croissance. 

## Conditions préalables

| Condition | Descriptif |
| ----------- | ----------- |
| Currents | Pour exporter des données dans Adobe, vous devez avoir configuré [Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/#access-currents) pour votre compte. |
| Compte Adobe Experience Platform | Un [compte Adobe Experience Platform](https://experience.adobe.com/#/platform/home) est nécessaire pour bénéficier de ce partenariat. |
| Permission de créer un connecteur | Vous devez disposer des autorisations nécessaires pour créer une connexion de source de streaming afin d'utiliser cette intégration. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créer un schéma XDM dans Adobe

1. Dans Adobe Experience Platform, allez dans **Schémas** > sélectionnez **Créer un schéma** > sélectionnez **Événement d'expérience** > sélectionnez **Suivant.**<br><br>![Page Adobe Schemas pour le schéma appelé "Braze Currents Walk-Through".][1]<br><br>
2. Donnez un nom et une description à votre schéma. 
3. Dans le panneau **Composition**, configurez les attributs de votre schéma :
- Dans **Groupes de champs**, sélectionnez **Ajouter**, puis ajoutez le groupe de champs **Événement utilisateur Braze Currents**.
- Sélectionnez **Enregistrer**.

Pour plus d'informations sur les schémas, consultez la documentation d'Adobe sur la [création de schémas](https://experienceleague.adobe.com/en/docs/experience-platform/xdm/tutorials/create-schema-ui).

### Étape 2 : Connecter Braze à Adobe Experience Platform

1. Dans Adobe Experience Platform, accédez à **Sources** > **Catalogue** > **Automatisation du marketing.**
2. Sélectionnez **Ajouter des données** pour les Braze Currents.
3. Téléchargez le [fichier d'échantillons Braze Currents](https://github.com/Appboy/currents-examples/blob/master/sample-data/Adobe/adobe_examples.json).<br><br>![Adobe "Ajouter une page de données".][2]<br><br>
4. Une fois votre fichier téléchargé, fournissez les détails de votre flux de données, y compris des informations sur votre jeu de données et le schéma auquel vous faites correspondre le mappage. 
    - Si vous connectez une source Braze Currents pour la première fois, créez un nouveau jeu de données et veillez à utiliser le schéma que vous avez créé à l'[étape 1.](#step-1-create-an-xdm-schema-in-adobe) 
    - Si ce n'est pas votre première fois, utilisez n'importe quel jeu de données existant qui fait référence au schéma de Braze.
5. Configurez le mappage de vos données et résolvez les problèmes.
    - Modifiez le mappage pour `id` de `to _braze.appID` à `_id` au niveau racine du schéma.
    - Assurez-vous que `properties.is_amp` est mappée à `_braze.messaging.email.isAMP`.
    - Supprimez le mappage `time` et `timestamp`, puis sélectionnez l'icône d'ajout > **Ajouter un champ calculé** et entrez **time * 1000.** Sélectionnez **Enregistrer**.
    - Sélectionnez **Mapper le champ cible** à côté du nouveau champ source et mappez-le à l'**horodatage** au niveau racine du schéma. <br><br>![Page Adobe "Add data" avec mappages.][3]<br><br>
6. Sélectionnez **Valider** pour confirmer que vous avez résolu les problèmes.

{% alert important %}
Les horodatages de Braze sont exprimés en secondes. Pour refléter correctement les horodatages dans Adobe Experience Platform, vos champs calculés doivent être exprimés en millisecondes. Pour convertir les secondes en millisecondes, utilisez le calcul suivant **: time * 1000.**
{% endalert %}

{: start="7"}
7\. Sélectionnez **Suivant**, vérifiez les détails de votre flux de données, puis sélectionnez **Terminer**.<br><br>![Page "Ajouter des données" d'Adobe sans erreur de mappage.][4]

### Étape 3 : Rassembler les informations d'identification

Recueillez les crédentiels suivants pour les saisir dans Braze, ce qui permettra à Braze d'envoyer des données à Adobe Experience Platform.

| Champ         |Descriptif                          |
|---------------|-------------------------------------|
| ID client     | L'ID du client associé à votre source Adobe Experience Platform. |
| Secret client | Le secret client associé à votre source Adobe Experience Platform. |
| ID de locataire     | L'ID du locataire associé à votre source Adobe Experience Platform. |
| Nom de l’environnement de test  | Le bac à sable associé à votre source Adobe Experience Platform.   |
| Identifiant de flux de données   | L'ID du flux de données associé à votre source Adobe Experience Platform.   |
| Endpoint de flux en continu  | L'endpoint de diffusion en continu associé à votre source Adobe Experience Platform. Braze le convertit automatiquement en endpoint de diffusion en continu par lots. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Étape 4 : Configurez Currents pour qu'il transmette les données en continu à votre source de données.

1. Dans Braze, allez dans **Intégrations partenaires** > **Exportation de données**, puis sélectionnez **Créer un nouveau courant.** 
2. Fournissez les éléments suivants :
    - Un nom pour le connecteur
    - Informations de contact pour les notifications concernant le connecteur
    - Les données d'identification de l'[étape 3](#step-3-gather-credentials)
3. Sélectionnez les événements que vous souhaitez recevoir.
4. Vous pouvez également configurer les exclusions ou les transformations de champs souhaitées.
5. Sélectionnez **Lancer courant.**

[1]: {% image_buster /assets/img/adobe/currents_sources.png %}
[2]: {% image_buster /assets/img/adobe/currents_add_data.png %}
[3]: {% image_buster /assets/img/adobe/currents_mapping.png %}
[4]: {% image_buster /assets/img/adobe/currents_no_errors.png %}