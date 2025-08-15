---
nav_title: Worthy
article_title: Worthy
description: "Cet article de référence présente le partenariat entre Braze et Worthy, une plateforme de personnalisation des messages qui vous permet de créer des expériences in-app riches et personnalisées et de les diffuser via Braze."
alias: /partners/worthy/
page_type: partner
search_tag: Partner

---

# Worthy

> L'intégration de [Worthy](https://worthy.ai/) et Braze vous permet de créer facilement des expériences sur-app personnalisées et riches en utilisant l'éditeur par glisser-déposer de Worthy et de les diffuser via Braze. En outre, Worthy effectuera automatiquement les opérations suivantes :

_Cette intégration est maintenue par Worthy._

## À propos de l'intégration

- Créez un serveur de contenu connecté et une API sécurisée pour votre envoi de messages.
- Construisez vos messages in-app en vous basant sur le résultat d’analyses et un suivi des clics qui apparaîtront directement dans Braze.
- Exportez automatiquement du HTML via l'éditeur par glisser-déposer de Worthy pour l'utiliser dans des campagnes de messages in-app **personnalisés** dans Braze, avec les connexions API requises et le contenu dynamique que vous configurez.

## Cas d'utilisation

- Expériences d'accueil personnalisées basées sur les sélections d'onboarding des utilisateurs.
- Expériences sur l'application pour les événements spéciaux et les promotions.
- Recueillir les commentaires et les évaluations des clients en fonction du comportement de l'app.
- Tester rapidement des idées de produits d'application potentiels
- Des avis riches, des nouvelles et des mises à jour de la communauté

## Conditions préalables

| Condition | Description |
| --- | --- |
| Compte [Worthy](https://worthy.ai/) | Un compte Worthy est nécessaire pour bénéficier de ce partenariat. |
| Braze SDK | Vous devrez configurer le SDK de Braze dans votre application mobile pour envoyer des messages in-app enrichis. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Intégration

### Étape 1 : Créer des envois de messages personnalisés dans Worthy

Naviguez vers votre application dans le tableau de bord Worthy, sélectionnez le **créateur de messages** et créez un message personnalisé que vous souhaitez utiliser pour engager vos utilisateurs.

### Étape 2 : Créer une campagne Braze

Créez une [campagne de messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/traditional/create/) dans Braze et définissez le **type de message** sur **Code personnalisé**.

### Étape 3 : Copiez votre message personnalisé dans Braze

Dans le créateur du message, cliquez sur **Exporter** et sélectionnez **Braze** pour exporter votre message personnalisé afin de l'utiliser dans des campagnes de communication. Copiez le contenu exporté dans la zone de texte HTML sous **HTML + fichier zip des ressources** dans l'éditeur de campagne de Braze.

C'est tout ! Vous pouvez immédiatement tester votre message personnalisé à l'aide de l'onglet **Test** de l'éditeur de campagne de Braze. 

