---
nav_title: Worthy
article_title: Worthy
description: "Cet article de référence présente le partenariat entre Braze et Worthy, une plateforme de personnalisation des messages qui vous permet de créer des expériences in-app riches et personnalisées et de les diffuser via Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partenaire

---

# Worthy

L’intégration de [Worthy](https://worthy.ai/) et Braze vous permet de créer facilement des expériences in-app riches et personnalisées à l’aide de l’éditeur glisser-déposer de Worthy et de les diffuser via Braze. De plus, Worthy exécute automatiquement les actions suivantes :

- Créer un serveur de Contenu connecté et une API sécurisée pour votre envoi de messages.
- Construire vos messages in-app avec des analytiques et un suivi des clics qui apparaîtront directement dans Braze.
- Exporter automatiquement du HTML via l’éditeur glisser-déposer de Worthy pour l’utiliser dans des campagnes de messages in-app avec **code personnalisé** dans Braze, avec les connexions API requises et le contenu dynamique que vous configurez.

## Cas d’utilisation

- Expériences de bienvenue personnalisées basées sur les sélections d’onboarding de l’utilisateur
- Expériences in-app pour des événements spéciaux et des promotions
- Collecte de commentaires et notations des clients en fonction du comportement des applications
- Test rapide des idées potentielles des produits d’application
- Avis précieux, actualités et mises à jour communautaires

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte [Worthy](https://worthy.ai/) | Un compte Worthy est nécessaire pour profiter de ce partenariat. |
| SDK Braze | Vous devrez configurer le SDK Braze dans votre application mobile pour envoyer des messages in-app riches. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

### Étape 1 : Créez des envois de messages personnalisés dans Worthy

Accédez à votre application dans le Tableau de bord de Worthy, sélectionnez **Message Creator (Créateur de messages)** et créez un message personnalisé que vous souhaitez utiliser pour engager vos utilisateurs.

### Étape 2 : Créer une campagne Braze

Créez une [campagne de messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) dans Braze et définissez **Message Type (Type de message)** sur **Custom Code (Code personnalisé)**.

### Étape 3 : Copier votre message personnalisé dans Braze

Dans le créateur de message Worthy, cliquez sur **Export (Exporter)** et sélectionnez **Braze** pour exporter votre message personnalisé afin de l’utiliser dans des campagnes Braze. Copiez le contenu exporté dans la zone de texte HTML sous **HTML + Asset Zip (HTML + Zip de l’actif)** dans l’éditeur de campagne Braze.

Et voilà ! Vous pouvez immédiatement tester votre message personnalisé en utilisant l’onglet **Test** dans l’éditeur de campagne Braze. 
