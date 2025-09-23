---
nav_title: Toovio
article_title: Toovio
description: "Cet article de référence présente le partenariat entre Braze et Toovio, une société de données en tant que service, qui vous aide à découvrir vos données exploitables et à utiliser les éléments les plus importants pour obtenir des résultats incrémentaux en fonction d'objectifs prédéfinis."
alias: /partners/toovio/
page_type: partner
search_tag: Partner

---

# Toovio

> [Toovio](https://toovio.com/) est une société de données en tant que service alimentée par l'IA qui vous aide à découvrir vos données exploitables et à utiliser les éléments les plus critiques pour obtenir des résultats incrémentaux en fonction d'objectifs prédéfinis.

_Cette intégration est maintenue par Toovio._

## À propos de l'intégration

Le partenariat entre Braze et Toovio permet un envoi de messages en temps quasi réel, des outils de communication individualisés et l'accès aux outils de mesure de campagne avancés de Toovio.

## Prérequis

| Condition | Descriptif |
| ----------- | ----------- |
| Compte Toovio | Un compte Toovio est nécessaire pour bénéficier de ce partenariat. |
| Clé API REST de Braze | Une clé API Braze REST avec des autorisations `users.track`. <br><br> Celle-ci peut être créée dans le tableau de bord de Braze à partir de **Paramètres** > **Clés API**. |
| Braze Currents | Braze Currents permet aux clients de Braze de transmettre des données d'événements ou de comportement en continu à un partenaire de données de Braze (AWS S3, Google Cloud Storage ou Microsoft Azure Blob Storage) pour un traitement externe à la plateforme Braze. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

L'intégration suivante permet à Toovio de générer des déclencheurs ciblant des clients spécifiques et de communiquer quasiment en temps réel. Les déclencheurs déterminés par Toovio seront transmis à Braze via l'[`/users/track`endpoint Braze]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

### Étape 1 : Définir le partenaire de données

Un emplacement/localisation du flux de données Currents doit être partagé avec Toovio ; cela permet à Toovio d'accéder et de traiter les données d'événements et de comportements des utilisateurs.

### Étape 2 : Implémenter une campagne déclenchée

Créez une [campagne déclenchée par l'API de]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/) Braze en fonction des événements personnalisés que Toovio ciblera. En outre, il convient de définir les attributs et les valeurs de l'utilisateur cible qui déclencheront la campagne.

### Étape 3 : Créez votre compte Toovio

Contactez Toovio à [info@toovio.com](mailto:info@toovio.com?subject=New%20Customer%20Request) avec l'objet "requête nouveau client" pour créer un compte. Toovio travaillera avec les clients pour mettre en place des déclencheurs et des modèles sous-jacents.


