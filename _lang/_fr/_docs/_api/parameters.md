---
page_order: 2.4
nav_title: Paramètres
article_title: Paramètres de l'API
layout: glossary_page
glossary_top_header: "Paramètres"
glossary_top_text: "Utilisez ces paramètres pour définir vos requêtes API. Bien que les paramètres dont vous avez besoin soient listés sous les terminaux, cela devrait vous donner plus de détails sur leurs nuances et autres spécifications."
description: "Ce glossaire couvre en détail les paramètres impliqués dans la réalisation de requêtes API."
page_type: glossary
glossaries:
  - 
    name: Clé d'API REST groupe d'applications
    description: La <code>api_key</code> indique le titre de l'application avec laquelle les données de cette requête sont associées et authentifie le demandeur en tant que personne autorisée à envoyer des messages à l'application. Il doit être inclus avec chaque requête en tant qu'en-tête d'autorisation HTTP. Il se trouve dans la section <strong>Console développeur</strong> du tableau de bord Braze.
    field: "Clé api_key"
  - 
    name: App Identifier
    description: Si vous voulez envoyer des push à un ensemble de jetons de l'appareil (au lieu des utilisateurs), vous devez indiquer au nom de quelle application spécifique vous envoyez des messages. Dans ce cas, vous fournirez l'identifiant d'application approprié dans un objet Tokens. Il se trouve dans la section <strong>Console développeur</strong> du tableau de bord Braze.
    field: "app_id"
  - 
    name: ID d'utilisateur externe
    description: Un identifiant unique pour envoyer un message à des utilisateurs spécifiques. Cet identifiant devrait être le même que celui que vous avez défini dans le Braze SDK. Vous ne pouvez cibler que les utilisateurs qui ont déjà été identifiés via le SDK ou l'API de l'utilisateur. Un maximum de 50 identifiants d'utilisateurs externes sont autorisés dans une requête. <br> <br> Pour déclencher des terminaux de campagne, si vous fournissez ce champ, les critères seront calqués avec les segments de la campagne et seuls les utilisateurs qui sont dans la liste des identifiants d'utilisateurs externes et le segment de la campagne recevront le message.
    field: "ID_utilisateur_externe"
  - 
    name: Segment Identifier
    description: Le <code>segment_id</code> indique le segment auquel le message doit être envoyé. Un identificateur de segment pour chacun des segments que vous avez créés se trouve dans la section <strong>Console de développeur</strong> du tableau de bord Braze. <br> <br> Pour les terminaisons du message, si vous fournissez à la fois un identifiant de segment et une liste des identifiants d'utilisateurs externes dans une seule demande de messagerie. les critères seront calqués et seuls les utilisateurs qui se trouvent dans la liste des identifiants d'utilisateurs externes et le segment fourni recevront le message.
    field: "identifiant_segment"
  - 
    name: Identifiant de la campagne
    description: Pour les terminaux de messagerie, la <code>campaign_id</code> indique la campagne API dans laquelle les analytiques d'un message doivent être suivies. Un identifiant de campagne pour chacune des campagnes que vous avez créées se trouve dans la section <strong>Console de développeur</strong> du tableau de bord de Braze. Si vous fournissez un identifiant de campagne dans le corps de la requête, vous devez fournir un <code>message_variation_id</code> dans chacun des objets du message indiquant la variante représentée de votre campagne. <br> <br> Pour les fins de déclenchement de la campagne, le <code>campaign_id</code> indique l'ID API de la campagne à déclencher. Ce champ est requis pour toutes les requêtes de point de terminaison de déclenchement.
    field: "campaign_id"
  - 
    name: Identifiant du canevas
    description: Pour les terminaux déclencheurs de Canvas , le <code>canvas_id</code> indique l'identifiant du Canvas à déclencher ou à planifier. Ce champ est requis pour toutes les requêtes de point de terminaison de déclenchement.
    field: "id_toile"
  - 
    name: Envoyer l'identifiant
    description: Pour les points de terminaison de messagerie, le <code>send_id</code> indique l'envoi sous lequel les analytiques d'un message doivent être suivies. Le <code>send_id</code> vous permet de récupérer des analytiques pour une instance spécifique d'une campagne envoyée via le point de terminaison <code>sends/data_series</code>. Les campagnes de déclenchement API et API envoyées en tant que diffusion génèreront automatiquement un identifiant d'envoi si un identifiant d'envoi n'est pas fourni. <br> <br> Si vous voulez spécifier votre propre <code>send_id</code>, vous devez d'abord en créer un via le <code>sends/id/create</code> endpoint. Le <code>send_id</code> doit être tous les caractères ASCII et au plus 64 caractères de long.  Vous pouvez réutiliser un identifiant d'envoi à travers plusieurs envois de la même campagne si vous voulez grouper l'analyse de ces envois ensemble. <br> <br> Veuillez noter que le suivi <code>send_id</code> n'est pas disponible pour les e-mails envoyés via Mailjet. <br> <br> Les conversions de campagne sont attribuées au dernier <code>send_id suivi</code> que l'utilisateur a reçu de cette campagne, à moins que le dernier envoi de l'utilisateur reçu ne soit désuivi.
    field: "id_expéditeur"
  - 
    name: Propriétés du déclencheur
    description: "Lors de l'utilisation d'un des terminaux pour envoyer une campagne avec la livraison déclenchée par API, vous pouvez fournir une carte des clés et des valeurs pour personnaliser votre message. Si vous faites une requête API qui contient un objet dans <code>\"trigger_properties\"</code>, les valeurs de cet objet peuvent alors être référencées dans votre modèle de message sous l'espace de noms <code>api_trigger_properties</code>. <br> <br> Par exemple, une requête avec <code>\"trigger_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79. 9}</code> pourrait ajouter le mot \"chaussures\" au message en ajoutant <code>{{api_trigger_properties.${product_name}}}</code>."
    field: "format@@0 trigger_properties"
  - 
    name: Propriétés de l'entrée de la toile
    description: "Lorsque vous utilisez l'un des points de terminaison pour déclencher ou planifier un Canvas via l'API, vous pouvez fournir une carte des clés et des valeurs pour personnaliser les messages envoyés par les premières étapes de votre Canvas, dans l'espace de noms <code>\"canvas_entry_properties\"</code>. <br> <br> Par exemple, une requête avec <code>\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79. 9}</code> pourrait ajouter le mot \"chaussures\" à un message en ajoutant <code>{{canvas_entry_properties.${product_name}}}</code>."
    field: "Propriétés de la toile"
  - 
    name: Diffusion
    description: "Lorsque vous envoyez un message à un public de segment ou de campagne en utilisant un point de terminaison de l'API, Braze vous demande de définir explicitement si votre message est ou non un « envoyer » à un grand groupe d'utilisateurs en incluant un booléen <code>broadcast</code> dans l'appel API. C'est-à-dire, si vous avez l'intention d'envoyer un message API à l'ensemble du segment qu'une campagne ou Canvas cible, vous devez inclure <code>broadcast: true</code> dans votre appel API. <br><br>La diffusion est un champ requis et la valeur par défaut définie par Braze lorsqu'une campagne ou Canvas est faite est <code>diffusée : false</code>. Vous ne pouvez pas avoir à la fois la liste <code>broadcast: true</code> et une liste de destinataires <code></code> spécifiée. Si le drapeau <code>broadcast</code> est défini à true et qu'une liste explicite de destinataires est fournie, le point de terminaison de l'API retournera une erreur. De même, y compris <code>broadcast: false</code> et ne pas fournir de liste de destinataires retournera une erreur. \n<br><br>Faites preuve de prudence lorsque vous mettez <code>broadcast: true</code>, comme paramétrage involontaire de ce drapeau peut vous faire envoyer votre campagne ou Canvas à un public plus grand que prévu. Le drapeau <code>diffusion</code> est requis pour se protéger contre les envois accidentels à de grands groupes d'utilisateurs."
    field: "Diffusion"
---

