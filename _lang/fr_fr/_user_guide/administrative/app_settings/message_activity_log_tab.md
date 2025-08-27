---
nav_title: Journal des activités liées aux messages
article_title: Journal des activités liées aux messages
page_order: 5
page_type: reference
description: "Cet article de référence décrit le journal d'activité des messages qui vous montre les messages associés à vos campagnes et à vos envois. Vous trouverez également ici des informations sur la façon de comprendre les messages du journal."

---

# Journal des activités de message {#dev-console-troubleshooting}

> Le **journal d'activité des messages** vous permet de voir tous les messages (en particulier les messages d'erreur) associés à vos campagnes et à vos envois.

Vous pouvez voir les transactions de campagne API, résoudre les problèmes sur les messages défaillants et recueillir des informations sur la manière d’améliorer la livraison des notifications ou de résoudre les problèmes techniques existants.

Pour accéder au journal, allez dans **Réglages** > **Journal d'activité des messages.**

![Message Activity Log]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Outre cet article, nous vous recommandons également de consulter notre cours d'apprentissage sur l ['assurance qualité et les outils de débogage](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) Braze, qui explique comment utiliser le journal d'activité des messages pour effectuer vos propres opérations de résolution des problèmes et de débogage.
{% endalert %}

Vous pouvez filtrer en fonction des contenus suivants enregistrés dans le **journal d'activité des messages :**

- Erreurs de notification push
- Erreurs de message avorté
- Erreurs de Webhook
- Erreurs de messagerie
- Enregistrements des messages API
- Erreurs de contenu connecté
- Erreurs d’audience connectée de l’API REST
- Erreurs d’aliasing de l’utilisateur
- Erreurs de test A/B
- Erreurs de SMS/MMS
- Erreurs dans WhatsApp
- Erreurs de production en ligne/instantané
- Mauvais déclencheurs d'utilisateurs

Ces messages peuvent provenir de notre propre système, de vos apps ou plateformes, ou de nos partenaires tiers. Cela peut entraîner un nombre infini de messages pouvant apparaître dans ce journal.

## Comprendre les messages du journal

Pour déterminer ce que vos messages signifient, prêtez attention au libellé de chaque message et aux colonnes qui lui correspondent, car cela peut vous aider à résoudre les problèmes en utilisant des indices contextuels. 

Par exemple, si vous avez une entrée de journal dont le message indique "empty-cart_app" et que vous n'êtes pas sûr de ce que cela signifie, regardez à gauche dans la colonne **Type.**  Si vous voyez « Erreur de message annulé », vous pouvez supposer que le message était ce qui a été écrit comme [message annulé]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages) avec Liquid, et que le message a été annulé parce que le destinataire prévu du message disposait d’un panier vide dans votre application.

### Messages courants

Plusieurs types de messages courants existent, et certains peuvent même fournir des liens de résolution des problèmes pour vous aider à diagnostiquer et résoudre les problèmes.

Les messages suivants sont donnés à titre d'exemple et peuvent ne pas correspondre exactement à ce qui est affiché dans la colonne **Message** de votre journal.

| Type de message | Message potentiel | Description |
|---|---|---|
| Échec provisoire de livraison | L'adresse e-mail same@example.com a fait l'objet d'un échec provisoire d'envoi. | L’adresse e-mail était valide et le message e-mail a été acheminé jusqu’au serveur de messagerie du destinataire, mais a été rejeté pour un problème « temporaire ». <br><br>Les raisons les plus courantes de l'échec provisoire d'envoi sont les suivantes : {::nomarkdown} <ul> <li> La boîte de réception était pleine (l’utilisateur a dépassé son quota) </li> <li> Le serveur était hors service </li> <li> Le message était trop volumineux pour la boîte de réception du destinataire </li>  </ul> {:/} Si un e-mail a fait l'objet d'un échec provisoire d'envoi, nous effectuons généralement une nouvelle tentative dans un délai de 72 heures, mais le nombre de tentatives varie d'un destinataire à l'autre. |
| Échec d'envoi définitif | Le compte d’e-mail que vous avez essayé de contacter n’existe pas. Essayez de vérifier que l’adresse e-mail du destinataire ne contient pas de fautes de frappe ou d’espaces inutiles. | Votre message n'a jamais atteint la boîte de réception de cette personne parce qu'il n'y avait pas de boîte de réception à atteindre. Si vous souhaitez aller plus loin, les messages de ce type peuvent parfois contenir des liens dans la colonne **Voir les détails** qui vous permettront de consulter le profil du destinataire.|
| Bloc | Le message spam est rejeté en raison de la politique anti-spam. | Votre message a été classé comme spam. Cette erreur d’e-mail est enregistrée pour un utilisateur si nous avons reçu un événement de l'ESP indiquant que l'e-mail a été abandonné. ll se peut qu’il soit destiné à ce destinataire, mais si vous voyez souvent ce message, vous devriez peut-être revoir vos habitudes d’envoi ou le contenu de votre message. Pensez aussi au passé : avez-vous [réchauffé votre IP]({{site.baseurl}}/user_guide/message_building_by_channel/email/email_setup/ip_warming/)? Si ce n’est pas le cas, contactez Braze pour des conseils sur la façon de procéder.|
| Erreurs de message annulé | empty-cart_web | Si vous avez une application avec un panier ou que vous créez un envoi avec un message annulé dans le Liquid, vous pouvez personnaliser le message qui vous est renvoyé si l’envoi est annulé. Dans ce cas, le message renvoyé est empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Pourquoi mon message ne figure-t-il pas dans cette liste ?

Les messages du journal d'activité des messages peuvent provenir de différentes sources : Braze, vos apps ou plateformes, ou nos partenaires tiers. Cela signifie qu'il existe un nombre infini de messages susceptibles d'apparaître dans ce journal - comme vous pouvez l'imaginer, nous ne pouvons pas tous les énumérer !

Par exemple, certains messages de "blocage" potentiels, en plus de celui énuméré dans le tableau précédent, pourraient être les suivants :

- Malheureusement, les messages de [_IP_ADDRESS_] n'ont pas été envoyés. Veuillez contacter votre fournisseur de services Internet car une partie de son réseau figure sur notre liste de blocage.
- Message rejeté en raison de la politique locale.
- Le message a été bloqué par le destinataire comme étant du spam.
- Service indisponible, l'hôte du client [_IP_ADDRESS_] est bloqué par Spamhaus.

## Durée de conservation des données

Les erreurs des 60 dernières heures sont disponibles dans les journaux d'activité des messages. Les journaux datant de plus de 60 heures sont nettoyés et ne sont plus accessibles. 

### Nombre de journaux d'erreurs stockés

Le nombre de journaux enregistrés est influencé par plusieurs conditions. Par exemple, si une campagne planifiée est envoyée à des milliers d'utilisateurs, nous verrons potentiellement un échantillon des erreurs dans le journal d'activité des messages au lieu de toutes les erreurs.

Voici un aperçu des conditions affectant le nombre de journaux enregistrés :
- Jusqu'à 20 journaux d'erreurs de contenu connecté seront enregistrés pour la même campagne au cours d'une heure d'horloge fixe.
- Jusqu'à 100 journaux d'erreurs du même type seront enregistrés au cours d'une heure d'horloge fixe par espace de travail pour les types d'erreurs suivants :
    - Erreurs de message avorté
    - Erreurs de Webhook
    - Erreurs de notification push
    - Erreurs de production en ligne/instantané
    - Mauvais déclencheurs d'utilisateurs

