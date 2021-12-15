---
nav_title: Journal d'activité des messages
article_title: Journal d'activité des messages
page_order: 1
page_type: Référence
description: "Cet article de référence décrit le journal d'activité des messages dans la Console développeur, qui vous montre les messages associés à vos campagnes et envois."
---

# Onglet Journal d'activité des messages {#dev-console-troubleshooting}

> Cet article de référence décrit le journal d'activité des messages dans la Console développeur, qui vous montre les messages associés à vos campagnes et envois. En plus de cet article, nous vous recommandons également de consulter notre cours LAB [Assurance Qualité et Outils de débogage](https://lab.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/) qui couvre la façon d'utiliser le journal d'activité des messages pour effectuer votre propre dépannage et débogage.

Le journal d'activité des messages, dans la Console Développeurs, vous donne la possibilité de voir tous les messages, en particulier les messages d'erreur, associés à vos campagnes et envois. Vous pouvez voir les transactions de campagne de l’API, les détails de dépannage sur les messages échoués et recueillir des informations sur la façon d’améliorer la livraison des notifications ou de résoudre les problèmes techniques existants.

!\[Journal d'activité du message\]\[2\]

Ces messages peuvent provenir de notre propre système, de vos applications ou plates-formes, ou de nos partenaires tiers. Cela peut résulter en un nombre infini de messages qui peuvent apparaître dans ce journal.

Pour déterminer ce que vos messages signifient, faites attention au libellé de chaque message et aux colonnes qui le concernent, car il peut vous aider à résoudre des problèmes en utilisant des indices de contexte. Par exemple, si vous avez une entrée de log dont le message est "vide-cart_app" et que vous n'êtes pas sûr de ce que cela signifie. regardez à gauche à la colonne Type . Si vous voyez "Erreur de message annulé", vous pouvez supposer que le message a été écrit comme le message d'abandon en utilisant [Liquid][1], et que le message a été abandonné parce que le destinataire prévu du message avait un panier vide dans votre application.

Cependant, il y a certains types de messages courants que vous pourriez voir, et certains pourraient même fournir des liens de dépannage pour vous aider à diagnostiquer et résoudre les problèmes.

| Type de message          | Exemple de texte dans la colonne de message                                                                                            | Contexte/Explication                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Bloquer                  | Le compte de messagerie que vous avez essayé d'atteindre est désactivé. En savoir plus à _URL SAMPLE_.                                 | Votre message n'a jamais atteint la boîte de réception de cette personne - parce qu'il n'y avait pas de boîte de réception à atteindre ! Si vous voulez creuser plus loin, des messages comme celui-ci peuvent parfois avoir des liens dans la colonne __Voir les détails__ qui vous permettra de voir le profil du destinataire prévu.                                                                          |
| Bloquer                  | Les messages indésirables sont rejetés en raison de la politique anti-spam. Pour plus d'informations, veuillez visiter _l'URL SAMPLE_. | Uh oh. On dirait que votre message a été catégorisé comme spam ici. Cela peut être juste pour ce destinataire prévu, mais si vous voyez ce message beaucoup, vous voudrez peut-être réévaluer vos habitudes d'envoi ou le contenu de votre message. De plus, rappelez-vous - avez-vous fait un \[warm-up\]\[8\]? Si ce n'est pas le cas, adressez-vous à Braze pour obtenir des conseils sur la marche à suivre. |
| Erreur de message annulé | carte_web vide                                                                                                                         | Si vous avez une application avec un panier ou que vous créez un envoi avec un message d'abandon dans le Liquid, vous pouvez personnaliser le message qui vous est retourné si l'envoi est abandonné. Dans ce cas, le message retourné est vide-cart_web.                                                                                                                                                        |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}
[2]: {% image_buster /assets/img_archive/message_activity_log.png %} [8]: {% image_buster /assets/img_archive/UserLogs1.png %}


[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/aborting_messages/#aborting-messages
