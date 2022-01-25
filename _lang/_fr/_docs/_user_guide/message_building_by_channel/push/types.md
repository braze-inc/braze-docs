---
nav_title: "Types de notifications push"
article_title: Types de notifications push
page_order: 1
page_type: glossary
description: "Ce glossaire répertorie les différents types de Notifications Push que vous pouvez utiliser Braze pour envoyer."
channel: Pousser
layout: glossary_page
glossary_top_header: "Types de notifications push"
glossary_top_text: "Il existe de nombreux types de notifications push que vous pouvez utiliser pour interagir avec vos clients. Ils peuvent être rétrécis par canal et utilisés pour répondre aux besoins de plusieurs utilisateurs. Vous pouvez configurer la plupart de ces paramètres dans vos campagnes push, mais il y a des notes dans les descriptions ci-dessous qui indiquent si des configurations d'arrière-plan sont nécessaires et ce qu'elles pourraient être."
glossary_tag_name: Canaux
glossary_filter_text: "Sélectionnez n'importe quel canal ci-dessous pour affiner les options de type poussé."
#category to icon/fa or image mapping
glossary_tags:
  - 
    name: iOS
  - 
    name: Android
  - 
    name: Web
glossaries:
  - 
    name: "Push normal"
    description: "Le message Push tout à fait complet. Celles-ci apparaissent sur l'appareil de votre utilisateur avec un son de notification et un message qui se glisse dans une barre de notification ou dans une pile."
    tags:
      - iOS
      - Android
      - Web
  - 
    name: "Push Web"
    description: "Ces messages push apparaissent dans les applications Web ou les navigateurs. Ils doivent toujours être autorisés à rejoindre le client. Notez que Web Push ne fonctionne pas si l'utilisateur utilise un navigateur caché."
    tags:
      - Web
  - 
    name: "Pousser les campagnes primaires"
    description: "Campagnes de messages intégrés utilisées pour obtenir des utilisateurs un signal explicite d'opt-in ou d'opt-out. Grâce à l'astérisque, vous pouvez éviter d'envoyer des notifications aux utilisateurs qui sont susceptibles de désactiver push via les paramètres de l'appareil. Pour iOS, les campagnes de push sont pertinentes en tant que notifications push de premier plan (i.e. les notifications de réveil de l'appareil) ne sont pas activées tant qu'un utilisateur n'opte pas explicitement dans l'invite push native d'iOS."
    tags:
      - iOS
      - Android
      - Web
  - 
    name: "Envoyer des histoires"
    description: "Les Histoires Push sont des messages immersifs qui transmettent à votre utilisateur un voyage visuel sous la forme d’un carrousel. Ceux-ci ne sont disponibles que pour les appareils mobiles."
    tags:
      - iOS
      - Android
  - 
    name: "Appuyer avec les boutons d'action"
    description: "Les boutons Push avec Action sont des messages qui vous permettent de fournir des options à vos utilisateurs et de proposer plusieurs appels à l'action."
    tags:
      - iOS
      - Android
      - Web
  - 
    name: "Notifications Rich Push"
    description: "Les notifications Rich Push sont des notifications avec des images immersives et du contenu créatif qui peuvent s'étendre au-delà d'une simple icône et appeler au texte d'action."
    tags:
      - iOS
      - Android
  - 
    name: "Notification Push silencieuse"
    description: "Une notification push qui ne réveille pas l'appareil lors de l'affichage sur l'appareil. À la place, la notification sera stockée dans la zone de notification de l'appareil."
    tags:
      - iOS
      - Android
  - 
    name: "Notifications push provisoires pour iOS"
    description: "Introduit par Apple dans iOS 12, l'autorisation provisoire se produit automatiquement à l'installation des applications iOS, permettant aux marques d'envoyer des notifications silencieuses sans afficher une invite push aux utilisateurs. Lorsque le push silencieux est envoyé et visualisé dans la barre de notification de l'appareil, les utilisateurs auront la possibilité d'autoriser ou d'arrêter les notifications push."
    tags:
      - iOS
  - 
    name: "Notifications Push HTML"
    description: "Les notifications Push HTML sont des messages push qui sont codés en HTML et n'utilisent pas les modèles de push prédéfinis que Braze fournit. Avoir la possibilité de créer des notifications push HTML permet à votre entreprise d'avoir une totale liberté créative et une image de marque cohérente quand il s'agit de la façon dont vous voulez que ces messages push apparaissent."
    tags:
      - Android
  - 
    name: "IDs de notification & ID de canal"
    description: "Les ID de notification et les ID de canal vous permettent de remplacer ou de mettre à jour les notifications push déjà reçues, mais pas ouvertes, par l'utilisateur."
    tags:
      - iOS
      - Android
  - 
    name: "Notifications Push en arrière-plan"
    description: "Notifications push qui ne sont pas affichées pour l'appareil. Habituellement utilisé pour envoyer des paquets d'informations à l'application pour les processus en arrière-plan et le suivi de la désinstallation. Un jeton de push en arrière-plan est requis pour l'envoi d'un push en arrière-plan."
    tags:
      - iOS
      - Android
      - Web
  - 
    name: "Notifications Push portables"
    description: "Ces notifications push permettent aux marques d’envoyer des messages directement à des appareils portables comme l’Apple Watch."
    tags:
      - iOS
---

