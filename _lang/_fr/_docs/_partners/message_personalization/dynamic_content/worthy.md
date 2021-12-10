---
nav_title: Véritable
article_title: Véritable
description: "Cet article décrit le partenariat entre Braze et Worthy, une plateforme de personnalisation de messages qui vous permet de créer des expériences personnalisées et riches dans l'application et de les transmettre par l'intermédiaire de Braze."
alias: /fr/partners/worthy/
page_type: partenaire
search_tag: Partenaire
---

# Véritable

L'intégration de [digne](https://worthy.ai/) et de Braze vous permet de créer facilement des personnalisés, riche expérience dans l'application en utilisant l'éditeur de glisser-déposer de Worthy et en les livrant à travers Brésil. De plus, Worthy fera automatiquement ce qui suit :

- Créez un serveur de contenu connecté et une API sécurisée pour votre messagerie.
- Construisez vos messages dans l'application avec des outils d'analyse et de suivi des clics qui apparaîtront directement en Brésil.
- Exporter automatiquement le HTML via l'éditeur de glisser-déposer de Worthy pour l'utiliser dans les campagnes de messages de **Code Personnalisé** dans l'application au Brésil, avec les connexions API requises et le contenu dynamique que vous configurez.

## Cas d'utilisation

- Expériences d'accueil personnalisées basées sur les sélections d'intégration des utilisateurs
- Expériences dans l'application pour les événements spéciaux et les promotions
- Collecter les commentaires et évaluations des clients en fonction du comportement de l'application
- Tester rapidement les idées potentielles de produits d'application
- Notifications, actualités et mises à jour de la communauté

## Pré-requis

| Exigences                          | Libellé                                                                                                                |
| ---------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| Compte [digne](https://worthy.ai/) | Un compte utile est requis pour profiter de ce partenariat.                                                            |
| SDK Braze                          | Vous devrez configurer le Braze SDK dans votre application mobile pour envoyer des messages riches dans l'application. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4}

## Intégration

### Étape 1 : Créer une messagerie personnalisée en digne

Accédez à votre application dans le tableau de bord digne de ce nom, sélectionnez le **Créateur de messages**, et créez un message personnalisé que vous souhaitez utiliser pour engager vos utilisateurs.

### Étape 2 : Créer une campagne de Braze

Créez une campagne de message [dans l'application]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/create/) dans Braze et réglez le **Type de message** sur **Code personnalisé**.

### Étape 3 : Copiez votre message personnalisé dans Braze

Dans le créateur de messages dignes, cliquez sur **Exporter** et sélectionnez **Braze** pour exporter votre message personnalisé à utiliser dans les campagnes de Braze. Copiez le contenu exporté dans la zone de texte HTML sous **HTML + Asset Zip** dans l'éditeur de campagne Braze.

Voilà! Vous pouvez immédiatement tester votre message personnalisé à l'aide de l'onglet **Test** dans l'éditeur de campagne Braze. 
