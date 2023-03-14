---
nav_title: Peak
article_title: Peak
description: "Intégration de l’intelligence décisionnelle de la plateforme Peak à la plateforme Braze"
alias: /partners/Peak/
page_type: partner
search_tag: Partenaire

---

# Peak

> [Peak](https://platform.peak.ai/), une plateforme d’intelligence décisionnelle, est un système de bout en bout où l’intelligence décisionnelle est l’exploitation commerciale de l’IA pour améliorer la prise de décision des entreprises, augmenter les revenus et les bénéfices.

Le partenariat entre Braze et Peak vous permet de prendre la probabilité et les attributs de prédiction du taux d’attrition en fonction des comportements et interactions des clients, et de les importer dans Braze pour les utiliser dans la segmentation et le ciblage des clients. 

## Conditions préalables

Pour commencer, un locataire Peak doit héberger l’intégration entre Peak et Braze. Cela est traditionnellement créé lors de l’onboarding des clients Peak. De plus, une solution d’intelligence décisionnelle est initialement requise, car cela génère des sorties basées sur l’IA qui seront ensuite intégrées à Braze.

| Condition | Description |
| ----------- | ----------- |
| Locataire Peak | Une instance de la plateforme Peak, appelée locataire, est requise pour héberger et orchestrer l’intégration. |
| Solution d’intelligence décisionnelle | L’intégration entre Peak et Braze repose sur des sorties basées sur l’IA et nécessite donc une solution Peak ou de client déployée au sein de votre locataire. |
| Clé d’API REST Braze | Une clé d’API REST Braze avec des autorisations `users.track`. <br><br>Pour créer une clé d’API, accédez au **Tableau de bord de Braze > Developer Console > REST API Key (Clé d’API REST) > Create New API Key (Créer une nouvelle clé d’API)**. |

## Intégration

L’intelligence client de la solution Peak utilise un modèle pour prévoir une gamme d’attributs prospectifs basés sur les comportements et interactions des clients. Ces attributs sont stockés dans Peak et peuvent être utilisés pour générer une segmentation prédictive, y compris la probabilité d’attrition d’un client. La mise à jour de ces attributs prédictifs sera basée sur une cadence configurable (quotidienne ou hebdomadaire).

### Étape 1 : Exécuter le modèle et extraire les clients

L’intégration est déclenchée à la suite de l’exécution du modèle d’IA et du recalcul des attributs prédictifs du client. Ces sorties d’IA sont stockées dans Peak, y compris lorsqu’un attribut est mis à jour avec un nouveau statut ou une nouvelle valeur.

Sur la base du moment où les attributs ont été mis à jour, une sélection est effectuée pour recueillir tous les clients avec des attributs prédictifs mis à jour depuis la dernière synchronisation entre Peak et Braze.

### Étape 2 : Mettre à jour Braze

Avec les clients et les attributs associés mis à jour, Peak les envoie par POST à Braze en utilisant l’endpoint [/user/track][1], en utilisant l’en-tête [bulk]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates).

À la réception des codes d’état réussis de l’API, Peak enregistre la synchronisation réussie entre Peak et Braze.

### Étape 3 : Comment utiliser cette intégration

Une fois que la synchronisation entre Peak et Braze aboutit, les utilisateurs mis à jour incluent désormais les nouveaux attributs. Utilisez ces attributs dans les campagnes et les Canvas pour cibler les utilisateurs et personnaliser les messages.

[1]: {{site.baseurl}}/api/endpoints/user_data/post_user_track/