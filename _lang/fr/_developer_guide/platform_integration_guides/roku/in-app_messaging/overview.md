---
nav_title: Aperçu
article_title: Aperçu du message In-App pour Roku
platform: Roku
channel: messages In-App
page_order: 0
page_type: reference
description: "Cet article présente une vue d’ensemble de la messagerie in-app Roku, y compris les meilleures pratiques et les cas d’utilisation."

---

# Messages in-app

Les [messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/) vous aident à obtenir du contenu à votre utilisateur sans interrompre votre journée avec une notification push. Des messages in-app personnalisés et adaptés améliorent l’expérience utilisateur et aident votre audience à tirer le meilleur parti de votre application. Grâce à un choix de mises en page et d’outils de personnalisation, les messages In-App supposent un engagement inédit de vos utilisateurs.

Pour voir des exemples de messages in-app, consultez nos [études de cas][6].

![Trois images de messages in-app potentiels Roku qu’un utilisateur pourrait créer. Ces exemples incluent « prise de contrôle en plein écran », « bannière de page d’accueil » et « notificateur d’angle ».][3]

## Types de messages in-app

Créez un message in-app pour Roku en sélectionnant **Appareils Roku** comme plateforme de messages in-app.

![][4]

## Documentation technique

Visitez notre [guide d’intégration][5] pour obtenir des instructions sur l’affichage des messages in-app et la journalisation des impressions et des clics.

![Exemple de « bannière de page d’accueil » montrant les différents composants nécessaires pour créer la bannière personnalisée. Les composants répertoriés incluent le composant de composition du message (affichant le corps, le texte du bouton, l’image, le comportement du bouton attribué (lien profond) et les paires clé-valeur), les détails du backend (audience répertoriée comme « utilisateurs ayant regardé la saison 1 », les interactions prévues (liens profonds de bouton vers l’application, la fermeture du message rejette le message et le rejet automatique après 10 secondes), le déclencheur (démarrage de la session) et la paire clé-valeur (modèle = homepage_banner)).][2]

## Tests et QR

La fonction d’envoi de test n’est pas prise en charge pour les messages in-app Roku. Pour tester un message, lancez la campagne filtrée uniquement par votre ID utilisateur.

[1]: {% image_buster /assets/img/roku/Roku-In-App-Messages-Flow.png %}
[2]: {% image_buster /assets/img/roku/Roku-In-App-Messages-Example.png %}
[3]: {% image_buster /assets/img/roku/Docs-Imagery.png %}
[4]: {% image_buster /assets/img/roku/1-Platform-Selector.png %}
[5]: {{ site.baseurl }}/developer_guide/platform_integration_guides/roku/in-app_messaging/integration
[6]: https://www.braze.com/customers
