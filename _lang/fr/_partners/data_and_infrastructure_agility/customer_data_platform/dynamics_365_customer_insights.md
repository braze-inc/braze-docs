---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "Cet article de référence présente le partenariat entre Braze et Dynamics 365 Customer Insights, une plateforme de données client de premier plan qui vous permet d’exporter des segments de clients vers Braze pour les utiliser dans des campagnes ou des Canvas."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partenaire
---

# Dynamics 365 Customer Insights
 
> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) est une plateforme de données client de premier plan qui offre des expériences client personnalisées avec une vue à 360 degrés de vos clients.

L’intégration de Braze et Dynamics 365 Customer Insights vous permet d’exporter des segments de clients vers Braze pour les utiliser dans des campagnes ou des Canvas.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Dynamics 365 Customer Insights  | Un compte [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) est requis pour profiter de ce partenariat. Vous aurez besoin d’un accès administrateur pour afficher et modifier les connexions dans votre compte Dynamics 365 Customer Insights afin d’accéder aux plug-ins nécessaires. |
| Clé d’API REST Braze | Une clé API REST Braze avec toutes les autorisations est requise. <br><br> Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |
{: .reset-td-br-1 .reset-td-br-2}

## Intégration

### Étape 1 : Configurer la connexion Braze

Dans Customer Insights, accédez à **Admin > Connections (Connexions)**. Ensuite, sélectionnez **Add connections (Ajouter des connexions)** et choisissez **Braze** pour configurer la connexion. 

1. Donnez à votre connexion un nom reconnaissable dans le champ **Display name (Nom d’affichage)**. 
2. Choisissez qui peut utiliser cette connexion. Si vous laissez ce champ vide, la valeur par défaut sera « Administrators (Administrateurs) ». Pour plus d’informations, consultez la section [Autoriser les contributeurs à utiliser une connexion pour les exportations](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Saisissez votre clé API Braze pour vous connecter.
4. Cliquez sur **I agree (J’accepte)** pour accepter l’avis de conformité et de confidentialité des données.
5. Sélectionnez **Connect (Connexion)** pour initialiser la connexion à Braze.
6. Sélectionner **Add yourself as export user (M’ajouter en tant qu’utilisateur d’exportation)** et fournissez vos informations d’identification Customer Insights.
7. Cliquez sur **Save (Enregistrer)** pour finaliser la connexion. 

### Étape 2 : Configurer une exportation

Vous pouvez configurer cette exportation si vous avez accès à une connexion de ce type. Pour plus d’informations, consultez [Aperçu des exportations](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. Dans Customer Insights, accédez à **Data (Données) > Exports (Exportations)**. Pour créer une nouvelle exportation, sélectionnez **Add destination (Ajouter une destination)**.
2. Dans le champ **Connection for export (Connexion pour l’exportation)**, choisissez une connexion pour la section Braze. Si vous ne voyez pas ce nom de section, aucune connexion de ce type n’est disponible pour vous. 
3. Saisissez votre endpoint REST dans le champ du nom d'hôte au format suivant : `rest.iad-03.braze.com`.
4. Dans la section **Data matching (Correspondance des données)**, dans le champ **Email (E-mail)** sélectionnez le champ représentant l’adresse e-mail d’un client. Ensuite, dans le champ **Customer ID (ID client)**, sélectionnez le champ représentant l’ID du client Braze. Vous pouvez également choisir un champ supplémentaire (facultatif) pour faire correspondre les données. 
5. Enfin, cliquez sur **Save (Enregistrer)**. 

Notez que les exportations ne s’exécutent pas immédiatement après avoir été enregistrées. Cette exportation s’exécutera avec chaque [actualisation planifiée](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab). Vous pouvez également [exporter des données à la demande](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand). 

### Comment utiliser cette intégration

Une fois vos segments exportés avec succès vers Braze, vous pourrez les trouver en tant qu'attributs personnalisés sur les profils utilisateur portant le même nom que le segment trouvé dans Dynamics 365 Customer Insights. 

Pour créer un segment avec ces utilisateurs, dans Braze accédez à **Segments**, créez un nouveau segment et choisissez **Custom Attributes (Attributs personnalisés)** comme filtre. À partir de là, vous pouvez choisir l'attribut personnalisé Dynamics 365. Une fois créé, vous pouvez sélectionner votre segment comme filtre d’audience au moment de créer une campagne ou un Canvas.

{% alert note %}
Pour plus d’informations sur cette intégration, consultez l’[article sur l’intégration](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze) Braze de Microsoft.
{% endalert %}

[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints