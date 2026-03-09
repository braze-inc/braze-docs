---
nav_title: Préparation de votre orchestration
article_title: Préparation de votre orchestration
page_order: 3
page_type: reference
description: "Cet article de référence explique ce que vous devez préparer avant de configurer l'orchestration pour BrazeAI Decisioning Studio, notamment le choix de votre CEP et la collecte des informations d'identification et des ressources nécessaires."
---

# Préparation de votre orchestration

> Cet article de référence explique ce que vous devez préparer avant de configurer l'orchestration pour BrazeAI Decisioning Studio™, notamment le choix de votre plateforme d'engagement client (CEP) et la collecte des informations d'identification et des ressources nécessaires.

## Qu'est-ce que l'orchestration ?

L'orchestration est la connexion entre Decisioning Studio et votre plateforme d'engagement client (CEP). Une fois que votre agent décisionnel a déterminé l'action optimale pour chaque client, l'orchestration met en œuvre ces décisions en déclenchant des communications personnalisées via votre CEP.

Considérez cela de la manière suivante :

- **Decisioning Studio** détermine *le contenu* à envoyer et *le moment opportun* pour l'envoi.
- **Votre CEP** gère *la manière* de l'envoyer.

## Choisir votre CEP

La première étape consiste à déterminer quelle plateforme d'engagement client vous utiliserez avec Decisioning Studio. Votre choix influe sur la complexité de la configuration et les fonctionnalités disponibles.

### CEP pris en charge

| CEP | Studio de prise de décision Go | Studio de prise de décision Pro | Type d’intégration |
|-----|:---------------------:|:----------------------:|------------------|
| **Braze** | ✓ | ✓ | Intégration de l'API native (recommandée) |
| **Salesforce Marketing Cloud** | ✓ | ✓ | Événements API + Générateur de parcours |
| **Klaviyo** | ✓ | ✓ | Événements API + Flux |
| **Autres CEP** | — | ✓ | Personnalisé (fichier de recommandations) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert tip %}
Si vous utilisez déjà Braze comme CEP, nous vous recommandons d'utiliser l'intégration native Braze pour une expérience de configuration optimale.
{% endalert %}

## Ce dont vous aurez besoin pour vous préparer

Avant de configurer l'orchestration, veuillez rassembler les éléments suivants en fonction du CEP que vous avez choisi.

{% tabs %}
{% tab Braze %}

| Produit | Description |
|------|-------------|
| **Clé d'API REST** | Une nouvelle clé API avec des autorisations pour les données utilisateur, les messages, les campagnes, Canvas, les segments et les modèles. |
| **URL du tableau de bord de Braze** | L'URL de votre instance Braze (par exemple, `https://dashboard-01.braze.com`). |
| **Identifiant de l'application** | La clé API associée à l'application que vous souhaitez suivre (disponible dans **Paramètres** > **Paramètres de l'application**). |
| **Nom d'affichage et adresse e-mail** | Les informations relatives à l'expéditeur à utiliser pour vos campagnes (disponibles dans **Paramètres** > **Préférences e-mail**). |
| **Modèles de base** | Les modèles de message que votre agent utilisera pour l'orchestration. Vous créerez des campagnes déclenchées par API pour chaque modèle. |
| **ID utilisateur test** | Un ID pour tester l'intégration avant le lancement. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Produit | Description |
|------|-------------|
| **Informations d'identification du package d'application** | ID client, clé secrète client, URI de base d'authentification, URI de base REST et URI de base SOAP provenant d'un package installé avec intégration API serveur à serveur. |
| **Autorisations API** | Portées pour les canaux, les ressources, les automatisations, les parcours, les contacts, les extensions de données et les événements de suivi. |
| **Extensions de données** | Vous aurez besoin d'extensions de données pour les données sur les utilisateurs abonnés, les données d'engagement et les recommandations. |
| **Modèles d'e-mail** | Les modèles que vous souhaitez que Decisioning Studio utilise, avec les ID de modèle pour chacun d'entre eux. |
| **Accès au générateur de parcours** | Accès pour créer et activer des parcours en plusieurs étapes avec des sources d'événements API. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Produit | Description |
|------|-------------|
| **Clé API privée** | Une nouvelle clé API avec des autorisations d'accès complètes pour les événements, les flux, les listes, les indicateurs, les profils et les modèles. |
| **Modèles d'e-mail** | Les modèles que vous souhaitez que Decisioning Studio utilise. Les modèles doivent être associés à un flux (vous pouvez créer un flux marque substitutive à cette fin). |
| **Informations sur l'expéditeur** | Le nom et l'adresse e-mail de l'expéditeur à utiliser pour vos campagnes. |
| **Accès au flux** | Accès pour créer et activer des flux avec des déclencheurs d’indicateurs. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

{% alert note %}
Les intégrations CEP personnalisées sont uniquement disponibles avec Decisioning Studio Pro.
{% endalert %}

Si vous utilisez un CEP autre que Braze, SFMC ou Klaviyo, Decisioning Studio Pro peut réaliser l'intégration via une approche par fichier de recommandations :

| Produit | Description |
|------|-------------|
| **Capacité d'ingestion de données** | Votre CEP doit être capable d'ingérer des fichiers de recommandations (généralement au format CSV ou JSON) contenant des décisions personnalisées pour chaque client. |
| **Prise en charge du contenu dynamique** | Vos campagnes doivent prendre en charge le remplissage dynamique des champs en fonction des données de recommandation. |
| **Ressources d'ingénierie personnalisées** | Votre équipe devra créer l'intégration nécessaire pour lire les fichiers de recommandations et activer les déclencheurs de communications. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planification de vos campagnes

Avant de configurer l'orchestration, veuillez prendre en considération les détails suivants :

### Modèles de base

Un modèle de base est un modèle de message que votre agent décisionnaire pourrait utiliser. Veuillez considérer :

- **Combien de modèles ?** Votre agent peut utiliser un ou plusieurs modèles. Dans le cas où il y a plusieurs modèles, l'agent peut effectuer la personnalisation du modèle que chaque client reçoit.
- **Quels canaux ?** E-mail, notification push, SMS ou une combinaison de ces moyens. Chaque canal peut nécessiter des modèles et des campagnes distincts.
- **Quels éléments dynamiques ?** Veuillez identifier les éléments de votre message que l'agent effectuera pour le personnaliser (ligne d'objet, CTA, offres, timing, etc.). Ces éléments deviendront des propriétés de déclencheur API ou des marques substitutives dynamiques.

### Paramètres de rééligibilité

Vos campagnes doivent permettre aux utilisateurs de recevoir des messages à plusieurs reprises :

- Pour effectuer des tests, il est recommandé d'envoyer la même campagne à plusieurs reprises au même utilisateur.
- En production, l'agent peut déterminer qu'une même campagne est optimale pour un utilisateur pendant plusieurs jours consécutifs.

{% alert note %}
Lors de la configuration de la rééligibilité pour les tests, les agents de Decisioning Studio sont conçus pour respecter les limites de fréquence et n'enverront pas la même campagne à un utilisateur plus d'une fois par jour en production.
{% endalert %}

### Propriétés du déclencheur API

Pour les intégrations Braze, veuillez déterminer les aspects que votre agent optimisera. Ces éléments deviennent des propriétés de déclencheur API qui transmettent des valeurs dynamiques à vos campagnes :

| Exemple de dimension | Propriété de déclencheur de l'API |
|-------------------|---------------------|
| Ligne d'objet | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Appel à l'action | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Offre | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Montant de la remise | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Bonnes pratiques

Veuillez garder à l'esprit ces bonnes pratiques lorsque vous vous préparez à l'orchestration :

1. **Commencez par des choses simples.** Commencez par un canal et un ou deux modèles. Vous pourrez vous développer ultérieurement, à mesure que vous découvrirez ce qui fonctionne.
2. **Veuillez effectuer des tests approfondis.** Avant le lancement, veuillez tester votre intégration avec un petit groupe d'utilisateurs afin de vérifier que le contenu dynamique s'affiche correctement.
3. **Veuillez documenter votre configuration.** Veuillez conserver une trace des ID de campagne, des ID de modèle, des clés API et des autres identifiants. Veuillez vous référer à ces informations dans le portail Decisioning Studio.
4. **Coordonnez-vous avec votre équipe.** La configuration de l'orchestration peut impliquer les équipes marketing, ingénierie et données. Veuillez vous assurer que chaque personne comprend son rôle dans le processus.
5. **Prévoyez des données de rétroaction.** L'orchestration ne consiste pas seulement à envoyer des messages, mais également à collecter les données d'engagement et de conversion qui aident votre agent à apprendre. Veuillez consulter [la section Préparation de vos sources de données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/getting_started/preparing_your_data_sources/) pour plus de détails.

## Étapes suivantes

Une fois que vous avez rassemblé vos informations d'identification et planifié vos campagnes, vous êtes prêt à configurer l'orchestration :

- [Studio de prise de décision Go : Configurer l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Studio Pro de prise de décision : Configurer l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)

