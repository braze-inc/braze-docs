---
nav_title: Recurly
article_title: Recurly
description: "Recurly est la principale plateforme de gestion des abonnements et de facturation des marques de vente directe aux consommateurs qui cherchent à développer leurs abonnements et leurs revenus récurrents."
alias: /partners/recurly/
page_type: partner
search_tag: partner
---

# Recurly

> [Recurly](https://recurly.com/) est une plateforme de gestion des abonnements et de facturation. La plateforme intégrée Recurly simplifie l'automatisation du cycle de vie des abonnements à grande échelle en permettant aux équipes de gérer et d'optimiser l'expérience des abonnés - depuis le test de nouveaux plans, offres et promotions jusqu'à la gestion des méthodes de paiement, des intégrations et des informations.

_Cette intégration est maintenue par Recurly._

## À propos de l'intégration

L'intégration entre Recurly et Braze simplifie le processus de partage des données d'abonnement avec Braze, ce qui permet une communication ciblée avec les clients.

- Exploitez les événements du cycle de vie des abonnements Recurly (par exemple, les renouvellements, les pauses ou les annulations d'abonnement) dans Braze pour déclencher des campagnes et des communications personnalisées.
- Exploitez les données d'abonnement Recurly (par exemple, les plans d'abonnement, les modules complémentaires ou le statut) pour créer et gérer les utilisateurs, les segments et les Canvases de Braze afin d'exécuter des campagnes et des communications spécifiques aux cohortes.
- Envoyez les données Recurly directement à Braze afin de prendre en charge davantage de cas d'utilisation de messages supplémentaires et de réduire les frais généraux de développement.

Vous trouverez plus de détails sur l'utilisation de Recurly avec Braze dans la [documentation de Recurly.](https://docs.recurly.com/docs/braze-integration)

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Recurly | Un plan d'abonnement Elite [Recurly](https://recurly.com/) avec l’indicateur de fonctionnalité Braze activé est nécessaire pour tirer parti de ce partenariat. L'activation des factures de crédit dans votre plateforme Recurly est également nécessaire.|
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. Comme Recurly n'utilise que l'endpoint `users.track`, nous vous recommandons de déployer une clé Recurly spécifique avec cette seule autorisation. |
| Endpoint REST de Braze | [L'URL de votre endpoint REST.][1] Votre endpoint dépendra de l'URL de Braze pour votre instance. |

## Intégration

Avant de commencer, assurez-vous d'avoir des comptes actifs à la fois sur Braze et sur Recurly.

### Connecter Recurly à Braze

1. Dans Recurly, allez dans **Intégrations** > **Braze**. Lors de la première navigation vers la page de configuration de l'intégration de Braze dans Recurly, l'interface vous invitera à connecter les deux systèmes.

2. Fournissez les informations d'identification suivantes :

- **URL de l'instance :** L'endpoint REST de Braze de l'instance auprès de laquelle vous êtes provisionné.
- **Clé API (identifiant) :** La clé API REST de Braze que Recurly doit utiliser lors de l'envoi de requêtes à Braze.

N'oubliez pas de copier l'URL de votre instance Braze. Par exemple, votre URL pourrait ressembler à ceci : 

```
<https://dashboard-03.braze.com/dashboard/app_usage?locale=en>
```

{:start="3"}
3\. Après avoir saisi vos informations d'identification, cliquez sur **Connecter**.

## Grâce à cette intégration

### Identifiants pris en charge

Recurly utilise le paramètre `account_code` d'un compte comme `external_id` dans Braze. Pour cette raison, le paramètre `account_code` de vos comptes Recurly doit correspondre au paramètre `external_id` de votre utilisateur Braze.

### Événements personnalisés

Pour un engagement client efficace, vous devez [configurer des événements personnalisés][2] dans Braze afin de recevoir les événements déclenchés par Recurly. Veillez à inclure chaque événement de Recurly pour une intégration complète des données. Ces événements peuvent également être suivis dans le cadre de l'[analyse/analytique de Braze][3]. Une fois configurés, ces événements personnalisés peuvent être utilisés pour segmenter les utilisateurs ou personnaliser les messages. 

| Braze Custom Event (événement personnalisé)| Événement Recurly |
| ----------- | ----------- |
| Nouvel abonnement Recurly              | Déclenché lors de la création d'un abonnement                            |
| Renouvellement d’abonnement Recurly          | Déclenché lors du renouvellement d'un abonnement                                |
| Abonnement Recurly mis à jour          | Déclenché lorsque les attributs d'un abonnement changent (changement de plan, de prix ou de quantité). |
| Abonnement Recurly annulé         | Déclenché lors de l'annulation d'un abonnement                           |
| Abonnement Recurly réactivé      | Déclenché lorsqu'un abonnement annulé est réactivé.               |
| Abonnement Recurly interrompu           | Déclenché lorsqu'un abonnement est mis en pause.                   |
| Abonnement Recurly réactivé          | Déclenché lorsqu'un abonnement interrompu est réactivé.                              |
| Abonnement Recurly expiré          | Déclenché à l'expiration d'un abonnement                               |
| Facture Recurly créée               | Déclenché lors de la création d'une facture                                |
| Paiement réussi de Recurly            | Déclenché lorsqu'une facture a été recouvrée.                 |
| Remboursement Recurly émis                 | Déclenché lors de la délivrance d'un remboursement                                   |
| Échec du paiement récurrent Recurly      | Déclenché en cas d'échec de la facturation d'un renouvellement d'abonnement.          |

### Mise en lots et limite de débit

Comme Recurly utilise l'endpoint `/users/track` de Braze, l'intégration est soumise aux limites de débit standard de Braze, à savoir 50 000 requêtes par minute.

Recurly met en lots certains événements du cycle de vie de l'abonnement sous forme d'appels API uniques à Braze afin de réduire le nombre d'appels effectués.

- La création de plusieurs abonnements en même temps est mise en lots et envoyée à Braze sous la forme d'une requête unique.
- Lorsque plusieurs abonnements sont renouvelés en même temps pour un compte, chacun de ces renouvellements est regroupé en une seule requête.
- Les événements du cycle de vie de l'abonnement au même modèle sont envoyés en une seule requête. Par exemple, une facture nouvellement créée avec un paiement enverrait une seule requête API avec les événements personnalisés `Recurly Invoice Created` et `Recurly Successful Payment`.

Les lots sont envoyés à Braze par groupes de 75 événements maximum à la fois. Par exemple, si 100 abonnements sont créés en même temps, Recurly fera deux requêtes d'API à Braze. Pour plus d'informations, reportez-vous à la section [relative à la mise en lot des requêtes de suivi des utilisateurs][4].


[1]: {{site.baseurl}}/developer_guide/rest_api/basics/#endpoints
[2]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/
[3]: {{site.baseurl}}/user_guide/data_and_analytics/custom_data/custom_events/#analytics
[4]: {{site.baseurl}}/api/api_limits/#batch-user-track
