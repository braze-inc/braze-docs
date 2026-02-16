---
nav_title: Connecter les sources de données
article_title: Connecter les sources de données
page_order: 1
description: "Découvrez comment BrazeAI Decisioning Studio Go se connecte aux données de vos clients via votre plateforme d'engagement client."
---

# Connecter les sources de données

> BrazeAI Decisioning Studio™ Go se connecte aux données de vos clients par l'intermédiaire de votre plateforme d'engagement client (CEP). Cet article explique quelles données sont utilisées et comment fonctionne la connexion.

## Comment Go accède aux données des clients

Contrairement à Decisioning Studio Pro, qui prend en charge les intégrations de données directes avec diverses sources, Decisioning Studio Go accède aux données clients par l'intermédiaire de votre CEP. Cela signifie que :

- Les **données d'audience** sont tirées directement des segments ou des listes définis dans votre CEP (Braze, Salesforce Marketing Cloud ou Klaviyo) et ne peuvent inclure que certains attributs prédéfinis (pas de données 1P).
- Les **données d'engagement** (ouvertures, clics, envois) sont capturées par le biais de requêtes automatisées ou d'intégrations natives avec votre CEP.
- **Aucune configuration supplémentaire du pipeline de données n'** est nécessaire au-delà de ce que vous configurez dans votre CEP.

## Modèles d'intégration pris en charge

Decisioning Studio Go prend en charge les CEP suivantes pour l'accès aux données :

| CEP | Source d'audience | Données d’engagement |
|-----|-----------------|-----------------|
| **Braze** | Segments | Exportation de Braze Currents |
| **Salesforce Marketing Cloud** | Extensions de données | Automatisation des requêtes SQL |
| **Klaviyo** | Segments | Intégration de l'API native |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

## Données requises par la CEP

{% tabs %}
{% tab Braze %}

### Exigences en matière de données Braze

Pour les intégrations Braze, Decisioning Studio Go nécessite :

1. **Braze Currents**: Vous devez avoir activé et configuré Braze Currents pour exporter des données d'engagement vers Decisioning Studio Go. L'agent peut ainsi tirer des enseignements des réponses des clients.

2. **Accès au segment**: La clé API que vous créez doit disposer d'autorisations permettant d'accéder aux segments qui définissent votre audience cible.

3. **Données relatives au profil utilisateur**: Tous les attributs du profil utilisateur ou les attributs personnalisés que vous souhaitez que l'agent prenne en compte doivent être accessibles via l'API de Braze.

{% alert important %}
Assurez-vous que votre exportation Braze Currents inclut les données de toutes les campagnes avec lesquelles vous souhaitez effectuer une comparaison (y compris les campagnes BAU).
{% endalert %}

{% endtab %}
{% tab Salesforce Marketing Cloud %}

### Exigences en matière de données du SFMC

Pour les intégrations à Salesforce Marketing Cloud, Decisioning Studio Go requiert :

1. **Extensions de données**: Votre audience doit être définie dans une extension de données à laquelle Decisioning Studio Go peut accéder. Utilisez le SubscriberKey comme identifiant principal de l'utilisateur.
2. **Suivi de l'accès aux événements**: Tant que le paquet d'applications installées prend en charge la configuration automatisée de bout en bout, aucune configuration supplémentaire n'est nécessaire. 

Les extensions de données et les requêtes SQL sont configurées dans le cadre de la [configuration de l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/).

{% endtab %}
{% tab Klaviyo %}

### Exigences relatives aux données de Klaviyo

Pour les intégrations Klaviyo, Decisioning Studio Go requiert :

1. **Accès au segment**: Votre audience doit être définie comme un segment Klaviyo auquel la clé API peut accéder.
2. **Données du profil**: La clé API doit avoir un accès complet aux profils pour lire les attributs personnalisés.
3. **Accès aux indicateurs**: La clé API doit disposer d'un accès complet aux indicateurs et aux événements pour capturer les données d'engagement.

{% endtab %}
{% endtabs %}

## Bonnes pratiques

- **Maintenez les données à jour**: Veillez à ce que vos segments d'audience et vos données personnalisées soient mis à jour régulièrement (au minimum, quotidiennement) afin que l'agent travaille avec des informations actualisées.
- **Incluez les attributs pertinents**: Réfléchissez aux caractéristiques des clients susceptibles d'influer sur la pertinence des messages. Les données démographiques, l'historique de l'engagement, le comportement d'achat et l'étape du cycle de vie sont autant de signaux précieux.

## Étapes suivantes

Maintenant que vous comprenez comment Go se connecte aux données, passez à la configuration de votre intégration CEP :

- [Mettre en place l'orchestration]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/decisioning_studio_go/set_up_orchestration/)

