---
nav_title: "Types de notifications push"
article_title: Types de notifications push
page_order: 1
page_type: glossary
description: "Ce glossaire répertorie les différents types de notifications push que vous pouvez utiliser avec Braze."
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
  - name: "Poussée régulière"
    description: "Le message global de Push. Ceux-ci apparaissent sur l'appareil de votre utilisateur avec un son de notification et un message qui glisse ou apparaît dans une barre ou une pile de notification."
    tags:
      - iOS
      - Android
      - Web
  - name: "Web Push"
    description: "Ces messages-appels apparaissent dans les applications web ou les navigateurs. Ils ont toujours besoin d'autorisations pour atteindre le client. Notez que la fonction Web Push ne fonctionne pas si l'utilisateur utilise un navigateur caché."
    tags:
      - Web
  - name: "Campagnes d'amorçage"
    description: "Campagnes d'envoi de messages in-app utilisées pour obtenir un signal explicite de push opt-in ou opt-out de la part des utilisateurs. Grâce à l'amorce, vous pouvez éviter d'envoyer des notifications aux utilisateurs qui sont susceptibles de désactiver le push via les paramètres de l'appareil. Pour iOS, les campagnes push sont pertinentes car les notifications push au premier plan (telles que les notifications qui réveillent l'appareil) ne sont pas activées tant que l'utilisateur n'a pas explicitement opté pour l'invite push native d'iOS."
    tags:
      - iOS
      - Android
      - Web
  - name: "Contenus push"
    description: "Les contenus push sont des messages immersifs qui emmènent votre utilisateur à travers un voyage visuel sous la forme d'un carrousel. Celles-ci sont disponibles pour les appareils mobiles uniquement."
    tags:
      - iOS
      - Android
  - name: "Poussez avec les boutons d'action push"
    description: "Les boutons d'action push sont des messages qui vous permettent d'offrir des options à vos utilisateurs et de proposer plusieurs appels à l'action."
    tags:
      - iOS
      - Android
      - Web
  - name: "Notifications push riches"
    description: "Les notifications push riches sont des notifications avec des images immersives et un contenu créatif qui peuvent s'étendre au-delà d'une simple icône et d'un texte d'appel à l'action."
    tags:
      - iOS
      - Android
  - name: "Notifications push provisoires pour iOS"
    description: "Introduite par Apple dans iOS 12, l'autorisation provisoire se produit automatiquement à l'installation pour les apps iOS, ce qui permet aux marques d'envoyer des notifications silencieuses sans afficher d'invite push aux utilisateurs. Lorsque le push silencieux est envoyé et affiché dans le bac de notification de l'appareil, les utilisateurs auront la possibilité d'autoriser ou d'interrompre les notifications push."
    tags:
      - iOS
  - name: "Notifications push HTML"
    description: "Les notifications push HTML sont des messages push codés en dur en HTML et qui n'utilisent pas les modèles de push prédéfinis fournis par Braze. La possibilité de créer des notifications push HTML permet à votre entreprise de bénéficier d'une liberté de création totale et d'une image de marque cohérente en ce qui concerne l'aspect de ces messages push."
    tags:
      - Android
  - name: "ID de notification et ID de canal"
    description: "Les ID de notification et les ID de canal vous permettent de remplacer ou de mettre à jour les notifications push déjà reçues, mais non ouvertes, par l'utilisateur."
    tags:
      - iOS
      - Android
  - name: "Notifications push en arrière-plan ou silencieuses"
    description: "Les notifications push qui ne sont pas rendues sur l'appareil. Généralement utilisé pour envoyer des paquets d'informations à l'application pour les processus d'arrière-plan et le suivi de la désinstallation. Un jeton de push activé en arrière-plan est nécessaire pour qu'un push en arrière-plan ou silencieux soit envoyé."
    tags:
      - iOS
      - Android
      - Web
  - name: "Notifications push à porter sur soi"
    description: "Ces notifications push permettent aux marques d'envoyer des messages directement aux appareils wearables comme l'Apple Watch."
    tags:
      - iOS

---
