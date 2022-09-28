---
nav_title: Timing Intelligent
article_title: Timing Intelligent
page_order: 2
description: "Lors de la planification d’une campagne, vous pouvez utiliser le timing intelligent pour transmettre votre message à chaque utilisateur au moment où Braze détermine qu’une personne est la plus susceptible de s’engager. Le présent article explique comment implémenter le timing intelligent dans vos campagnes et vos Canvas."

---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon2.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Timing Intelligent

> Le présent article explique comment implémenter le timing intelligent dans vos campagnes et vos Canvas.

Lorsque vous [planifiez une campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/), vous pouvez utiliser le timing intelligent (précédemment « livraison intelligente ») pour transmettre votre message à chaque utilisateur lorsque Braze détermine qu’il est le plus susceptible de s’engager (ouvrir ou cliquer).

Braze calcule l’heure d’envoi optimale en fonction d’une analyse statistique des dernières interactions de votre utilisateur avec votre messagerie (selon le canal) et votre application. Pour activer le timing intelligent, sélectionnez **Timing Intelligent** sur la page **Delivery** (Livraison) lors de la création d’une campagne de livraison planifiée. Notez que cette fonctionnalité n’est pas disponible pour les campagnes basées sur les actions et déclenchées par API et ne doit pas être utilisée avec les campagnes utilisant les [heures calmes]({{site.baseurl}}/user_guide/intelligence/faqs/#/#can-i-use-quiet-hours-in-my-intelligent-timing-campaign), la [limitation du taux]({{site.baseurl}}/user_guide/intelligence/faqs/#can-i-use-intelligent-timing-and-rate-limiting), ou le [réchauffement IP]({{site.baseurl}}/user_guide/intelligence/faqs/#can-i-use-intelligent-timing-while-ip-warming). 

## Envoyer la campagne

Avec le Timing Intelligent, vous pouvez choisir le ou les jours auxquels votre message sera envoyé et, facultativement, choisir d’envoyer la campagne selon une planification récurrente. Nous vous recommandons d’utiliser le timing intelligent uniquement lorsque vous pouvez planifier la campagne au moins 24 heures avant la date d’envoi pour garantir que les périodes optimales des utilisateurs ne sont pas passées lorsque la campagne est lancée. Si une campagne est lancée et que le moment optimal pour un utilisateur est déjà passé, le message sera envoyé immédiatement. S’il était il y a plus d’une heure, le message n’est pas envoyé du tout.

Afin de garantir que chaque utilisateur éligible puisse être inclus et recevoir votre campagne à son timing intelligent, nous vous recommandons de lancer votre campagne 48 heures avant l’heure d’envoi planifiée. Un seul jour couvre environ 48 heures. En fonction du lieu de résidence de vos utilisateurs, ils peuvent avoir besoin de plus de 24 heures pour recevoir leur message à timing intelligent, car le moment peut déjà être dépassé lorsque la campagne démarre. 

![Spécifier des options de planification basées sur le temps lorsque le timing intelligent est choisi, tel que le moment d’envoi optimal.][1]

### Fenêtre temporelle

Vous pouvez également spécifier une fenêtre temporelle pendant la journée au cours de laquelle le timing intelligent doit envoyer les messages. Cela est utile si votre campagne concerne un événement, une vente ou une promotion spécifique. 

Si l’heure optimale d’un utilisateur est calculée comme tombant en dehors de cette fenêtre, le message sera planifié à l’extrémité la plus proche de cette fenêtre par rapport au moment optimal calculé initialement. Cette « extrémité » est le moment le plus proche de l’heure optimale pour l’utilisateur. Par exemple, si l’heure optimale est 22 h mais que la livraison intelligente est entre 13 h et 20 h, ce message particulier sera envoyé à 20 h.

## Filtrer les segments

Lors de l’utilisation du timing intelligent, Braze recommande que les filtres de segment de votre campagne autorisent une fenêtre de 3 jours minimum. Par exemple, au lieu d’utiliser les filtres `First used more than 1 day ago` et `First used less than 3 days ago`, nous vous recommandons d’utiliser les filtres `First used more than 1 day ago` et `First used less than 4 days ago`. En effet, les fenêtres horaires de moins de trois jours peuvent entraîner la sortie de certains utilisateurs du segment avant que leur heure d’envoi optimale ne soit atteinte.

![][3]

## Options de secours

Pour les utilisateurs dont les données sont insuffisantes pour calculer un moment d’envoi optimal, il existe deux options à choisir.

**Option 1 : Spécifier l’heure de secours**
- Vous pouvez spécifier une heure de secours dans le fuseau horaire local des utilisateurs en choisissant **Custom Fallback** (Heure de secours personnalisée) et en saisissant l’heure souhaitée. Si l’utilisateur n’a pas de fuseau horaire, le fuseau horaire de la société sera utilisé à la place.<br>
<br>
Si vous lancez une campagne avec un timing intelligent dans les 24 heures avant la date d’envoi et activez une heure de secours personnalisée, les utilisateurs dont les heures optimales sont déjà passées recevront la campagne à l’heure de secours personnalisée spécifiée dans leur heure locale (ou l’heure de l’entreprise s’ils n’ont pas de fuseau horaire). Le message s’enverra immédiatement si l’heure de secours personnalisée spécifiée est déjà passée dans le fuseau horaire d’un utilisateur.

**Option 2 : Choisir l’heure la plus populaire parmi les utilisateurs**
- Vous pouvez également définir l’heure de secours pour être le moment le plus populaire au cours duquel vos autres utilisateurs utilisent votre application. Si le moment le plus populaire d’utilisation de l’application tombe en dehors de la fenêtre de livraison que vous avez spécifiée, l’extrémité la plus proche de cette plage horaire sera utilisée à la place. <br>
<br>
Dans les rares cas où vous envoyez vers une application pour laquelle il n’y a pas assez de données pour calculer quand l’application est la plus utilisée (par ex. une application entièrement nouvelle et sans données), le timing intelligent bascule sur 17 h dans le fuseau horaire local de l’utilisateur (ou fuseau horaire de la société si l’utilisateur n’a pas de temps local défini).

Il est important de connaître les limitations de l’utilisation précoce du timing intelligent dans le cycle de vie d’un utilisateur lorsque des données limitées sont disponibles. Cependant, il est toujours utile, car même les utilisateurs avec peu de sessions enregistrées peuvent offrir des informations sur leur comportement. Le timing intelligent calculera plus efficacement l’heure d’envoi optimale plus tard dans le cycle de vie d’un utilisateur. 

## Campagnes déclenchées et Canvas

Si une campagne déclenchée ou un Canvas Step est activé pour envoyer un message avec un timing intelligent à un utilisateur, il est possible que l’heure d’envoi optimale de l’utilisateur soit antérieure à l’heure de la journée où la campagne ou l’étape a été déclenchée. Dans ce cas, le message sera immédiatement envoyé.

## Aperçu graphique

Sur les pages **Delivery** (Livraison) et **Target Users** (Utilisateurs cibles) dans l’assistant de campagne, vous pouvez générer un graphique pour voir combien d’utilisateurs recevront le message selon le timing intelligent à chaque heure de la journée. 

![Graphique d’aperçu du timing intelligent montrant les estimations du nombre d’utilisateurs qui recevront le message au cours d’une heure donnée, déterminée par leurs données d’engagement antérieures.][2]

Pour ce faire, assurez-vous de spécifier au préalable une audience sur la page **Target Users** (Utilisateurs cibles). Une fois que vous l’avez fait, cliquez sur **Refresh Data** (Actualiser les données) pour voir le graphique sur les pages correspondantes. Chaque fois que vous modifiez des paramètres du timing intelligent ou de l’audience, vous devez cliquer à nouveau sur **Refresh Data** (Actualiser les données) pour afficher un graphique mis à jour.  

Le graphique affiche séparément en bleu les utilisateurs qui disposaient de suffisamment de données pour calculer une heure optimale et en rouge les utilisateurs qui obtiendront une heure en fonction de votre heure de secours choisie (heure de secours personnalisée ou heure la plus populaire de l’application). Vous pouvez également basculer les filtres de calcul pour choisir quelles données sont utilisées pour calculer les horaires dans le graphique (données d’engagement ou heure la plus populaire de l’application). Pour les campagnes multicanales, vous pouvez examiner les heures séparément par canal en modifiant le canal sélectionné dans la liste déroulante en haut du graphique.

[1]: {% image_buster /assets/img/optimal-send-time.png %}
[2]: {% image_buster /assets/img/intel-timing-preview.png %}
[3]: {% image_buster /assets/img/intelligent_timing.png %}
