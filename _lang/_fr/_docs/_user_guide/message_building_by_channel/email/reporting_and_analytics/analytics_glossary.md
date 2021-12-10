---
nav_title: Glossaire de l'email Analytics
article_title: Glossaire de l'email Analytics
page_order: 20
layout: glossary_page
glossary_top_header: "Glossaire de l'email Analytics"
glossary_top_text: "Ce sont des termes que vous trouverez dans la section analytique de votre campagne de courriel ou de Canvas, après le lancement. Recherchez les mesures dont vous avez besoin ci-dessous. <br>  <br> Ce glossaire n'inclut pas nécessairement des métriques que vous pourriez voir dans des courants ou dans d'autres rapports téléchargés en dehors de votre compte Braze."
description: "Ce glossaire comprend les termes que vous trouverez dans la section analytique de votre campagne de courriel ou de Canvas, après le lancement. Ce glossaire n'inclut pas les métriques de courants."
channel:
  - Email
glossaries:
  - 
    name: Variation
    description: Variation d'une campagne, différente de celle définie par le créateur.
    calculation: Compter
  - 
    name: Emailable
    description: Les utilisateurs qui ont une adresse e-mail enregistrée et qui ont explicitement choisi ou abonné.
    calculation: Compter
  - 
    name: "% d'audience"
    description: Pourcentage d'utilisateurs ayant reçu une variante particulière.
    calculation: Nombre de destinataires dans la variante / Destinataires uniques
  - 
    name: Destinataires uniques
    description: Destinataires quotidiens uniques. Le nombre d'utilisateurs qui ont reçu un message particulier dans une journée. Ce numéro est reçu du Brésil.
    calculation: Compter
  - 
    name: Envois ou messages envoyés
    description: Le nombre total de messages envoyés dans une campagne de courriel. Ce numéro est reçu du Brésil.
    calculation: Compter
  - 
    name: "Livraisons"
    description: Le nombre total de messages envoyés avec succès et reçus par les parties par courriel.
    calculation: Envois - Bounces
  - 
    name: "Livraisons %"
    description: Le nombre total de messages envoyés avec succès et reçus par les parties par courriel.
    calculation: (Envois - Bounces) / (Sends)
  - 
    name: Bounces
    description: 'Le nombre total de messages qui ont été envoyés sans succès ou désignés comme « retournés » ou « non reçus » des services d''envoi utilisés ou non reçus par les utilisateurs désirés. Cela peut se produire parce qu''il n''y a pas de jeton de push valide, les adresses e-mail sont incorrectes ou désactivées, ou l''utilisateur s''est désabonné après le lancement de la campagne. <br><br> <b>Hard Bounces</b>&#58 ; Un rebond dur est un message e-mail qui a été retourné à l''expéditeur parce que l''adresse du destinataire est invalide. Un rebond dur peut se produire parce que le nom de domaine n''existe pas ou parce que le destinataire est inconnu. Si un email a reçu un rebond dur, nous arrêterons toute demande future à cette adresse e-mail. <br><br><b>Bounces Soft</b>&#58 ; Un "soft bounce" est un message d''e-mail qui va aussi loin que le serveur de messagerie du destinataire mais est rebondi non distribué avant qu''il ne soit envoyé au destinataire. Un rebond souple peut se produire parce que la boîte de réception du destinataire est pleine, le serveur était en panne, ou le message était trop grand pour la boîte de réception du destinataire. Si un e-mail a reçu un rebond en douceur, nous allons généralement réessayer dans un délai de 72 heures. mais le nombre de tentatives de réessai varie d''un récepteur à l''autre. <br><br> Vous pouvez également suivre les bounces durs et durs dans le <a href=''/docs/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/#message-activity-log-tab''>Journal d''activité des messages</a>. <br><br><i> Un e-mail bounce pour les clients utilisant Sendgrid consiste en des bounces durs, du spam et des e-mails envoyés à des adresses invalides. </i>'
    calculation: Compter
  - 
    name: "Bounces % ou Bounce Rate"
    description: Le pourcentage de messages qui ont été envoyés ou désignés comme « retournés » ou « non reçus » de la part des services d'envoi utilisés ou non reçus par les utilisateurs désirés. Cela peut se produire parce qu'il n'y a pas de jeton de push valide, les adresses e-mail sont incorrectes ou désactivées, ou l'utilisateur s'est désabonné après le lancement de la campagne. <br> <i> Un email bounce pour les clients utilisant Sendgrid consiste en des bounces durs, du spam (`spam_report_drops`) et des emails envoyés à des adresses invalides (`invalid_emails`). </i>
    calculation: Bounces / Envoie
  - 
    name: Spam
    description: Le nombre total d'e-mails envoyés qui ont été marqués comme "spam". Braze désabonne automatiquement les utilisateurs qui ont marqué un e-mail comme spam, et ces utilisateurs ne seront pas ciblés par de futurs e-mails.
    calculation: (Marqué comme Spam) / (Sends)
  - 
    name: "% Spam ou Spam Rate"
    description: Le pourcentage d'e-mails envoyés qui ont été marqués ou autrement désignés comme « spam ». Braze désabonne automatiquement les utilisateurs qui ont marqué un e-mail comme spam, et ces utilisateurs ne seront pas ciblés par de futurs e-mails.
    calculation: (Marqué comme Spam) / (Sends)
  - 
    name: Ouvertures uniques
    description: Le nombre total d'e-mails livrés qui ont été ouverts par un seul utilisateur au moins une fois. Ce suivi est effectué sur une période de 7 jours pour l'Email.
    calculation: (Ouverts uniques) / (Livraisons)
  - 
    name: "Ouverture unique % ou Taux d'ouverture unique"
    description: Le pourcentage d'e-mails livrés qui ont été ouverts par un seul utilisateur au moins une fois. Ce suivi est effectué sur une période de 7 jours pour l'Email.
    calculation: (Ouverts uniques) / (Livraisons)
  - 
    name: Clics uniques
    description: Nombre de destinataires différents qui ont cliqué dans un message au moins une fois. Ce suivi est effectué sur une période de 7 jours pour l'Email.
    calculation: Compter
  - 
    name: "Clics uniques % ou Taux de clics"
    description: Nombre de destinataires différents qui ont cliqué dans un message au moins une fois. Ce suivi est effectué sur une période de 7 jours pour l'Email.
    calculation: Clics uniques / Livraisons
  - 
    name: Désabonnés ou désabonnés
    description: Nombre de messages aboutissant à une désinscription. Les désinscriptions se produisent lorsqu'un utilisateur clique sur le lien de désinscription de Braze.
    calculation: Compter
  - 
    name: "Unsubscribers % ou Unsub Rate"
    description: Pourcentage de messages envoyés, ce qui a entraîné une désinscription. Les désinscriptions se produisent lorsqu'un utilisateur clique sur le lien de désinscription de Braze.
    calculation: Désabonnements/Livraisons
  - 
    name: Revenus
    description: 'Le revenu total en dollars des bénéficiaires de la campagne dans la fenêtre de conversion <a href=''/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#primary-conversion-event''>principale</a> définie.'
    calculation: Compter
  - 
    name: Conversions Principales (A) ou Événement de Conversion Primaire
    description: Le nombre de fois où un événement défini s'est produit après avoir interagi ou vu un message reçu d'une campagne de Braze. Cet événement défini est déterminé par le marketeur lors de la construction de la campagne.
    calculation: Compter
  - 
    name: Conversions Principales (A) ou Événement de Conversion Primaire
    description: Le pourcentage de fois qu'un événement défini s'est produit après avoir interagi ou vu un message reçu d'une campagne de Braze. Cet événement défini est déterminé par le marketeur lors de la construction de la campagne.
    calculation: Conversions primaires / Destinataires uniques
  - 
    name: Confiance
    description: Le pourcentage de confiance qu'une certaine variante d'un message surpasse le groupe de contrôle.
  - 
    name: Ouverture de la machine
    description: Inclut les e-mails qui sont ouverts sans engagement utilisateur par les appareils Apple avec <a href='/docs/user_guide/message_building_by_channel/email/mpp/'>Mail Privacy Protection</a> activé. <br> Cette métrique est tracée à partir du 11 novembre 2021 pour Sendgrid et le 2 décembre 2021 pour Sparkpost.
    calculation: Compter
  - 
    name: Autres Ouvertures
    description: Inclut les courriels qui n'ont pas été identifiés comme "Machine Opens", comme quand un utilisateur ouvre un courriel.
    calculation: Compter
---

