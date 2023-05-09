---
nav_title: FAQ
article_title: FAQ sur les activités en direct
page_order: 2
description: "Le présent article fournit des réponses aux questions fréquemment posées sur les activités en direct."
tool: Live Activities
platform:
  - iOS
---

# Foire aux questions

## Fonctionnalité et support

### Comment puis-je rejoindre le programme d’accès anticipé aux activités en direct ? 

Les activités en direct sont actuellement en accès anticipé. Contactez votre gestionnaire de compte Braze si vous souhaitez participer. Il n’y a pas de coût ou de documents supplémentaires requis pour rejoindre ce programme d’accès anticipé.

### Quelles plateformes prennent en charge les activités en direct ?

Les activités en direct sont actuellement une fonctionnalité spécifique à iOS. L’article Activités en direct couvre les [conditions préalables][2] à la gestion des activités en direct via le SDK Swift de Braze.

### Braze prend-il en charge les activités en direct en tant que campagne ou Canvas Step ?

Non, cela n’est pas pris en charge actuellement.

## Notifications push et activités en direct

### Que se passe-t-il si une notification push est envoyée alors qu’une activité en direct est active ? 

![Un écran de téléphone avec une activité sportive en direct « Bulls vs Bears » vers le milieu de l’écran et un texte « lorem ipsum » de notification push en bas de l’écran.][4]{: style="max-width:30%;float:right;margin-left:15px;"}

Les activités en direct et les notifications push occupent différents écrans et n'entrent pas en conflit sur l'écran d'un utilisateur.



### Si les activités en direct exploitent la fonctionnalité de message de notification push, les notifications push doivent-elles être activées pour recevoir les activités en direct ?

Bien que les activités en direct reposent sur des notifications push pour les mises à jour, elles sont contrôlées par différents paramètres utilisateur. Un utilisateur à la possibilité de s’abonner aux activités en direct mais pas aux notifications push, et vice versa. 

Apple exige que l’utilisateur initie l’activité en direct par le biais d’une action dans votre application, par exemple, en passant une commande. Ce jeton d’activité en direct expire au bout de huit heures. 

### Les activités en direct nécessitent-elles des amorces de notification push ?

Les [amorces de notification push][1] sont une bonne pratique pour inviter vos utilisateurs à s’abonner aux notifications push de votre application. Cependant, il n’y a pas de demande de la part du système pour s’abonner aux activités en direct. Les utilisateurs sont, par défaut, abonnés aux activités en direct lorsqu’ils se mettent à niveau vers iOS 16.1 et ultérieurs.

## Sujets techniques et résolution des problèmes

### Je reçois une réponse « Accès refusé » lorsque j’essaie d’utiliser l’endpoint `live_activity/update`. Pourquoi ?

Les clés API que vous utilisez doivent disposer des autorisations appropriées pour accéder aux différents endpoints de l’API Braze. Si vous utilisez une clé API que vous avez précédemment créée, il est possible que vous ayez omis de mettre à jour ses autorisations. Lisez notre [aperçu de la sécurité des clés API][3] pour le revoir.

### Est-ce que l’endpoint `messages/send` partage les limites de débit avec l’endpoint `messages/live_activity/update` ? 

L’endpoint `messages/live_activity/update` a une limite de débit distincte de tout autre endpoint Braze. Par défaut, la limite de débit pour l’endpoint `messages/live_activity/update` est de 250 000 requêtes par heure par groupe d’apps. Pour plus d’informations, consultez l’[article sur la limite de débit][5].


[1]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/push_primer_messages/
[2]: {{site.baseurl}}/developer_guide/platform_integration_guides/swift/live_activities/live_activities/#prerequisites
[3]: {{site.baseurl}}/api/basics/#rest-api-key-security
[4]: {% image_buster /assets/img/push-vs-live-activities.png %}
[5]: {{site.baseurl}}/api/api_limits/