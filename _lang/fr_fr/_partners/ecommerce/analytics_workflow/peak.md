---
nav_title: Peak
article_title: Peak
description: "Cet article de référence décrit le partenariat entre Braze et Peak, une plateforme d'intelligence décisionnelle, qui vous permet de prendre la probabilité de désabonnement prédite et les attributs basés sur les comportements et interactions des clients, et de les importer dans Braze pour les utiliser dans la segmentation et le ciblage des clients."
alias: /partners/Peak/
page_type: partner
search_tag: Partner

---

# Peak

> [Peak](https://platform.peak.ai/), une plateforme d'intelligence décisionnelle qui utilise l'intelligence artificielle à des fins commerciales pour améliorer la prise de décision commerciale, augmenter le chiffre d'affaires et les bénéfices.

_Cette intégration est maintenue par Peak._

## À propos de l'intégration

Le partenariat entre Braze et Peak vous permet d’importer dans Braze les prévisions d’attrition et les attributs basés sur les comportements et interactions des clients afin de les utiliser dans la segmentation et le ciblage des clients. 

## Prérequis

Pour commencer, un locataire Peak doit héberger l'intégration entre Peak et Braze. Ceci est traditionnellement créé lors de l'onboarding des clients Peak. De plus, une solution d'intelligence décisionnelle est initialement requise car elle génère les résultats pilotés par l'intelligence artificielle qui seront ensuite intégrés dans Braze.

| Exigence | Descriptif |
| ----------- | ----------- |
| Locataire Peak | Une instance de la plateforme Peak, connue sous le nom de locataire, est requise pour héberger et orchestrer l'intégration. |
| Solution d'intelligence décisionnelle | L'intégration entre Peak et Braze est basée sur des résultats pilotés par l'intelligence artificielle et nécessite donc une solution Peak ou de client déployée au sein de votre locataire. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br>Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |

## Intégration

L'intelligence client de la solution Peak utilise un modèle pour prédire une gamme d'attributs prospectifs basés sur les comportements et les interactions des clients. Ces attributs sont stockés dans Peak et peuvent être utilisés pour générer une segmentation prédictive, y compris la probabilité de désabonnement d'un client. La mise à jour de ces attributs prédictifs sera basée sur une cadence configurable (quotidienne ou hebdomadaire).

### Étape 1 : Exécuter le modèle et extraire les clients

L'intégration est déclenchée par l'exécution du modèle d'intelligence artificielle et le recalcul des attributs prédictifs des clients. Ces sorties d'intelligence artificielle sont stockées dans Peak, y compris lorsqu'un attribut est mis à jour avec un nouveau statut ou une nouvelle valeur.

En fonction du moment où les attributs ont été mis à jour, une sélection est effectuée pour collecter tous les clients avec des attributs prédictifs mis à jour depuis la dernière synchronisation entre Peak et Braze.

### Étape 2 : Mettre à jour Braze

Une fois les clients mis à jour et les attributs associés, Peak les enverra à Braze en utilisant le [`/user/track` endpoint]({{site.baseurl}}/api/endpoints/user_data/post_user_track/) et l'en-tête [bulk]({{site.baseurl}}/api/endpoints/user_data/post_user_track/#making-bulk-updates).

À la réception des codes d’état réussi de l'API, Peak enregistrera la synchronisation réussie entre Peak et Braze.

### Étape 3 : Utilisation de cette intégration

Une fois la synchronisation entre Peak et Braze réussie, les utilisateurs mis à jour incluent désormais les nouveaux attributs. Utilisez ces attributs dans les campagnes et les canvas pour cibler les utilisateurs et personnaliser les messages.


