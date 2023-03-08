---
nav_title: Glossaire analytique pour l’e-mail
article_title: Glossaire analytique pour l’e-mail 
page_order: 20
layout: glossary_page
glossary_top_header: "Glossaire analytique pour l’e-mail"
glossary_top_text: "Il s’agit des termes que vous trouverez dans la section d’analyse de votre campagne par e-mail ou de Canvas, après son lancement. Recherchez les indicateurs dont vous avez besoin dans ce glossaire. <br><br> Ce glossaire n’inclut pas nécessairement les indicateurs que vous pouvez voir dans Currents ou d’autres rapports téléchargés en dehors de votre compte Braze."

description: "Ce glossaire inclut les termes que vous trouverez dans la section d’analyse de votre campagne par e-mail ou de Canvas, après son lancement. Ce glossaire n’inclut pas les indicateurs Currents."
channel:
  - e-mail

glossaries:
  - name: "Variation"
    description: Variation d’une campagne, différente telle que définie par le créateur.
    calculation: Total
  - name: "Emailable"
    description: Les utilisateurs qui ont une adresse e-mail enregistrée et qui se sont explicitement abonnés ou ont souscrit.
    calculation: Total
  - name: "% d’audience"
    description: Pourcentage d’utilisateurs ayant reçu une variante particulière.
    calculation: Nombre de destinataires dans la variante / destinataires uniques
  - name: "Destinataires uniques"
    description: Destinataires uniques quotidiens. Nombre d’utilisateurs qui ont reçu un message spécifique dans une journée. Ce chiffre est envoyé par Braze.
    calculation: Total
  - name: "Envoi ou messages envoyés"
    description: Le nombre total de messages envoyés dans une campagne par e-mail. Ce chiffre est envoyé par Braze.
    calculation: Total
  - name: "Livraisons"
    description: Le nombre total de messages (envois) envoyés avec succès et reçus par des parties emailable.
    calculation: Envois - Bounces
  - name: "% de livraisons"
    description: Le nombre total de messages (envois) envoyés avec succès et reçus par des parties emailable.
    calculation: (Envoi - Bounces) / (Envois)
  - name: "Bounces"
    description: Nombre total de messages qui n’ont pas été envoyés ou désignés comme « retournés » ou « non reçus » des services d’envoi utilisés ou non reçus par les utilisateurs emailable visés. Cela peut se produire parce qu’il n’y a pas de jeton de notification push valide, que les adresses e-mail étaient incorrectes ou désactivées, ou que l’utilisateur s’est désabonné une fois la campagne lancée. <br><br> <b>Hard Bounces</b>&#58; Un hard bounce est un e-mail renvoyé à l’expéditeur, car l’adresse du destinataire n’était pas valide. Un hard bounce peut se produire parce que le nom de domaine n’existe pas ou parce que le destinataire est inconnu. Si un e-mail reçoit un hard bounce, nous arrêterons toute demande future à cette adresse e-mail. <br><br><b>Soft Bounces</b>&#58; Un soft bounce est un e-mail qui atteint le serveur de messagerie du destinataire, mais est renvoyé non livré avant qu’il ne soit transmis au destinataire. Un soft bounce peut se produire parce que la boîte de réception du destinataire est pleine, que le serveur était en panne ou que le message était trop volumineux pour la boîte de réception du destinataire. Si un e-mail reçoit un soft bounce, nous réessaierons généralement après une période de 72 heures, mais le nombre de tentatives varie d’un destinataire à l’autre. <br><br> Vous pouvez également suivre les hard bounces et les soft bounces dans le <a href='/docs/user_guide/administrative/app_settings/developer_console/message_activity_log_tab/#message-activity-log-tab'>Journal d’activité de message</a>.  <br><br><i> Pour les clients utilisant SendGrid, les rebonds d’e-mail regroupent les hard bounces, les courriers indésirables et les e-mails envoyés à des adresses non valides. </i>
    calculation: Total
  - name: "% de rebonds ou taux de rebonds"
    description: Pourcentage de messages qui n’ont pas été envoyés ou désignés comme « retournés » ou « non reçus » des services d’envoi utilisés ou non reçus par les utilisateurs emailable visés. Cela peut se produire parce qu’il n’y a pas de jeton de notification push valide, que les adresses e-mail étaient incorrectes ou désactivées, ou que l’utilisateur s’est désabonné une fois la campagne lancée. <br> <i> Pour les clients utilisant SendGrid, les rebonds d’e-mail regroupent les hard bounces, les courriers indésirables (`spam_report_drops`) et les e-mails envoyés à des adresses non valides (`invalid_emails`). </i>
    calculation: Bounces / Envois
  - name: "Spam"
    description: Nombre total d’e-mails livrés marqués comme « spam ». Braze désinscrit automatiquement les utilisateurs qui ont marqué un e-mail comme spam, et ces utilisateurs ne seront pas ciblés par des e-mails futurs.
    calculation: (Marqué comme spam) / (Envois)
  - name: "% de spams ou taux de spams"
    description: Le pourcentage d’e-mails livrés qui ont été marqués ou désignés comme « spam ». Braze désinscrit automatiquement les utilisateurs qui ont marqué un e-mail comme spam, et ces utilisateurs ne seront pas ciblés par des e-mails futurs.
    calculation: (Marqué comme spam) / (Envois)
  - name: "Ouverture unique"
    description: Nombre total d’e-mails livrés ouverts au moins une fois par un utilisateur unique ou automatiquement. Pour l’e-mail, la période de suivi est de 7 jours.
    calculation: (Ouvertures uniques) / (Livraisons)
  - name: "% d’ouvertures uniques ou taux d’ouvertures uniques"
    description: Pourcentage d’e-mails livrés ouverts au moins une fois par un utilisateur unique. Pour l’e-mail, la période de suivi est de 7 jours.
    calculation: (Ouvertures uniques) / (Livraisons)
  - name: "Clics uniques"
    description: Nombre distinct de destinataires ayant cliqué dans un message au moins une fois. Pour l’e-mail, la période de suivi est de 7 jours.
    calculation: Total
  - name: "% de clics uniques ou taux de clics uniques"
    description: Nombre distinct de destinataires ayant cliqué dans un message au moins une fois. Pour l’e-mail, la période de suivi est de 7 jours.
    calculation: Clics / Livraisons uniques
  - name: "Désabonnés"
    description: Nombre de messages entraînant un désabonnement. Les désabonnements se produisent lorsqu’un utilisateur clique sur le lien de désinscription de Braze.
    calculation: Total
  - name: "% de désabonnés ou taux de désabonnés"
    description: Pourcentage de messages livrés qui ont entraîné un désabonnement. Les désabonnements se produisent lorsqu’un utilisateur clique sur le lien de désinscription de Braze.
    calculation: Désinscriptions / Livraisons
  - name: "Revenue"
    description: Le revenu total en dollars de destinataires de campagne dans la <a href='/docs/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/#primary-conversion-event'>fenêtre de conversion principale définie</a>.
    calculation: Total
  - name: "Conversions principales (A) ou événement de conversion primaire"
    description: Le nombre de fois où un événement défini se produit après l’interaction ou la consultation d’un message reçu d’une campagne Braze. Cet événement défini est déterminé par le marketeur lors de la création de la campagne.
    calculation: Total
  - name: "Conversions principales (A) ou événement de conversion primaire"
    description: Le pourcentage de fois où un événement défini se produit après l’interaction ou la consultation d’un message reçu d’une campagne Braze. Cet événement défini est déterminé par le marketeur lors de la création de la campagne.
    calculation: "Conversions principales / Destinataires uniques"
  - name: "Confiance"
    description: Le pourcentage de confiance qu’une certaine variante d’un message fasse mieux que le groupe de contrôle.
  - name: "Ouverture automatique"
    description: Inclut la proportion des « ouvertures » qui sont affectées par la Protection de la confidentialité dans Mail (MPP) d’Apple pour iOS 15. Par exemple, si un utilisateur ouvre un e-mail à l’aide de l’application Mail sur un appareil Apple, cette opération sera enregistrée comme « Ouverture automatique ». Cet indicateur est suivie à compter du 11 novembre 2021 pour SendGrid et du 2 décembre 2021 pour SparkPost.
    calculation: Total
  - name: "Autre ouverture"
    description: Inclut les e-mails qui n’ont pas été identifiés comme « Ouverture automatique ». Par exemple, lorsqu’un utilisateur ouvre un e-mail sur une autre plate-forme (par exemple une application Gmail sur un téléphone, Gmail sur le navigateur de bureau), l’opération sera enregistrée comme « Autre ouverture ». Notez qu’un utilisateur peut également ouvrir un e-mail (l’ouverture est alors comptabilisée comme « Autre ouverture ») avant qu’un comptage « Ouverture automatique » soit enregistré. Si un utilisateur ouvre un e-mail une fois (ou plus) après un événement d’ouverture automatique depuis une boîte de réception de courrier non-Apple, le nombre de fois que l’utilisateur ouvre l’e-mail est comptabilisé dans « Autre ouverture » et une seule fois vers « Ouverture unique ».
    calculation: Total
  - name: "Taux de Click-to-Open"
    description: Le pourcentage d’e-mails uniques ouverts sur lesquels on a cliqué au moins une fois.
    calculation: Clics uniques / Ouvertures uniques

---
