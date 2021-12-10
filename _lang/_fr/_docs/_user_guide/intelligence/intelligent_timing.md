---
nav_title: Timing Intelligent
article_title: Timing Intelligent
page_order: 2
description: "Lors de la planification d'une campagne, vous pouvez utiliser Intelligent Timing pour transmettre votre message à chaque utilisateur au moment où Braze détermine qu'une personne est le plus susceptible d'engager. Cet article explique comment mettre en œuvre un calendrier intelligent dans vos campagnes et Canvases."
---

# Timing Intelligent

Pour en savoir plus sur la livraison de la campagne, consultez notre [cours LAB de mise en place de campagne](http://lab.braze.com/campaign-setup-delivery-targeting-conversions)!

> Lors de la planification d'une campagne, vous pouvez utiliser le Timing Intelligent (précédemment Intelligent Delivery) pour envoyer votre message à chaque utilisateur au moment où Braze détermine qu'un individu est le plus susceptible d'engager.

Braze calcule le temps d'envoi optimal basé sur une analyse statistique des interactions passées de votre utilisateur avec votre messagerie (sur une base par canal) et l'application. Pour activer le Timing Intelligent, sélectionnez simplement le Timing Intelligent sur la page de livraison lors de la création d'une campagne de livraison planifiée. Notez que cette fonctionnalité n'est pas disponible pour les campagnes par actions ou par API.

Avec le Timing Intelligent, vous pouvez choisir le(s) __jour(s) où votre message va être envoyé__ et, optionnellement, choisissez d'envoyer la campagne sur un planning récurrent. Nous vous recommandons d'utiliser le Timing Intelligent uniquement lorsque vous pouvez planifier la campagne __au moins 24 heures à l'avance__ de la date d'envoi pour vous assurer que les heures optimales des utilisateurs ne sont pas passées lors du lancement de la campagne. Si une campagne est lancée et que le temps optimal d’un utilisateur est déjà passé, le message sort immédiatement. S'il y a plus d'une heure dans le passé, le message n'est pas du tout envoyé.

Vous pouvez également désigner __une fenêtre de temps__ pendant la journée dans laquelle le Timing Intelligent doit envoyer des messages. Ceci est utile si votre campagne concerne un événement spécifique, une vente ou une promotion. Si le temps optimal d'un utilisateur est calculé comme étant en dehors de cette fenêtre, le message sera programmé au bord de la fenêtre la plus proche du temps initialement calculé. Ce "bord" est le temps le plus proche du temps optimal de l'utilisateur. Par exemple, si le délai optimal est de 22h mais que la livraison intelligente est de 13h à 20h, le message indiqué sera envoyé à 20h.

Lorsque vous utilisez le Timing intelligent, Braze recommande que les filtres de votre campagne permettent une fenêtre de 3 jours minimum. Par exemple, au lieu d'utiliser les filtres « utilisé pour la première fois il y a plus d'un jour » et « utilisé pour la première fois il y a moins de 3 jours nous recommandons d’utiliser les filtres « pour la première fois il y a plus d’un jour » et « utilisé pour la première fois il y a moins de 4 jours ». Ceci est dû au fait que les fenêtres de temps de moins de 3 jours peuvent entraîner la chute de certains utilisateurs du segment avant que leur temps d'envoi optimal ne soit atteint.

!\[Temps d'envoi optimal\]\[1\]

## Options de repli

Pour les utilisateurs qui ne disposent pas de données suffisantes pour calculer une heure d'envoi optimale, il y a deux options parmi lesquelles choisir.

__Option 1 : Spécifiez le temps de récupération__<br> Vous pouvez spécifier une heure de repli dans les fuseaux horaires locaux des utilisateurs en choisissant l'option de repli personnalisé et en entrant l'heure désirée. (Si l'utilisateur n'a pas de fuseau horaire, le fuseau horaire de l'entreprise sera utilisé à la place.) Si vous lancez une campagne avec un Timing Intelligent dans les 24 heures suivant la date d'envoi, et que vous activez la fonction de repli personnalisé, les utilisateurs dont les temps optimaux ont déjà passé recevront plutôt la campagne à l'heure spécifiée Custom Fallback dans leur heure locale (ou l'heure de la société s'ils n'ont pas de fuseau horaire). Si la fonction de repli personnalisé spécifiée est déjà passée dans le fuseau horaire d’un utilisateur, le message sera envoyé immédiatement.

__Option 2 : Choisissez le temps le plus populaire parmi les utilisateurs__<br> Vous pouvez également choisir le moment le plus populaire où votre application est utilisée par tous les autres utilisateurs comme repli. Si le temps d'utilisation de l'application la plus populaire tombe en dehors de la fenêtre de livraison que vous avez spécifiée, le bord le plus proche de cet intervalle sera utilisé à la place. Dans le cas rare où vous envoyez à une application où il n'y a pas assez de données pour calculer quand l'application est la plus utilisée (par ex. une application complètement nouvelle sans données) Le Timing Intelligent retombe à 17h dans le fuseau horaire local de l'utilisateur (ou le fuseau horaire de l'entreprise si l'utilisateur n'a pas d'heure locale).

Il est important d’être conscient des limites de l’utilisation de Timing Intelligent dès le début du cycle de vie d’un utilisateur lorsque des données limitées pour Intelligent Timing sont disponibles. Mais elle peut encore être précieuse. Considérez un utilisateur qui n'a enregistré qu'une seule session. Le moment où cet utilisateur a enregistré sa session pourrait très bien être le meilleur moment pour tenter de les engager. Le Timing intelligent n’utiliserait que les données de la première session de l’utilisateur et, en tant que telle, engagerait l’utilisateur à ce moment-là. En général, le Timing Intelligent calcule plus efficacement le temps d’envoi optimal plus tard dans le cycle de vie d’un utilisateur.

## Campagnes déclenchées et Canvases

Si une campagne déclenchée ou l'étape Canvas est activée pour envoyer un message à l'utilisateur avec le Timing Intelligent, il est possible que le temps d'envoi optimal de l'utilisateur soit avant l'heure à laquelle la campagne ou l'étape a été déclenchée. Dans ce cas, le message sera envoyé immédiatement.

## Aperçu du graphique

!\[Graphique d'aperçu du Timing Intelligent\]\[2\]

Sur les pages des utilisateurs de livraison et de destination vous pouvez générer un graphique pour voir combien d'utilisateurs recevront le message selon le Timing Intelligent à chaque heure de la journée. Tout d'abord, assurez-vous de spécifier un public sur la page Utilisateurs cibles. Une fois que vous avez fait cela, cliquez sur « Rafraîchir les données » pour voir le graphique sur les pages correspondantes. Chaque fois que vous modifiez des paramètres concernant le Timing Intelligent ou le public, vous devrez cliquer à nouveau sur « Rafraîchir les données » pour obtenir une mise à jour du graphique.

Le graphique affiche également séparément les utilisateurs qui avaient assez de données pour calculer un temps optimal en bleu et les utilisateurs qui recevront un temps en fonction de votre choix de repli (Custom Fallback ou le plus populaire App Time) en rouge. Vous pouvez activer séparément les barres représentant les utilisateurs avec des temps optimaux calculés avec les données d'engagement ou de repli de votre choix en cliquant sur la case à cocher à côté de leurs étiquettes dans la légende. Pour les campagnes multicanaux, vous pouvez examiner les heures séparément par canal en changeant le canal sélectionné dans le menu déroulant en haut du graphique.
[1]: {% image_buster /assets/img/optimal-send-time.png %} [2]: {% image_buster /assets/img/intel-timing-preview.png %}