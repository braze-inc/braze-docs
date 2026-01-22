## Contrôles de base

### Mon message in-app ne s'est pas affiché pour un utilisateur

1. L'utilisateur était-il dans le segment au début de la session, lorsque le SDK demande de nouveaux messages in-app ?
2. L'utilisateur était-il éligible ou rééligible pour recevoir le message in-app conformément aux règles de ciblage de la campagne ?
3. L'utilisateur a-t-il été affecté par une limite de fréquence ?
4. L'utilisateur faisait-il partie d'un groupe de contrôle ? Vérifiez si votre campagne est configurée pour les tests A/B.
5. Un message in-app différent et plus prioritaire s'est-il affiché à la place du message attendu ?
6. Mon appareil était-il dans l'orientation correcte spécifiée par la campagne ?
7. Mon message a-t-il été supprimé par l'intervalle de temps minimum de 30 secondes par défaut entre les déclencheurs, imposé par le SDK ?

### Mon message in-app n'a pas été affiché à tous les utilisateurs sur cette plateforme.

1. Votre campagne est-elle configurée pour cibler les applications mobiles ou les navigateurs web, selon le cas ? Par exemple, si votre campagne ne cible que les navigateurs web, elle ne sera pas envoyée aux appareils Android.
2. Avez-vous mis en place une interface utilisateur personnalisée et fonctionne-t-elle comme prévu ? Y a-t-il d'autres manipulations ou suppressions personnalisées côté application qui pourraient interférer avec l'affichage ? 
3. Cette plateforme et cette version de l'application en particulier ont-elles déjà affiché avec succès des messages in-app ?
4. Le déclencheur a-t-il eu lieu localement sur l'appareil ? Notez qu'un appel d’API REST ne peut pas être utilisé pour déclencher un message in-app dans le SDK.

### Mon message in-app ne s'est pas affiché pour tous les utilisateurs

1. L'action de déclenchement a-t-elle été configurée correctement dans le tableau de bord, ainsi que dans l'intégration de l'app ?
2. Un message in-app différent et plus prioritaire s'est-il affiché à la place du message attendu ?
3. Utilisez-vous une version récente du SDK ? Certains types de messages in-app exigent une version déterminée du SDK.
4. Les sessions ont-elles été intégrées correctement dans votre intégration ? L'analyse/analytique des sessions fonctionne-t-elle pour cette application ?

### Mon message in-app a mis beaucoup de temps à s'afficher

1. Si vous diffusez des images ou des vidéos volumineuses à partir de votre réseau de diffusion de contenus dans un message in-app basé sur HTML, vérifiez que vos fichiers sont optimisés pour être aussi petits que possible et que votre réseau de diffusion de contenus est performant.
2. Vérifiez si vous avez configuré un `delay` pour votre message in-app sur le tableau de bord.
{% case include.sdk %}
  {% when "iOS", "Android" %}
3. Selon les circonstances, les messages in-app téléchargeront ou chargeront les images pertinentes à partir du disque avant de les afficher. Si vous disposez d'une connexion réseau lente ou d'appareils très peu performants, ce processus peut prendre du temps. Veillez à ce que vos images soient optimisées pour être aussi petites que possible.
{% endcase %}

Pour une discussion plus approfondie de ces scénarios, consultez <a id="troubleshooting-in-app-advanced">la section sur la résolution des problèmes avancés</a>.

## Problèmes d'analyse des impressions et des clics

{% if include.sdk == "iOS" %}
### Les impressions et les clics ne sont pas enregistrés

Si vous avez défini un délégué de message in-app pour gérer manuellement l'affichage du message ou les actions de clic, vous devez consigner manuellement les [clics](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logclick(buttonid:using:)) et les [impressions](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/logimpression(using:)) sur le message in-app.
{% elsif include.sdk == "Android" %}
### Les impressions et les clics ne sont pas enregistrés
Si vous avez défini un délégué de message in-app pour gérer manuellement l'affichage du message ou les actions de clic, vous devez consigner manuellement les clics et les impressions sur le message in-app.
{% endif %}

### Les impressions sont inférieures à la valeur attendue

1. Les déclencheurs mettent du temps à se synchroniser avec l’appareil au démarrage de la session, il peut donc y avoir une condition de concurrence si les utilisateurs enregistrent un événement ou achètent juste après avoir démarré une session. Une possible solution pourrait être de changer la campagne pour qu’elle se déclenche au démarrage de la session, puis de segmenter l’événement ou l’achat prévu. Notez que cela enverrait le message in-app à l’application au prochain démarrage de la session après que l’événement se soit produit.

2. Si la campagne est déclenchée par un début de session ou un événement personnalisé, vous devez vous assurer que cet événement ou cette session est suffisamment fréquent pour déclencher le message. Vérifiez ces données sur les pages [Aperçu]({{site.baseurl}}/user_guide/data_and_analytics/analytics/understanding_your_app_usage_data/#understanding-your-app-usage-data) (pour les données de session) ou [Événements personnalisés]({{site.baseurl}}/user_guide/data_and_analytics/configuring_reporting/#configuring-reporting):

![La page des événements personnalisés affiche un graphique indiquant le nombre de fois où l'événement personnalisé Ajouté aux favoris s'est produit sur une période d'un mois.]({% image_buster /assets/img_archive/trouble5.png %})

### Les impressions sont plus faibles qu'auparavant

1. Assurez-vous que personne n'a modifié involontairement le segment ou la campagne depuis le lancement. Nos Journaux de modifications des segments et des campagnes vous informeront sur les changements, qui les a faits et quand.

![Lien pour afficher le journal des modifications sur la page des détails de la campagne avec sept modifications depuis que l'utilisateur a consulté la campagne pour la dernière fois]({% image_buster /assets/img_archive/trouble4.png %})

2. Assurez-vous que vous n'avez pas réutilisé votre événement déclencheur dans une campagne de messages in-app distincte avec une priorité plus élevée.

## Résolution avancée des problèmes {#troubleshooting-in-app-advanced}

La plupart des problèmes de messages in-app peuvent être divisés en deux catégories principales : livraison et affichage. Pour savoir pourquoi un message in-app attendu ne s'est pas affiché sur votre appareil, confirmez que le <a id="troubleshooting-in-app-message-delivery">message in-app a bien été envoyé à l'appareil</a>, puis <a id="troubleshooting-in-app-message-display">résolvez le problème d'affichage du message.</a>

### Résolution des problèmes réception/distribution {#troubleshooting-in-app-message-delivery}

Le SDK demande des messages in-app aux serveurs Braze au démarrage de la session. Pour vérifier si les messages intégrés à l'application sont livrés à votre appareil, vous devez vous assurer que les messages intégrés à l'application sont à la fois demandés par le SDK et renvoyés par les serveurs Braze.

#### Vérifier si les messages sont demandés et retournés

1. Ajoutez vous en tant qu'utilisateur test]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/#adding-test-users) sur le tableau de bord.
2. Configurez une campagne de messages in-app ciblée pour votre utilisateur.
3. Assurez-vous qu’une nouvelle session se produit dans votre application.
4. Utilisez le journal des événements utilisateurs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) pour vérifier que votre appareil demande des messages in-app au démarrage de la session. Recherchez la requête SDK associée à l’événement de démarrage de session de votre utilisateur test.
  - Si votre application était censée demander des messages intégrés déclenchés, vous devriez voir `trigger` dans le champ **Réponses demandées** sous **Données de réponse**.
  - Si votre application était censée demander des messages intégrés originaux, vous devriez voir `in_app` dans le champ **Réponses demandées** sous **Données de réponse**.
5. Utilisez les journaux des événements utilisateurs]({{ site.baseurl }}/user_guide/administrative/app_settings/developer_console/event_user_log_tab/#event-user-log-tab) pour vérifier si les messages in-app corrects sont renvoyés dans les données de réponse.<br>![]({% image_buster /assets/img_archive/event_user_log_iams.png %})

##### Résoudre les problèmes de messages non demandés

Si vos messages in-app ne sont pas demandés, il est possible que votre application ne suive pas correctement les sessions, car les messages in-app sont actualisés au démarrage de la session. Assurez-vous également que votre application démarre réellement une session en fonction de la sémantique du délai d’expiration de session de votre application :

![La demande de SDK trouvée dans le journal des événements utilisateurs affichant un événement de démarrage de session réussi.]({% image_buster /assets/img_archive/event_user_log_session_start.png %})

##### Résoudre les problèmes de messages non renvoyés

Si les messages in-app ne sont pas renvoyés, vous risquez probablement d’avoir un problème de ciblage de campagne :

1. Votre segment ne contient pas votre utilisateur.
  - Vérifiez dans l'onglet [\*\*Engagement**]({{ site.baseurl }}/user_guide/engagement_tools/segments/using_user_search/#engagement-tab) ] de votre utilisateur si le segment correct apparaît sous **Segments**.
2. Votre utilisateur a déjà reçu le message in-app, mais n’était pas rééligible pour le recevoir à nouveau.
  - Vérifiez les [paramètres de rééligibilité de la campagne]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) sous l'étape **Réception/distribution** du **Composeur de campagne** et assurez-vous que les paramètres de rééligibilité correspondent à votre configuration de test.
3. Votre utilisateur a atteint la limite de fréquence pour la campagne.
  - Vérifiez les paramètres de la campagne [limite de fréquence]]({{ site.baseurl }}/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#frequency-capping) et assurez-vous qu'ils correspondent à votre configuration de test.
4. Si un groupe de contrôle a été créé pour la campagne, votre utilisateur peut être tombé dans le groupe de contrôle.
  - Vous pouvez vérifier si cela s'est produit en créant un segment avec un filtre de variante de campagne reçue, où la variante de campagne est définie sur **Contrôle**, et vérifier si votre utilisateur est tombé dans ce segment.
  - Lors de la création de campagnes à des fins de test d’intégration, veillez à désactiver l’ajout d’un groupe de contrôle.


### Résolution des problèmes de l'affichage {#troubleshooting-in-app-message-display}

Si votre application demande et reçoit avec succès des messages in-app, mais qu'ils ne s'affichent pas, il se peut que la logique de l'appareil empêche l'affichage :

1. L'événement déclencheur se déclenche-t-il comme prévu ? Pour le vérifier, essayez de configurer le message pour qu'il se déclenche à l'aide d'une action différente (comme le démarrage d'une session) et vérifiez s'il s'affiche.
{% if include.sdk == "iOS" %}
2. Les messages in-app déclenchés sont limités en débit en fonction de l'[intervalle de temps minimum entre les déclenchements]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), qui est de 30 secondes par défaut.
{% elsif include.sdk == "Android" %}
2. Les messages in-app déclenchés sont limités en débit en fonction de l'[intervalle de temps minimum entre les déclenchements]({{site.baseurl}}/developer_guide/platform_integration_guides/android/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), qui est de 30 secondes par défaut.
{% elsif include.sdk == "Web" %}
2. Les messages in-app déclenchés sont limités en débit en fonction de l'[intervalle de temps minimum entre les déclenchements]({{site.baseurl}}/developer_guide/platform_integration_guides/web/in-app_messaging/in-app_message_delivery/#minimum-time-interval-between-triggers), qui est de 30 secondes par défaut.
{% endif %}
3. Les échecs de téléchargement d’images empêcheront l’affichage des messages in-app contenant des images. Vérifiez les journaux de votre appareil pour vous assurer que les téléchargements d’images n’échouent pas. Essayez de supprimer temporairement votre image de votre message pour voir si elle s'affiche.
{% case include.sdk %}
  {% when "iOS", "Android" %}
4. Si vous avez défini un délégué pour personnaliser la gestion des messages in-app, vérifiez votre délégué pour vous assurer qu’il n’affecte pas l’affichage du message in-app.
  {% when "Web" %}
5. Si vous avez une gestion personnalisée des messages dans l’application via `braze.subscribeToInAppMessage` ou `appboy.subscribeToNewInAppMessages`, vérifiez cet abonnement pour s’assurer qu’il n’affecte pas l’affichage des messages dans l’application.
{% endcase %}
{% case include.sdk %}
  {% when "iOS", "Android" %}
6. Si l’orientation de l’appareil ne correspond pas à l’orientation spécifiée par le message in-app, il ne s’affichera pas. Assurez-vous que votre appareil est dans la bonne orientation.
{% endcase %}
7. Si votre message in-app est déclenché par le démarrage de la session et que vous avez défini un délai d'attente prolongé, cela aura une incidence sur la vitesse à laquelle vous pouvez afficher les messages. Par exemple, si le délai d'expiration de votre session est fixé à 300 secondes, le fait de fermer et de rouvrir l'application en moins de temps que cela n'actualisera pas la session, de sorte qu'un message in-app déclenché par le démarrage d'une session ne s'affichera pas.

