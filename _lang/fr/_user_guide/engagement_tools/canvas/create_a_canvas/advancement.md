---
nav_title: Comportements d’avancement
article_title: Comportements d’avancement
page_order: 10
alias: /auto_advance/
page_type: reference
description: "Cet article de référence décrit la fonctionnalité Comportement d’avancement de Braze et aborde les divers scénarios qui peuvent se présenter au fur et à mesure que vous évoluez dans un Canvas."
tool: Canvas

---

# Avancement de vos utilisateurs dans les composants Canvas

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cet article est disponible à titre de référence pour comprendre comment vos utilisateurs avancent dans les composants Canvas de l’éditeur d’origine. <br><br>Pour les composants de Canvas Flow, le **comportement d’avancement** est défini pour toujours faire avancer immédiatement l’audience, à savoir **Audience avancée immédiatement**. Ceci est aussi applicable aux [étapes déconnectées]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/change_your_canvas_after_launch/#disconnected-steps/).
{% endalert %}

La fonctionnalité **Comportement d’avancement** vous permet de choisir les critères d’avancement de votre [composant Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/). 

![Paramètres Comportement d’avancement avec deux options pour avancer l’audience lorsque le message est envoyé ou avancer immédiatement l’audience.][1]

Les utilisateurs doivent répondre aux critères de l’étape pour passer à l’étape suivante. Avec les étapes de [message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/), vous pouvez activer les validations de livraison pour vérifier que votre audience répond aux critères de livraison pour l’envoi du message. Ceci fait partie du critère d’étape lorsque vous utilisez Canvas Flow. Ainsi, si un utilisateur ne répond pas aux critères de validation de livraison, il quittera le Canvas.

Lorsque l’option **Avancer lorsqu’un message est envoyé** est sélectionnée, les utilisateurs passeront uniquement aux étapes Canvas suivantes dans les cas suivants :

- Un message e-mail est envoyé
- Une notification push est envoyée
- Un webhook est envoyé
- Un message in-app est consulté
- Une carte de contenu est envoyée

Lorsque l’option **Audience avancée immédiatement** est sélectionnée, les utilisateurs passeront aux étapes Canvas suivantes dans les cas suivants :

- Un message est envoyé ou le message in-app dans l’étape devient actif
- Le webhook n’est pas envoyé, car ce dernier entraîne une ou plusieurs erreurs
- Une notification push ou un e-mail n’est pas envoyé, car l’utilisateur n’est pas joignable par notification push ou par e-mail
- Tentative d’envoi de carte de contenu 
- Une carte est annulée et n’est pas envoyée
- Un message n’est pas envoyé, car il est en limite de fréquence
- Un message n’est pas envoyé, car il est annulé.

### Étapes planifiées

Pour un comportement planifié, les utilisateurs doivent respecter les options d’audience de l’étape pour avancer dans l’étape. Si l’étape a un [événement d’exception]({{site.baseurl}}/user_guide/engagement_tools/canvas/create_a_canvas/exception_events/), les utilisateurs qui effectuent l’événement d’exception n’avanceront pas dans l’étape.

Lors de l’envoi d’un composant multicanal avec [Timing Intelligent]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/), nous pouvons envoyer ou essayer d’envoyer des messages à différents moments pour différents canaux. Braze avancera automatiquement des utilisateurs lors de la tentative d’envoi du premier message dans un composant.

### Étapes basées sur une action

Pour des étapes basées sur une action, les utilisateurs doivent effectuer l’action de déclenchement et satisfaire aux options d’audience afin de passer à l’étape suivante. Si l’étape a un événement d’exception, les utilisateurs qui effectuent l’événement d’exception n’avanceront pas dans l’étape.

{% alert important %}
Les utilisateurs qui avancent dans une étape sans recevoir des messages ne seront pas pris en compte comme destinataire unique pour l’étape. Les utilisateurs doivent recevoir un ou plusieurs messages à partir d’une étape pour être pris en compte comme destinataire unique.
{% endalert %}

## Cas d’utilisation

L’avancement fonctionne bien lorsqu’une communication ultérieure est associée aux messages précédents. Par exemple, vous ne voudriez pas envoyer une notification push de suivi concernant un e-mail qui n’a jamais été envoyé aux utilisateurs.

Il peut arriver que vous souhaitiez que les utilisateurs continuent à avancer dans un Canvas même s’ils ne reçoivent pas un message spécifique. Par exemple, vous auriez pu avoir une notification push de « Bienvenue » le 3e jour et un e-mail de « Bienvenue » le 6e jour. Il est possible que certains de vos utilisateurs ne soient pas joignables via les notifications push, car tout le monde ne s’abonne pas aux messages de notification push. Vous pourriez envoyer un e-mail le 6e jour à tous les utilisateurs même si une notification push n’a pas été envoyée le 3e jour.

Dans ce scénario, vous pouvez utiliser les options de Comportement d’avancement de Braze pour garantir que les utilisateurs continuent à avancer dans le Canvas même si la notification push n’a pas été envoyée le 3e jour.

Si vous souhaitez que tous les utilisateurs reçoivent l’e-mail le 6e jour, même s’ils n’ont pas reçu la notification push du 3e jour, vous pouvez définir le **comportement d’avancement** sur **Audience avancée automatiquement** pour la notification push du 3e jour.

Lorsque vous sélectionnerez le comportement d’avancement **Audience avancée immédiatement** pour la notification push du 3e jour, les utilisateurs avanceront dans le parcours lorsque Braze tente d’envoyer la notification push. Les utilisateurs qui ne satisfont pas aux options d’audience et qui ne sont pas joignables via la notification push ne recevront pas de notification push de toute façon, mais ils progresseront dans le parcours.

{% details Comportement d’avancement dans le Canvas précédent %}

Avant la version du Comportement d’avancement, Braze permettait aux utilisateurs de progresser dans un composant Canvas une fois que le message avait été envoyé à partir de ce composant. Par exemple, si un composant Canvas contenait un e-mail et une notification push, les utilisateurs ne passeraient pas aux étapes suivantes du Canvas tant que Braze n’a pas envoyé la notification push ou l’e-mail à l’utilisateur.

Si la notification push ou l’e-mail n’avait pas été envoyé à l’utilisateur, ce dernier n’accéderait pas aux étapes suivantes dans le Canvas.

Les clients Braze qui n’ont pas participé aux premières étapes de la version bêta des messages in-app de Canvas, disposent de l’option de Comportement d’avancement « Message envoyé », appliquée à toutes les étapes Canvas créées avant le 30 juillet 2019. Avant la version du Comportement d’avancement, l’avancement de l’utilisateur s’effectuait lorsque des messages étaient envoyés depuis Canvas Step.

Les clients Braze qui n’ont pas participé aux premières étapes de la version bêta des messages In-App de Canvas, disposent de l’option d’avancement « Message envoyé », appliquée à toutes les étapes Canvas créées avant le 30 juillet 2019 et « Audience avancée après le délai » appliquée à toutes les étapes Canvas avec les messages In-App créés avant le 30 juillet 2019. Avant la version du Comportement d’avancement, l’avancement de l’utilisateur s’effectuait lorsque les messages in-app Canvas devenaient actifs.

{% enddetails %}

[1]: {% image_buster /assets/img/push-advancement-behavior.png %} "Advancement Behavior"
