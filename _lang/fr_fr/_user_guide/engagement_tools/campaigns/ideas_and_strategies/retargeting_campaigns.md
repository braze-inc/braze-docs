---
nav_title: Campagnes de reciblage
article_title: Campagnes de reciblage
page_order: 2
page_type: reference
description: "Le présent article de référence explique comment et pourquoi vous devriez envisager des campagnes de reciblage basées sur les messages que vos utilisateurs reçoivent."
tool:
  - Campaigns
  
---

# Campagnes de reciblage

> En reciblant les campagnes sur la base des actions précédentes de l’utilisateur, comme ouvrir ou non un e-mail, vous pouvez aider à les reclasser, ouvrant la porte à une approche marketing efficace et axée sur les données.

{% alert note %}
Cet article comprend des informations sur les fils d’actualité, qui deviennent obsolètes. Braze recommande aux clients qui utilisent notre outil de fil d’actualités de passer à notre canal de communication de cartes de contenu : il est plus flexible, plus personnalisable et plus fiable. Consultez le [guide de migration]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/migrating_from_news_feed/) pour en savoir plus.
{% endalert %}

Braze fournit un support pour recibler les utilisateurs sur la base des messages qu’ils ont reçus. Vous pouvez recibler les utilisateurs sur la base de leurs interactions avec vos campagnes, Canvas et cartes de fil d’actualité. 

Chacun de ces filtres de reciblage vous fournit plusieurs options après les avoir ajoutés. Pour en savoir plus sur le ciblage des utilisateurs, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes !

![La section Détails du segment avec le menu déroulant pour les filtres disponibles.][1]{: style="max-width:80%;"}

## Filtres de reciblage

Vous pouvez utiliser les filtres de reciblage dans cette section pour vos utilisateurs au sein de vos campagnes, Canvas et cartes de fil d’actualité.

### Carte cliquée

Utilisez le filtre pour trouver les utilisateurs qui ont ou n’ont pas cliqué sur une carte de fil d’actualité donnée.

![][2]

### Campagne cliquée/ouverte

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n’ont pas :

- Cliqué sur un e-mail
- Cliqué sur un message in-app
- Ouvert directement une notification push
- Ouvert un e-mail
- Consulté un message in-app

![][3]

Vous pouvez ajouter des spécifications supplémentaires en sélectionnant la campagne que vous souhaitez recibler.

### Cliqué ou ouvert une campagne ou Canvas avec un tag

Utilisez ce filtre pour trouver des utilisateurs qui ont ou n’ont pas interagi avec des campagnes ou des Canvas comportant une balise donnée :

- Cliqué sur un e-mail
- Cliqué sur un message in-app
- Ouvert directement une notification push
- Ouvert un e-mail
- Consulté un message in-app

![][16]

### Convertis par la campagne 

Utilisez ce filtre pour trouver des utilisateurs qui ont ou n’ont pas été convertis (en fonction de la conversion principale) dans votre campagne cible. 

Pour les campagnes récurrentes, ce filtre indique si les utilisateurs se sont convertis à partir du message le plus récent de la campagne.

![][12]

### Convertis par le Canvas 

Utilisez ce filtre pour trouver des utilisateurs qui ont ou n’ont pas été convertis (en fonction de la conversion principale) dans votre Canvas cible.

Pour les Canvas récurrents, ce filtre fait référence au fait que les utilisateurs se sont déjà convertis une fois qu’ils ont parcouru le Canvas.

![][18]

### Dans le groupe de contrôle de campagne 

Utilisez ce filtre pour trouver des utilisateurs qui sont ou ne sont pas dans le groupe de contrôle de votre campagne cible.

![][13]

### Dans le groupe de contrôle de Canvas 

Utilisez ce filtre pour trouver des utilisateurs qui font ou ne font pas partie du groupe de contrôle de votre Canvas cible, qui peut être sélectionné dans le menu déroulant.

![][19]

### Dernier message reçu de la campagne donnée 

Utilisez ce filtre pour trouver les utilisateurs qui ont reçu une campagne spécifique avant ou après une date ou un nombre de jours spécifié. Ce filtre ne tient pas compte du moment où les utilisateurs ont reçu d'autres campagnes.

![][14]

### Dernier message reçu à partir d’une campagne ou d’un Canvas avec une balise 

Utilisez ce filtre pour trouver les utilisateurs qui ont reçu une campagne spécifique ou un Canvas comportant une balise donnée avant ou après une date ou un nombre de jours spécifié. Ce filtre ne tient pas compte du fait que les utilisateurs ont reçu d'autres campagnes ou canevas.

![][17]

### Message reçu de la campagne 

Utilisez ce filtre pour trouver des utilisateurs qui ont ou n’ont pas reçu votre campagne cible.

![][4]

### Message reçu à partir d’une campagne ou d’un Canvas avec tag 

Utilisez ce filtre pour trouver des utilisateurs qui ont ou n’ont pas reçu votre campagne ou votre Canvas portant votre balise cible.

![][15]

## Avantages des campagnes de reciblage

Le reciblage est particulièrement efficace lorsque le segment d’origine a également inclus une action spécifique que vous souhaitez voir entreprendre par les utilisateurs. Supposons par exemple que vous ayez une carte ciblée sur les utilisateurs qui n’ont jamais effectué d’achat. La carte annonce une promotion pour un achat à prix réduit dans l’application. Le segment initial ressemble à ce qui suit :

- L’argent dépensé dans l’application est exactement de 0
- Dernière utilisation de l’application il y a moins de 14 jours

Le nombre total d’utilisateurs dans le segment est de 100 000 et vous savez à l’aide des statistiques de fil d’actualité que 60 000 utilisateurs uniques ont affiché la carte et que 20 000 utilisateurs uniques ont cliqué sur la carte. Par le biais du segmenteur, nous pouvons voir combien de ces utilisateurs qui ont cliqué sur la carte ont effectivement réalisé un achat :

- L’argent dépensé dans l’application est supérieur à 0
- La carte cliquée est « Nom de la carte »

Après avoir examiné ces statistiques, nous pouvons faire un segment d’utilisateurs qui ont cliqué sur la carte, mais qui n’ont pas effectué d’achat :

- L’argent dépensé dans l’application est exactement de 0
- La carte cliquée est « Nom de la carte »

Nous pouvons recibler ce segment avec des messages supplémentaires autour de la promotion ou d’un autre achat dans l’application. Le reciblage peut être effectué avec une autre carte de fil d’actualité ou par une campagne de communication. Une approche multicanal vous permet d’atteindre les utilisateurs là où ils sont les plus susceptibles de répondre, augmentant ainsi l’efficacité de vos campagnes.

[1]: {% image_buster /assets/img_archive/retarget.png %}
[2]: {% image_buster /assets/img_archive/clickedcard.png %}
[3]: {% image_buster /assets/img_archive/clickedopened.png %}
[4]: {% image_buster /assets/img_archive/receivedcamp.png %}
[12]: {% image_buster /assets/img_archive/converted_from_campaign.png %}
[13]: {% image_buster /assets/img_archive/campaign_control_group.png %}
[14]: {% image_buster /assets/img_archive/last_received_specific_campaign.png %}
[15]: {% image_buster /assets/img_archive/received_campaign_with_tag.png %}
[16]: {% image_buster /assets/img_archive/retarget_tag_filter.png %}
[17]: {% image_buster /assets/img_archive/last_received_campaign_with_tag.png %}
[18]: {% image_buster /assets/img_archive/converted_from_canvas.png %}
[19]: {% image_buster /assets/img_archive/canvas_control_group.png %}
