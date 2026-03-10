---
nav_title: Timing intelligent
article_title: Timing intelligent
page_order: 1.3
description: "Cet article donne une vue d'ensemble du timing intelligent (anciennement Intelligent Delivery) et de son utilisation dans vos campagnes et Canvas."
---

# [![Cours Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/intelligent-timing){: style="float:right;width:120px;border:0;" class="noimgborder"}Timing intelligent

> Utilisez le timing intelligent pour diffuser votre message à chaque utilisateur au moment optimal déterminé par Braze, c'est-à-dire lorsque l'utilisateur est le plus susceptible d'interagir (ouvrir ou cliquer). Vous pouvez ainsi vérifier plus facilement que vous envoyez des messages à vos utilisateurs à leur moment préféré, ce qui peut augmenter l'engagement.

## À propos du timing intelligent

Braze calcule le moment d'envoi optimal à partir d'une analyse statistique des interactions passées de vos utilisateurs avec votre application et avec chaque canal de messagerie. Les données d'interaction suivantes sont utilisées :

- Heures de session
- Ouvertures push directes
- Ouvertures push influencées
- Clics e-mail
- Ouvertures e-mail (hors [ouvertures machine]({{site.baseurl}}/user_guide/data/report_metrics/#machine-opens))
- Clics SMS (uniquement si [raccourcissement de lien]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) et suivi avancé sont activés)

Si un utilisateur n'a pas de données d'engagement pertinentes pour calculer le moment optimal, vous pouvez spécifier une heure de repli.

## Cas d'usage

- Envoyer des campagnes récurrentes qui ne sont pas sensibles au temps
- Automatiser des campagnes avec des utilisateurs dans plusieurs fuseaux horaires
- Lors de l'envoi de messages à vos utilisateurs les plus engagés (ils auront le plus de données d'engagement)

Pour les étapes de configuration détaillées dans les campagnes et Canvas, les heures creuses, l'heure de repli, les limites et la FAQ, consultez la version complète de cet article dans le sommaire à gauche ou l'aide du tableau de bord Braze.
