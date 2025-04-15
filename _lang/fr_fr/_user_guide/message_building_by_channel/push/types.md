---
nav_title: "Types de notifications Push"
article_title: Types de notifications Push
page_order: 1
page_type: glossary
description: "Ce glossaire répertorie les différents types de notifications push que vous pouvez envoyer par le biais de Braze."
channel: push

layout: glossary_page
glossary_top_header: "Types of push notifications"
glossary_top_text: "There are many types of push notifications you can use to interact with your customers. These can be narrowed by channel and used to meet the needs of many different users. You can configure most of these settings in your Push campaigns, but there are notes in the following descriptions that will indicate whether any backend configurations are needed and what those might be."

glossary_tag_name: Channels
glossary_filter_text: "Select any of the following channels to narrow Push Type options."

# category to icon/fa or image mapping
glossary_tags:
  - name: iOS
  - name: Android
  - name: Web

glossaries:
  - name: "Regular Push"
    description: "Le message Push tout-en-un. Celui-ci apparaît sur l’appareil de votre utilisateur avec un son de notification et un message qui glisse ou s’affiche dans une barre ou une pile de notification."
    tags:
      - iOS
      - Android
      - Web
  - name: "Notification push Web"
    description: "Ces messages de notification push apparaissent dans les applications Web ou les navigateurs. Ils exigent toujours l’autorisation du client. Notez que les notifications push sur Web ne fonctionnent pas si l’utilisateur est en navigation privée."
    tags:
      - Web
  - name: "Push Primer Campaigns"
    description: "Push Primer Campaigns (Campagnes de messages in-app) utilisées pour obtenir un signal explicite d’abonnement ou de désabonnement des utilisateurs. À travers l’amorce, vous pouvez éviter d’envoyer des notifications aux utilisateurs susceptibles de désactiver les paramètres de notification push de l’appareil. Pour iOS, les campagnes push sont pertinentes car les notifications push au premier plan (comme les notifications qui réveillent l'appareil) ne sont pas activées tant qu'un utilisateur n'a pas explicitement accepté l'invite push native d'iOS."
    tags:
      - iOS
      - Android
      - Web
  - name: "Contenu push"
    description: "Les Push Stories (Bandes message push) sont des messages immersifs qui amènent votre utilisateur à travers un voyage visuel sous la forme d’un carrousel. Elles sont disponibles uniquement pour les appareils mobiles."
    tags:
      - iOS
      - Android
  - name: "Push with Action Buttons"
    description: "Les notifications push avec des boutons d'action sont des messages qui vous permettent de fournir des options à vos utilisateurs et d'offrir plusieurs appels à l'action."
    tags:
      - iOS
      - Android
      - Web
  - name: "Rich Push Notifications"
    description: "Les Rich Push Notifications (Notifications push enrichies) sont des notifications avec des images immersives et un contenu créatif qui peuvent se développer au-delà d’une simple icône et d’un texte d’invite à l’action."
    tags:
      - iOS
      - Android
  - name: "Silent Push Notification"
    description: "Une Silent Push Notification (Notification push silencieuse) ne réveille pas l’appareil lors du rendu sur l’appareil. La notification sera alors stockée dans la barre de notification de l’appareil."
    tags:
      - iOS
      - Android
  - name: "Provisional Push Notifications pour iOS"
    description: "Introduites par Apple dans iOS 12, l’autorisation provisoire se produit automatiquement à l’installation pour les applications iOS, ce qui permet aux marques d’envoyer des notifications silencieuses sans afficher une invite de notification push aux utilisateurs. Lorsque la notification push provisoire est envoyée et affichée dans la barre de notification de l’appareil, les utilisateurs auront la possibilité d’autoriser ou d’interrompre les notifications push."
    tags:
      - iOS
  - name: "Notifications push HTML"
    description: "Les HTML Push Notifications (Notifications Push HTML) sont des messages push codés en HTML et qui n’utilisent pas les modèles de notification push prédéfinis fournis par Braze. La possibilité de créer des notifications push HTML permet à votre entreprise d’avoir une liberté de création totale et une image de marque cohérente lorsqu’il s’agit de la façon dont vous souhaitez que ces messages push soient affichés."
    tags:
      - Android
  - name: "Notification IDs &amp; Channel IDs"
    description: "Les Notification IDs &amp; Channel IDs (ID de notification et ID de canal) vous permettent de remplacer ou de mettre à jour les notifications push déjà reçues, mais non ouvertes, par l’utilisateur."
    tags:
      - iOS
      - Android
  - name: "Background Push Notifications"
    description: "Les Background Push Notifications (Notifications push en arrière-plan) sont celles non rendues pour l’appareil. Généralement utilisées pour envoyer des paquets d’informations à l’application pour les processus d’arrière-plan et le suivi de désinstallation. Un jeton de notification push activé pour l’arrière-plan est requis pour l’envoi de notification push en arrière-plan."
    tags:
      - iOS
      - Android
      - Web
  - name: "Wearable Push Notifications"
    description: "Les Wearable Push Notifications (Notifications push portables) permettent aux marques d’envoyer des messages directement sur des appareils portables comme Apple Watch."
    tags:
      - iOS

---
