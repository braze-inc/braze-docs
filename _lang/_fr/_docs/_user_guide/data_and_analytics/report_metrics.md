---
page_order: 0
nav_title: Glossaire des indicateurs
article_title: Glossaire des indicateurs
layout: glossary_page
glossary_top_header: "Glossaire des indicateurs"
glossary_top_text: "Ce sont des termes que vous trouverez dans vos rapports dans votre compte Braze. Recherchez les métriques dont vous avez besoin ou filtrez par canal. <br>  <br> Ce glossaire n'inclut pas nécessairement des métriques que vous pourriez voir dans des courants ou d'autres rapports téléchargés en dehors de votre compte Braze."
page_type: glossary
description: "Ce glossaire définit les termes que vous trouverez dans vos rapports dans votre compte Braze."
tool: Rapports
glossary_tag_name: Canaux
glossary_filter_text: "Sélectionnez les canaux ci-dessous pour affiner le glossaire :"
#channel to icon/fa or image mapping
glossary_tags:
  - 
    name: Cartes de contenu
  - 
    name: Courriel
  - 
    name: Message In-App
  - 
    name: Flux d'actualité
  - 
    name: Push Web
  - 
    name: Push iOS
  - 
    name: Push Android
  - 
    name: Webhook
  - 
    name: SMS
glossaries:
  - 
    name: Variation
    description: Variation d'une campagne, différente de celle définie par le créateur.
    calculation: Compter
    tags:
      - Cartes de contenu
      - Courriel
      - Message In-App
      - Push Web
      - Push iOS
      - Push Android
      - Webhook
      - SMS
  - 
    name: Audience
    description: Pourcentage d'utilisateurs ayant reçu un message particulier. Ce numéro est reçu du Brésil.
    tags:
      - Tous
  - 
    name: Destinataires uniques
    description: Destinataires quotidiens uniques. Le nombre d'utilisateurs qui ont reçu un message particulier dans une journée. Ce numéro est reçu du Brésil.
    calculation: Compter
    tags:
      - Tous
  - 
    name: Impressions totales
    description: Le nombre de fois où le message ou la carte dans l'application a été consulté (si un utilisateur est affiché un message deux fois, il sera compté deux fois). Ce nombre est une somme du nombre d'événements de l'impression que Braze reçoit des SDK.
    calculation: Compter
    tags:
      - Message In-App
      - Flux d'actualité
      - Cartes de contenu
  - 
    name: Impressions uniques
    description: Le nombre total d'utilisateurs qui ont reçu et visionné un message ou une carte dans l'application en une journée. Pour les messages intégrés à l'application, les impressions uniques peuvent être incrémentées à nouveau après 24 heures si la rééligibilité est activée et qu'un utilisateur effectue l'action de déclenchement. Inversement, le nombre ne doit pas incrémenter la deuxième fois qu'un utilisateur voit une fiche de contenu. Ce numéro est reçu du Brésil.
    calculation: Compter
    tags:
      - Message In-App
      - Flux d'actualité
      - Cartes de contenu
  - 
    name: Envoie
    description: Le nombre total de messages envoyés dans une campagne. Ce numéro est reçu du Brésil.
    calculation: Compter
    tags:
      - Cartes de contenu
      - Courriel
      - Message In-App
      - Push Web
      - Push iOS
      - Push Android
      - Webhook
      - SMS
  - 
    name: Envoie à l'opérateur
    description: Cette statistique est la somme des livraisons confirmées, des rejets et des envois lorsque la livraison ou le rejet n'a pas été confirmée par le transporteur. Il y a des cas où les transporteurs ne fournissent pas de livraison ou de confirmation rejetée, car certains transporteurs ne fournissent pas cette confirmation ou n'ont pas pu le faire au moment de l'envoi.
    calculation: Compter
    tags:
      - SMS
  - 
    name: Livraisons
    description: Le nombre total de demandes de messages acceptées par le serveur de messagerie récepteur.
    calculation: Compter
    tags:
      - Tous les Push
      - Courriel
      - Push Web
      - Push iOS
      - Push Android
  - 
    name: Livraisons confirmées
    description: L'opérateur a confirmé que le SMS a été envoyé au numéro de téléphone cible. En tant que client de Braze, les livraisons sont facturées pour votre allocation SMS.
    calculation: Compter
    tags:
      - SMS
  - 
    name: Bounces
    description: Le nombre total de messages qui ont échoué. Cela peut se produire parce qu'il n'y a pas de jeton de push valide, les adresses e-mail sont incorrectes ou désactivées, ou l'utilisateur s'est désabonné après le lancement de la campagne. <br> <i> Un email bounce pour les clients utilisant Sendgrid consiste en bounces durs, spam et e-mails envoyés à des adresses invalides. </i>
    calculation: (Bounces) / (Sends)
    tags:
      - Tous les Push
      - Courriel
      - Push Web
      - Push iOS
  - 
    name: Refus
    description: Le SMS a été rejeté par l'opérateur. Cela peut se produire pour plusieurs raisons, y compris le filtrage du contenu de l'opérateur, disponibilité de l'appareil de destination, le numéro de téléphone n'est plus en service, etc. En tant que client de Braze, les rejets sont facturés pour votre allocation de SMS.
    calculation: Compter
    tags:
      - SMS
  - 
    name: Échec de livraison
    description: Le SMS n'a pas pu être envoyé en raison d'un débordement de file d'attente (l'envoi de SMS à un taux supérieur à celui que vos codes longs ou courts peuvent gérer).
    calculation: (Envoyés) - (Envoyé au transporteur)
    tags:
      - SMS
  - 
    name: Spam
    description: Le nombre total d'e-mails envoyés qui ont été marqués comme "spam".
    calculation: (Marqué comme Spam) / (Sends)
    tags:
      - Courriel
  - 
    name: Erreurs
    description: Le nombre d'erreurs retournées par les événements du webhook (incrémenté pendant le processus d'envoi).
    tags:
      - Webhook
  - 
    name: Ouvertures totales
    description: Le nombre total de messages qui ont été ouverts.
    calculation: (Ouvrirs) / (Livraisons) (pour Email); (Ouvertures directes) / (Livreries) (pour Push Web); (Ouvertures uniques) / (Livraisons) (pour Push iOS, Android, Kindle)
    tags:
      - Courriel
      - Push iOS
      - Push Android
      - Push Web
      - Tous les Push
  - 
    name: Ouvertures uniques
    description: Le nombre total d'e-mails livrés qui ont été ouverts par un seul utilisateur au moins une fois. Ce suivi est effectué sur une période de 7 jours pour l'Email.
    calculation: (Ouverts uniques) / (Livraisons)
    tags:
      - Courriel
  - 
    name: Ouvertures directes
    description: Le nombre total (et le pourcentage) des notifications push qui ont été directement ouvertes à partir de cette push.
    calculation: (Ouvertures directes) / (Livraisons)
    tags:
      - Push iOS
      - Push Android
  - 
    name: Ouvertures influencées
    description: Le nombre total (et pourcentage) des utilisateurs qui ont ouvert l'application après l'envoi de la notification push, sans ouvrir directement le push.
    calculation: (Ouvertures influentes) / (Livraisons)
    tags:
      - Push iOS
      - Push Android
  - 
    name: Nombre total de clics
    description: Le nombre total (et pourcentage) des utilisateurs qui ont cliqué dans l'e-mail ou la carte livrée.
    calculation: (Total des clics) / (Livraisons) (pour E-mail) ou (Total des clics) / (Total des impressions) (pour les cartes de contenu)
    tags:
      - Courriel
      - Flux d'actualité
      - Cartes de contenu
  - 
    name: Clics uniques
    description: Nombre de destinataires différents qui ont cliqué dans un message au moins une fois. Ce suivi est effectué sur une période de 7 jours pour l'Email. Notez que les clics sur les liens de désinscription fournis par Brésil sont comptés comme des clics uniques.
    calculation: (Clics uniques) / (Livraisons) (pour Email) ou (Clics uniques) / (Impressions uniques) (pour Cartes de Contenu)
    tags:
      - Courriel
      - Flux d'actualité
      - Cartes de contenu
  - 
    name: Clics sur le corps
    description: S'active lorsque quelqu'un clique sur un message de glissement vers le haut, modal ou plein écran dans l'application qui n'a pas de boutons.
    calculation: (Corps Clics) / (Impressions)
    tags:
      - Message In-App
  - 
    name: Bouton 1 Clics
    description: Nombre total de clics sur le bouton 1 du message.
    calculation: (Bouton 1 clics) / (Impressions)
    tags:
      - Message In-App
  - 
    name: Bouton 2 clics
    description: Nombre total de clics sur le bouton 2 du message.
    calculation: (Bouton 2 clics) / (Impressions)
    tags:
      - Message In-App
  - 
    name: Clique sur le corps
    description: Les notifications de Push Story enregistrent un corps de clic lorsque la notification est cliquée. Il ne sera pas enregistré quand un message est développé, ou pour des clics sur le bouton d'action.
    calculation: (Corps Clics) / (Impressions)
    tags:
      - Push iOS
      - Push Android
  - 
    name: Se désabonner
    description: Le nombre de destinataires dont le statut d'abonnement est passé à celui désabonné suite au clic sur Braze a fourni l'URL de désinscription.
    calculation: (Désabonnements) / (Livraisons)
    tags:
      - Courriel
  - 
    name: Revenus
    description: Le revenu total en dollars provenant des bénéficiaires de la campagne dans la fenêtre de conversion principale définie.
    tags:
      - Cartes de contenu
      - Courriel
      - Message In-App
      - Push Web
      - Push iOS
      - Push Android
      - Webhook
      - SMS
  - 
    name: Conversions Principales (A) ou Événement de Conversion Primaire
    description: Le nombre de fois où un événement défini s'est produit après avoir interagi ou vu un message reçu d'une campagne de Braze. Cet événement défini est déterminé par le marketeur lors de la construction de la campagne. Pour les courriels, Push et Webhooks, nous commençons à suivre les conversions après l'envoi initial. Pour les cartes de contenu et les messages dans l'application, ce nombre commence quand ils affichent une carte de contenu ou un message pour la première fois.
    tags:
      - Cartes de contenu
      - Courriel
      - Message In-App
      - Push Web
      - Push iOS
      - Push Android
      - Webhook
      - SMS
  - 
    name: Taux de conversion
    description: Le pourcentage de fois qu'un événement défini s'est produit par rapport à tous les destinataires d'un message envoyé. Cet événement défini est déterminé lorsque vous construisez la campagne.
    calculation: (Conversions Primaires) / (Destinataires Uniques)
    tags:
      - Cartes de contenu
      - Courriel
      - Message In-App
      - Push Web
      - Push iOS
      - Push Android
      - Webhook
      - SMS
  - 
    name: Conversions (B, C, D)
    description: Événements de conversion supplémentaires ajoutés après le <b>Événement de conversion primaire</b>. Le nombre de fois où un événement défini s'est produit après avoir interagi ou vu un message reçu d'une campagne de Braze. Cet événement défini est déterminé par le marketeur lors de la construction de la campagne. Pour les courriels, Push et Webhooks, nous commençons à suivre les conversions après l'envoi initial. Pour les cartes de contenu et les messages dans l'application, ce nombre commence quand ils affichent une carte de contenu ou un message pour la première fois.
    tags:
      - Cartes de contenu
      - Courriel
      - Message In-App
      - Push Web
      - Push iOS
      - Push Android
      - Webhook
      - SMS
  - 
    name: Confiance
    description: Le pourcentage de confiance qu'une certaine variante d'un message surpasse le groupe de contrôle.
    tags:
      - Cartes de contenu
      - Courriel
      - Message In-App
      - Push Web
      - Push iOS
      - Push Android
      - Webhook
      - SMS
  - 
    name: En attente d'une nouvelle tentative
    description: Le nombre de requêtes qui ont été temporairement rejetées par le serveur récepteur, mais qui ont quand même tenté de les renvoyer par ESP. L'ESP recommencera la livraison jusqu'à ce qu'une période de délai soit atteinte (généralement après 72 heures).
    tags:
      - Courriel
  - 
    name: Nombre total de licenciements
    description: Le nombre de fois où les cartes de contenu d'une campagne ont été rejetées. Si un utilisateur rejette un message deux fois, il ne sera compté qu'une seule fois.
    calculation: Compter
    tags:
      - Cartes de contenu
  - 
    name: Remises en cause uniques
    description: Le nombre d'utilisateurs qui ont rejeté les cartes de contenu d'une campagne. Un utilisateur qui rejette une carte de contenu d'une campagne plusieurs fois représente un rejet unique.
    calculation: (Rejetons uniques) / (Impressions uniques)
    tags:
      - Cartes de contenu
  - 
    name: Clics AMP
    description: Le nombre total d'utilisateurs qui ont cliqué dans la version AMP de votre courriel AMP HTML.
    tags:
      - Courriel
  - 
    name: Reçu
    description: Cartes de contenu - Reçu lorsque les utilisateurs affichent la carte dans l'application.<br>Push - Reçu lorsque des messages sont envoyés du serveur Braze au fournisseur de push.<br>Email - Reçu lorsque des messages sont envoyés du serveur de Braze au fournisseur de services de messagerie.<br>SMS/MMS - "Livré" une fois que le fournisseur de SMS a reçu la confirmation de l'opérateur en amont et de l'appareil de destination.<br>Message In-App - Reçu au moment de l'affichage en fonction de l'action de déclenchement définie.
    tags:
      - Courriel
      - Cartes de contenu
      - Message In-App
      - Push Web
      - Push iOS
      - Push Android
      - SMS
  - 
    #- name: Total Direct Revenue
    #description: The amount of revenue generated by this campaign, based on last-click attribution*. This metric is only available on Campaign Comparison Reports, via the <a href='/docs/user_guide/data_and_analytics/your_reports/report_builder/'>Report Builder</a>.<br><br>*Last-click attribution means that in order for revenue to be attributed to a campaign, that campaign must&#58; <br> 1. Be the last campaign the user clicked prior to purchasing, and <br> 2. Be clicked by the user less than 3 days prior to purchasing.
    #tags:
    #- Email
    #- Content Cards
    #- In-App Message
    #- Web Push
    #- iOS Push
    #- Android Push
    #- name: Unique Direct Purchases
    #description: The number of users who purchased, based on last-click attribution*. This metric is only available on Campaign Comparison Reports, via the <a href='/docs/user_guide/data_and_analytics/your_reports/report_builder/'>Report Builder</a>.<br><br>*Last-click attribution means that in order for revenue to be attributed to a campaign, that campaign must&#58; <br> 1. Be the last campaign the user clicked prior to purchasing, and <br> 2. Be clicked by the user less than 3 days prior to purchasing.
    #tags:
    #- Email
    #- Content Cards
    #- In-App Message
    #- Web Push
    #- iOS Push
    #- Android Push
    #- name: Total Direct Purchases
    #description: The total number of purchases made, based on last-click attribution*. This metric counts multiple purchases from a single user, for example if one user makes two purchases, the count will increment by two. This metric is only available on Campaign Comparison Reports, via the <a href='/docs/user_guide/data_and_analytics/your_reports/report_builder/'>Report Builder</a>.<br><br>*Last-click attribution means that in order for revenue to be attributed to a campaign, that campaign must&#58; <br> 1. Be the last campaign the user clicked prior to purchasing, and <br> 2. Be clicked by the user less than 3 days prior to purchasing.
    #tags:
    #- Email
    #- Content Cards
    #- In-App Message
    #- Web Push
    #- iOS Push
    #- Android Push
    #- name: Revenue per Recipient
    #description: The total direct revenue divided by unique recipients. This metric is only available on Campaign Comparison Reports, via the <a href='/docs/user_guide/data_and_analytics/your_reports/report_builder/'>Report Builder</a>.
    #calculation: (Total Direct Revenue) / (Unique Recipients)
    #tags:
    #- Email
    #- Content Cards
    #- In-App Message
    #- Web Push
    #- iOS Push
    #- Android Push
    name: Choix envoyés
    description: Nombre total de choix sélectionnés lorsque l'utilisateur clique sur le bouton Soumettre sur la page de question de l'enquête d'un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>Sondage simple</a>.
    tags:
      - Message In-App
  - 
    name: Bouton de la page de confirmation
    description: Total des clics sur le bouton d'appel à l'action sur la page de confirmation d'un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>sondage simple</a>.
    tags:
      - Message In-App
  - 
    name: Révocation de la page de confirmation
    description: Total des clics sur le bouton fermer (x) sur la page de confirmation d'un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>sondage simple</a>.
    tags:
      - Message In-App
  - 
    name: Révocation de la page du sondage
    description: Total des clics sur le bouton fermer (x) sur la page de question de l'enquête d'un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>Sondage simple</a>.
    tags:
      - Message In-App
  - 
    name: Soumissions d'Enquête
    description: Total des clics sur le bouton Soumettre d'un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>Sondage simple</a>.
    tags:
      - Message In-App
  - 
    name: Taux de clics pour ouvrir
    description: Le pourcentage d'e-mails ouverts qui ont été cliqués. Cette métrique n'est disponible que dans le <a href='/docs/user_guide/data_and_analytics/your_reports/report_builder/'>Constructeur de rapport</a>.
    calculation: (Clics uniques) / (Ouvertures uniques) (pour E-mail)
    tags:
      - Courriel
---

