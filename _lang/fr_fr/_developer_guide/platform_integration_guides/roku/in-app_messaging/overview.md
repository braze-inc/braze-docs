---
nav_title: Aperçu
article_title: Aperçu du message in-app pour Roku
platform: Roku
channel: in-app messages
page_order: 0
page_type: reference
description: "Cet article présente une vue d’ensemble de la messagerie in-app Roku, y compris les meilleures pratiques et les cas d’utilisation."

---

# Aperçu des messages in-app

> Les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) vous permettent d'envoyer du contenu à votre utilisateur sans interrompre sa journée avec une notification push. Des messages in-app personnalisés et adaptés améliorent l’expérience utilisateur et aident votre audience à tirer le meilleur parti de votre application. Grâce à un choix de mises en page et d’outils de personnalisation, les messages in-app supposent un engagement inédit de vos utilisateurs.

Consultez nos [études de cas](https://www.braze.com/customers) pour voir des exemples d'envois de messages in-app.

![Trois images de messages in-app potentiels Roku qu’un utilisateur pourrait créer. Ces exemples incluent "fullscreen takeover", "homepage banner", et "corner notifier".]({% image_buster /assets/img/roku/Docs-Imagery.png %})

## Types de messages in-app

Créez un message in-app pour Roku en sélectionnant **Appareils Roku** comme plateforme de messages in-app.

![]({% image_buster /assets/img/roku/1-Platform-Selector.png %})

## Documentation technique

Consultez notre [guide d'intégration]({{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration) pour obtenir des instructions sur l'affichage des messages in-app et l'enregistrement des impressions et de l'analyse des clics.

![Exemple de « bannière de page d’accueil » montrant les différents composants nécessaires pour créer la bannière personnalisée. Les composants répertoriés comprennent le composant de composition du message (affichant le corps, le texte du bouton, l'image, le comportement assigné au bouton (lien profond) et les paires clé-valeur), les détails du backend (audience répertoriée comme "utilisateurs ayant regardé la saison 1", les interactions prévues (le bouton renvoie à l'application, la création de liens profonds désactive le message et l'interruption automatique après 10 secondes), le déclencheur (démarrage de la session) et la paire clé-valeur (template = homepage_banner)).]({% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %})

## Tests et QR

La fonction d’envoi de test n’est pas prise en charge pour les messages in-app Roku. Pour tester un message, lancez la campagne filtrée uniquement par votre ID utilisateur.

