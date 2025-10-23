---
nav_title: Personalize.AI
article_title: Personalize.AI
description: "Cet article de référence présente le partenariat entre Braze et Personalize.AI, une plateforme commerciale SaaS basée sur l'intelligence artificielle qui favorise la croissance des chiffres d'affaires grâce à des recommandations personnalisées."
alias: /partners/personalize_ai/
page_type: partner
search_tag: Partner
---

# Personalize.AI

> [Personalize.AI](https://www.zs.com/solutions/artificial-intelligence-and-analytics/personalize-ai/) s’associe à Braze pour générer des revenus supplémentaires en diffusant des messages personnalisés et des offres envoyées par l'intermédiaire de Braze. 

L'intégration de Braze et de Personalize.AI vous permet d'exporter des données de Personalize.AI vers la plateforme Braze pour la personnalisation et le ciblage des messages.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Personalize.AI instance | Une instance Personalize.AI est nécessaire pour profiter de ce partenariat. |
| Clé API REST de Braze | Une clé API REST Braze avec toutes les permissions. <br><br>Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Endpoint REST Braze | L'URL de votre endpoint REST. Votre endpoint dépendra de l'[URL de Braze pour votre instance]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Cas d'utilisation

* Déployer des tests, y compris une stratification flexible, pour obtenir des résultats à partir du retour d'information des clients.
* Fournir des recommandations personnalisées pour les articles et les offres, y compris le traitement, le moment opportun et le contenu.
* Identifiez des objectifs prioritaires et ciblez votre audience optimale grâce à Braze.
* Identifier les possibilités de réengagement des utilisateurs qui n'ont plus d'expérience.
* Exploiter les données de géolocalisation pour trouver la bonne audience pour les emplacements/localisations nouvellement ouverts.
* Utilisez la modélisation lookalike pour créer des données disponibles limitées pour les nouveaux utilisateurs, en les associant aux recommandations les plus pertinentes.
* Identifier les bons moyens d'engager les clients tout au long de leur cycle de vie. 
* Évaluer de manière proactive la probabilité que les clients se désabonnent et attribuer un score de risque pour identifier des indicateurs précoces de désabonnement.
* Cibler les clients avec des interventions personnalisées pour éviter qu'ils ne deviennent inactifs.

## Intégration

### Configurez une connexion avec Braze en Personalize.AI

1. Dans Personalize.AI, accédez à l'onglet **Integrations**, situé sous **Operationalization**, dans votre instance Personalize.AI.
2. Cliquez sur **Braze**. 
3. Configurez votre intégration avec Braze.
    * **Nom de la connexion :** Donnez un nom à votre connexion. Ce nom désignera votre intégration sur le site Personalize.AI.
    * **Fréquence de synchronisation :** La fréquence de synchronisation détermine la fréquence à laquelle Personalize.AI exporte des données vers Braze. Sélectionnez **Quotidien**, **Hebdomadaire** ou **Mensuel**. 
    * **Clé API :** Ajoutez votre clé API Braze.
    * **URL DE L'API :** Ajoutez l'URL de votre endpoint REST de Braze.
4. Cliquez sur **EXPORT** pour exporter les données vers Braze.

Une fois vos données exportées, Personalize.AI continuera à transmettre des données à Braze aux intervalles déterminés par la fréquence de synchronisation que vous avez définie lors de l'intégration.

## Grâce à cette intégration

Personalize.AI exporte les identifiants utilisés pour le ciblage personnalisé dans Braze. Ces attributs personnalisés indiquent le moment, le contenu, le traitement et les offres pour chaque client. En fonction de l'intégration, les champs peuvent être transmis en tant qu'événement ou tirés dans les [API de contenu connecté]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/public_apis/) au lieu d'être stockés dans le profil du client. Personalize.AI prend en charge l'utilisation de `external_id` en tant qu'identifiant.

Les attributs de données importés dans Braze sont nommés de manière intuitive pour être utilisés dans Canvases, en suivant une terminologie cohérente. Par exemple, l'attribut `C402_Target_Variant` dans Personalize.AI serait exporté vers Braze en tant que `"P.AI_Model_Treatment"`. Les attributs exportés depuis Personalize.AI sont conçus pour ne pas interférer avec les attributs existants ou le suivi que vous utilisez. Ces attributs sont validés en permanence afin que vous puissiez les référencer en toute confiance. 

Voici, par exemple, un ensemble d'attributs clients en rapport avec un exemple de Canvas axé sur le désabonnement.

| Personalize.AI attribut | Valeur |
| ----------- | ------------- | 
| `Customer_ID` | 12345 |
| `Target_Canvas` | C4 |
| `Target_Objective` |  "Atténuation des désabonnements" |
| `C4_Target_Date` | 3/1/2023 |
| `C4_Target_Variant` | Traitement |
| `C4_Treatment` | "P.AI_Model" |
| `C4_Offer_Value` | 3 $ |
| `C4_Item_Recom` | "Salade César |
| `C4_Subject_Line` | "Vous nous manquez |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }


