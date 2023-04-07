---
page_order: 0
nav_title: Glossaire d’indicateurs de rapport
article_title: Glossaire d’indicateurs de rapport
layout: glossary_page
glossary_top_header: "Glossaire d’indicateurs de rapport"
glossary_top_text: "Voici des termes que vous trouverez dans vos rapports sur votre compte Braze. Recherchez les métriques dont vous avez besoin ou filtrez par canal. <br>  <br> Ce glossaire n’inclut pas nécessairement les mesures que vous pouvez voir dans Currents ou d’autres rapports téléchargés en dehors de votre compte Braze."

page_type: glossary
description: "Ce glossaire définit les termes que vous trouverez dans vos rapports sur votre compte Braze."
tool: Reports

glossary_tag_name: Canaux
glossary_filter_text: "Sélectionnez Canaux pour affiner le glossaire :"

# canal à icône/fa ou mappage d’image
glossary_tags:
  - name: Cartes de contenu
  - name: E-mail
  - name: Message in-app
  - name: Notification push Web
  - name: Notification push iOS
  - name: Notification push Android
  - name: Webhook
  - name: SMS
  - name: WhatsApp

glossaries:
  - name: Variation
    description: Variation d’une campagne, différente telle que définie par le créateur.
    calculation: Total
    tags:
      - Cartes de contenu
      - E-mail
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
      - Webhook
      - SMS
      - WhatsApp
  - name: Audience
    description: Pourcentage d’utilisateurs ayant reçu un message particulier. Ce chiffre est envoyé par Braze.
    tags:
      - Tous
  - name: Destinataires uniques
    description: Destinataires uniques quotidiens. Nombre d’utilisateurs qui ont reçu un message spécifique dans une journée. Ce chiffre est envoyé par Braze.
    calculation: Total
    tags:
      - Tous
  - name: Impressions totales
    description: Nombre de fois où le message in-app a été visualisé (si un utilisateur voit deux fois un message, il sera comptabilisé deux fois). Ce nombre est une somme du nombre d’événements d’impression que Braze reçoit des SDK.
    calculation: Total
    tags:
      - Message in-app
      - Cartes de contenu
  - name: Impressions uniques
    description: Nombre total d’utilisateurs qui ont reçu et affiché un message in-app ou une carte spécifique en une journée. Pour les messages in-app, les impressions uniques peuvent être incrémentées de nouveau après 24 heures si la rééligibilité est activée et qu’un utilisateur effectue l’action de déclenchement. Inversement, le compteur ne doit pas s’incrémenter la deuxième fois qu’un utilisateur voit une carte de contenu. Ce chiffre est envoyé par Braze.
    calculation: Total
    tags:
      - Message in-app
      - Cartes de contenu
  - name: Envois
    description: Le nombre total de messages envoyés dans une campagne. Ce chiffre est envoyé par Braze. Notez qu’au lancement d’une campagne planifiée, cet indicateur inclura tous les messages envoyés, qu’ils aient été envoyés ou non en raison d’une limitation du taux.
    calculation: Total
    tags:
      - Cartes de contenu
      - E-mail
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
      - Webhook
      - SMS
  - name: Envois à l’opérateur
    description: Cette statistique est la somme des livraisons confirmées, des rejets et des envois pour lesquels la livraison ou le rejet n’a pas été confirmé par l’opérateur. Il y a des cas où les opérateurs ne confirment pas la livraison ou le rejet, car c’est leur politique, ou bien ils n’ont pas pu le faire au moment de l’envoi.
    calculation: Total
    tags:
      - SMS
  - name: Livraisons
    description: Nombre total de demandes de messages acceptées par le serveur d’e-mail destinataire.
    calculation: Total
    tags:
      - Toutes les notifications push
      - E-mail
      - Notification push Web
      - Notification push iOS
      - Notification push Android
  - name: Livraisons confirmées
    description: L’opérateur a confirmé que le SMS a été envoyé au numéro de téléphone cible. En tant que client Braze, les livraisons sont facturées vers votre attribution SMS.
    calculation: Total
    tags:
      - SMS
  - name: Rebonds
    description: Nombre total de messages qui ont échoué. Cela peut se produire parce qu’il n’y a pas de jeton de notification push valide, que les adresses e-mail étaient incorrectes ou désactivées, ou que l’utilisateur s’est désabonné une fois la campagne lancée. <br> <i> Pour les clients utilisant SendGrid, les rebonds d’e-mail regroupent les hard bounces, les courriers indésirables et les e-mails envoyés à des adresses non valides. </i>
    calculation: (Bounces)/(Envois)
    tags:
      - Toutes les notifications push
      - E-mail
      - Notification push Web
      - Notification push iOS
  - name: Rejets
    description: "Le SMS a été rejeté par l’opérateur. Cela peut se produire pour plusieurs raisons, notamment : filtrage du contenu par l’opération, disponibilité de l’appareil destinataire, numéro de téléphone plus en service, etc. En tant que client Braze, les rejets sont facturés vers votre attribution SMS."
    calculation: Total
    tags:
      - SMS
  - name: Échecs de livraison
    description: Le SMS n’a pas pu être envoyé, car les files d’attente étaient pleines (envoi de SMS à un rythme que vos codes courts ou longs ne pouvaient pas suivre).
    calculation: (Envois) - (Envois à l’opérateur)
    tags:
      - SMS
  - name: Spam
    description: "Nombre total d’e-mails livrés marqués comme « spam »."
    calculation: (Marqué comme spam) / (Envois)
    tags:
      - E-mail
  - name: Erreurs
    description: Nombre d’erreurs renvoyées par les événements du webhook (incrémentées pendant le processus d’envoi).
    tags:
      - Webhook
  - name: Nombre total d’ouvertures
    description: Nombre total de messages qui ont été ouverts.
    calculation: (Ouverture)/(Livraisons) (pour e-mail) ; (Ouverture directe)/(Livraisons) (pour la notification push Web) ; (Ouvertures uniques)/(Livraisons) (pour Push iOS, Android, Kindle)
    tags:
      - E-mail
      - Notification push iOS
      - Notification push Android
      - Notification push Web
      - Toutes les notifications push
  - name: Ouverture unique
    description: Nombre total d’e-mails livrés ouverts au moins une fois par un utilisateur unique. Pour l’e-mail, la période de suivi est de 7 jours.
    calculation: (Ouvertures uniques) / (Livraisons)
    tags:
      - E-mail
  - name: Ouvertures directes
    description: Nombre total (et pourcentage) de notifications push directement ouvertes à partir de cette notification push.
    calculation: (Ouvertures directes)/(Livraisons)
    tags:
      - Notification push iOS
      - Notification push Android
  - name: Ouvertures influencées
    description: Nombre total (et pourcentage) d’utilisateurs ayant ouvert l’application après l’envoi de la notification push, sans ouvrir directement la notification push.
    calculation: (Ouvertures influencées)/(Livraisons)
    tags:
      - Notification push iOS
      - Notification push Android
  - name: Nombre total de clics
    description: Nombre total (et pourcentage) d’utilisateurs ayant cliqué sur l’e-mail ou la carte envoyé.
    calculation: (Nombre total de clics)/(Livraisons) (pour e-mail) ou (Total Clics)/(Total Impressions) (pour les cartes de contenu)
    tags:
      - E-mail
      - Cartes de contenu
  - name: Clics uniques
    description: Nombre distinct de destinataires ayant cliqué dans un message au moins une fois. Pour l’e-mail, la période de suivi est de 7 jours. Notez que les clics sur les liens de désinscription fournis par Braze sont comptabilisés comme des clics uniques.
    calculation: (Clics uniques)/(Livraisons) (pour e-mail) ou (Clics uniques)/(Impressions uniques) (pour les cartes de contenu)
    tags:
      - E-mail
      - Cartes de contenu
  - name: Body Clicks
    description: Se produit lorsque quelqu’un clique sur un message In-App modal, slide-up ou plein écran sans boutons.
    calculation: (Body Clicks)/(Impressions)
    tags:
      - Message in-app
  - name: Clics Boutons 1
    description: Nombre total de clics sur le bouton 1 du message.
    calculation: (Boutons 1)/(Impressions)
    tags:
      - Message in-app
  - name: Clics Boutons 2
    description: Nombre total de clics sur le bouton 2 du message.
    calculation: (Bouton 2 clics)/(Impressions)
    tags:
      - Message in-app
  - name: Body Click
    description: Les notifications de Push Story enregistrent un clic sur le corps du message (body click) quand la notification est cliquée. Aucun body click ne sera enregistré quand un message est développé ou lors de clics sur des boutons d’action.
    calculation: (Body Clicks)/(Impressions)
    tags:
      - Notification push iOS
      - Notification push Android
  - name: Désinscriptions
    description: Le nombre de destinataires dont le statut d’abonnement est passé à Désabonné suite à un clic sur l’URL de désinscription de Braze.
    calculation: (Désinscriptions)/(Livraisons)
    tags:
      - E-mail
  - name: Total des revenus
    description: Le revenu total en dollars de destinataires de campagne dans la fenêtre de conversion principale définie. Cet indicateur est disponible uniquement sur les rapports de comparaison de campagne, via le <a href='/docs/user_guide/data_and_analytics/reporting/report_builder/'>Créateur de rapports</a>
    tags:
      - Cartes de contenu
      - E-mail
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
      - Webhook
      - SMS
      - WhatsApp
  - name: Conversions principales (A) ou événement de conversion primaire
    description: Le nombre de fois où un événement défini se produit après l’interaction ou la consultation d’un message reçu d’une campagne Braze. Cet événement défini est déterminé par le marketeur lors de la création de la campagne. Pour les e-mails, la notification push et les webhooks, nous commençons à suivre les conversions après l’envoi initial. Pour les cartes de contenu et les messages in-app, ce compteur commence lorsque les utilisateurs voient une carte de contenu ou un message pour la première fois.
    tags:
      - Cartes de contenu
      - E-mail
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
      - Webhook
      - SMS
      - WhatsApp
  - name: Taux de conversion
    description: Pourcentage d’occurrence d’un événement défini pour tous les destinataires d’un message envoyé. Cet événement défini est déterminé lors de la création de la campagne.
    calculation: (Conversions principales)/(Destinataires uniques)
    tags:
      - Cartes de contenu
      - E-mail
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
      - Webhook
      - SMS
  - name: Conversions (B, C, D)
    description: Autres événements de conversion ajoutés après <b>l’événement de conversion primaire</b>. Le nombre de fois où un événement défini se produit après l’interaction ou la consultation d’un message reçu d’une campagne Braze. Cet événement défini est déterminé par le marketeur lors de la création de la campagne. Pour les e-mails, la notification push et les webhooks, nous commençons à suivre les conversions après l’envoi initial. Pour les cartes de contenu et les messages in-app, ce compteur commence lorsque les utilisateurs voient une carte de contenu ou un message pour la première fois.
    tags:
      - Cartes de contenu
      - E-mail
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
      - Webhook
      - SMS
  - name: Confiance
    description: Le pourcentage de confiance qu’une certaine variante d’un message fasse mieux que le groupe de contrôle.
    tags:
      - Cartes de contenu
      - E-mail
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
      - Webhook
      - SMS
      - WhatsApp
  - name: En attente d’une nouvelle tentative
    description: Nombre de demandes rejetées temporairement par le serveur de réception, mais que le fournisseur de services de courrier électronique essaye quand même de renvoyer. Le fournisseur de services de courrier électronique va réessayer jusqu’à ce qu’un délai soit atteint (généralement 72 heures).
    tags:
      - E-mail
  - name: Total des rejets
    description: Nombre de fois où les cartes de contenu d’une campagne ont été rejetées. Si un utilisateur rejette deux fois un message, il ne sera compté qu’une seule fois.
    calculation: Total
    tags:
      - Cartes de contenu
  - name: Rejets uniques
    description: Nombre d’utilisateurs qui ont rejeté les cartes de contenu d’une campagne. Un utilisateur qui rejette plusieurs fois une carte de contenu d’une campagne constitue un rejet unique.
    calculation: (Rejets uniques)/(Impressions uniques)
    tags:
      - Cartes de contenu
  - name: Clics AMP
    description: Nombre total d’utilisateurs ayant cliqué sur la version AMP de votre e-mail AMP HTML.
    tags:
      - E-mail
  - name: Reçu
    description: Cartes de contenu - Reçu lorsque les utilisateurs voient la carte dans l’application.<br>Notification push - Reçu lorsque les messages sont envoyés du serveur Braze au fournisseur de services de notification push.<br>E-mail - Reçu lorsque les messages sont envoyés du serveur Braze au fournisseur de services d’e-mail.<br>SMS/MMS - « Livré » une fois que le fournisseur SMS reçoit la confirmation de l’opérateur en amont et de l’appareil de l’utilisateur.<br>Message In-App - Reçu au moment de l’affichage en fonction de l’action de déclenchement définie.<br>WhatsApp - Reçu au moment de l’affichage en fonction de l’action de déclenchement définie.
    tags:
      - E-mail
      - Cartes de contenu
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
      - SMS
      - WhatsApp
  - name: Total des revenus directs
    description: Le montant des revenus générés par cette campagne, basé sur l’attribution au dernier clic*. Cet indicateur est disponible uniquement sur les rapports de comparaison de campagne, via le <a href='/docs/user_guide/data_and_analytics/reporting/report_builder/'>Créateur de rapports</a>.<br><br>*L’attribution « Last Click » (au dernier clic) signifie que pour que les revenus soient attribués à une campagne, cette campagne doit&#58; <br> 1. Être la dernière campagne que l’utilisateur a cliquée avant l’achat, et <br> 2. Avoir été cliquée par l’utilisateur moins de 3 jours avant l’achat.
    tags:
      - E-mail
      - Cartes de contenu
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
#  - name: Achats directs uniques
#    Description : Nombre d’utilisateurs qui ont acheté, basé sur l’attribution au dernier clic*. Cet indicateur est disponible uniquement sur les rapports de comparaison de campagne, via le <a href='/docs/user_guide/data_and_analytics/reporting/report_builder/'>Créateur de rapports</a>.<br><br>*L’attribution « Last Click » (au dernier clic) signifie que pour que les revenus soient attribués à une campagne, cette campagne doit&#58; <br> 1. Être la dernière campagne que l’utilisateur a cliquée avant l’achat, et <br> 2. Avoir été cliquée par l’utilisateur moins de 3 jours avant l’achat.
#    tags :
#      - E-mail
#      - Cartes de contenu
#      - Message in-app
#      - Notification push Web
#      - Notification push iOS
#      - Notification push Android
  - name: Total des achats directs
    description: Nombre total d’achats effectués, basé sur l’attribution au dernier clic*. Cet indicateur peut compter plusieurs achats pour un utilisateur. Si, par exemple un utilisateur fait deux achats, le compteur sera incrémenté de deux. Cet indicateur est disponible uniquement sur les rapports de comparaison de campagne, via le <a href='/docs/user_guide/data_and_analytics/reporting/report_builder/'>Créateur de rapports</a>.<br><br>*L’attribution « Last Click » (au dernier clic) signifie que pour que les revenus soient attribués à une campagne, cette campagne doit&#58; <br> 1. Être la dernière campagne que l’utilisateur a cliquée avant l’achat, et <br> 2. Avoir été cliquée par l’utilisateur moins de 3 jours avant l’achat.
    tags:
      - E-mail
      - Cartes de contenu
      - Message in-app
      - Notification push Web
      - Notification push iOS
      - Notification push Android
#  - name: Revenu par destinataire
#    Description : Le chiffre d’affaires direct total divisé par les destinataires uniques. Cet indicateur est disponible uniquement sur les rapports de comparaison de campagne, via le <a href='/docs/user_guide/data_and_analytics/reporting/report_builder/'>Créateur de rapports</a>.
#    calcul : (Revenu direct total)/(Destinataires uniques)
#    tags :
#      - E-mail
#      - Cartes de contenu
#      - Message in-app
#      - Notification push Web
#      - Notification push iOS
#      - Notification push Android
  - name: Choix soumis
    description: Nombre total de choix sélectionnés lorsque l’utilisateur clique sur le bouton Envoyer sur la page de questions d’un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>sondage simple</a>.
    tags:
      - Message in-app
  - name: Bouton de page de confirmation
    description: Le nombre total de clics sur le bouton d’action de la page de confirmation d’un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>sondage simple</a>.
    tags:
      - Message in-app
  - name: Rejets Page de Confirmation
    description: Le nombre total de clics sur le bouton Fermer (x) de la page de confirmation d’un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>sondage simple</a>.
    tags:
      - Message in-app
  - name: Rejets Page de Sondage
    description: Le nombre total de clics sur le bouton Fermer (x) de la page de questions d’un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>sondage simple</a>.
    tags:
      - Message in-app
  - name: Soumissions de sondage
    description: Nombre total de clics sur le bouton Envoyer d’un <a href='/docs/user_guide/message_building_by_channel/in-app_messages/templates/simple_survey/' target='_blank'>sondage simple</a>.
    tags:
      - Message in-app
  - name: Taux de Click-to-Open
    description: Pourcentage d’e-mails ouverts qui ont été consultés. Cet indicateur est disponible uniquement dans le <a href='/docs/user_guide/data_and_analytics/reporting/report_builder/'>Créateur de rapports</a>.
    calculation: (Clics uniques)/(Ouvertures uniques) (pour e-mail)
    tags:    
      - E-mail       
---
