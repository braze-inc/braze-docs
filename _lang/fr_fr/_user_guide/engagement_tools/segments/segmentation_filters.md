---
page_order: 2
nav_title: Filtres de segmentation
article_title: Filtres de segmentation
layout: glossary_page
glossary_top_header: "Filtres de segmentation"
glossary_top_text: "Le SDK de Braze vous offre un puissant arsenal de filtres pour segmenter et cibler vos utilisateurs en fonction de fonctionnalités et d'attributs spécifiques. Vous pouvez rechercher ou restreindre ces filtres par catégorie de filtre.<br><br>Pour en savoir plus sur les différents types de données d'attributs personnalisés que vous pouvez utiliser pour segmenter les utilisateurs, consultez <a href=\"/docs/user_guide/data_and_analytics/custom_data/custom_attributes/#custom-attribute-data-types\">Types de données d'attributs personnalisés</a>."

page_type: glossary
tool: Segments
description: "Ce glossaire répertorie les filtres disponibles pour segmenter et cibler vos utilisateurs."
search_rank: 2
glossary_tag_name: Filter Category
glossary_filter_text: "Select a category to narrow the glossary:"

# channel to icon/fa or image mapping
glossary_tags:
  - name: Appartenance à un segment ou un fichier CSV
  - name: Attribut personnalisé
  - name: Événements personnalisés
  - name: Sessions
  - name: Reciblage
  - name: Comportement d’abonnement aux canaux
  - name: Comportement d’achat
  - name: E-commerce
  - name: Attributs démographiques
  - name: Application
  - name: Désinstallation
  - name: Appareils
  - name: Localisation
  - name: Appartenance à une cohorte
  - name: Attribution d’installation
  - name: Informations et prévisions
  - name: Activité sociale
  - name: Autres filtres

glossaries:
  - name: Appartenance à un segment
    description: "Vous permet de filtrer en fonction de l'appartenance à un segment partout où des filtres sont utilisés (comme les segments, les campagnes et d'autres) et de cibler plusieurs segments différents au sein d'une même campagne. <br><br>Notez que les segments utilisant déjà ce filtre ne peuvent pas être inclus ou imbriqués dans d'autres segments, car cela pourrait créer un cycle dans lequel le segment A inclurait le segment B, qui essaierait à son tour d'inclure le segment A. Dans ce cas, la segmentation ne cesserait de se référer à elle-même, ce qui rendrait impossible le calcul de la personne qui en fait partie. En outre, l'imbrication de segments de ce type ajoute de la complexité et peut ralentir les choses. Au lieu de cela, recréez le segment que vous essayez d'inclure en utilisant les mêmes filtres."
    tags:
      - Segment or CSV membership
  - name: Extension de segment Braze
    description: "Après avoir créé une Segment Extension dans le tableau de bord de Braze, vous pouvez choisir d’inclure ou d’exclure ces extensions de votre segment."
    tags:
      - Segment or CSV membership
  - name: Mis à jour/importés depuis un fichier CSV
    description: Segmente vos utilisateurs selon s’ils font partie d’un téléchargement CSV ou non.
    tags:
      - Segment or CSV membership
  - name: Attributs personnalisés
    description: "Détermine si un utilisateur correspond ou non à une valeur d'attribut enregistrée personnalisée. <br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Custom attribute
  - name: Créé à
    description: "Segmentation des utilisateurs en fonction de la date de création de leur profil utilisateur. Si un utilisateur a été ajouté par CSV ou API, ce filtre reflète la date à laquelle il a été ajouté. Si l'utilisateur n'est pas ajouté par CSV ou API et que sa première session est suivie par le SDK, ce filtre reflète la date de cette première session."
    tags:
      - Other Filters
  - name: Attributs personnalisés imbriqués
    description: "Les attributs qui sont les propriétés des attributs personnalisés.<br><br>Lors du filtrage d'un attribut personnalisé de temps imbriqué, vous pouvez choisir de filtrer en fonction du \"Jour de l'année\" ou de l'\"Heure\". L'option \"Jour de l'année\" ne vérifie que le mois et le jour à des fins de comparaison. \"Time\" compare l'horodatage complet, y compris l'année."
    tags:
      - Custom attribute
  - name: Jour de l’événement récurrent
    description: "Ce filtre examine le mois et le jour de l’attribut personnalisé avec le type de données « date », mais ne prend pas l’année en compte. Ce filtre est utile pour les événements annuels.<br><br>Fuseau horaire :<br>Ce filtre s'ajuste aux fuseaux horaires dans lesquels se trouve l'utilisateur, à condition que le message soit envoyé en utilisant l'option de planification de l'heure locale ; dans le cas contraire, ce filtre utilise le fuseau horaire de votre entreprise."
    tags:
      - Custom attribute
  - name: Événement personnalisé
    description: "Détermine si un utilisateur a effectué un événement spécialement enregistré.<br><br> Exemple :<br>Activité terminée avec le nom de l'activité.<br><br>Fuseau horaire :<br>UTC - Jour calendaire = 1 jour calendaire correspond à 24-48 heures d'historique de l'utilisateur."
    tags:
      - Custom events
  - name: Premier événement personnalisé
    description: "Détermine la première fois qu’un utilisateur a effectué un événement spécialement enregistré. (période de 24 heures) <br><br>Exemple :<br> Premier panier abandonné il y a moins d’un jour<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Custom events
  - name: Dernier événement personnalisé 
    description: "Détermine l'heure la plus récente à laquelle un utilisateur a effectué un événement enregistré spécialement. Ce filtre prend en charge les décimales, telles que 0,25 heure. (période de 24 heures) <br><br>Exemple :<br> Dernier panier d’achats abandonné il y a moins d’un jour<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Custom events
  - name: X événements personnalisés en Y jours
    description: "Détermine si un utilisateur a effectué un événement spécialement enregistré entre 0 et 50 fois au cours du dernier nombre de jours civils indiqué, c’est-à-dire entre 1 et 30. (Jour calendaire = 1 jour calendaire correspond à 24-48 heures d'historique de l'utilisateur)<br> <a href=\"/docs/x-in-y-behavior/\"> En savoir plus sur le comportement « X dans Y » ici.</a> <br><br>Exemple :<br>Le panier a été abandonné exactement 0 fois au cours du dernier jour civil<br><br>Fuseau horaire :<br>UTC - Pour tenir compte de tous les fuseaux horaires, 1 jour calendrier examine 24 à 48 heures de l'historique de l'utilisateur, selon l'heure à laquelle le segment est évalué ; pour 2 jours calendrier, il examine 48 à 72 heures de l'historique de l'utilisateur, et ainsi de suite."
    tags:
      - Custom events
  - name: X propriétés d’événement personnalisé en Y jours
    description: "Détermine si un utilisateur a effectué un événement spécialement enregistré en relation avec la propriété spécifique entre 0 et 50 fois au cours du dernier nombre de jours civils indiqué, compris entre 1 et 30. (Jour calendaire = 1 jour calendaire correspond à 24-48 heures d'historique de l'utilisateur)<br><a href=\"/docs/x-in-y-behavior/\">En savoir plus sur le comportement « X dans Y » ici.</a> <br><br>Exemple :<br> Ajouté aux favoris avec la propriété « event_name » exactement 0 fois au cours du dernier jour calendaire<br><br>Fuseau horaire :<br>UTC - Pour tenir compte de tous les fuseaux horaires, 1 jour calendrier examine 24 à 48 heures de l'historique de l'utilisateur, selon l'heure à laquelle le segment est évalué ; pour 2 jours calendrier, il examine 48 à 72 heures de l'historique de l'utilisateur, et ainsi de suite."
    tags:
      - Custom events
  - name: Adresse e-mail 
    description: "Ce filtre vous permet de désigner les destinataires de votre campagne en fonction de leur adresse e-mail individuelle pour mener des tests. Cette fonction peut également être utilisée pour envoyer des e-mails transactionnels à tous vos utilisateurs (y compris ceux qui se sont désabonnés) en utilisant le spécificateur \"L'adresse e-mail n'est pas vide\" dans le filtre, afin de maximiser la réception/distribution des e-mails quel que soit le statut de l'abonnement. <br><br>Ce filtre vérifie uniquement si les profils utilisateurs ont une adresse e-mail, alors que le filtre <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-available\">Email disponible</a> vérifie des critères supplémentaires."
    tags:
      - Other Filters
  - name: ID utilisateur externe
    description: Ce filtre vous permet de désigner les destinataires de votre campagne en fonction de leurs ID individuels pour mener des tests.
    tags:
      - Other Filters
  - name: "N° de compartiment aléatoire"
    description: Segmente vos utilisateurs en utilisant un nombre attribué de manière aléatoire (compris entre 0 et 9 999). Ce filtre permet de créer des segments d’utilisateurs réellement aléatoires et distribués de manière uniforme pour les tests A/B et les tests multivariés.
    tags:
      - Other Filters
  - name: Nombre de sessions
    description: "Segmentez vos utilisateurs par le nombre de sessions qu'ils ont eues dans l'une de vos applications au sein de votre espace de travail."
    tags:
      - Sessions
  - name: Nombre de sessions pour l’application
    description: Segmente vos utilisateurs en fonction du nombre de sessions qu’ils ont eus dans une application désignée.
    tags:
      - Sessions
  - name: X Sessions In Last Y Days
    description: "Segmente vos utilisateurs en fonction du nombre de sessions (entre 0 et 50) qu’ils ont initiés dans votre application dans le dernier nombre de jours civils indiqué, compris entre 1 et 30. <br> <a href=\"/docs/x-in-y-behavior/\">En savoir plus sur le comportement « X dans Y » ici.</a>"
    tags:
      - Sessions
  - name: Première application utilisée
    description: "Segmente vos utilisateurs en fonction de la première date enregistrée à laquelle ils ont ouvert votre application. <em>Cela permet de capturer la première session qu'ils ont effectuée en utilisant une version de votre application avec l'intégration SDK Braze.</em> (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Sessions
  - name: Première application utilisée
    description: "Segmentez vos utilisateurs par le premier moment enregistré où ils ont ouvert l'une de vos applications dans votre espace de travail. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Sessions
  - name: Dernière application utilisée
    description: "Segmentez vos utilisateurs par le moment le plus récent où ils ont ouvert votre application. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Sessions
  - name: Dernière application utilisée
    description: "Segmentez vos utilisateurs par le moment le plus récent où ils ont ouvert une application spécifique et désignée. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Sessions
  - name: Durée médiane des sessions
    description: Segmente vos utilisateurs en fonction de la durée médiane de leurs sessions dans votre application.
    tags:
      - Sessions
  - name: Message reçu de la campagne
    description: "Segmente vos utilisateurs selon s’ils ont reçu ou non une campagne donnée. Ce filtre ne retient que les utilisateurs auxquels le message a été explicitement envoyé, et non les autres utilisateurs ayant le même e-mail ou le même numéro de téléphone qui ont reçu des messages en double. Pour capturer les utilisateurs en double, utilisez <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign ou Canvas with Tag.</a><br><br> Pour les cartes de contenu, les bannières et les messages in-app, il s'agit du moment où un utilisateur enregistre une impression, et non du moment où la carte ou le message in-app est envoyé.<br><br>Pour les notifications push et les webhooks, ceci correspond au moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, c'est lorsque la dernière demande d'API de message est envoyée à WhatsApp, et non lorsque le message est livré sur l'appareil de l'utilisateur. <br><br>Pour les e-mails, c'est lorsque une demande d'e-mail est envoyée au fournisseur de service de messagerie (peu importe si elle est effectivement livrée).<br><br>Pour les SMS, ceci correspond au moment où le dernier message a été livré au fournisseur de SMS. Cela ne garantit pas que le message a été livré à l'appareil de l'utilisateur."
    tags:
      - Retargeting
  - name: Variante de campagne reçue
    description: "Segmente vos utilisateurs en fonction de la variante de campagne multivariée qu’ils ont reçue. Ce filtre ne retient que les utilisateurs auxquels le message a été explicitement envoyé, et non les autres utilisateurs ayant le même e-mail ou le même numéro de téléphone qui ont reçu des messages en double. Pour capturer les utilisateurs en double, utilisez <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign ou Canvas with Tag.</a><br><br> Pour les cartes de contenu, les bannières et les messages in-app, il s'agit du moment où un utilisateur enregistre une impression, et non du moment où la carte ou le message in-app est envoyé.<br><br>Pour les notifications push et les webhooks, ceci correspond au moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, c'est lorsque la dernière demande d'API de message est envoyée à WhatsApp, et non lorsque le message est livré sur l'appareil de l'utilisateur. <br><br>Pour les e-mails, c'est lorsque une demande d'e-mail est envoyée au fournisseur de service de messagerie (peu importe si elle est effectivement livrée).<br><br>Pour les SMS, ceci correspond au moment où le dernier message a été livré au fournisseur de SMS. Cela ne garantit pas que le message a été livré à l'appareil de l'utilisateur."
    tags:
      - Retargeting
  - name: A reçu un message de l’étape du canvas
    description: "Segmente vos utilisateurs selon s’ils ont reçu ou non un composant Canvas donné. Ce filtre ne retient que les utilisateurs auxquels le message a été explicitement envoyé, et non les autres utilisateurs ayant le même e-mail ou le même numéro de téléphone qui ont reçu des messages en double. Pour capturer les utilisateurs en double, utilisez <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign ou Canvas with Tag.</a><br><br> Pour les cartes de contenu et les messages intégrés, c'est lorsque l'utilisateur enregistre une impression, et non lorsque la carte ou le message intégré est envoyé.<br><br>Pour les notifications push et les webhooks, ceci correspond au moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, c'est lorsque la dernière demande d'API de message est envoyée à WhatsApp, et non lorsque le message est livré sur l'appareil de l'utilisateur. <br><br>Pour les e-mails, c'est lorsque une demande d'e-mail est envoyée au fournisseur de service de messagerie (peu importe si elle est effectivement livrée).<br><br>Pour les SMS, ceci correspond au moment où le dernier message a été livré au fournisseur de SMS. Cela ne garantit pas que le message a été livré à l'appareil de l'utilisateur."
    tags:
      - Retargeting
  - name: Dernier message reçu de l’étape du canvas donnée
    description: "Segmentez vos utilisateurs en fonction du moment où ils ont reçu un composant Canvas spécifique. Ce filtre ne capture que les utilisateurs auxquels le message a été explicitement envoyé, et non les autres utilisateurs ayant le même e-mail ou le même numéro de téléphone qui ont reçu des messages en double. Pour capturer les utilisateurs en double, utilisez <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign ou Canvas with Tag (Message reçu d'une campagne ou d'un canevas avec étiquette)</a>. Ce filtre ne tient pas compte du fait que les utilisateurs ont reçu d'autres composants de Canvas."
    tags:
      - Retargeting
  - name: Dernier message reçu d’une campagne donnée
    description: "Segmente vos utilisateurs selon s’ils ont reçu ou non une campagne donnée. Ce filtre ne capture que les utilisateurs auxquels le message a été explicitement envoyé, et non les autres utilisateurs ayant le même e-mail ou le même numéro de téléphone qui ont reçu des messages en double. Pour capturer les utilisateurs en double, utilisez <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters/#received-message-from-campaign-or-canvas-with-tag\">Received Message from Campaign ou Canvas with Tag (Message reçu d'une campagne ou d'un canevas avec étiquette)</a>. Ce filtre ne tient pas compte du moment où les utilisateurs ont reçu d'autres campagnes."
    tags:
      - Retargeting
  - name: A reçu un message d’une campagne ou d’un canvas avec une balise
    description: "Segmente vos utilisateurs selon s’ils ont reçu ou non une campagne ou un Canvas spécifique avec une balise spécifique. Contrairement à \"Received Message from Campaign\" et \"Received Message from Canvas Step\", ce filtre capture tous les utilisateurs ayant le même e-mail ou le même numéro de téléphone qui ont reçu des messages en double.<br><br> Pour les cartes de contenu, les bannières (campagnes uniquement) et les messages in-app, il s'agit du moment où un utilisateur enregistre une impression, et non du moment où la carte ou le message in-app est envoyé.<br><br>Pour les notifications push et les webhooks, ceci correspond au moment où le message est envoyé à l'utilisateur.<br><br> Pour WhatsApp, c'est lorsque la dernière demande d'API de message est envoyée à WhatsApp, et non lorsque le message est livré sur l'appareil de l'utilisateur. <br><br>Pour les e-mails, c'est lorsque une demande d'e-mail est envoyée au fournisseur de service de messagerie (peu importe si elle est effectivement livrée). Lorsque plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lors de l'envoi initial, seul le profil de l'utilisateur ciblé spécifique est mis à jour. <br>- Lorsque l'e-mail est délivré, ou si l'utilisateur ouvre l'e-mail ou un lien contenu dans l'e-mail, tous les utilisateurs partageant cette adresse e-mail semblent avoir reçu le message.<br><br>Pour les SMS, ceci correspond au moment où le dernier message a été livré au fournisseur de SMS. Cela ne garantit pas que le message a été livré à l'appareil de l'utilisateur."
    tags:
      - Retargeting
  - name: A reçu un message pour la dernière fois d’une campagne ou d’un canvas avec une balise
    description: "Segmentez vos utilisateurs en fonction du moment où ils ont reçu une campagne ou un Canvas spécifique avec une étiquette spécifique. Ce filtre ne tient pas compte du fait que les utilisateurs ont reçu d'autres campagnes ou canevas. (période de 24 heures)"
    tags:
      - Retargeting
  - name: N’a jamais reçu un message issu d’une campagne ou d’une étape de canvas
    description: Segmente vos utilisateurs selon s’ils ont ou non reçu une campagne ou un composant Canvas.
    tags:
      - Retargeting
  - name: Dernier e-mail reçu
    description: "Segmente vos utilisateurs en fonction de la dernière fois où ils ont reçu l’un de vos messages par e-mail. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Retargeting
  - name: Dernière notification push reçue
    description: "Segmentez vos utilisateurs par la dernière fois qu'ils ont reçu l'une de vos notifications push. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Retargeting
  - name: Dernière impression des messages in-app
    description: "Segmentez vos utilisateurs par la dernière fois qu'ils ont vu un message intégré."
    tags:
      - Retargeting
  - name: Dernier SMS reçu
    description: "Segmentez vos utilisateurs en fonction du moment où le dernier message a été livré au fournisseur de SMS. Cela ne garantit pas que le message a été livré à l'appareil de l'utilisateur. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Retargeting
  - name: Dernier webhook reçu
    description: "Segmentez vos utilisateurs par la dernière fois que Braze a envoyé un webhook pour cet utilisateur. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Retargeting
  - name: Dernière réception WhatsApp
    description: "Segmentez vos utilisateurs par la dernière fois qu'ils ont reçu un message WhatsApp. C'est lorsque la dernière demande d'API de message est envoyée à WhatsApp, et non lorsque le message est livré sur l'appareil de l'utilisateur. (période de 24 heures)<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Retargeting
  - name: "Activités en ligne/en production/instantanée enregistrées pour l'application"
    description: "Segmente vos utilisateurs selon qu'ils sont ou non inscrits pour démarrer une ligne/en production/instantanée via les notifications push iOS pour une app spécifique."
    tags:
      - Devices
  - name: Campagne cliquée/ouverte
    description: "Filtrer par interaction avec une campagne spécifique. Pour les envois de messages e-mail, l'événement d'ouverture comprend à la fois les ouvertures machine et les ouvertures non machine.<br><br> Pour les e-mails, vous avez également la possibilité de filtrer par \"a ouvert n'importe quel e-mail (ouverture par la machine)\" et \"a ouvert n'importe quel e-mail (autres ouvertures)\". Les clics sur les liens de désinscription et les centres de préférences ne sont pas pris en compte dans ce filtre. Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur original change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants avec cette adresse e-mail au lieu de l'utilisateur original.<br><br>Pour les SMS, une interaction est définie comme :<br>- L'utilisateur a envoyé un SMS de réponse correspondant à une catégorie de mots-clés donnée pour la dernière fois. Ceci est attribué à la campagne la plus récente reçue par tous les utilisateurs avec ce numéro de téléphone. La campagne doit avoir été reçue au cours des quatre dernières heures.<br>L'utilisateur a sélectionné pour la dernière fois un lien raccourci dans un message SMS avec le suivi des clics activé, provenant d'une campagne donnée."
    tags:
      - Retargeting
  - name: Campagne ou Canvas avec balise cliqué(e)/ouvert(e)
    description: "Filtrer par interaction avec une campagne spécifique qui a une étiquette spécifique. Pour les envois de messages e-mail, l'événement d'ouverture comprend à la fois les ouvertures machine et les ouvertures non machine.<br><br> Pour les e-mails, vous avez la possibilité de filtrer par \"a ouvert n'importe quel e-mail (ouverture par la machine)\" et \"a ouvert n'importe quel e-mail (autres ouvertures)\". Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur original change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants avec cette adresse e-mail au lieu de l'utilisateur original.<br><br>Pour les SMS, une interaction est définie comme :<br>- L'utilisateur a envoyé un SMS de réponse correspondant à une catégorie de mots-clés donnée pour la dernière fois. Ceci est attribué à la campagne la plus récente reçue par tous les utilisateurs avec ce numéro de téléphone. La campagne doit avoir été reçue au cours des quatre dernières heures.<br>Lorsque l'utilisateur a sélectionné pour la dernière fois un lien raccourci dans un message SMS avec le suivi des clics activé, à partir d'une campagne ou d'une étape de Canvas donnée avec une balise."
    tags:
      - Retargeting
  - name: Étape cliquée/ouverte
    description: "Filtrer par interaction avec un composant Canvas spécifique. Pour les envois de messages e-mail, l'événement d'ouverture comprend à la fois les ouvertures machine et les ouvertures non machine.<br><br>Pour les e-mails, vous avez la possibilité de filtrer par \"a ouvert n'importe quel e-mail (ouverture par la machine)\" et \"a ouvert n'importe quel e-mail (autres ouvertures)\".<br><br>Pour les SMS, une interaction est définie comme :<br>- L'utilisateur a envoyé un SMS de réponse correspondant à une catégorie de mots-clés donnée pour la dernière fois. Ceci est attribué à la campagne la plus récente reçue par tous les utilisateurs avec ce numéro de téléphone. La campagne doit avoir été reçue au cours des quatre dernières heures. <br>- L'utilisateur a sélectionné pour la dernière fois un lien raccourci dans un message SMS avec le suivi des clics activé, à partir d'une étape de canvas donnée."
    tags:
      - Retargeting
  - name: Alias cliqué dans la campagne
    description: "Filtrez vos utilisateurs en fonction de savoir s'ils ont cliqué sur un alias spécifique dans une campagne spécifique. Ceci s'applique uniquement aux e-mails. <br><br> Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur original change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants avec cette adresse e-mail au lieu de l'utilisateur original."
    tags:
      - Retargeting
  - name: "Alias cliqué dans l'étape de Canvas"
    description: "Filtrez vos utilisateurs en fonction de leur clic sur un alias spécifique dans un Canvas spécifique. Ceci s'applique uniquement aux e-mails. <br><br> Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur original change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants avec cette adresse e-mail au lieu de l'utilisateur original."
    tags:
      - Retargeting
  - name: "Alias cliqué dans n'importe quelle campagne ou étape de canvas"
    description: "Filtrez vos utilisateurs en fonction de leur clic sur un alias spécifique dans une campagne ou un Canvas. Ceci s'applique uniquement aux e-mails. <br><br> Si plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lorsque l'e-mail est ouvert ou cliqué, tous les autres utilisateurs ayant la même adresse e-mail voient également leur profil mis à jour. <br>- Si l'utilisateur original change son adresse e-mail après l'envoi du message et avant l'ouverture ou le clic, l'ouverture ou le clic est appliqué à tous les utilisateurs restants avec cette adresse e-mail au lieu de l'utilisateur original."
    tags:
      - Retargeting
  - name: "Échec d'envoi définitif"
    description: "Segmente vos utilisateurs selon que leur adresse e-mail a subi ou non un échec d’envoi définitif (par exemple, adresse e-mail non valide)."
    tags:
      - Retargeting
  - name: "Échec provisoire d'envoi"
    description: "Segmentez vos utilisateurs en fonction du nombre d'échecs provisoires d'envoi X fois en Y jours. Les filtres Segment ne peuvent remonter que 30 jours en arrière, mais vous pouvez remonter plus loin grâce aux extensions de segments.<br><br>Ce filtre fonctionne différemment d'un échec provisoire d'envoi dans Currents. Le filtre de segment Soft Bounced comptabilise un échec provisoire d'envoi s'il n'y a pas eu de réception/distribution réussie pendant la période de réessai de 72 heures. Dans Currents, chaque tentative infructueuse est envoyée sous la forme d'un échec provisoire d'envoi." 
    tags:
      - Retargeting
  - name: Vous a marqué comme spam
    description: Segmente vos utilisateurs selon s’ils ont marqué vos messages comme spam.
    tags:
      - Retargeting
  - name: Numéro de téléphone non valide 
    description: Segmente vos utilisateurs selon si leur numéro de téléphone est valide ou non valide.
    tags:
      - Retargeting
  - name: Dernier envoi SMS spécifique Entrant Catégorie de mot-clé
    description: "Segmentez vos utilisateurs en fonction du moment où ils ont envoyé un SMS pour la dernière fois à un groupe d'abonnement spécifique dans une catégorie de mots-clés spécifique." 
    tags:
      - Retargeting
  - name: Convertis par la campagne
    description: Segmente vos utilisateurs selon s’ils ont été convertis ou non grâce à une campagne donnée. Ce filtre n’inclut pas les utilisateurs du groupe de contrôle.
    tags:
      - Retargeting
  - name: Convertis par le Canvas
    description: Segmente vos utilisateurs selon s’ils ont été convertis ou non grâce à un Canvas donné. Ce filtre n’inclut pas les utilisateurs du groupe de contrôle.
    tags:
      - Retargeting
  - name: Dans le groupe de contrôle de campagne
    description: Segmente vos utilisateurs selon s’ils faisaient ou non partie du groupe de contrôle d’une campagne multivariée donnée.
    tags:
      - Retargeting
  - name: Dans le groupe de contrôle de Canvas
    description: "Segmente vos utilisateurs selon s’ils faisaient ou non partie du groupe de contrôle d’un Canvas donné. Ce filtre évalue uniquement les utilisateurs qui sont entrés dans le Canvas.<br><br>Par exemple, si vous filtrez les utilisateurs qui ne font pas partie du groupe de contrôle pour un Canvas, vous recevez tous les utilisateurs qui sont entrés dans le Canvas mais qui ne font pas partie du groupe de contrôle."
    tags:
      - Retargeting
  - name: Dernière inscription dans un groupe de contrôle
    description: "Segmentez vos utilisateurs par la dernière fois qu'ils sont tombés dans le groupe de contrôle d'une campagne. <br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Retargeting
  - name: Entrés dans une variante du Canvas
    description: "Segmente vos utilisateurs selon s’ils sont ou non rentrés dans une variante d’un Canvas donné. Ce filtre évalue tous les utilisateurs.<br><br>Par exemple, si vous filtrez sur les utilisateurs qui ne sont pas entrés dans un groupe de contrôle de variation de Canvas, vous recevez tous les utilisateurs qui ne font pas partie du groupe de contrôle, qu'ils soient entrés ou non dans le Canvas."
    tags:
      - Retargeting
  - name: Dernier message reçu
    description: "Segmentez vos utilisateurs en déterminant le dernier message reçu. (période de 24 heures)<br><br> Pour les cartes de contenu, les bannières et les messages in-app, il s'agit de la date à laquelle un utilisateur a enregistré une impression pour la dernière fois, et non de la date à laquelle la carte ou le message in-app a été envoyé pour la dernière fois.<br><br>Pour les notifications push et les webhooks, c'est lorsque tout message a été envoyé à l'utilisateur.<br><br> Pour WhatsApp, c'est lorsque la dernière demande d'API de message a été envoyée à WhatsApp, et non lorsque le message a été livré sur l'appareil de l'utilisateur. <br><br>Pour les e-mails, c'est lorsque une demande d'e-mail est envoyée au fournisseur de service de messagerie (peu importe si elle est effectivement livrée). Lorsque plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lors de l'envoi initial, seul le profil de l'utilisateur ciblé spécifique est mis à jour. <br>- Lorsque l'e-mail est délivré, ou si l'utilisateur ouvre l'e-mail ou un lien contenu dans l'e-mail, tous les utilisateurs partageant cette adresse e-mail semblent avoir reçu le message.<br><br>Pour les SMS, ceci correspond au moment où le dernier message a été livré au fournisseur de SMS. Cela ne garantit pas que le message a été livré à l'appareil de l'utilisateur.<br><br>Exemple :<br>Dernier message reçu il y a moins de 1 jour = il y a moins de 24 heures<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Retargeting
  - name: Dernière interaction avec un message
    description: "Segmente vos utilisateurs en fonction de la dernière fois qu'ils ont cliqué ou ouvert l'un de vos canaux d'envoi de messages (Bannières, carte de contenu, e-mail, in-app, SMS, push, WhatsApp). Pour les envois de messages e-mail, l'événement d'ouverture comprend à la fois les ouvertures machine et les ouvertures non machine. (période de 24 heures)<br><br>Pour les e-mails, c'est lorsque une demande d'e-mail est envoyée au fournisseur de service de messagerie (peu importe si elle est effectivement livrée). Vous avez également la possibilité de filtrer par \"a ouvert n'importe quel e-mail (ouverture par la machine)\" et \"a ouvert n'importe quel e-mail (autres ouvertures)\". Lorsque plusieurs utilisateurs partagent la même adresse e-mail :<br>- Lors de l'envoi initial, seul le profil de l'utilisateur ciblé spécifique est mis à jour. <br>- Lorsque l'e-mail est délivré, ou si l'utilisateur ouvre l'e-mail ou un lien contenu dans l'e-mail, tous les utilisateurs partageant cette adresse e-mail semblent avoir reçu le message.<br><br>Pour les SMS, c'est lorsque l'utilisateur a sélectionné pour la dernière fois un lien raccourci dans un message avec le suivi des clics activé.<br><br>Fuseau horaire :<br>Fuseau horaire de l’entreprise"
    tags:
      - Retargeting
  - name: Carte cliquée 
    description: "Segmente vos utilisateurs selon qu’ils aient cliqué ou non sur une carte de contenu donnée. Ce filtre est disponible en tant que sous-filtre de « Campagne cliquée/ouverte », « Campagne ou Canvas avec balise cliqué/ouvert » et « Étape cliquée/ouverte »."
    tags:
      - Retargeting
  - name: Indicateurs de fonctionnalité
    description: "Le segment de vos utilisateurs qui ont actuellement activé un <a href=\"/docs/developer_guide/feature_flags/\">flag de fonctionnalité</a> particulier."
    tags:
      - Retargeting
  - name: Groupe d’abonnement
    description: "Segmentez vos utilisateurs par leur groupe d'abonnement pour l'e-mail, le SMS/MMS ou WhatsApp. Les groupes archivés n'apparaissent pas et ne peuvent pas être utilisés."
    tags:
      - Channel subscription behavior
  - name: Adresse e-mail disponible
    description: "Segmente vos utilisateurs selon qu'ils ont une adresse e-mail valide ou qu'ils sont abonnés ou non à l'e-mail. Ce filtre vérifie trois critères : si l'utilisateur s'est désabonné des e-mails, si Braze a reçu un échec définitif et si l'e-mail a été marqué comme spam. Si l'un de ces critères est rempli, ou si un e-mail n'existe pas pour un utilisateur, celui-ci n'est pas inclus.<br><br>Notez que si vous envoyez un message transactionnel, les utilisateurs dont l'\"e-mail disponible\" est <code>false</code> ne sera pas inclus dans le calcul de l'audience mais pourra tout de même recevoir un message. Cependant, le calcul de l'audience ne prend en compte que les utilisateurs abonnés ou ayant opté pour un abonnement. <br><br>Pour les messages électroniques pour lesquels le statut d'abonnement est important, nous vous suggérons d'utiliser le filtre \"Email disponible\" au lieu du filtre \" <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#email-address\">Adresse e-mail\"</a>; les critères supplémentaires peuvent vous aider à cibler les utilisateurs qui veulent vraiment voir vos messages."
    tags:
      - Channel subscription behavior
  - name: Date d’abonnement aux e-mails
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils se sont abonnés aux communications par e-mail.
    tags:
      - Channel subscription behavior
  - name: État d’abonnement aux e-mails
    description: Segmente vos utilisateurs en fonction du statut de leur abonnement aux communications par e-mail.
    tags:
      - Channel subscription behavior
  - name: Date de désinscription aux e-mails 
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils se sont désabonnés des futures communications par e-mail.
    tags:
      - Channel subscription behavior
  - name: Notification push au premier plan activée
    description: "Segmentez vos utilisateurs qui ont une autorisation de push provisoire ou qui sont activés pour le push au premier plan. Ce décompte inclut plus précisément :<br>1. Les utilisateurs d'iOS qui sont provisoirement autorisés pour les notifications push. <br>2. Les utilisateurs qui sont activés pour le push au premier plan et dont le statut d'abonnement au push n'est pas désabonné, pour n'importe laquelle de vos applications. Pour ces utilisateurs, ce décompte inclut uniquement les notifications push au premier plan.<br><br>Les utilisateurs qui se sont désinscrits ne sont pas pris en compte dans le calcul de l'option \"Foreground Push Enabled\". <br><br>Après avoir segmenté avec ce filtre, vous pouvez voir une répartition des personnes qui font partie de cette segmentation pour Android, iOS et le web dans le panneau du bas, appelé <em>Utilisateurs joignables</em>."
    tags:
      - Channel subscription behavior
  - name: Notifications push en avant-plan activées pour l’application
    description: "Segments par le fait que les utilisateurs ont activé les notifications push pour votre application sur leur appareil. Utilisateurs pour lesquels la fonction \"push\" est activée au premier plan pour une application. Cela ne tient pas compte de l'état de l'abonnement au service \"push\". Ce décompte inclut les utilisateurs qui ont provisoirement autorisé les jetons de notification push en premier plan et en arrière-plan."
    tags:
      - Channel subscription behavior
  - name: "Notifications push d'arrière-plan ou d'avant-plan activées"
    description: "Segmentation selon que les utilisateurs ont un jeton de poussée et ne se sont pas désabonnés. Utilisateurs pour lesquels la fonction push est activée en arrière-plan ou en avant-plan pour l'une de vos applications."
    tags:
      - Channel subscription behavior
  - name: Date d’abonnement aux notifications push
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils ont activé les notifications push.
    tags:
      - Channel subscription behavior
  - name: État d’abonnement aux notifications push
    description: "Segmente vos utilisateurs en fonction de leur <a href=\"/docs/user_guide/message_building_by_channel/push/users_and_subscriptions/#push-subscription-state\">statut de leur inscription</a> aux notifications push."
    tags:
      - Channel subscription behavior
  - name: Date de désinscription aux notifications push
    description: Segmente vos utilisateurs en fonction de la date à laquelle ils se sont désinscrits des notifications push.
    tags:
      - Channel subscription behavior
  - name: Produit acheté
    description: Segmente vos utilisateurs en fonction des produits qu’ils ont achetés dans votre application.
    tags:
      - Purchase behavior
  - name: Nombre total d’achats
    description: Segmente vos utilisateurs en fonction du nombre d’achats qu’ils ont effectués dans votre application.
    tags:
      - Purchase behavior
  - name: X produits achetés au cours des Y derniers jours
    description: "Filtrer les utilisateurs par le nombre de fois qu'un produit spécifique a été acheté."
    tags:
      - Purchase behavior
  - name: X achats dans les Y derniers jours
    description: "Segmente vos utilisateurs en fonction du nombre de fois (entre 0 et 50) qu’ils ont effectué un achat dans le dernier nombre de jours civils indiqué, compris entre 1 et 30. <br> <a href=\"/docs/x-in-y-behavior/\">En savoir plus sur le comportement « X dans Y » ici.</a>"
    tags:
      - Purchase behavior
  - name: X propriétés d’achat en Y jours
    description: "Segmente vos utilisateurs en fonction du nombre de fois où un achat a été effectué par rapport à une certaine propriété d’achat dans le dernier nombre de jours civils indiqué, compris entre 1 et 30. <br> <a href=\"/docs/x-in-y-behavior/\">En savoir plus sur le comportement « X dans Y » ici.</a>"
    tags:
      - Purchase behavior
  - name: Premier achat
    description: Segmentez vos utilisateurs par le premier moment où un utilisateur a effectué un achat dans votre application.
    tags:
      - Purchase behavior
  - name: "Premier achat pour l'application"
    description: Segmentez vos utilisateurs par le premier moment où un utilisateur a effectué un achat depuis votre application.
    tags:
      - Purchase behavior
  - name: Dernier achat effectué
    description: "Filtrer les utilisateurs par la dernière fois qu'ils ont effectué un achat."
    tags: 
      - Purchase behavior
  - name: Dernier produit acheté
    description: Filtrer les utilisateurs en fonction de la date à laquelle ils ont acheté un produit spécifique pour la dernière fois.
    tags:
      - Purchase behavior
  - name: Argent dépensé
    description: Segmente vos utilisateurs en fonction du montant qu’ils ont dépensé dans votre application.
    tags:
      - Purchase behavior
  - name: X argent dépensé en Y jours
    description: "Segmente vos utilisateurs en fonction du montant dépensé dans votre application au cours du dernier nombre de jours civils indiqué, compris entre 1 et 30. Ce montant ne comprend que la somme des 50 derniers achats. <br> <a href=\"/docs/x-in-y-behavior/\">En savoir plus sur le comportement « X dans Y » ici.</a>"
    tags:
      - Purchase behavior
  - name: Dernière commande passée (730 derniers jours)
    description: "Segmente vos utilisateurs en fonction de la date à laquelle ils ont passé leur dernière commande, qui est basée sur l'<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement recommandé par eCommerce</a> pour la commande passée (les espaces de travail qui ne suivent pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour, et la fenêtre d'observation maximale est celle des deux dernières années.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Nombre total de commandes (730 derniers jours)
    description: "Segmente vos utilisateurs en fonction du nombre total de commandes passées par un utilisateur au cours des deux dernières années, sur la base de l' <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour la commande passée (les espaces de travail qui ne suivent pas les événements eCommerce ne disposent pas de données pour ce filtre). Ce décompte exclut les commandes annulées, qui doivent être suivies à l'aide de l'<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement recommandé par l'eCommerce</a> pour les commandes annulées. Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Nombre total de commandes
    description: "Segmente vos utilisateurs en fonction du nombre total de commandes passées par un utilisateur au cours de sa vie, sur la base de l' <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour la commande passée (les espaces de travail qui ne suivent pas les événements eCommerce ne disposent pas de données pour ce filtre). Ce décompte exclut les commandes annulées, qui doivent être suivies à l'aide de l'<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement recommandé par l'eCommerce</a> pour les commandes annulées. Les utilisateurs sont évalués pour ce filtre en temps réel.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Nombre total de commandes annulées (730 derniers jours)
    description: "Segmente vos utilisateurs en fonction du nombre total de commandes annulées par un utilisateur au cours des deux dernières années, sur la base de l'<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement recommandé par eCommerce</a> pour la commande passée (les espaces de travail qui ne suivent pas les événements eCommerce ne disposent pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Valeur vie client (730 derniers jours)
    description: "Segmente vos utilisateurs en fonction du chiffre d'affaires total qu'un utilisateur est censé générer au cours de son historique d'achat avec votre marque. Le calcul porte sur les 730 derniers jours et prend la valeur moyenne des commandes (AOV), la multiplie par le nombre total de commandes passées, puis tient compte de la durée d'achat active de l'utilisateur (le temps écoulé entre sa première et sa dernière commande). Ce filtre utilise les données suivies dans les <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événements recommandés par eCommerce</a>(les espaces de travail qui ne suivent pas les événements eCommerce ne disposent pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Valeur totale des remboursements (730 derniers jours)
    description: "Segmente vos utilisateurs en fonction de la valeur des remboursements accordés à un utilisateur au cours des deux dernières années, sur la base de l'<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement recommandé par eCommerce</a> pour la commande remboursée (les espaces de travail qui ne suivent pas les événements eCommerce ne disposent pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Valeur totale du remboursement
    description: "Segmente vos utilisateurs en fonction de la valeur totale des remboursements accordés à un utilisateur au cours de sa vie, sur la base de l'<a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement recommandé par eCommerce</a> pour la commande remboursée (les espaces de travail qui ne suivent pas les événements eCommerce ne disposent pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre en temps réel.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: "Chiffre d'affaires total (730 derniers jours)"
    description: "Segmente vos utilisateurs en fonction du chiffre d'affaires total généré par les commandes d'un utilisateur au cours des deux dernières années, calculé en soustrayant le chiffre d'affaires associé à l' <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour la commande remboursée du chiffre d'affaires associé à l'événement eCommerce pour la commande passée (les espaces de travail qui ne suivent pas les événements eCommerce ne disposent pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Total des revenus
    description: "Segmente vos utilisateurs en fonction du chiffre d'affaires total généré par les commandes d'un utilisateur tout au long de sa vie, calculé en soustrayant le chiffre d'affaires associé à l' <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour la commande remboursée du chiffre d'affaires associé à l'événement eCommerce pour la commande passée (les espaces de travail qui ne suivent pas les événements eCommerce n'ont pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre en temps réel.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Valeur moyenne des commandes (730 derniers jours)
    description: "Segmente vos utilisateurs en fonction de la valeur moyenne des commandes passées par un utilisateur au cours des deux dernières années, sur la base de l' <a href=\"/docs/user_guide/data/activation/custom_data/recommended_events/ecommerce_events\">événement eCommerce recommandé</a> pour la commande passée (les espaces de travail qui ne suivent pas les événements eCommerce ne disposent pas de données pour ce filtre). Les utilisateurs sont évalués pour ce filtre une fois par jour.<br><br>Ce filtre est en version bêta. Contactez votre gestionnaire de compte Braze si vous souhaitez utiliser ce filtre."
    tags:
      - eCommerce
  - name: Pays
    description: Segmente vos utilisateurs en fonction de leur dernier pays indiqué.
    tags:
      - Demographic attributes
  - name: Ville
    description: Segmente vos utilisateurs en fonction de leur dernière ville indiquée.
    tags:
      - Demographic attributes
  - name: Langue
    description: Segmente vos utilisateurs en fonction de leur langue préférée.
    tags:
      - Demographic attributes
  - name: Âge
    description: "Segmente vos utilisateurs en fonction de leur âge, comme indiqué dans votre application."
    tags:
      - Demographic attributes
  - name: Anniversaire
    description: "Segmente vos utilisateurs en fonction de leur date d’anniversaire, comme indiqué dans votre application. <br> Les utilisateurs dont la date d'anniversaire est le 29 février sont inclus dans les segmentations incluant le 1er mars.<br><br>Pour cibler les anniversaires de décembre ou de janvier, insérez uniquement la logique de filtrage dans la période de 12 mois de l'année que vous ciblez. En d'autres termes, ne pas insérer de logique qui se réfère au mois de décembre de l'année civile précédente ou à janvier de l'année suivante. Par exemple, pour cibler les anniversaires de décembre, vous pouvez filtrer sur « le 31 décembre », « avant le 31 décembre » ou « après le 30 novembre »."
    tags:
      - Demographic attributes
  - name: Genre
    description: "Segmente vos utilisateurs en fonction de leur sexe, comme indiqué dans votre application."
    tags:
      - Demographic attributes
  - name: Numéro de téléphone non formaté
    description: "Segmente vos utilisateurs en fonction de leur numéro de téléphone non formaté. Ne comprend pas de parenthèses, de tirets ou d'autres symboles."
    tags:
      - Demographic attributes
  - name: Prénom
    description: "Segmente vos utilisateurs en fonction de leur prénom, comme indiqué dans votre application."
    tags:
      - Demographic attributes
  - name: Nom
    description: "Segmente vos utilisateurs en fonction de leur nom de famille, comme indiqué dans votre application."
    tags:
      - Demographic attributes
  - name: A une application
    description: "Segmente vos utilisateurs selon s’ils ont installé ou non votre application à un moment donné. Il s'agit des utilisateurs qui ont installé votre application et de ceux qui l'ont désinstallée par le passé. Cela exige généralement que les utilisateurs ouvrent l’application (démarrer une session) à inclure dans ce filtre. Cependant, il existe certaines exceptions, comme si un utilisateur a été importé dans Braze et associé manuellement à votre application."
    tags:
      - App
  - name: Nom de la version la plus récente de l’application
    description: "Segments par le nom récent de l'application de l'utilisateur.<br><br>Lorsque vous utilisez \"less than\" ou \"less than or equal to\", si la version de l'application principale n'existe pas, ce filtre renvoie `vrai` car l'utilisateur est plus ancien que la version de l'application. Cela signifie que si la dernière version de l'application principale de l'utilisateur n'existe pas, elle correspond automatiquement au filtre."
    tags:
      - App 
  - name: Numéro de version de l’application la plus récente
    description: "Segments par le numéro de version récente de l'application de l'utilisateur.<br><br>Lorsque vous utilisez \"less than\" ou \"less than or equal to\", si la version de l'application principale n'existe pas, ce filtre renvoie `vrai` car l'utilisateur est plus ancien que la version de l'application. Cela signifie que si la dernière version de l'application principale de l'utilisateur n'existe pas, elle correspond automatiquement au filtre.<br><br>Il peut s'écouler un certain temps avant que les versions actuelles de l'application ne soient mises à jour. La version de l'app sur le profil utilisateur se met à jour lorsque les informations sont capturées par le SDK, qui s'appuie sur le moment où les utilisateurs ouvrent leurs apps. Si l'utilisateur n'ouvre pas l'application, la version actuelle ne sera pas mise à jour. Ces filtres ne s'appliquent pas non plus rétroactivement. Il est bon d'utiliser \"supérieur à\" ou \"égal à\" pour les versions actuelles et futures, mais l'utilisation de filtres de versions antérieures peut entraîner des comportements inattendus."
    tags:
      - App 
  - name: Application désinstallée
    description: Segmente vos utilisateurs selon s’ils ont désinstallé votre application sans l’avoir réinstallée.
    tags:
      - Uninstall 
  - name: Opérateur mobile
    description: Segmente vos utilisateurs en fonction de leur opérateur mobile.
    tags:
      - Devices
  - name: Nombre d’appareils
    description: Segmente vos utilisateurs en fonction du nombre d’appareils avec lequel ils ont consulté votre application.
    tags:
      - Devices
  - name: Modèle de l’appareil
    description: Segmente vos utilisateurs en fonction de la version du modèle de leur smartphone.
    tags:
      - Devices
  - name: Système d’exploitation de l’appareil
    description: "Segmente vos utilisateurs qui ont un appareil ou plus comportant le système d’exploitation donné. Pour segmenter les utilisateurs en fonction d'une série de systèmes d'exploitation, utilisez le filtre <a href=\"/docs/user_guide/engagement_tools/segments/segmentation_filters#device-os-version-number\">Numéro de version du système d'exploitation de l'appareil.</a> "
    tags:
      - Devices
  - name: "Numéro de version du système d'exploitation de l’appareil"
    description: "Segmente vos utilisateurs qui possèdent un ou plusieurs appareils dont la version du système d'exploitation se situe dans une fourchette spécifiée. Par exemple, vous pouvez cibler les utilisateurs dont la version du système d'exploitation iOS est supérieure ou égale à 26.0."
    tags:
      - Devices
  - name: Emplacement le plus récent de l’appareil
    description: "Segmente vos utilisateurs en fonction de l’<a href=\"/docs/user_guide/engagement_tools/campaigns/ideas_and_strategies/localizing_a_campaign/\">information de localisation</a> à partir de l’appareil utilisé le plus récemment."
    tags:
      - Devices      
  - name: Modèle de montre le plus récent
    description: Segmente vos utilisateurs en fonction du modèle le plus récent de leur montre connectée.
    tags:
      - Devices    
  - name: Autorisés provisoirement sur iOS
    description: Ce filtre vous permet de trouver des utilisateurs qui sont provisoirement autorisés sur iOS 12 pour une application donnée.
    tags:
      - Devices   
  - name: Navigateur Web
    description: Segmente vos utilisateurs en fonction du navigateur Web qu’ils utilisent pour accéder à votre site Internet.
    tags:
      - Devices
  - name: IDFA de l’appareil
    description: Ce filtre vous permet de désigner les destinataires de votre campagne par IDFA pour mener des tests.
    tags:
      - Advertising use cases
  - name: IDFV de l’appareil
    description: Ce filtre vous permet de désigner les destinataires de votre campagne par IDFV pour mener des tests.
    tags:
      - Advertising use cases 
  - name: ID publicitaire Google de l’appareil
    description: "Segmentez vos utilisateurs par l'identifiant publicitaire Google."
    tags:
      - Advertising use cases
  - name: ID publicitaire Roku de l’appareil
    description: "Segmentez vos utilisateurs par l'ID publicitaire Roku."
    tags:
      - Advertising use cases
  - name: ID publicitaire Windows de l’appareil
    description: "Segmentez vos utilisateurs par l'ID publicitaire Windows."
    tags:
      - Advertising use cases  
  - name: Suivi des campagnes publicitaires activé
    description: "Vous permet de filtrer en fonction de si vos utilisateurs ont choisi de participer au suivi publicitaire. Le suivi des campagnes publicitaires est lié à l’IDFA (Identifier For Advertisers, ou identifiant pour les annonceurs) attribué par Apple pour identifier les appareils des utilisateurs d’iOS, ce qui peut être défini par les SDK. Cet identifiant permet aux annonceurs de suivre les utilisateurs et de leur envoyer des publicités ciblées."
    tags:
      - Advertising use cases
  - name: La localisation la plus récente
    description: Segmente vos utilisateurs en fonction du dernier emplacement enregistré depuis lequel ils ont utilisé votre application.
    tags:
      - Location
  - name: Localisation disponible
    description: "Segmente vos utilisateurs selon s’ils ont indiqué ou non leur localisation. Pour utiliser ce filtre, votre application doit <a href=\"/docs/search/?query=location%20tracking\">inclure une fonction de géolocalisation.</a>"
    tags:
      - Location
  - name: Cohortes Amplitude
    description: Les clients utilisant Amplitude peuvent enrichir leurs segments en choisissant et en important leurs cohortes dans Amplitude.
    tags:
      - Cohort membership
  - name: Cohortes du census
    description: Les clients qui utilisent Census peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Census.
    tags:
      - Cohort membership
  - name: Cohortes Heap
    description: Les clients qui utilisent Heap peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Heap.
    tags:
      - Cohort membership
  - name: Cohortes Hightouch
    description: Les clients qui utilisent Hightouch peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Hightouch.
    tags:
      - Cohort membership
  - name: Cohortes Kubit
    description: Les clients qui utilisent Kubit peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Kubit.
    tags:
      - Cohort membership
  - name: Cohortes Mixpanel
    description: Les clients qui utilisent Mixpanel peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Mixpanel.
    tags:
      - Cohort membership
  - name: Cohortes du segment
    description: Les clients qui utilisent Segment peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Segment.
    tags:
      - Cohort membership
  - name: Cohortes Tinyclues
    description: Les clients qui utilisent Tinyclues peuvent compléter leurs segments en choisissant et en important leurs cohortes dans Tinyclues.
    tags:
      - Cohort membership
  - name: Annonce d’attribution d’installation
    description: Segmente vos utilisateurs en fonction de l’annonce à laquelle leur installation a été attribuée.
    tags:
      - User Attributes
  - name: Groupe d’annonces d’attribution d’installation
    description: "Segmentez vos utilisateurs par le groupe d'annonces auquel leur installation a été attribuée."
    tags:
      - Install Attribution
  - name: Campagne d’attribution d’installation
    description: Segmente vos utilisateurs en fonction de la campagne publicitaire à laquelle leur installation a été attribuée.
    tags:
      - Install Attribution
  - name: Source d’attribution d’installation
    description: Segmente vos utilisateurs en fonction de la source à laquelle leur installation a été attribuée.
    tags:
      - Install Attribution
  - name: Catégorie de risque d’attrition
    description:  Segmentez vos utilisateurs par catégorie de risque de désabonnement selon une prédiction spécifique.
    tags:
      - Intelligence and predictive
  - name: Score du risque d’attrition
    description: Segmentez vos utilisateurs par score de risque de désabonnement selon une prédiction spécifique.
    tags:
      - Intelligence and predictive
  - name: Catégorie de probabilité d’événement
    description: "Segmentez vos utilisateurs en fonction de la probabilité qu'ils effectuent un événement selon une prédiction spécifique."
    tags:
      - Intelligence and predictive
  - name: Score de probabilité d’événement
    description: "Segmentez vos utilisateurs en fonction de la probabilité qu'ils effectuent un événement selon une prédiction spécifique."
    tags:
      - Intelligence and predictive
  - name: Canal intelligent
    description: Segmentez vos utilisateurs par leur canal le plus actif au cours des trois derniers mois.
    tags:
      - Intelligence and predictive
  - name: Probabilité d’ouverture des messages
    description: "Filtre vos utilisateurs en fonction de leur probabilité d'ouvrir un message sur un canal spécifié sur une échelle de 0 à 100%. Les utilisateurs sans données suffisantes pour mesurer une probabilité pour une chaîne peuvent être sélectionnés en utilisant \"est vide.\"<br><br>Pour les e-mails, les ouvertures de machines sont exclues du calcul de la probabilité."
    tags:
      - Intelligence and predictive
  - name: Nombre d’amis Facebook utilisant l’application
    description: "Segmentez vos utilisateurs en fonction du nombre d'amis Facebook qu'ils ont qui utilisent la même application."
    tags:
      - Social activity
  - name: Connectés à Facebook
    description: Segmentez vos utilisateurs en fonction de leur connexion de votre application à Facebook.
    tags:
      - Social activity
  - name: Connectés à Twitter
    description: Segmentez vos utilisateurs en fonction de leur connexion de votre application à X (anciennement Twitter).
    tags:
      - Social activity
  - name: Nombre de followers sur Twitter
    description: "Segmentez vos utilisateurs en fonction du nombre de followers qu'ils ont sur X (anciennement Twitter)."
    tags:
      - Social activity
  - name: Numéro de téléphone
    description: "Segmente vos utilisateurs en fonction du champ du numéro de téléphone au format E.164.<br><br> Lorsqu'un numéro de téléphone est envoyé à Braze, Braze tente de le contraindre au <a href=\"/docs/user_guide/message_building_by_channel/sms/phone_numbers/user_phone_numbers/#importing-phone-numbers\">format e.164</a> qui est utilisé pour l'envoi à travers les canaux SMS et WhatsApp. Le processus de coercition peut échouer si le numéro n'est pas formaté correctement, ce qui fait que le profil utilisateur a un numéro de téléphone non formaté mais pas de numéro de téléphone d'envoi. Ce filtre de segmentation renvoie les utilisateurs en fonction de leur numéro de téléphone au format e.164 (lorsqu'il est disponible).<br><br>Cas d'utilisation :<br> - Utilisez ce filtre pour comprendre la taille de l'audience cible la plus précise lors de l'envoi de SMS ou de messages WhatsApp.  <br>- Utilisez des expressions régulières (regex) avec ce filtre pour segmenter les numéros de téléphone avec un code pays spécifique. <br>- Utilisez ce filtre pour segmenter les utilisateurs en fonction des numéros de téléphone qui n'ont pas passé le processus de coercition e.164."
    tags:
      - Other filters
---
