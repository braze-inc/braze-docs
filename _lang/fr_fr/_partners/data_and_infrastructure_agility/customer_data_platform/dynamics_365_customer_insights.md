---
nav_title: Dynamics 365 Customer Insights
article_title: Dynamics 365 Customer Insights
description: "Cet article de référence présente le partenariat entre Braze et Dynamics 365 Customer Insights, une plateforme de données client d'entreprise de premier plan, qui vous permet d'exporter des segments de clients vers Braze pour les utiliser dans des campagnes ou des Canvases."
alias: /partners/dynamics_365_customer_insights/
page_type: partner
search_tag: Partner
---

# Dynamics 365 Customer Insights
 
> [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) est une plateforme de données client d'entreprise de premier plan qui offre des expériences client personnalisées avec une vue à 360 degrés de vos clients.



## À propos de l'intégration

L'intégration de Braze et de Dynamics 365 Customer Insights vous permet d'exporter des segments de clients vers Braze afin de les utiliser dans des campagnes ou des Canvases.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Dynamics 365 Customer Insights (informations sur les clients) | Un compte [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) est nécessaire pour bénéficier de ce partenariat. Vous aurez besoin d'un accès en tant qu'administrateur pour voir et modifier les connexions dans votre compte Dynamics 365 Customer Insights afin d'accéder aux plugins nécessaires. |
| Clé d'API REST Braze |  <br><br> Cette clé peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
|  |  |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Établir une connexion Braze

Dans Customer Insights, accédez à **Admin > Connexions**. Ensuite, sélectionnez **Ajouter des connexions** et choisissez **Braze** pour configurer la connexion. 

1. Donnez à votre connexion un nom reconnaissable dans le champ **Nom d'affichage.**  
2. Choisissez qui peut utiliser cette connexion. Si vous laissez ce champ vide, la valeur par défaut sera Administrateurs. Pour plus d'informations, reportez-vous à la section [Autoriser les contributeurs à utiliser une connexion pour les exportations](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. 
4. Sélectionnez **J'accepte** de confirmer la conformité des données et de la confidentialité.
5. Sélectionnez **Connecter** pour initialiser la connexion avec Braze.
6. Sélectionnez **S'ajouter en tant qu'utilisateur d'exportation** et fournissez vos informations d'identification Customer Insights.
7. Sélectionnez **Enregistrer** pour terminer la connexion.

### Étape 2 : 

1. 
2. 
3. 

### Étape 3 : Configurer une exportation

Vous pouvez configurer cette exportation si vous avez accès à une connexion de ce type. Pour plus d'informations, reportez-vous à l'[aperçu des exports](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. Dans Customer Insights, accédez à **Données > Exportations.** Pour créer une nouvelle exportation, sélectionnez **Ajouter une destination.**
2.  Si vous ne voyez pas le nom de cette section, c'est qu'aucune connexion de ce type n'est disponible.
3. 
4. Dans la section **Correspondance des données**, dans le champ **Email**, sélectionnez le champ qui représente l'adresse e-mail d'un client.  
  a. 
  b. 
5.  

Notez que le fait d'enregistrer une exportation ne l'exécute pas immédiatement. Cette exportation sera exécutée à chaque [actualisation planifiée](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab). Vous pouvez également [exporter des données à la requête](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand). 


### Grâce à cette intégration

  Par exemple, `"Segment_API_Identifier": "0000-0000-0000"`

  Une fois le segment créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

{% alert note %}
Pour plus d'informations sur cette intégration, consultez l'article de Microsoft [sur l'intégration de Braze](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze).
{% endalert %}


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
