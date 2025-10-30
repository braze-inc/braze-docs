---
nav_title: Campagnes de reciblage
article_title: Campagnes de reciblage
page_order: 2
page_type: reference
description: "Cet article de référence explique comment et pourquoi vous devriez envisager des campagnes de reciblage basées sur les messages reçus par vos utilisateurs."
tool:
  - Campaigns
  
---

# Campagnes de reciblage

> En reciblant les campagnes en fonction des actions précédentes de l'utilisateur, comme l'ouverture ou non d'un e-mail, vous pouvez aider à reclasser vos utilisateurs, ouvrant ainsi la voie à une approche marketing axée sur les données efficace.

Braze permet de recibler les utilisateurs en fonction des messages qu'ils ont reçus. Vous pouvez recibler les utilisateurs en fonction de leurs interactions avec vos campagnes et Canvas. 

Chacun de ces filtres de reciblage vous offre plusieurs options après les avoir ajoutés. Pour en savoir plus sur le ciblage des utilisateurs, consultez notre [cours d'apprentissage Braze](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sur la configuration des campagnes !

!section Détails du segment avec le menu déroulant des filtres disponibles.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Filtres de reciblage

Vous pouvez utiliser les filtres de reciblage de cette section pour vos utilisateurs au sein de vos campagnes et Canevas.

### Campagne cliquée/ouverte

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas :

- Cliquez sur un e-mail
- Cliquez sur un message in-app
- Ouverture directe d'une notification push
- Ouverture d'un e-mail
- Consultation d'un message in-app

\![]({% image_buster /assets/img_archive/clickedopened.png %})

Vous pouvez le préciser en sélectionnant la campagne que vous souhaitez recibler.

### Cliquez ou ouvrez la campagne ou le canvas avec l'étiquette

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas interagi avec des campagnes ou des Canvas avec une étiquette donnée :

- Cliquez sur un e-mail
- Cliquez sur un message in-app
- Ouverture directe d'une notification push
- Ouverture d'un e-mail
- Consultation d'un message in-app

\![]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Converti de la campagne 

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas converti (en fonction de la conversion principale) dans votre campagne cible. 

Pour les campagnes récurrentes, ce filtre indique si les utilisateurs se sont convertis au message le plus récent de la campagne.

\![]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Converti en toile 

Utilisez ce filtre pour trouver des utilisateurs qui ont ou n'ont pas converti (sur la base de la conversion principale) dans votre Canvas cible.

Pour les Canvas récurrents, ce filtre permet de savoir si les utilisateurs se sont déjà convertis à chaque fois qu'ils ont parcouru le Canvas.

\![]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### Dans le groupe de contrôle de la campagne 

Utilisez ce filtre pour trouver des utilisateurs qui font ou ne font pas partie du groupe de contrôle de votre campagne de ciblage.

\![]({% image_buster /assets/img_archive/campaign_control_group.png %})

### Dans le groupe de contrôle Canvas 

Utilisez ce filtre pour trouver des utilisateurs qui font ou ne font pas partie du groupe de contrôle de votre Canvas cible, qui peut être sélectionné dans le menu déroulant.

\![]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Dernier message reçu d'une campagne spécifique 

Utilisez ce filtre pour trouver les utilisateurs qui ont reçu une campagne spécifique pour la dernière fois avant ou après une date ou un nombre de jours spécifiés. Ce filtre ne tient pas compte du moment où les utilisateurs ont reçu d'autres campagnes.

\![]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Dernier message reçu d'une campagne spécifique ou d'un Canvas avec étiquette 

Utilisez ce filtre pour trouver les utilisateurs qui ont reçu pour la dernière fois une campagne spécifique ou un Canvas avec une étiquette donnée avant ou après une date ou un nombre de jours spécifiés. Ce filtre ne tient pas compte du fait que les utilisateurs ont reçu d'autres campagnes ou canevas.

\![]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Réception d'un message de la campagne 

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas reçu votre campagne cible.

\![]({% image_buster /assets/img_archive/receivedcamp.png %})

### Réception d'un message de la campagne ou de Canvas avec une étiquette 

Utilisez ce filtre pour trouver les utilisateurs qui ont ou n'ont pas reçu une campagne ou un canvas comportant votre étiquette cible.

\![]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Avantages des campagnes de reciblage

Le reciblage est particulièrement efficace lorsque le segment d'origine comprenait également une action spécifique que vous souhaitez voir les utilisateurs entreprendre. Par exemple, disons que vous avez une carte ciblée sur les utilisateurs qui n'ont jamais effectué d'achat. La carte annonce une promotion pour un achat in-app à prix réduit. Le segment initial se présente comme suit :

- L'argent dépensé dans l'application est exactement 0
- Dernière application utilisée il y a moins de 14 jours

Le nombre total d'utilisateurs dans le segment est de 100 000 et vous savez, d'après les statistiques de la carte de contenu, que 60 000 utilisateurs uniques ont vu la carte et que 20 000 utilisateurs uniques ont cliqué sur la carte. Grâce à la segmentation, nous pouvons voir combien de ces utilisateurs qui ont cliqué sur la carte ont effectivement effectué un achat :

- L'argent dépensé dans l'application est supérieur à 0
- La carte cliquée est le nom de la carte

Après avoir examiné ces statistiques, nous pouvons établir une segmentation des utilisateurs qui ont cliqué sur la carte, mais n'ont pas effectué d'achat :

- L'argent dépensé dans l'application est exactement supérieur à 0
- La carte cliquée est le nom de la carte

Nous pouvons recibler ce segment avec des envois de messages supplémentaires autour de la promotion ou d'un autre achat in-app. Le reciblage peut se faire au moyen d'une campagne d'envoi de messages. Une approche multicanal vous permet d'atteindre les utilisateurs là où ils sont le plus susceptibles de répondre, augmentant ainsi l'efficacité de vos campagnes.

