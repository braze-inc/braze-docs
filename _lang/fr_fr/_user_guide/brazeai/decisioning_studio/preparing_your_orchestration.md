---
nav_title: Préparer votre orchestration
article_title: Préparer votre orchestration
page_order: 5
page_type: reference
description: "Cet article de référence explique ce que vous devez préparer avant de configurer l'orchestration pour BrazeAI Decisioning Studio, notamment le choix de votre CEP et la collecte des informations d'identification et des ressources requises."
---

# Préparer votre orchestration

> Cet article de référence explique ce que vous devez préparer avant de configurer l'orchestration pour BrazeAI Decisioning Studio™, notamment le choix de votre plateforme d'engagement client (CEP) et la collecte des informations d'identification et des ressources requises.

## Qu'est-ce que l'orchestration ?

L'orchestration est la connexion entre Decisioning Studio et votre plateforme d'engagement client (CEP). Une fois que votre agent décisionnel détermine l'action optimale pour chaque client, l'orchestration exécute ces décisions en déclenchant des communications personnalisées par le biais de votre CEP.

Pensez-y de la manière suivante :

- **Decisioning Studio** décide *ce qu'* il faut envoyer et *quand* il faut l'envoyer
- **Votre CEP** gère la *manière de* l'envoyer

## Choisir votre CEP

La première étape consiste à déterminer quelle plateforme d'engagement client vous utiliserez avec Decisioning Studio. Votre choix affecte la complexité de la configuration et les fonctionnalités disponibles.

### PEC soutenus

| CEP | Décisions Studio Go | Decisioning Studio Pro | Type d'intégration |
|-----|:---------------------:|:----------------------:|------------------|
| **Braze** | ✓ | ✓ | Intégration de l'API native (recommandée) |
| **Salesforce Marketing Cloud** | ✓ | ✓ | Événements API + Générateur de parcours (Journey Builder) |
| **Klaviyo** | ✓ | ✓ | Événements API + Flux |
| **Autres CEP** | - | ✓ | Personnalisé (fichier de recommandation) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

{% alert tip %}
Si vous utilisez déjà Braze comme CEP, nous vous recommandons d'utiliser l'intégration native de Braze pour une configuration plus fluide.
{% endalert %}

## Ce dont vous avez besoin pour vous préparer

Avant de mettre en place l'orchestration, rassemblez les éléments suivants en fonction de la CEP que vous avez choisie.

{% tabs %}
{% tab Braze %}

| Produit | Description |
|------|-------------|
| **Clé d'API REST** | Une nouvelle clé API avec des autorisations pour les données des utilisateurs, les messages, les campagnes, les Canvas, les segments et les modèles. |
| **URL du tableau de bord de Braze** | L'URL de votre instance Braze (par exemple, `https://dashboard-01.braze.com`). |
| **ID de l'application** | La clé API associée à l'application que vous souhaitez suivre (vous la trouverez dans **Paramètres** > **Paramètres de l'application**). |
| **Nom et adresse d'affichage de l'e-mail** | Les informations sur l'expéditeur à utiliser pour vos campagnes (dans **Paramètres** > **Préférences d'e-mail**). |
| **Modèles de base** | Les modèles de messages que votre agent utilisera pour l'orchestration. Vous créerez des campagnes déclenchées par l'API pour chaque modèle. |
| **ID de l'utilisateur test** | Un ID utilisateur pour tester l'intégration avant le lancement. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

| Produit | Description |
|------|-------------|
| **Informations d'identification du paquet d'applications** | ID du client, secret du client, URI de base d'authentification, URI de base REST et URI de base SOAP à partir d'un package installé avec une intégration API de serveur à serveur. |
| **Autorisations API** | Scopes pour les canaux, les ressources, les automatisations, les parcours, les contacts, les extensions de données et les événements de suivi. |
| **Extensions de données** | Vous aurez besoin d'extensions de données pour les données relatives aux utilisateurs, les données d'engagement et les recommandations. |
| **Modèles d'e-mail** | Les modèles que vous souhaitez que Decisioning Studio utilise, avec les ID de modèle pour chacun d'entre eux. |
| **Accès au générateur de voyage** | Accès pour créer et activer des parcours en plusieurs étapes avec des sources d'entrée d'événements API. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Klaviyo %}

| Produit | Description |
|------|-------------|
| **Clé API privée** | Une nouvelle clé API avec des autorisations d'accès complètes pour les événements, les flux, les listes, les indicateurs, les profils et les modèles. |
| **Modèles d'e-mail** | Les modèles que vous souhaitez que Decisioning Studio utilise. Les modèles doivent être associés à un flux (vous pouvez créer un flux marque substitutive à cette fin). |
| **Informations sur l'expéditeur** | Le nom et l'adresse e-mail de l'expéditeur à utiliser pour vos campagnes. |
| **Accès au flux** | Accès à la création et à l'activation de flux avec déclencheurs d'indicateurs. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% tab Other CEPs %}

{% alert note %}
Les intégrations CEP personnalisées ne sont disponibles qu'avec Decisioning Studio Pro.
{% endalert %}

Si vous utilisez une CEP autre que Braze, SFMC ou Klaviyo, Decisioning Studio Pro peut s'intégrer par le biais d'une approche de fichier de recommandation :

| Produit | Description |
|------|-------------|
| **Capacité d'ingestion de données** | Votre CEP doit pouvoir ingérer des fichiers de recommandations (généralement CSV ou JSON) contenant des décisions personnalisées pour chaque client. |
| **Prise en charge du contenu dynamique** | Vos campagnes doivent permettre de remplir les champs de manière dynamique en fonction des données de recommandation. |
| **Ressources d'ingénierie personnalisées** | Votre équipe devra créer l'intégration pour lire les fichiers de recommandation et déclencher les communications. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% endtab %}
{% endtabs %}

## Planifier vos campagnes

Avant de mettre en place l'orchestration, tenez compte des détails suivants :

### Modèles de base

Un modèle de base est tout modèle de message que votre agent décisionnel pourrait utiliser. Considérez :

- **Combien de modèles ?** Votre agent peut travailler avec un ou plusieurs modèles. S'il y en a plusieurs, l'agent peut personnaliser le modèle que chaque client reçoit.
- **Quels canaux ?** E-mail, push, SMS, ou une combinaison des deux. Chaque canal peut nécessiter des modèles et des campagnes distincts.
- **Quels sont les éléments dynamiques ?** Identifiez les parties de votre message que l'agent personnalisera (lignes d'objet, CTA, offres, timing, etc.). Ceux-ci deviendront des propriétés de déclencheurs API ou des marqueurs substitutifs dynamiques.

### Paramètres de réadmissibilité

Vos campagnes doivent permettre aux utilisateurs de recevoir des messages plusieurs fois :

- Pour les tests, vous voudrez envoyer la même campagne au même utilisateur à plusieurs reprises
- En production, l'agent peut déterminer que la même campagne est optimale pour un utilisateur sur des jours consécutifs

{% alert note %}
Lors de la mise en place de la réadmissibilité pour les tests, les agents de Decisioning Studio sont conçus pour respecter les limites de fréquence et n'enverront pas la même campagne à un utilisateur plus d'une fois par jour en production.
{% endalert %}

### Propriétés du déclencheur API

Pour les intégrations de Braze, prévoyez les dimensions que votre agent optimisera. Ces propriétés deviennent des déclencheurs d'API qui transmettent des valeurs dynamiques à vos campagnes :

| Exemple de dimension | Propriété de déclencheur API |
|-------------------|---------------------|
| Ligne d'objet | {% raw %}`{{api_trigger_properties.${subject_line}}}`{% endraw %} |
| Appel à l'action | {% raw %}`{{api_trigger_properties.${cta_message}}}`{% endraw %} |
| Offre | {% raw %}`{{api_trigger_properties.${offer_id}}}`{% endraw %} |
| Montant de l'escompte | {% raw %}`{{api_trigger_properties.${discount}}}`{% endraw %} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

## Bonnes pratiques

Gardez ces bonnes pratiques à l'esprit lorsque vous vous préparez à l'orchestration :

1. **Commencez simplement.** Commencez par un canal et un ou deux modèles. Vous pourrez l'élargir par la suite, au fur et à mesure que vous apprendrez ce qui fonctionne.
2. **Effectuez un test approfondi.** Avant le lancement, testez votre intégration avec un petit groupe d'utilisateurs pour vérifier que le contenu dynamique s'affiche correctement.
3. **Documentez votre configuration.** Gardez une trace des ID de campagne, des ID de modèle, des clés API et d'autres identifiants. Vous devrez les référencer dans le portail Decisioning Studio.
4. **Coordonnez votre action avec celle de votre équipe.** La configuration de l'orchestration peut impliquer des équipes de marketing, d'ingénierie et de données. Veillez à ce que chacun comprenne son rôle dans le processus.
5. **Prévoyez des données de retour d'information.** L'orchestration ne consiste pas seulement à envoyer des messages, mais aussi à collecter les données d'engagement et de conversion qui permettent à votre agent d'apprendre. Pour plus de détails, voir [Préparer vos sources de données]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/preparing_your_data_sources/).

## Étapes suivantes

Une fois que vous avez rassemblé vos informations d'identification et planifié vos campagnes, vous êtes prêt à implémenter l'orchestration :

- [Décision Studio Go : Mettre en place l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)
- [Decisioning Studio Pro : Mettre en place l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_pro/set_up_orchestration/)
