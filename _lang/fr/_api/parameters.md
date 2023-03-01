---
page_order: 2.4
nav_title: Paramètres
article_title: Paramètres d’API
layout: glossary_page
glossary_top_header: "Paramètres"
glossary_top_text: "Utilisez ces paramètres pour définir vos demandes API. Les paramètres dont vous avez besoin sont affichés sous les endpoints, mais cette liste exhaustive vous donnera plus d’informations sur leurs nuances et autres spécifications."

description: "Ce glossaire traite en détail les paramètres impliqués dans la réalisation des demandes API." 
page_type: glossary

glossaries:
  - name: Clé API REST du groupe d’apps
    description: La <code>api_key</code> indique le titre de l’application avec laquelle les données de cette demande sont associées et authentifie le demandeur comme quelqu’un qui est autorisé à envoyer des messages à l’application. Elle doit être incluse dans chaque demande comme en-tête d’autorisation HTTP. Elle se trouve dans la section <strong>Developer Console (Console du développeur)</strong> du tableau de bord de Braze.
    field: "api_key"
  - name: Identifiant d’application
    description: Si vous souhaitez envoyer des notifications push à un ensemble de jetons de périphérique (plutôt qu’à des utilisateurs), vous devez indiquer au nom de quelle application spécifique vous envoyez le message. Dans ce cas, vous fournirez l’identifiant d’application approprié dans un objet Jeton. Elle se trouve dans la section <strong>Developer Console (Console du développeur)</strong> du tableau de bord de Braze.
    field: "app_id"
  - name: ID d’utilisateur externe
    description: Identifiant unique pour envoyer un message à des utilisateurs spécifiques. Cet identifiant doit être identique à celui que vous avez défini dans le SDK Braze. Pour l’envoi du message, vous ne pouvez cibler que les utilisateurs qui ont déjà été identifiés via le SDK ou l’API utilisateur. Un maximum de 50 ID d’utilisateur externes est autorisé par demande. <br> <br> Pour les endpoints de déclenchement de campagne, si vous fournissez ce champ, les critères seront superposés avec les segments de la campagne et seuls les utilisateurs qui figurent dans la liste des ID d’utilisateur externe et le segment de la campagne recevront le message.
    field: "external_user_ids"
  - name: Identifiant de segment
    description: Le <code>segment_id</code> indique le segment auquel le message doit être envoyé. Vous trouverez l’identifiant de segment de chacun des segments que vous avez créés dans la section <strong>Developer Console (Console du développeur)</strong> du tableau de bord de Braze. <br> <br> Pour les endpoints de message, si vous fournissez un identifiant de segment et une liste d’ID d’utilisateur externe dans une demande de messagerie unique, les critères seront superposés et seuls les utilisateurs qui se trouvent dans la liste des ID d’utilisateur externe et dans le segment fourni recevront le message.
    field: "segment_id"
  - name: Identifiant de campagne
    description: Pour les endpoints de messagerie, le <code>campaign_id</code> indique la campagne API dans laquelle l’analyse d’un message doit être suivie. Vous trouverez l’identifiant de campagne de chacune des campagnes que vous avez créées dans la section <strong>Developer Console (Console du développeur)</strong> du tableau de bord de Braze. Si vous fournissez un identifiant de campagne dans le corps de la demande, vous devez indiquer <code>message_variation_id</code> dans chacun des objets de message affichant la variante représentée de votre campagne. <br> <br> Pour les endpoints de déclenchement de campagne, le <code>campaign_id</code> indique l’ID API de la campagne à déclencher. Ce champ est obligatoire pour toutes les demandes d’endpoint de déclenchement.
    field: "campaign_id"
  - name: Identifiant de Canvas
    description: Pour les endpoints de déclenchement de Canvas, le <code>canvas_id</code> indique l’identifiant du Canvas à déclencher ou à planifier. Ce champ est obligatoire pour toutes les demandes d’endpoint de déclenchement.
    field: "canvas_id"
  - name: Identifiant d’envoi
    description: Pour les endpoints de messagerie, le <code>send_id</code> indique la campagne API dans laquelle l’analyse d’un message doit être suivie. Le <code>send_id</code> vous permet de récupérer des analyses pour une instance spécifique d’une campagne envoyée via l’endpoint <code>sends/data_series</code>. Les API et campagnes déclenchées par API qui sont envoyées en tant que diffusion génèrent automatiquement un identifiant d’envoi si un identifiant d’envoi n’est pas fourni. <br> <br> Si vous souhaitez spécifier votre propre <code>send_id</code>, vous devrez d’abord en créer un via l’endpoint <code>sends/id/create</code>. Le <code>send_id</code> ne peut comporter que des caractères ASCII et ne peut faire plus de 64 caractères.  Vous pouvez réutiliser un identifiant d’envoi sur plusieurs envois de la même campagne si vous souhaitez regrouper les analyses de ces envois. <br> <br> Notez que le suivi <code>send_id</code> n’est pas disponible pour les e-mails envoyés via Mailjet. <br> <br> Les conversions de campagne sont attribuées au dernier <code>send_id</code> suivi que l’utilisateur a reçu dans le cadre de cette campagne, à moins que le dernier envoi qu’il ait reçu n’ait pas été suivi.
    field: "send_id"
  - name: Propriétés du déclencheur
    description: "Lorsque vous utilisez l’un des endpoints pour envoyer une campagne avec une livraison déclenchée par API, vous pouvez fournir un mappage de clés et des valeurs pour personnaliser votre message. Si vous faites une demande API qui contient un objet dans <code>\"trigger_properties\"</code>, les valeurs de cet objet peuvent alors être référencées dans votre modèle de message sous l’espace de nom <code>api_trigger_properties</code>. <br> <br> Par exemple, une requête avec <code>\"trigger_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}</code> pourrait inclure le terme \"chaussures\" au message en ajoutant <code>{{api_trigger_properties.${product_name}}}</code>."
    field: "trigger_properties"
  - name: Propriétés d’entrées de Canvas
    description: "Lorsque vous utilisez l’un des endpoints pour déclencher ou programmer un Canvas via l’API, vous pouvez fournir une carte des clés et des valeurs pour personnaliser les messages envoyés dès les premières étapes de votre Canvas, dans l’espace de nom <code>\"canvas_entry_properties\"</code>. <br> <br> Par exemple, une requête avec <code>\"canvas_entry_properties\" : {\"product_name\" : \"shoes\", \"product_price\" : 79.99}</code> pourrait inclure le terme \"chaussures\" à un message en ajoutant <code>{{canvas_entry_properties.${product_name}}}</code>."
    field: "canvas_entry_properties"
  - name: Diffusion
    description: "Lorsque vous envoyez un message à un segment ou à une audience de campagne à l’aide d’un endpoint API, Braze vous demande de définir explicitement si votre message est une \"diffusion\" à un grand groupe d’utilisateurs en ajoutant un booléen <code>broadcast</code> dans l’appel d’API. C’est-à-dire que si vous souhaitez envoyer un message API à l’ensemble du segment que cible une campagne ou un Canvas, vous devrez inclure <code>broadcast: true</code> dans votre appel d’API. <br><br>La diffusion est un champ obligatoire et la valeur par défaut définie par Braze lorsqu’une campagne ou Canvas est lancé(e) avec le paramètre <code>broadcast: false</code>. Vous ne pouvez pas avoir <code>broadcast: true</code> et une liste <code>recipients</code> spécifiée en même temps. Si l’indicateur <code>broadcast</code> est défini sur Vrai et une liste explicite de destinataires est fournie, l’endpoint de l’API renvoie une erreur. De même, inclure <code>broadcast: false</code> et ne pas fournir de liste de destinataires renvoie une erreur. 
    
    <br><br>Faites attention lors de la configuration de <code>broadcast: true</code> car en configurant involontairement cet indicateur, vous pourriez envoyer votre campagne ou Canvas à une audience plus importante que prévue. L’indicateur <code>broadcast</code> est requis pour vous protéger contre les envois accidentels à de grands groupes d’utilisateurs."
    field: "broadcast"
    
---

