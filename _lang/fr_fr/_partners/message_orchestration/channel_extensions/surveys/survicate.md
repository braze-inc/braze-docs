---
nav_title: Survicate
article_title: Survicate
description: "Cet article de référence présente le partenariat entre Braze et Survicate, une plateforme de feedback client qui vous aide à collecter, analyser et agir sur les informations clients sur plusieurs canaux et tout au long du parcours client."
alias: /partners/survicate/
page_type: partner
search_tag: Partner

---

# Survicate

![Exemple illustrant à quoi pourrait ressembler une enquête HTML intégrée (première question) dans un e-mail Braze.][2]{: style="float:right;max-width:40%;border:0; margin-left:8px;"}

> [Survicate][1] est une plateforme de feedback client qui vous aide à collecter, analyser et agir sur les informations clients sur plusieurs canaux et tout au long du parcours client.  

_Cette intégration est maintenue par Survicate._

## À propos de l'intégration

Grâce à l'intégration entre Braze et Survicate, vous pouvez intégrer des enquêtes directement dans vos e-mails Braze afin d'augmenter les taux de réponse. Les réponses aux enquêtes se synchronisent automatiquement avec les profils des utilisateurs de Braze sous forme d'attributs personnalisés ou d'événements. Grâce aux informations en temps réel, il est facile de suivre et d'analyser les commentaires parallèlement aux données clients et de créer des suivis ciblés.

## Cas d'utilisation

Braze et Survicate travaillent ensemble pour couvrir un éventail de cas d'utilisation du feedback, vous aidant à collecter des informations exploitables sur les utilisateurs et à améliorer l'expérience client :

- Mesurer la satisfaction des clients (CSAT, Net Promoter Score, CES, etc.)
- Recueillir les commentaires sur les produits
- Réaliser des études d'utilisateurs ou de marketeurs
- Recueillir des informations à des étapes critiques du parcours client.
- Déclenchez des flux de travail personnalisés et automatisez des campagnes de suivi en fonction des commentaires des clients.

## Principales fonctionnalités de l'intégration

L'intégration de Survicate et de Braze offre une synchronisation des données en temps réel, de sorte que les informations les plus récentes des enquêtes Survicate sont immédiatement disponibles dans Braze. En fonction des réponses à l'enquête, vous pouvez utiliser ces données pour prendre des mesures personnalisées en temps voulu.

- **Envoyez les réponses à l'enquête à Braze sous forme d'attributs personnalisés**: Enrichissez les profils utilisateurs de Braze avec des données issues de réponses à des enquêtes.
- **Déclenchez des événements personnalisés dans Braze**: Utilisez les événements basés sur les réponses à l'enquête pour cibler des groupes spécifiques ou lancer des campagnes de suivi.
- **Créez des segments détaillés**: Créez des segments Braze en utilisant les données des enquêtes Survicate pour personnaliser davantage votre action de sensibilisation.

## Conditions préalables

| Condition | Description |
| ----------- | ----------- |
| Compte Survicate | Vous devez disposer d'un compte Survicate pour activer cette intégration. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Intégration

### Étape 1 : Créez votre enquête dans Survicate

1. Dans votre panneau Survicate, sélectionnez **Créer une nouvelle enquête**.
2. Choisissez votre canal de sondage : des**sondages par e-mail, par lien, sur le site Web, dans le produit et dans l'application mobile** sont disponibles. 
3. Concevez votre enquête à partir de zéro, utilisez le créateur d'enquêtes par intelligence artificielle ou choisissez parmi plus de 100 modèles prêts à l'emploi.

![Quatre options pour créer une enquête : partir de zéro, utiliser un modèle, création assistée par l'intelligence artificielle et importation de questions.][4]

### Étape 2 : Identifiez automatiquement les répondants grâce aux e-mails de Braze

1. Une fois que votre enquête est prête, accédez à l'onglet **Configuration.** 
2. Pour *Identifier les répondants avec*, sélectionnez **Braze**. Les réponses sont ainsi automatiquement liées aux profils de vos clients Braze. Il n'est donc pas nécessaire de demander des informations de contact dans votre enquête.

![Braze est sélectionné comme répondant.][5]

### Étape 3 : Connecter l'intégration

1. Ensuite, dans l'**onglet Connecter**, trouvez Braze et sélectionnez **Connecter** pour intégrer. 
2. Insérez la clé API de l'espace de travail de votre compte Braze et l'URL de l'instance Braze.

![Champs permettant de saisir la clé API de l'espace de travail et l'URL de l'instance de Braze.][3]

### Étape 4 : Partagez votre enquête

1. Ensuite, dans l'onglet **Partage**, choisissez l'endroit où vous souhaitez placer votre sondage. Les options comprennent
- **Lien direct**: Copiez le lien pour l'utiliser dans Braze sous forme de bouton ou d'hyperlien.
- **Première question intégrée**: Copiez le code HTML pour intégrer la première question de l'enquête directement dans le corps d'un e-mail de Braze.
- **Lancer une enquête sur votre site web ou dans un produit**: Installez le code de suivi une seule fois et mettez les enquêtes en ligne directement à partir du panneau Survicate.

### Étape 5 : Ajoutez l'enquête à votre campagne d'e-mailing Braze

1. Dans Braze, collez le lien de l'enquête ou le code HTML dans le contenu de votre campagne d'e-mail.
2. Commencez à recueillir des commentaires et à suivre les réponses directement dans Survicate.


[1]: https://survicate.com/integrations/braze-survey/?utm_source=braze&utm_medium=integrations&utm_campaign=helpcenter
[2]:  {% image_buster /assets/img/survicate/survicate_asset_1.png %}
[3]:  {% image_buster /assets/img/survicate/image1.png %}
[4]:  {% image_buster /assets/img/survicate/survicate_asset_3.png %}
[5]:  {% image_buster /assets/img/survicate/survicate_asset_2.png %}
