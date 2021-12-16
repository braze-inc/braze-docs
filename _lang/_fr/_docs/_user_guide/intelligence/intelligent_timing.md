---
nav_title: Timing Intelligent
article_title: Timing Intelligent
page_order: 2
description: "Lors de la planification d'une campagne, vous pouvez utiliser Intelligent Timing pour transmettre votre message à chaque utilisateur au moment où Braze détermine qu'une personne est le plus susceptible d'engager. Cet article explique comment implémenter le Timing Intelligent dans vos campagnes et Canvases."
---

# Timing Intelligent

> Cet article explique comment implémenter le Timing Intelligent dans vos campagnes et Canvases. Pour plus de détails sur le Timing Intelligent et ses avantages, consultez notre cours [Intelligent Timing](https://lab.braze.com/intelligent-timing) LAB.

Lorsque [planifiez une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/), vous pouvez utiliser Intelligent Timing (précédemment Intelligent Delivery) pour envoyer votre message à chaque utilisateur lorsque Braze détermine qu'une personne est le plus susceptible de s'engager (ouvrir ou cliquer).

Braze calcule le temps d'envoi optimal basé sur une analyse statistique des interactions passées de votre utilisateur avec votre messagerie (sur une base par canal) et l'application. Pour activer le Timing intelligent, sélectionnez **Timing intelligent** sur la page **Livraison** lors de la création d'une campagne de livraison planifiée. Notez que cette fonctionnalité n'est pas disponible pour les campagnes basées sur l'action et déclenchées par API, et ne doit pas être utilisée avec [heures silencieuses]({{site.baseurl}}/user_guide/intelligence/faqs/#/#can-i-use-quiet-hours-in-my-intelligent-timing-campaign), [limitation de taux]({{site.baseurl}}/user_guide/intelligence/faqs/#can-i-use-intelligent-timing-and-rate-limiting), ou [campagnes de réchauffement IP]({{site.baseurl}}/user_guide/intelligence/faqs/#can-i-use-intelligent-timing-while-ip-warming).

## Envoi de la campagne

Avec le Timing intelligent, vous pouvez choisir le jour ou le jour où votre message sera envoyé et, éventuellement, choisir d'envoyer la campagne sur un planning récurrent. Nous vous recommandons d'utiliser le Timing Intelligent uniquement lorsque vous pouvez planifier la campagne au moins 24 heures avant la date d'envoi pour vous assurer que les heures optimales des utilisateurs ne sont pas passées lors du lancement de la campagne. Si une campagne est lancée et que le temps optimal d'un utilisateur est déjà passé, le message sort immédiatement. S'il y a plus d'une heure dans le passé, le message n'est pas du tout envoyé.

!\[Temps d'envoi optimal\]\[1\]

### Fenêtre du temps

Vous pouvez également désigner une fenêtre de temps durant la journée dans laquelle le Timing Intelligent doit envoyer des messages. Ceci est utile si votre campagne concerne un événement spécifique, une vente ou une promotion.

Si le temps optimal d'un utilisateur est calculé comme étant en dehors de cette fenêtre, le message sera programmé au bord de la fenêtre la plus proche du temps initialement calculé. Ce "bord" est le temps le plus proche du temps optimal de l'utilisateur. Par exemple, si le temps optimal est de 22h, mais que la livraison intelligente est de 13h à 20h, le message indiqué sera envoyé à 20h.

## Filtrage des segments

Lorsque vous utilisez le Timing intelligent, Braze recommande que les filtres de votre campagne permettent une fenêtre de 3 jours minimum. Par exemple, au lieu d'utiliser les filtres "utilisé pour la première fois il y a plus d'un jour" et "utilisé pour la première fois il y a moins de 3 jours", nous recommandons d'utiliser les filtres "pour la première fois il y a plus d'un jour" et "pour la première fois utilisé il y a moins de 4 jours". Ceci est dû au fait que les fenêtres de temps de moins de 3 jours peuvent entraîner la chute de certains utilisateurs du segment avant que leur temps d'envoi optimal ne soit atteint.<br><br>!\[Exemple de filtre de timing intelligents\]\[3\]

## Options de repli

Pour les utilisateurs qui ne disposent pas de données suffisantes pour calculer une heure d'envoi optimale, il y a deux options parmi lesquelles choisir.

__Option 1 : Spécifier le temps de récupération__
- Vous pouvez spécifier une heure de repli dans les fuseaux horaires locaux des utilisateurs en choisissant **fonction de repli** et en entrant l'heure désirée. Si l'utilisateur n'a pas de fuseau horaire, le fuseau horaire de l'entreprise sera utilisé à la place.<br><br>Si vous lancez une campagne avec le Timing Intelligent dans les 24 heures suivant la date d'envoi et activez une fonction personnalisée les utilisateurs dont les temps optimaux ont déjà passé recevront plutôt la campagne à l'heure spécifiée Custom Fallback dans leur heure locale (ou l'heure de la société s'ils n'ont pas de fuseau horaire). Le message sera envoyé immédiatement si le Custom Fallback spécifié est déjà passé dans le fuseau horaire d'un utilisateur.

__Option 2 : Choisissez le temps le plus populaire parmi les utilisateurs__
- Vous pouvez également définir le repli pour être le moment le plus populaire où tous les autres utilisateurs utilisent votre application. Si le temps d'utilisation de l'application la plus populaire tombe en dehors de la fenêtre de livraison que vous avez spécifiée, le bord le plus proche de cet intervalle sera utilisé à la place. <br><br>Dans le cas rare que vous envoyez à une application où il n'y a pas assez de données pour calculer quand l'application est la plus utilisée (par ex. une toute nouvelle application sans données) Le Timing Intelligent retarde à 17h dans le fuseau horaire local de l'utilisateur (ou fuseau horaire de l'entreprise si l'utilisateur n'a pas d'heure locale).

Il est important d'être conscient des limites de l'utilisation du Timing Intelligent tôt dans le cycle de vie d'un utilisateur lorsque des données limitées sont disponibles. Il peut cependant être précieux, car même les utilisateurs ayant quelques sessions enregistrées peuvent vous donner une idée de leur comportement. Le Timing Intelligent calculera plus efficacement le temps d'envoi optimal plus tard dans le cycle de vie d'un utilisateur.

## Campagnes déclenchées et Canvases

Si une campagne déclenchée ou l'étape Canvas est activée pour envoyer un message à l'utilisateur avec le Timing Intelligent, il est possible que le temps d'envoi optimal de l'utilisateur soit avant l'heure à laquelle la campagne ou l'étape a été déclenchée. Dans ce cas, le message sera envoyé immédiatement.

## Aperçu du graphique

!\[Graphique d'aperçu du Timing Intelligent\]\[2\]

Sur les pages **Livraison** et **Utilisateurs cibles** de l'assistant de campagne, vous pouvez générer un graphique pour voir combien d'utilisateurs recevront le message selon le Timing Intelligent à chaque heure de la journée.

Pour ce faire, assurez-vous d'abord de spécifier un public sur la page **Utilisateurs cibles**. Une fois que vous avez fait cela, cliquez sur **Actualiser les données** pour voir le graphique sur les pages correspondantes. Chaque fois que vous modifiez des paramètres concernant le Timing Intelligent ou l'audience, vous devrez cliquer à nouveau sur **Actualiser les données** pour voir une mise à jour du graphique.

Le graphique affiche séparément les utilisateurs qui avaient assez de données pour calculer un temps optimal en bleu et les utilisateurs qui recevront un temps en fonction de la valeur de repli de votre choix (temps de repli personnalisé ou le plus populaire de l'application) en rouge. Vous pouvez également basculer les données utilisées pour calculer les heures en cliquant sur les cases à cocher au-dessus du graphique. Pour les campagnes multicanaux, vous pouvez examiner les heures séparément par canal en changeant le canal sélectionné dans le menu déroulant en haut du graphique.
[1]: {% image_buster /assets/img/optimal-send-time.png %} [2]: {% image_buster /assets/img/intel-timing-preview.png %} [3]: {% image_buster /assets/img/intelligent_timing.png %}