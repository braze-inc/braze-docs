---
nav_title: Campagnes de redistribution
article_title: Campagnes de redistribution
page_order: 2
page_type: Référence
description: "Cet article de référence décrit comment et pourquoi vous devriez envisager des campagnes de redistribution basées sur les messages reçus par vos utilisateurs."
tool:
  - Campagnes
---

# Campagnes de redistribution

> Cet article de référence va au-delà du concept de campagnes de redistribution et de la manière dont il peut être une stratégie de marketing bénéfique. <br> <br> En reciblant des campagnes basées sur les actions précédentes de l'utilisateur, que vous ayez ouvert ou non un courriel, vous pouvez aider à reclasser vos utilisateurs, en ouvrant la porte à une approche marketing efficace et axée sur les données.

Braze fournit un support pour les utilisateurs de reciblage en fonction des messages qu'ils ont reçus. Vous pouvez recibler les utilisateurs en fonction de leurs interactions avec vos campagnes, vos Canvases et vos cartes News Feed.

Chacun de ces filtres de recul vous offre plusieurs options après les ajouter. Pour en savoir plus sur le ciblage des utilisateurs, consultez notre [cours LAB de configuration de campagne](http://lab.braze.com/campaign-setup-delivery-targeting-conversions)!

!\[Campagnes de Retargeting\]\[1\]{: style="max-width:80%;"}

## Filtres de redistribution

Vous pouvez utiliser les filtres de reciblage dans cette section pour vos utilisateurs dans vos campagnes, vos Canvès et vos cartes de flux de nouvelles.

### Carte cliquée

Utilisez le filtre pour trouver les utilisateurs qui ont et n'ont pas cliqué sur une carte de flux d'actualités spécifique.

!\[Filtre de carte cliquée\]\[2\]

### Campagne cliquée/ouverte

Utilisez ce filtre pour trouver les utilisateurs qui ont ou non :

- A cliqué sur un e-mail
- A cliqué un message dans l'application
- Ouverture directe d'une notification push
- A ouvert un e-mail
- A regardé un message dans l'application

!\[Filtre de campagne cliqué/ouverte\]\[3\]

Ceci peut être précisé en sélectionnant la campagne que vous voulez redistribuer.

### Campagne ou Canvas cliquée ou ouverte avec étiquette

!\[Clicked or opened\]\[16\]

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas interagi avec des campagnes ou des Canvases avec un tag donné:

- A cliqué sur un e-mail
- A cliqué un message dans l'application
- Ouverture directe d'une notification push
- A ouvert un e-mail
- A regardé un message dans l'application

### Converti de la campagne

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas converti (basé sur la conversion principale) dans votre campagne cible.

Pour les campagnes récurrentes, ce filtre indique si les utilisateurs ont converti sur le message le plus récent de la campagne.

!\[Filtre de la campagne convertie\]\[12\]

### Converti depuis Canvas

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas converti (selon la conversion principale) dans votre Canvas cible.

Pour les Canvases récurrentes, ce filtre indique si les utilisateurs ont jamais converti depuis qu'ils ont traversé le Canvas.

!\[Filtre Converted From Canvas\]\[18\]

### Groupe de contrôle de campagne

Utilisez ce filtre pour trouver les utilisateurs qui sont ou non dans le groupe de contrôle de votre campagne cible.

!\[Groupe de contrôle de la campagne\]\[13\]

### Dans le Groupe de Contrôle de Canvas

Utilisez ce filtre pour trouver les utilisateurs qui sont ou ne sont pas dans le groupe de contrôle de votre Canvas cible, qui peut être sélectionné dans le menu déroulant.

!\[Groupe de contrôle de Canvas\]\[19\]

### Dernier message reçu de la campagne spécifique

Utilisez ce filtre pour trouver les utilisateurs qui ont reçu la dernière fois une campagne spécifique avant ou après une date ou un nombre de jours précis.

!\[Dernier filtre de campagne spécifique reçu\]\[14\]

### Dernier message reçu de campagne spécifique ou Canvas avec étiquette

Utilisez ce filtre pour trouver les utilisateurs qui ont reçu la dernière fois une campagne ou Canvas spécifique avec une étiquette donnée avant ou après une date ou un nombre de jours spécifiés.

!\[Dernière Campagne reçue avec Tag\]\[17\]

### Message reçu de la campagne

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas reçu votre campagne cible.

!\[Campagne reçue\]\[4\]

### Message reçu de la campagne ou de Canvas avec étiquette

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas reçu une campagne ou Canvas qui a votre balise cible.

!\[Campagne reçue avec Tag\]\[15\]

## Avantages avec campagnes de redistribution

La redistribution est particulièrement efficace lorsque le segment original inclut également une action spécifique que vous souhaitez voir prendre. Par exemple, disons que vous avez une carte destinée aux utilisateurs qui n'ont jamais fait d'achat. La carte annonce une promotion pour un achat réduit dans l'application. Le segment initial ressemble à ce qui suit :

- L'argent dépensé dans l'application est exactement 0
- Dernière application utilisée il y a moins de 14 jours

Le nombre total d'utilisateurs dans le segment est de 100 000 et vous savez à partir des statistiques du flux d'actualités que 60, 00 utilisateurs uniques ont consulté la carte et 20 000 utilisateurs uniques ont cliqué sur la carte. Grâce au segmenteur, nous pouvons voir combien d'utilisateurs qui ont cliqué sur la carte ont effectivement fait un achat:

- L'argent dépensé dans l'application est supérieur à 0
- La carte cliquée est le nom de la carte

Après avoir examiné ces statistiques, nous pouvons faire un segment d'utilisateurs qui ont cliqué sur la carte, mais qui n'ont pas fait d'achat:

- L'argent dépensé dans l'application est exactement à 0
- La carte cliquée est le nom de la carte

Nous pouvons rediriger ce segment avec des messages supplémentaires autour de la promotion ou d'un autre achat dans l'application. La redistribution peut être effectuée avec une autre carte de flux de nouvelles ou par le biais d'une campagne de messagerie. Une approche multicanale vous permet d'atteindre les utilisateurs où ils sont le plus susceptibles de répondre, augmentant ainsi l'efficacité de vos campagnes.
[1]: {% image_buster /assets/img_archive/retarget.png %} [2]: {% image_buster /assets/img_archive/clickedcard.png %} [3]: {% image_buster /assets/img_archive/clickedopened. ng %} [4]: {% image_buster /assets/img_archive/receivedcamp.png %} [12]: {% image_buster /assets/img_archive/converted_from_campaign.png %} [13]: {% image_buster /assets/img_archive/campaign_control_group. ng %} [14]: {% image_buster /assets/img_archive/last_received_specific_campaign.png %} [15]: {% image_buster /assets/img_archive/received_campaign_with_tag.png %} [16]: {% image_buster /assets/img_archive/retarget_tag_filter. ng %} [17]: {% image_buster /assets/img_archive/last_received_campaign_with_tag. ng %} [18]: {% image_buster /assets/img_archive/converted_from_canvas.png %} [19]: {% image_buster /assets/img_archive/canvas_control_group.png %}
