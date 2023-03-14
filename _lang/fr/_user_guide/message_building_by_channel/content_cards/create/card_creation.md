---
nav_title: Création de carte
article_title: Création de carte
alias: /card_creation/
description: "Cet article décrit les différences entre la création d’une carte de contenu au lancement de la campagne et sa création lors de la première impression."
page_order: 1
tool: Campagnes
channel:
  - cartes de contenu
---

# Création de carte

Vous pouvez choisir quand Braze évalue l’éligibilité et la personnalisation de l’audience pour les nouvelles campagnes de cartes de contenu en spécifiant quand la carte est créée.

{% alert important %}
Le contrôle de la création de cartes n’est pas disponible pour les étapes Canvas.
{% endalert %}

## Conditions préalables

Pour profiter de cette fonctionnalité, vous devez effectuer une mise à niveau vers les versions minimales du SDK suivantes :

{% sdk_min_versions web:4.2.0 android:23.0.0 ios:4.5.0 %}

Après la mise à niveau du SDK, vos utilisateurs mobiles doivent mettre à niveau leur application. Vous pouvez filtrer votre audience de campagne pour [cibler uniquement les utilisateurs sur ces versions minimales d’application]({{site.baseurl}}/user_guide/engagement_tools/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

## Aperçu

Vous pouvez choisir quand Braze crée une carte à l’étape **Livraison** lors de la création d’une nouvelle [campagne de cartes de contenu][2] à livraison programmée.

![Section Contrôles de la carte de contenu lors de la modification de la livraison d’une carte de contenu planifiée.][1]

Les options suivantes sont disponibles :

- **Au lancement de la campagne :** Le comportement par défaut précédent pour les cartes de contenu. Braze calcule l’éligibilité et la personnalisation de l’audience au lancement de la campagne, puis crée la carte et la stocke jusqu’à ce que l’utilisateur ouvre votre application.
- **À la première impression :** Lorsque l’utilisateur ouvre ensuite votre application (c’est-à-dire qu’il démarre une nouvelle [session][3]), Braze détermine les cartes de contenu auxquelles l’utilisateur est éligible, modélise les personnalisations telles que le Liquid ou le contenu connecté, puis crée la carte.

{% alert note %}
Pour les deux options, après la création d’une carte, Braze ne recalcule pas l’éligibilité ou la personnalisation de l’audience.
{% endalert %}

### Différences entre la création de cartes au lancement et lors de la première impression

Cette section décrit les différences entre la création d’une carte au lancement et sa création lors de la première impression.

<style type="text/css">
.tg td{word-break:normal;}
.tg th{word-break:normal;}
.leftHeader{font-size: 12px; font-weight: bold; background-color: #f4f4f7; text-transform: uppercase; color: #212123; font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;}
.tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}
</style>
<table class="tg">
<thead>
  <tr>
    <th class="tg-0pky"></th>
    <th class="tg-0pky">Lorsque la campagne est lancée</th>
    <th class="tg-0pky">À la première impression</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td class="leftHeader">Quand l’utiliser</td>
    <td class="tg-0pky">Si vous avez besoin que le contenu soit instantané à un moment spécifique (heure de lancement).</td>
    <td class="tg-0pky">Si vous avez besoin d’afficher des cartes pour des utilisateurs nouveaux ou anonymes qui peuvent entrer dans le segment après son lancement.<br><br>Si vous utilisez la personnalisation et souhaitez que le contenu le plus récent soit disponible sur la carte.</td>
  </tr>
  <tr>
    <td class="leftHeader">Audience</td>
    <td class="tg-0pky">Braze évalue l’appartenance à l’audience lorsque la campagne s’envoie.<br><br>L’éligibilité des utilisateurs nouveaux ou anonymes ne sera pas évaluée s’ils essaient d’afficher la carte après l’envoi de la campagne. Pour les campagnes récurrentes, cela se fera à l’intervalle de récurrence suivant.</td>
    <td class="tg-0pky">Braze évalue l’adhésion la prochaine fois où l’utilisateur ouvre votre application (démarre une session).<br><br> Ce paramètre aura une portée d’audience plus large car l’éligibilité de l’utilisateur nouveau ou anonyme sera toujours évaluée lorsqu’il essaiera d’afficher la carte.</td>
  </tr>
  <tr>
    <td class="leftHeader">Personnalisation</td>
    <td class="tg-0pky">Braze évalue le Liquid, le contenu connecté et les blocs de contenu au moment du lancement de la campagne. Pour les campagnes récurrentes, cela se fera à l’intervalle de récurrence suivant.</td>
    <td class="tg-0pky">Braze évalue le Liquid, le contenu connecté et les blocs de contenu au moment de la première impression ou après l’intervalle de récurrence suivant.</td>
  </tr>
  <tr>
    <td class="leftHeader">Analytique</td>
    <td class="tg-0pky"><em>Messages envoyés</em> fait référence au nombre de cartes créées et disponibles pour être consultées. Le fait que les utilisateurs aient consulté ou non la carte n’est pas comptabilisé.</td>
    <td class="tg-0pky"><em>Messages envoyés</em> fait référence au nombre de cartes affichées aux utilisateurs. <br><br>Bien que vos utilisateurs et vos impressions accessibles ne changent pas, vous pouvez vous attendre à voir une diminution du volume d’envoi (<em>Messages envoyés</em>) lorsqu’une carte est créée à la première impression par rapport au fait qu’elle soit créée au lancement de la campagne.</td>
  </tr>
  <tr>
    <td class="leftHeader">Temps de traitement</td>
    <td class="tg-0pky">Les cartes sont créées pour chaque utilisateur éligible du segment au moment du lancement. Pour les audiences importantes, nous recommandons de sélectionner <b>lors de la première impression</b>, car les cartes seront disponibles plus rapidement après le lancement.</td>
    <td class="tg-0pky">Les cartes sont créées la première fois qu’un utilisateur essaie de les visualiser, de sorte qu’il peut s’écouler 1 à 2 secondes pour qu’elles s’affichent lors de la première impression.</td>
  </tr>
</tbody>
</table>

## Considérations

### Modification de la création de la carte après le lancement

Braze recommande de ne pas modifier la façon dont les cartes sont créées après le lancement d’une campagne. En raison des différences dans la façon dont les messages envoyés sont calculés entre les deux types de création de cartes, changer la façon dont les cartes sont créées après le lancement de la campagne peut affecter la précision de votre volume d’envoi.

### Temps de traitement potentiel

Nous recommandons que les campagnes avec une audience importante utilisent l’option de créer des cartes dès la première impression, car les cartes seront disponibles beaucoup plus rapidement après le lancement de la campagne. Les campagnes déclenchées au démarrage de la session peuvent également choisir de créer une carte dès la première impression pour améliorer les performances.

Lorsque les cartes sont créées à la première impression, leur traitement peut prendre 1 à 2 secondes. La durée de ce temps de traitement dépend de divers facteurs, tels que la taille de la carte et la complexité des options de modélisation du message. Par exemple, le temps de traitement des cartes utilisant le Contenu connecté sera au moins aussi long que le temps de réponse du Contenu connecté.

### Versions antérieures du SDK

Si l’application d’un utilisateur exécute une version antérieure du SDK, il recevra toujours des cartes de contenu envoyées avec une création de carte spécifiée. Cependant, les cartes prendront plus de temps à apparaître pour ces utilisateurs et peuvent ne pas apparaître avant la prochaine synchronisation de la carte de contenu.

[1]: {% image_buster /assets/img_archive/card_creation.png %}
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/content_cards/create/
[3]: https://www.braze.com/resources/articles/whats-an-app-session-anyway
