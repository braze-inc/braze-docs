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

_Cette intégration est gérée par Dynamics 365 Customer Insights._

## À propos de l'intégration

L'intégration de Braze et de Dynamics 365 Customer Insights vous permet d'exporter des segments de clients vers Braze afin de les utiliser dans des campagnes ou des Canvases.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Dynamics 365 Customer Insights (informations sur les clients) | Un compte [Dynamics 365 Customer Insights](https://dynamics.microsoft.com/en-gb/ai/customer-insights/) est nécessaire pour bénéficier de ce partenariat. Vous aurez besoin d'un accès en tant qu'administrateur pour voir et modifier les connexions dans votre compte Dynamics 365 Customer Insights afin d'accéder aux plugins nécessaires. |
| Clé d'API REST Braze | Une clé API REST Braze est requise avec les autorisations `users.track` et `users.export.segment`. <br><br> Elle peut être créée dans le tableau de bord de Braze depuis **Paramètres** > **Clés d'API**. |
| Correspondance des identifiants de profil | Les profils de clients unifiés dans les segments exportés contiennent un champ conseillant une adresse e-mail et une adresse Braze `external_id`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Établir une connexion Braze

Dans Customer Insights, accédez à **Admin > Connexions**. Ensuite, sélectionnez **Ajouter des connexions** et choisissez **Braze** pour configurer la connexion. 

1. Donnez à votre connexion un nom reconnaissable dans le champ **Nom d'affichage.**  
2. Choisissez qui peut utiliser cette connexion. Si vous laissez ce champ vide, la valeur par défaut sera Administrateurs. Pour plus d'informations, reportez-vous à la section [Autoriser les contributeurs à utiliser une connexion pour les exportations](https://docs.microsoft.com/en-us/dynamics365/customer-insights/connections#allow-contributors-to-use-a-connection-for-exports).
3. Indiquez votre clé API Braze et votre endpoint REST au format `rest.iad-03.braze.com`.
4. Sélectionnez **J'accepte** de confirmer la conformité des données et de la confidentialité.
5. Sélectionnez **Connecter** pour initialiser la connexion avec Braze.
6. Sélectionnez **S'ajouter en tant qu'utilisateur d'exportation** et fournissez vos informations d'identification Customer Insights.
7. Sélectionnez **Enregistrer** pour terminer la connexion.

### Étape 2 : Créer un segment de Braze

1. Dans Braze, allez dans **Audience** > **Segments**.
2. Créez un segment des utilisateurs que vous souhaitez que Microsoft mette à jour via Dynamics 365 Customer Insights.
3. Saisir l' **identifiant API** du segment

### Étape 3 : Configurer une exportation

Vous pouvez configurer cette exportation si vous avez accès à une connexion de ce type. Pour plus d'informations, reportez-vous à l'[aperçu des exports](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#set-up-a-new-export).

1. Dans Customer Insights, accédez à **Données > Exportations.** Pour créer une nouvelle exportation, sélectionnez **Ajouter une destination.**
2. Dans le champ **Connexion pour l'exportation**, sélectionnez une connexion pour la section Braze. Si vous ne voyez pas le nom de cette section, c'est qu'aucune connexion de ce type n'est disponible.
3. Indiquez l'identifiant API du segment dans Braze.
4. Dans la section **Correspondance des données**, dans le champ **Email**, sélectionnez le champ qui représente l'adresse e-mail d'un client. Ensuite, dans le champ **ID client Braze**, sélectionnez le champ qui conseille l'ID Braze du client. Vous pouvez également sélectionner un champ supplémentaire, facultatif, pour les données correspondantes.
  a. Si vous mappez le site `external_id` dans Braze au champ ID client de Braze dans Customer Insights, les enregistrements existants seront mis à jour dans Braze lors de l'exportation.
  b. Si vous mappez un champ ID différent qui ne représente pas le `external_id` d'un enregistrement dans Braze, ou un champ vide, de nouveaux enregistrements seront créés dans Braze lors de l'exportation.
5. Enfin, sélectionnez les segments que vous souhaitez exporter et cliquez sur **Enregistrer.** 

Notez que le fait d'enregistrer une exportation ne l'exécute pas immédiatement. Cette exportation sera exécutée à chaque [actualisation planifiée](https://docs.microsoft.com/en-us/dynamics365/customer-insights/system#schedule-tab). Vous pouvez également [exporter des données à la requête](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-destinations#run-exports-on-demand). 


### Utilisation de cette intégration

Une fois vos segments exportés avec succès vers Braze, vous pouvez les retrouver en tant qu'attributs personnalisés dans les profils utilisateurs. L'attribut personnalisé sera nommé avec l'identifiant API du segment Braze qui a été saisi lors de la configuration de la connexion d'exportation. Par exemple, `"Segment_API_Identifier": "0000-0000-0000"`

Pour créer un segment de ces utilisateurs dans Braze, naviguez vers **Segments**, créez un nouveau segment et sélectionnez **Attributs personnalisés** comme filtre. À partir de là, vous pouvez choisir l'attribut personnalisé synchronisé par Dynamics 365. Une fois le segment créé, vous pouvez le sélectionner comme filtre d'audience lors de la création d'une campagne ou d'un Canvas.

{% alert note %}
Pour plus d'informations sur cette intégration, consultez l'article de Microsoft [sur l'intégration de Braze](https://docs.microsoft.com/en-us/dynamics365/customer-insights/export-braze).
{% endalert %}


