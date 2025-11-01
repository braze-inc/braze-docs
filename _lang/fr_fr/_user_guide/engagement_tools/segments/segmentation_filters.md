---
page_order: 2
nav_title: Filtres de segmentation
article_title: Filtres de segmentation
layout: glossary_page
glossary_top_header: "Segmentation Filters"
glossary_top_text: The Braze SDK provides you with a powerful arsenal of filters to segment and target your users based off of specific features and attributes. You can search or narrow these filters by filter category.<br><br>To learn about the different custom attribute data types you can use to segment users, view <a href="/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types">Custom attribute data types</a>.

page_type: glossary
tool: Segments
description: "Ce glossaire répertorie les filtres disponibles pour segmenter et cibler vos utilisateurs."
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Adhésion par segmentation ou CSV
  - name: Attributs personnalisés
  - name: Événements personnalisés
  - name: Sessions
  - name: Reciblage
  - name: "Comportement en matière d'abonnement aux chaînes"
  - name: "Comportement d'achat"
  - name: Caractéristiques démographiques
  - name: Application
  - name: Désinstaller
  - name: Appareils
  - name: Emplacements/localisation
  - name: Membres de la cohorte
  - name: "Attribution d'installation"
  - name: Intelligence et prédictions
  - name: Activité sociale
  - name: Autres filtres

glossaries:
  - name: Adhésion à un segment
    description: "Vous permet de filtrer en fonction de l'appartenance à un segment partout où les filtres sont utilisés (segments, campagnes et autres) et de cibler plusieurs segments différents au sein d'une même campagne. <br><br>Notez que les segments utilisant déjà ce filtre ne peuvent pas être inclus ou imbriqués dans d'autres segments, car cela pourrait créer un cycle dans lequel le segment A inclurait le segment B, qui essaierait à son tour d'inclure le segment A. Dans ce cas, la segmentation ne cesserait de se référer à elle-même, ce qui rendrait impossible le calcul de la personne qui en fait partie. En outre, l'imbrication de segments de ce type ajoute de la complexité et peut ralentir les choses. Au lieu de cela, recréez le segment que vous essayez d'inclure en utilisant les mêmes filtres."
    tags:
      - Segment or CSV membership
  - name: Braze Segment Extensions
    description: "Après avoir créé une extension de segment dans le tableau de bord de Braze, vous pouvez choisir d'inclure/exclure ces extensions dans votre segment."
    tags:
      - Segment or CSV membership
  - name: Mise à jour/importation à partir de CSV
    description: Segmente vos utilisateurs en fonction de leur participation ou non à un téléchargement CSV.
    tags:
      - Segment or CSV membership
  - name: Attributs personnalisés
    description: "Détermine si un utilisateur correspond ou non à une valeur d'attribut personnalisé enregistrée. <br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Custom attributes
  - name: Créé à
    description: "Segmentation des utilisateurs en fonction de la date de création de leur profil utilisateur. Si un utilisateur a été ajouté par CSV ou API, ce filtre reflète la date à laquelle il a été ajouté. Si l'utilisateur n'est pas ajouté par CSV ou API et que sa première session est suivie par le SDK, ce filtre reflète la date de cette première session."
    tags:
      - Other Filters
  - name: Attributs personnalisés imbriqués
    description: "Attributs qui sont les propriétés des attributs personnalisés.<br><br>Lorsque vous filtrez un attribut personnalisé temporel imbriqué, vous pouvez choisir de filtrer en fonction du \"Jour de l'année\" ou de l'\"Heure\". L'option \"Jour de l'année\" ne vérifiera que le mois et le jour à des fins de comparaison. \"Time\" comparera l'horodatage complet, y compris l'année."
    tags:
      - Custom attributes
  - name: "Jour de l'événement récurrent"
    description: "Ce filtre prend en compte le mois et le jour de l'attribut personnalisé dont le type de données est \"date\", mais ne prend pas en compte l'année. Ce filtre est utile pour les événements annuels.<br><br>Fuseau horaire :<br>Ce filtre s'ajuste à tous les fuseaux horaires dans lesquels se trouve l'utilisateur, à condition que le message soit envoyé en utilisant l'option de planification de l'heure locale ; sinon, ce filtre utilise le fuseau horaire de votre entreprise."
    tags:
      - Custom attributes
  - name: Événement personnalisé
    description: "Détermine si un utilisateur a effectué un événement spécialement enregistré.<br><br> Exemple :<br>Activité terminée avec la propriété activty_name.<br><br>Fuseau horaire :<br>UTC - Jour calendaire = 1 jour calendaire correspond à 24-48 heures d'historique de l'utilisateur."
    tags:
      - Custom events
  - name: "L'événement personnalisé First Did"
    description: "Détermine le moment le plus précoce où un utilisateur a effectué un événement spécialement enregistré. (période de 24 heures) <br><br>Exemple :<br> Premier abandon de panier Il y a moins d'un jour<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Custom events
  - name: Dernier événement personnalisé 
    description: "Détermine l'heure la plus tardive à laquelle un utilisateur a effectué un événement spécialement enregistré. Ce filtre prend en charge les décimales, telles que 0,25 heure. (période de 24 heures) <br><br>Exemple :<br> Dernier panier abandonné Il y a moins de 1 jour<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Custom events
  - name: X événement personnalisé dans Y jours
    description: "Détermine si un utilisateur a effectué un événement spécialement enregistré entre 0 et 50 fois au cours du dernier nombre de jours calendaires spécifié entre 1 et 30. (Jour calendaire = 1 jour calendaire permet d'examiner 24 à 48 heures d'historique de l'utilisateur)<br> <a href=\"/docs/x-in-y-behavior/\"> Pour en savoir plus sur le comportement X-in-Y, cliquez ici.</a> <br><br>Exemple :<br>Abandon du panier exactement 0 fois au cours des 1 derniers jours calendaires<br><br>Fuseau horaire :<br>UTC - Pour tenir compte de tous les fuseaux horaires, 1 jour calendrier examinera 24 à 48 heures de l'historique de l'utilisateur, en fonction de l'heure à laquelle le segment est évalué ; pour 2 jours calendrier, il examinera 48 à 72 heures de l'historique de l'utilisateur, et ainsi de suite."
    tags:
      - Custom events
  - name: "X propriétés d'événement personnalisé dans Y jours"
    description: "Détermine si un utilisateur a effectué un événement spécialement enregistré en relation avec un bien spécifique entre 0 et 50 fois au cours du dernier nombre de jours calendaires spécifié entre 1 et 30. (Jour calendaire = 1 jour calendaire permet d'examiner 24 à 48 heures d'historique de l'utilisateur)<br><a href=\"/docs/x-in-y-behavior/\">Pour en savoir plus sur le comportement X-in-Y, cliquez ici.</a> <br><br>Exemple :<br> Ajouté aux favoris avec la propriété \"event_name\" exactement 0 fois au cours des 1 derniers jours calendaires<br><br>Fuseau horaire :<br>UTC - Pour tenir compte de tous les fuseaux horaires, 1 jour calendrier examinera 24 à 48 heures de l'historique de l'utilisateur, en fonction de l'heure à laquelle le segment est évalué ; pour 2 jours calendrier, il examinera 48 à 72 heures de l'historique de l'utilisateur, et ainsi de suite."
    tags:
      - Custom events
  - name: Adresse e-mail 
    description: "Vous permet de désigner les destinataires de votre campagne par des adresses e-mail individuelles à des fins de test. Cette fonction peut également être utilisée pour envoyer des e-mails transactionnels à tous vos utilisateurs (y compris ceux qui se sont désabonnés) en utilisant le spécificateur \"L'adresse e-mail n'est pas vide\" dans le filtre, afin de maximiser la réception/distribution des e-mails quel que soit le statut de l'abonnement. <br><br>Ce filtre vérifie uniquement si les profils utilisateurs ont une adresse e-mail, alors que le filtre <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">Email disponible</a> vérifie des critères supplémentaires."
    tags:
      - Other Filters
  - name: ID externe
    description: "Vous permet de désigner les destinataires de votre campagne par ID d'utilisateur individuel à des fins de test."
    tags:
      - Other Filters
  - name: "Compartiment aléatoire"
    description: "Segmente vos utilisateurs en fonction d'un numéro attribué de manière aléatoire (de 0 à 9999 inclus). Il peut permettre la création de segments uniformément répartis d'utilisateurs véritablement aléatoires pour les tests A/B et multivariés."
    tags:
      - Other Filters
  - name: Nombre de sessions
    description: "Segmente vos utilisateurs en fonction du nombre de sessions qu'ils ont eues dans n'importe laquelle de vos applications au sein de votre espace de travail."
    tags:
      - Sessions
  - name: "Nombre de sessions pour l'application"
    description: "Segmente vos utilisateurs en fonction du nombre de sessions qu'ils ont eues dans une application spécifique et désignée."
    tags:
      - Sessions
  - name: X sessions dans les Y derniers jours
    description: "Segmente vos utilisateurs en fonction du nombre de sessions (entre 0 et 50) qu'ils ont eues dans votre application au cours du dernier nombre de jours calendaires spécifié entre 1 et 30. <br> <a href=\"/docs/x-in-y-behavior/\">Pour en savoir plus sur le comportement X-in-Y, cliquez ici.</a>"
    tags:
      - Sessions
  - name: Première application utilisée
    description: "Segmente vos utilisateurs en fonction de la première heure enregistrée à laquelle ils ont ouvert votre application. <em>Notez qu'il s'agit de la première session d'utilisation d'une version de votre application intégrant le SDK de Braze.</em> (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Sessions
  - name: "Première utilisation d'une application spécifique"
    description: "Segmente vos utilisateurs en fonction de la première heure enregistrée à laquelle ils ont ouvert l'une de vos applications au sein de votre espace de travail. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Sessions
  - name: Dernière application utilisée
    description: "Segmente vos utilisateurs en fonction de la dernière fois qu'ils ont ouvert votre application. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Sessions
  - name: Dernière application spécifique utilisée
    description: "Segmente vos utilisateurs en fonction de la dernière fois qu'ils ont ouvert une application spécifique et désignée. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Sessions
  - name: Durée médiane de la session
    description: Segmente vos utilisateurs en fonction de la durée médiane de leurs sessions dans votre application.
    tags:
      - Sessions
  - name: Message reçu de la campagne
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non une campagne spécifique.<br><br> Pour les cartes de contenu, les bannières et les messages in-app, il s'agit du moment où un utilisateur enregistre une impression, et non du moment où la carte ou le message in-app est envoyé.<br><br>Pour les push et les webhooks, c'est le moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, il s'agit du moment où la dernière demande d'API de message est envoyée à WhatsApp, et non du moment où le message est livré à l'appareil de l'utilisateur. <br><br>Pour les e-mails, il s'agit du moment où une demande d'e-mail est envoyée au fournisseur de services d'e-mail (indépendamment du fait qu'elle soit effectivement délivrée). Lorsque plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lors de l'envoi initial, seul le profil de l'utilisateur ciblé est mis à jour. <br>- Lorsque l'e-mail est délivré, ou si l'utilisateur ouvre l'e-mail ou un lien dans l'e-mail, tous les utilisateurs partageant cette adresse e-mail sembleront avoir reçu le message.<br><br>Pour les SMS, il s'agit de la date à laquelle le dernier message a été envoyé au fournisseur de SMS. Cela ne garantit pas que le message a été envoyé à l'appareil de l'utilisateur."
    tags:
      - Retargeting
  - name: Variante de campagne reçue
    description: "Segmente vos utilisateurs en fonction de la variante d'une campagne multivariée qu'ils ont reçue.<br><br> Pour les cartes de contenu, les bannières et les messages in-app, il s'agit du moment où un utilisateur enregistre une impression, et non du moment où la carte ou le message in-app est envoyé.<br><br>Pour les push et les webhooks, c'est le moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, il s'agit du moment où la dernière demande d'API de message est envoyée à WhatsApp, et non du moment où le message est livré à l'appareil de l'utilisateur. <br><br>Pour les e-mails, il s'agit du moment où une demande d'e-mail est envoyée au fournisseur de services d'e-mail (indépendamment du fait qu'elle soit effectivement délivrée). Lorsque plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lors de l'envoi initial, seul le profil de l'utilisateur ciblé est mis à jour. <br>- Lorsque l'e-mail est délivré, ou si l'utilisateur ouvre l'e-mail ou un lien dans l'e-mail, tous les utilisateurs partageant cette adresse e-mail sembleront avoir reçu le message.<br><br>Pour les SMS, il s'agit de la date à laquelle le dernier message a été envoyé au fournisseur de SMS. Cela ne garantit pas que le message a été envoyé à l'appareil de l'utilisateur."
    tags:
      - Retargeting
  - name: "Message reçu de l'étape du canvas"
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non un composant Canvas spécifique.<br><br> Pour les cartes de contenu et les messages in-app, il s'agit du moment où l'utilisateur enregistre une impression, et non du moment où la carte ou le message in-app est envoyé.<br><br>Pour les push et les webhooks, c'est le moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, il s'agit du moment où la dernière demande d'API de message est envoyée à WhatsApp, et non du moment où le message est livré à l'appareil de l'utilisateur. <br><br>Pour les e-mails, il s'agit du moment où une demande d'e-mail est envoyée au fournisseur de services d'e-mail (indépendamment du fait qu'elle soit effectivement délivrée). Lorsque plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lors de l'envoi initial, seul le profil de l'utilisateur ciblé est mis à jour. <br>- Lorsque l'e-mail est délivré, ou si l'utilisateur ouvre l'e-mail ou un lien dans l'e-mail, tous les utilisateurs partageant cette adresse e-mail sembleront avoir reçu le message.<br><br>Pour les SMS, il s'agit de la date à laquelle le dernier message a été envoyé au fournisseur de SMS. Cela ne garantit pas que le message a été envoyé à l'appareil de l'utilisateur."
    tags:
      - Retargeting
  - name: "Dernier message reçu d'une étape spécifique du canvas"
    description: "Segmente vos utilisateurs en fonction du moment où ils ont reçu un composant Canvas spécifique. Ce filtre ne tient pas compte du fait que les utilisateurs ont reçu d'autres composants de Canvas."
    tags:
      - Retargeting
  - name: "Dernier message reçu d'une campagne spécifique"
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non une campagne spécifique. Ce filtre ne tient pas compte du moment où les utilisateurs ont reçu d'autres campagnes."
    tags:
      - Retargeting
  - name: "Message reçu d'une campagne ou d'un canvas avec étiquette"
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non une campagne spécifique ou une toile avec une étiquette spécifique.<br><br> Pour les cartes de contenu, les bannières (campagnes uniquement) et les messages in-app, il s'agit du moment où un utilisateur enregistre une impression, et non du moment où la carte ou le message in-app est envoyé.<br><br>Pour les push et les webhooks, c'est le moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, il s'agit du moment où la dernière demande d'API de message est envoyée à WhatsApp, et non du moment où le message est livré à l'appareil de l'utilisateur. <br><br>Pour les e-mails, il s'agit du moment où une demande d'e-mail est envoyée au fournisseur de services d'e-mail (indépendamment du fait qu'elle soit effectivement délivrée). Lorsque plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lors de l'envoi initial, seul le profil de l'utilisateur ciblé est mis à jour. <br>- Lorsque l'e-mail est délivré, ou si l'utilisateur ouvre l'e-mail ou un lien dans l'e-mail, tous les utilisateurs partageant cette adresse e-mail sembleront avoir reçu le message.<br><br>Pour les SMS, il s'agit de la date à laquelle le dernier message a été envoyé au fournisseur de SMS. Cela ne garantit pas que le message a été envoyé à l'appareil de l'utilisateur."
    tags:
      - Retargeting
  - name: Dernier message reçu de la campagne ou du canvas avec étiquette
    description: "Segmente vos utilisateurs en fonction du moment où ils ont reçu une campagne spécifique ou une toile avec une étiquette spécifique. Ce filtre ne tient pas compte du fait que les utilisateurs ont reçu d'autres campagnes ou canevas. (période de 24 heures)"
    tags:
      - Retargeting
  - name: "N'a jamais reçu de message de la part de la campagne ou de l'étape du canvas"
    description: "Segmente vos utilisateurs selon qu'ils ont reçu ou non une campagne ou un composant Canvas."
    tags:
      - Retargeting
  - name: Dernier e-mail reçu
    description: "Segmente vos utilisateurs en fonction de la dernière fois qu'ils ont reçu l'un de vos messages e-mail. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Dernière poussée reçue
    description: "Segmente vos utilisateurs en fonction de la dernière fois qu'ils ont reçu l'une de vos notifications push. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Dernière impression du message in-app
    description: "Segmente vos utilisateurs en fonction de la dernière fois qu'ils ont consulté un message in-app."
    tags:
      - Retargeting
  - name: Dernier SMS reçu
    description: "Segmente vos utilisateurs en fonction de l'heure à laquelle le dernier message a été envoyé au fournisseur de SMS. Cela ne garantit pas que le message a été envoyé à l'appareil de l'utilisateur. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Dernier webhook reçu
    description: "Segmente vos utilisateurs en fonction de la dernière fois que Braze a envoyé un webhook pour cet utilisateur. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Dernier message reçu WhatsApp
    description: "Segmente vos utilisateurs en fonction de la dernière fois qu'ils ont reçu un message WhatsApp. Il s'agit du moment où la dernière demande d'API de message est envoyée à WhatsApp, et non du moment où le message est livré à l'appareil de l'utilisateur. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Campagne cliquée/ouverte
    description: "Filtrez par interaction avec une campagne spécifique. Pour les envois de messages e-mail, l'événement d'ouverture comprend à la fois les ouvertures machine et les ouvertures non machine.<br><br> Pour les e-mails, vous avez également la possibilité de filtrer par \"a ouvert n'importe quel e-mail (ouverture par la machine)\" et \"a ouvert n'importe quel e-mail (autres ouvertures)\". Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur initial change d'adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic s'applique à tous les autres utilisateurs possédant cette adresse e-mail au lieu de l'utilisateur initial.<br><br>Pour les SMS, une interaction est définie comme suit :<br>- L'utilisateur a envoyé en dernier lieu un SMS de réponse correspondant à une catégorie de mots-clés donnée. Ceci est attribué à la campagne la plus récente reçue par tous les utilisateurs avec ce numéro de téléphone. La campagne doit avoir été reçue au cours des quatre dernières heures.<br>- Le dernier lien raccourci sélectionné par l'utilisateur dans un message SMS dont le suivi des clics de l'utilisateur est activé, dans le cadre d'une campagne donnée."
    tags:
      - Retargeting
  - name: Campagne ou canvas cliqué/ouvert avec étiquette
    description: "Filtrez en fonction de l'interaction avec une campagne spécifique ayant une étiquette spécifique. Pour les envois de messages e-mail, l'événement d'ouverture comprend à la fois les ouvertures machine et les ouvertures non machine.<br><br> Pour les e-mails, vous avez la possibilité de filtrer par \"a ouvert n'importe quel e-mail (ouverture par la machine)\" et \"a ouvert n'importe quel e-mail (autres ouvertures)\". Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur initial change d'adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic s'applique à tous les autres utilisateurs possédant cette adresse e-mail au lieu de l'utilisateur initial.<br><br>Pour les SMS, une interaction est définie comme suit :<br>- L'utilisateur a envoyé en dernier lieu un SMS de réponse correspondant à une catégorie de mots-clés donnée. Ceci est attribué à la campagne la plus récente reçue par tous les utilisateurs avec ce numéro de téléphone. La campagne doit avoir été reçue au cours des quatre dernières heures.<br>- Date de la dernière sélection par l'utilisateur d'un lien abrégé dans un message SMS pour lequel le suivi des clics de l'utilisateur est activé, à partir d'une campagne donnée ou d'une étape Canvas avec étiquette."
    tags:
      - Retargeting
  - name: Étape cliquée/ouverte
    description: "Filtrer en fonction de l'interaction avec un composant Canvas spécifique. Pour les envois de messages e-mail, l'événement d'ouverture comprend à la fois les ouvertures machine et les ouvertures non machine.<br><br>Pour les e-mails, vous avez la possibilité de filtrer par \"a ouvert n'importe quel e-mail (ouverture par la machine)\" et \"a ouvert n'importe quel e-mail (autres ouvertures)\".<br><br>Pour les SMS, une interaction est définie comme suit :<br>- L'utilisateur a envoyé en dernier lieu un SMS de réponse correspondant à une catégorie de mots-clés donnée. Ceci est attribué à la campagne la plus récente reçue par tous les utilisateurs avec ce numéro de téléphone. La campagne doit avoir été reçue au cours des quatre dernières heures. <br>- L'utilisateur a sélectionné en dernier lieu un lien abrégé dans un message SMS pour lequel le suivi des clics de l'utilisateur est activé, à partir d'une étape du canvas donnée."
    tags:
      - Retargeting
  - name: Alias cliqué dans la campagne
    description: "Filtrez vos utilisateurs selon qu'ils ont cliqué sur un alias spécifique dans une campagne spécifique. Ceci ne s'applique qu'aux messages e-mail. <br><br> Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur initial change d'adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic s'applique à tous les autres utilisateurs possédant cette adresse e-mail au lieu de l'utilisateur initial."
    tags:
      - Retargeting
  - name: "Alias cliqué dans l'étape du canvas"
    description: "Filtrez vos utilisateurs selon qu'ils ont cliqué sur un alias d'utilisateur spécifique dans un canvas spécifique. Ceci ne s'applique qu'aux messages e-mail. <br><br> Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur initial change d'adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic s'applique à tous les autres utilisateurs possédant cette adresse e-mail au lieu de l'utilisateur initial."
    tags:
      - Retargeting
  - name: "Alias cliqué dans n'importe quelle campagne ou étape du canvas"
    description: "Filtrez vos utilisateurs selon qu'ils ont cliqué sur un alias spécifique dans une campagne ou un canvas. Ceci ne s'applique qu'aux messages e-mail. <br><br> Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur initial change d'adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic s'applique à tous les autres utilisateurs possédant cette adresse e-mail au lieu de l'utilisateur initial."
    tags:
      - Retargeting
  - name: "échec d'envoi définitif"
    description: "Segmentez vos utilisateurs selon que leur adresse e-mail a fait l'objet d'un échec d'envoi définitif (par exemple, l'adresse e-mail n'est pas valide)."
    tags:
      - Retargeting
  - name: "échec provisoire d'envoi"
    description: "Segmentez vos utilisateurs en fonction du nombre d'échecs provisoires d'envoi X fois en Y jours. Les filtres Segment ne peuvent remonter que 30 jours en arrière, mais vous pouvez remonter plus loin grâce aux extensions de segments.<br><br>Ce filtre fonctionne différemment d'un échec provisoire d'envoi dans Currents. Le filtre de segment Soft Bounced comptabilise un échec provisoire d'envoi s'il n'y a pas eu de réception/distribution réussie pendant la période de réessai de 72 heures. Dans Currents, chaque tentative infructueuse est envoyée sous la forme d'un échec provisoire d'envoi." 
    tags:
      - Retargeting
  - name: Vous a marqué comme spam
    description: "Segmente vos utilisateurs selon qu'ils ont ou non marqué vos messages comme étant du spam."
    tags:
      - Retargeting
  - name: Numéro de téléphone invalide 
    description: Segmente vos utilisateurs selon que leur numéro de téléphone est invalide ou non.
    tags:
      - Retargeting
  - name: Dernier SMS spécifique envoyé Catégorie de mots clés entrants
    description: "Segmente vos utilisateurs en fonction de la date de leur dernier envoi de SMS à un groupe d'abonnement spécifique au sein d'une catégorie de mots-clés spécifique." 
    tags:
      - Retargeting
  - name: Converti de la campagne
    description: "Segmente vos utilisateurs selon qu'ils ont converti ou non sur une campagne spécifique. Ce filtre n'inclut pas les utilisateurs qui font partie du groupe de contrôle."
    tags:
      - Retargeting
  - name: Converti en toile
    description: "Segmente vos utilisateurs selon qu'ils ont ou non converti sur un Canvas spécifique. Ce filtre n'inclut pas les utilisateurs qui font partie du groupe de contrôle."
    tags:
      - Retargeting
  - name: Dans le groupe de contrôle de la campagne
    description: "Segmente vos utilisateurs en fonction de leur appartenance ou non au groupe de contrôle d'une campagne multivariée spécifique."
    tags:
      - Retargeting
  - name: Dans le groupe de contrôle Canvas
    description: "Segmente vos utilisateurs en fonction de leur appartenance ou non au groupe de contrôle pour un Canvas spécifique. Ce filtre n'évalue que les utilisateurs qui sont entrés dans le Canvas.<br><br>Par exemple, si vous filtrez les utilisateurs qui ne font pas partie du groupe de contrôle pour un Canvas, vous recevrez tous les utilisateurs qui sont entrés dans le Canvas mais qui ne font pas partie du groupe de contrôle."
    tags:
      - Retargeting
  - name: Dernière inscription dans un groupe de contrôle
    description: "Segmente vos utilisateurs en fonction de la dernière fois qu'ils sont tombés dans le groupe de contrôle d'une campagne. <br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Saisi Variation de la toile
    description: "Segmente vos utilisateurs selon qu'ils sont entrés ou non dans un chemin de variation d'un Canvas spécifique. Ce filtre évalue tous les utilisateurs.<br><br>Par exemple, si vous filtrez sur les utilisateurs qui ne sont pas entrés dans le groupe de contrôle d'une variation du Canvas, vous recevrez tous les utilisateurs qui ne font pas partie du groupe de contrôle, qu'ils soient entrés ou non dans le Canvas."
    tags:
      - Retargeting
  - name: "Dernier envoi d'un message"
    description: "Segmente vos utilisateurs en déterminant le dernier message reçu. (période de 24 heures)<br><br> Pour les cartes de contenu, les bannières et les messages in-app, il s'agit de la date à laquelle un utilisateur a enregistré une impression pour la dernière fois, et non de la date à laquelle la carte ou le message in-app a été envoyé pour la dernière fois.<br><br>Pour les push et les webhooks, il s'agit du moment où un message a été envoyé à l'utilisateur.<br><br> Pour WhatsApp, il s'agit de la date à laquelle la dernière demande d'API de message a été envoyée à WhatsApp, et non de la date à laquelle le message a été livré à l'appareil de l'utilisateur. <br><br>Pour les e-mails, il s'agit du moment où une demande d'e-mail est envoyée au fournisseur de services d'e-mail (indépendamment du fait qu'elle soit effectivement délivrée). Lorsque plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lors de l'envoi initial, seul le profil de l'utilisateur ciblé est mis à jour. <br>- Lorsque l'e-mail est délivré, ou si l'utilisateur ouvre l'e-mail ou un lien dans l'e-mail, tous les utilisateurs partageant cette adresse e-mail sembleront avoir reçu le message.<br><br>Pour les SMS, il s'agit de la date à laquelle le dernier message a été envoyé au fournisseur de SMS. Cela ne garantit pas que le message a été envoyé à l'appareil de l'utilisateur.<br><br>Exemple :<br>Dernier message reçu Il y a moins d'un jour = il y a moins de 24 heures<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Dernier envoi de messages
    description: "Segmente vos utilisateurs en fonction de la dernière fois qu'ils ont cliqué ou ouvert l'un de vos canaux d'envoi de messages (Bannières, carte de contenu, e-mail, in-app, SMS, push, WhatsApp). Pour les envois de messages e-mail, l'événement d'ouverture comprend à la fois les ouvertures machine et les ouvertures non machine. (période de 24 heures)<br><br>Pour les e-mails, il s'agit du moment où une demande d'e-mail est envoyée au fournisseur de services d'e-mail (indépendamment du fait qu'elle soit effectivement délivrée). Vous avez également la possibilité de filtrer par \"a ouvert n'importe quel e-mail (ouverture par la machine)\" et \"a ouvert n'importe quel e-mail (autres ouvertures)\". Lorsque plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lors de l'envoi initial, seul le profil de l'utilisateur ciblé est mis à jour. <br>- Lorsque l'e-mail est délivré, ou si l'utilisateur ouvre l'e-mail ou un lien dans l'e-mail, tous les utilisateurs partageant cette adresse e-mail sembleront avoir reçu le message.<br><br>Pour les SMS, il s'agit du moment où l'utilisateur a sélectionné pour la dernière fois un lien abrégé dans un message pour lequel le suivi des clics de l'utilisateur est activé.<br><br>Fuseau horaire :<br>Fuseau horaire de l'entreprise"
    tags:
      - Retargeting
  - name: Carte cliquée 
    description: "Segmente vos utilisateurs selon qu'ils ont ou non cliqué sur une carte de contenu spécifique. Ce filtre est disponible en tant que sous-filtre de \"Campagne cliquée/ouverte\", \"Campagne cliquée/ouverte ou Canvas avec étiquette\", et \"Étape cliquée/ouverte\"."
    tags:
      - Retargeting
  - name: Drapeaux de fonctionnalité
    description: "Segmentation de vos utilisateurs pour lesquels une <a href=\"/docs/developer_guide/feature_flags/\">fonctionnalité</a> particulière est activée."
    tags:
      - Retargeting
  - name: "Groupe d'abonnement"
    description: "Segmente vos utilisateurs en fonction de leur groupe d'abonnement à l'e-mail, au SMS/MMS ou à WhatsApp. Les groupes archivés n'apparaissent pas et ne peuvent pas être utilisés."
    tags:
      - Channel subscription behavior
  - name: E-mail disponible
    description: "Segmente vos utilisateurs selon qu'ils ont une adresse e-mail valide ou qu'ils sont abonnés ou non à l'e-mail. Ce filtre vérifie trois critères : si l'utilisateur s'est désabonné des e-mails, si Braze a reçu un échec définitif et si l'e-mail a été marqué comme spam. Si l'un de ces critères est rempli, ou si un e-mail n'existe pas pour un utilisateur, celui-ci ne sera pas inclus.<br><br>Notez que si vous envoyez un message transactionnel, les utilisateurs dont l'\"e-mail disponible\" est <code>faux</code> ne seront pas inclus dans le calcul de l'audience mais pourront tout de même recevoir un message. Cependant, le calcul de l'audience n'inclura que les utilisateurs abonnés ou ayant opté pour l'abonnement. <br><br>Pour les messages électroniques pour lesquels le statut d'abonnement est important, nous vous suggérons d'utiliser le filtre \"Email disponible\" au lieu du filtre \" <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">Adresse e-mail\"</a>; les critères supplémentaires peuvent vous aider à cibler les utilisateurs qui veulent vraiment voir vos messages."
    tags:
      - Channel subscription behavior
  - name: "Date d'abonnement à l'e-mail"
    description: "Segmente vos utilisateurs en fonction de la date à laquelle ils se sont abonnés à l'e-mail."
    tags:
      - Channel subscription behavior
  - name: "Statut de l'abonnement à l'e-mail"
    description: "Segmente vos utilisateurs en fonction de leur statut d'abonnement à l'e-mail."
    tags:
      - Channel subscription behavior
  - name: "Date de désinscription de l'e-mail" 
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils se sont désabonnés des futurs e-mails.
    tags:
      - Channel subscription behavior
  - name: "Poussée d'avant-plan activée"
    description: "Segmente vos utilisateurs qui disposent d'une autorisation provisoire de push ou qui sont activés pour le push au premier plan. Plus précisément, ce décompte comprend<br>1. les utilisateurs iOS qui sont provisoirement autorisés pour le push. <br>2. Les utilisateurs qui sont activés pour le push au premier plan et dont le statut d'abonnement au push n'est pas désabonné, pour n'importe laquelle de vos applications. Pour ces utilisateurs, ce décompte ne comprend que les poussées de premier plan.<br><br>Les utilisateurs qui se sont désinscrits ne sont pas pris en compte dans le calcul de l'option \"Foreground Push Enabled\" (poussée en avant-plan activée). <br><br>Après avoir segmenté avec ce filtre, vous pourrez voir une répartition des personnes qui font partie de ce segment pour Android, iOS et le web dans le panneau du bas, appelé <em>Utilisateurs joignables</em>."
    tags:
      - Channel subscription behavior
  - name: "Activation de la poussée au premier plan pour l'application"
    description: "Segmentation selon que les utilisateurs ont activé ou non le push pour votre application sur leur appareil. Utilisateurs pour lesquels la fonction \"push\" est activée au premier plan pour une application. Cela ne tient pas compte de l'état de l'abonnement au service \"push\". Ce décompte inclut les utilisateurs qui ont provisoirement autorisé les jetons de poussée en avant-plan et en arrière-plan."
    tags:
      - Channel subscription behavior
  - name: "Poussée d'arrière-plan ou d'avant-plan activée"
    description: "Segmentation selon que les utilisateurs ont un jeton de poussée et ne se sont pas désabonnés. Utilisateurs pour lesquels la fonction push est activée en arrière-plan ou en avant-plan pour l'une de vos applications."
    tags:
      - Channel subscription behavior
  - name: "Pousser la date d'abonnement"
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils se sont abonnés à push.
    tags:
      - Channel subscription behavior
  - name: "Pousser l'état de l'abonnement"
    description: "Segmente vos utilisateurs en fonction de leur <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">statut d'abonnement</a> pour le push."
    tags:
      - Channel subscription behavior
  - name: Pousser Date de désabonnement
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils se sont désabonnés des futures notifications push.
    tags:
      - Channel subscription behavior
  - name: Produit acheté
    description: Segmente vos utilisateurs en fonction des produits achetés dans votre appli.
    tags:
      - Purchase behavior
  - name: "Nombre total d'achats"
    description: "Segmente vos utilisateurs en fonction du nombre d'achats qu'ils ont effectués dans votre appli."
    tags:
      - Purchase behavior
  - name: X produits achetés en Y jours
    description: "Filtrez les utilisateurs en fonction de la fréquence d'achat d'un produit spécifique."
    tags:
      - Purchase behavior
  - name: X Achats dans les Y derniers jours
    description: "Segmente vos utilisateurs en fonction du nombre de fois (entre 0 et 50) qu'ils ont effectué un achat au cours des derniers jours calendaires spécifiés entre 1 et 30. <br> <a href=\"/docs/x-in-y-behavior/\">Pour en savoir plus sur le comportement X-in-Y, cliquez ici.</a>"
    tags:
      - Purchase behavior
  - name: X achète un bien dans Y jours
    description: "Segmente vos utilisateurs en fonction du nombre de fois où un achat a été effectué en relation avec un certain bien d'achat au cours du dernier nombre de jours calendaires spécifié entre 1 et 30. <br> <a href=\"/docs/x-in-y-behavior/\">Pour en savoir plus sur le comportement X-in-Y, cliquez ici.</a>"
    tags:
      - Purchase behavior
  - name: Premier achat effectué
    description: Segmente vos utilisateurs en fonction de la première fois où un utilisateur a effectué un achat dans votre application.
    tags:
      - Purchase behavior
  - name: "Premier achat pour l'application"
    description: Segmente vos utilisateurs en fonction de la première fois où un utilisateur a effectué un achat à partir de votre application.
    tags:
      - Purchase behavior
  - name: Dernier achat effectué
    description: "Filtrez les utilisateurs en fonction de la dernière fois qu'ils ont effectué un achat."
    tags: 
      - Purchase behavior
  - name: Dernier produit acheté
    description: "Filtrez les utilisateurs en fonction de la date de leur dernier achat d'un produit spécifique."
    tags:
      - Purchase behavior
  - name: Argent dépensé
    description: "Segmente vos utilisateurs en fonction du montant qu'ils ont dépensé dans votre appli."
    tags:
      - Purchase behavior
  - name: X argent dépensé en Y jours
    description: "Segmente vos utilisateurs en fonction du montant qu'ils ont dépensé dans votre application au cours du dernier nombre de jours calendaires spécifié, compris entre 1 et 30. Ce montant ne comprendra que la somme des 50 derniers achats. <br> <a href=\"/docs/x-in-y-behavior/\">Pour en savoir plus sur le comportement X-in-Y, cliquez ici.</a>"
    tags:
      - Purchase behavior
  - name: Pays
    description: "Segmente vos utilisateurs en fonction de l'emplacement/localisation du dernier pays indiqué."
    tags:
      - Demographic attributes
  - name: Ville
    description: Segmente vos utilisateurs en fonction de leur dernier emplacement/localisation indiqué.
    tags:
      - Demographic attributes
  - name: Langue
    description: Segmente vos utilisateurs en fonction de leur langue préférée.
    tags:
      - Demographic attributes
  - name: "L'âge"
    description: "Segmente vos utilisateurs en fonction de leur âge, tel qu'ils l'ont indiqué depuis votre appli."
    tags:
      - Demographic attributes
  - name: Anniversaire
    description: "Segmente vos utilisateurs en fonction de leur date d'anniversaire, comme ils l'ont indiqué depuis votre appli. <br> Les utilisateurs dont l'anniversaire est le 29 février seront inclus dans les segmentations incluant le 1er mars.<br><br>Pour cibler les anniversaires de décembre ou de janvier, n'insérez la logique de filtrage que dans les 12 mois de l'année que vous ciblez. En d'autres termes, n'insérez pas de logique qui remonte au mois de décembre de l'année civile précédente ou au mois de janvier de l'année suivante. Par exemple, pour cibler les anniversaires de décembre, vous pouvez filtrer \"le 31 décembre\", \"avant le 31 décembre\" ou \"après le 30 novembre\"."
    tags:
      - Demographic attributes
  - name: Genre
    description: "Segmente vos utilisateurs par sexe, comme ils l'ont indiqué depuis votre appli."
    tags:
      - Demographic attributes
  - name: Numéro de téléphone non formaté
    description: "Segmente vos utilisateurs en fonction de leur numéro de téléphone non formaté. Ne comprend pas de parenthèses, de tirets ou d'autres symboles."
    tags:
      - Demographic attributes
  - name: Prénom
    description: "Segmente vos utilisateurs en fonction de leur prénom, tel qu'ils l'ont indiqué depuis votre appli."
    tags:
      - Demographic attributes
  - name: Nom de famille
    description: "Segmente vos utilisateurs en fonction de leur nom de famille, tel qu'ils l'ont indiqué depuis votre appli."
    tags:
      - Demographic attributes
  - name: "Dispose d'une application"
    description: "Segmentation en fonction de l'installation ou non de votre application par l'utilisateur. Il s'agit des utilisateurs qui ont installé votre application et de ceux qui l'ont désinstallée par le passé. En général, les utilisateurs doivent ouvrir l'application (démarrer une session) pour être inclus dans ce filtre. Il existe toutefois quelques exceptions, notamment si un utilisateur a été importé dans Braze et associé manuellement à votre appli."
    tags:
      - App
  - name: "Nom de la version la plus récente de l'application"
    description: "Segmentation en fonction du nom récent de l'application de l'utilisateur.<br><br>Lorsque vous utilisez \"less than\" ou \"less than or equal to\", si la version de l'application principale n'existe pas, ce filtre renverra `vrai` car l'utilisateur est plus ancien que la version de l'application. Cela signifie que si la dernière version de l'application principale de l'utilisateur n'existe pas, elle correspond automatiquement au filtre."
    tags:
      - App 
  - name: "Numéro de la version la plus récente de l'application"
    description: "Segmentation en fonction du numéro de version récente de l'application de l'utilisateur.<br><br>Lorsque vous utilisez \"less than\" ou \"less than or equal to\", si la version de l'application principale n'existe pas, ce filtre renverra `vrai` car l'utilisateur est plus ancien que la version de l'application. Cela signifie que si la dernière version de l'application principale de l'utilisateur n'existe pas, elle correspond automatiquement au filtre.<br><br>Il peut s'écouler un certain temps avant que les versions actuelles de l'application ne soient mises à jour. La version de l'app sur le profil utilisateur se met à jour lorsque les informations sont capturées par le SDK, qui s'appuie sur le moment où les utilisateurs ouvrent leurs apps. Si l'utilisateur n'ouvre pas l'application, la version actuelle ne sera pas mise à jour. Ces filtres ne s'appliquent pas non plus rétroactivement. Il est bon d'utiliser \"supérieur à\" ou \"égal à\" pour les versions actuelles et futures, mais l'utilisation de filtres de versions antérieures peut entraîner des comportements inattendus."
    tags:
      - App 
  - name: Désinstallé
    description: "Segmente vos utilisateurs selon qu'ils ont désinstallé ou non votre application et qu'ils ne l'ont pas réinstallée."
    tags:
      - Uninstall 
  - name: "Support de l'appareil"
    description: "Segmente vos utilisateurs en fonction de l'opérateur de leur appareil."
    tags:
      - Devices
  - name: "Nombre d'appareils"
    description: "Segmente vos utilisateurs en fonction du nombre d'appareils sur lesquels ils ont utilisé votre appli."
    tags:
      - Devices
  - name: "Modèle d'appareil"
    description: Segmente vos utilisateurs en fonction de la version du modèle de leur téléphone portable.
    tags:
      - Devices
  - name: Appareil OS
    description: "Segmente vos utilisateurs qui possèdent un ou plusieurs appareils avec le système d'exploitation spécifié."
    tags:
      - Devices
  - name: "Locale de l'appareil le plus récent"
    description: "Segmente vos utilisateurs en fonction des <a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">informations locales</a> de l'appareil le plus récemment utilisé."
    tags:
      - Devices      
  - name: Modèle de montre le plus récent
    description: Segmente vos utilisateurs en fonction de leur modèle de smartwatch le plus récent.
    tags:
      - Devices    
  - name: Autorisé provisoirement sur iOS
    description: Vous permet de trouver les utilisateurs qui sont provisoirement autorisés sur iOS 12 pour une application donnée.
    tags:
      - Devices   
  - name: Navigateur web
    description: "Segmente vos utilisateurs en fonction du navigateur web qu'ils utilisent pour accéder à votre site web."
    tags:
      - Devices
  - name: Appareil IDFA
    description: Vous permet de désigner les destinataires de votre campagne par IDFA à des fins de test.
    tags:
      - Advertising use cases
  - name: Appareil IDFV
    description: Vous permet de désigner les destinataires de votre campagne par IDFV à des fins de test.
    tags:
      - Advertising use cases 
  - name: "Appareil ID de l'annonce Google"
    description: "Segmente vos utilisateurs en fonction de l'ID de l'annonce Google."
    tags:
      - Advertising use cases
  - name: Appareil Roku Ad ID
    description: "Segmente vos utilisateurs en fonction de l'ID de la publicité Roku."
    tags:
      - Advertising use cases
  - name: Appareil Windows ID publicitaire
    description: "Segmente vos utilisateurs en fonction de l'ID de la publicité Windows."
    tags:
      - Advertising use cases  
  - name: Suivi des annonces activé
    description: "Vous permet de filtrer en fonction de l'abonnement de vos utilisateurs au suivi publicitaire. Le suivi publicitaire concerne l'IDFA ou \"identifiant pour les annonceurs\" attribué à tous les appareils iOS par Apple, qui peut être paramétré par les SDK. Cet identifiant permet aux annonceurs de suivre les utilisateurs et de leur proposer des publicités ciblées."
    tags:
      - Advertising use cases
  - name: Emplacement/localisation le plus récent
    description: Segmente vos utilisateurs en fonction du dernier emplacement/localisation enregistré où ils ont utilisé votre appli.
    tags:
      - Location
  - name: Emplacements/localisation disponibles
    description: "Segmente vos utilisateurs selon qu'ils ont ou non signalé leurs emplacements/localisations. Pour utiliser ce filtre, votre app doit <a href=\"/docs/search/?query=location%20tracking\">intégrer la géolocalisation</a>."
    tags:
      - Location
  - name: "Cohortes d'Amplitude"
    description: Les clients qui utilisent Amplitude peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Amplitude.
    tags:
      - Cohort membership
  - name: Cohortes de Census
    description: Les clients qui utilisent le Census peuvent compléter leurs segments en choisissant et en important leurs cohortes dans le Census.
    tags:
      - Cohort membership
  - name: Cohortes de tas
    description: Les clients qui utilisent Heap peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Heap.
    tags:
      - Cohort membership
  - name: Cohortes Hightouch
    description: Les clients qui utilisent Hightouch peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Hightouch.
    tags:
      - Cohort membership
  - name: Cohortes de Kubit
    description: Les clients qui utilisent Kubit peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Kubit.
    tags:
      - Cohort membership
  - name: Cohortes Mixpanel
    description: Les clients qui utilisent Mixpanel peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Mixpanel.
    tags:
      - Cohort membership
  - name: Cohortes de segments
    description: Les clients qui utilisent Segment peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Segment.
    tags:
      - Cohort membership
  - name: Cohortes de Tinyclues
    description: Les clients qui utilisent Tinyclues peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Tinyclues.
    tags:
      - Cohort membership
  - name: "Installer l'attribution d'installation"
    description: "Segmente vos utilisateurs en fonction de la publicité à laquelle leur attribution d'installation a été attribuée."
    tags:
      - User Attributes
  - name: "Installer l'attribution d'installation"
    description: "Segmente vos utilisateurs en fonction du groupe d'annonces auquel leur attribution d'installation a été attribuée."
    tags:
      - Install Attribution
  - name: "Installation d'une campagne d'attribution"
    description: Segmente vos utilisateurs en fonction de la campagne publicitaire à laquelle leur installation a été attribuée.
    tags:
      - Install Attribution
  - name: "Attribution d'installation Source"
    description: "Segmente vos utilisateurs en fonction de la source à laquelle leur attribution d'installation a été attribuée."
    tags:
      - Install Attribution
  - name: Catégorie de risque de désabonnement
    description:  "Segmente vos utilisateurs par catégorie de risque de désabonnement en fonction d'une prédiction spécifique."
    tags:
      - Intelligence and predictive
  - name: Score de risque de désabonnement
    description: Segmente vos utilisateurs par score de risque de désabonnement selon une prédiction spécifique.
    tags:
      - Intelligence and predictive
  - name: "Catégorie de probabilité d'événement"
    description: "Segmente vos utilisateurs en fonction de la probabilité qu'ils réalisent un événement selon une prédiction spécifique."
    tags:
      - Intelligence and predictive
  - name: "Score de vraisemblance de l'événement"
    description: "Segmente vos utilisateurs en fonction de la probabilité qu'ils réalisent un événement selon une prédiction spécifique."
    tags:
      - Intelligence and predictive
  - name: Canal intelligent
    description: Segmentez vos utilisateurs par le canal le plus actif au cours des trois derniers mois.
    tags:
      - Intelligence and predictive
  - name: Message ouvert Probabilité
    description: "Filtre vos utilisateurs en fonction de leur probabilité d'ouvrir un message sur un canal spécifié sur une échelle de 0 à 100 %. Les utilisateurs ne disposant pas de données suffisantes pour mesurer la probabilité d'un canal peuvent être sélectionnés à l'aide de l'option \"est vide\"."
    tags:
      - Intelligence and predictive
  - name: "Nombre d'amis Facebook utilisant l'application"
    description: "Segmente vos utilisateurs en fonction du nombre d'amis Facebook qui utilisent la même application."
    tags:
      - Social activity
  - name: Connecté à Facebook
    description: "Segmente vos utilisateurs selon qu'ils ont ou non connecté votre application à Facebook."
    tags:
      - Social activity
  - name: Twitter connecté
    description: "Segmente vos utilisateurs selon qu'ils ont ou non connecté votre appli à X (anciennement Twitter)."
    tags:
      - Social activity
  - name: Nombre de followers sur Twitter
    description: "Segmente vos utilisateurs en fonction du nombre de followers X (anciennement Twitter) qu'ils ont."
    tags:
      - Social activity
  - name: Numéro de téléphone
    description: "Segmente vos utilisateurs en fonction du champ du numéro de téléphone au format E.164.<br><br> Lorsqu'un numéro de téléphone est envoyé à Braze, Braze tente de le contraindre au <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">format e.164</a> qui est utilisé pour l'envoi à travers les canaux SMS et WhatsApp. Le processus de coercition peut échouer si le numéro n'est pas formaté correctement, ce qui fait que le profil utilisateur a un numéro de téléphone non formaté mais pas de numéro de téléphone d'envoi. Ce filtre de segmentation renvoie les utilisateurs en fonction de leur numéro de téléphone au format e.164 (lorsqu'il est disponible).<br><br>Cas d'utilisation :<br> - Utilisez ce filtre pour comprendre la taille de l'audience cible la plus précise lors de l'envoi de SMS ou de messages WhatsApp.  <br>- Utilisez des expressions régulières (regex) avec ce filtre pour segmenter les numéros de téléphone avec un code pays spécifique. <br>- Utilisez ce filtre pour segmenter les utilisateurs en fonction des numéros de téléphone qui n'ont pas passé le processus de coercition e.164."
    tags:
      - Other filters
---
