---
nav_title: Reciblage utilisateur
article_title: Reciblage utilisateur par SMS
page_order: 5
description: "Cet article de référence explique comment les utilisateurs peuvent recibler leurs messages via les interactions par SMS."
page_type: reference
tool:
  - Campagnes
channel:
  - SMS

---

# Reciblage SMS

Outre le changement de l’état d’abonnement de l’utilisateur et l’envoi de réponses automatiques selon les mots-clés entrants, Braze enregistre les interactions dans le profil utilisateur pour filtrer et déclencher des messages. Ces filtres et déclencheurs vous permettent de filtrer les utilisateurs ayant reçu des SMS et de déclencher des messages lorsque les utilisateurs reçoivent des SMS d’une campagne par SMS spécifique. 

{% alert tip %}
Pour en savoir plus sur les mots-clés personnalisés et comment configurer des messages bidirectionnels afin de profiter de ces options de reciblage, consultez notre article sur les [mots-clés personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/).
{% endalert %}  

## Options de reciblage

### Filtrer les utilisateurs par SMS

Les utilisateurs peuvent être filtrés par le dernier SMS reçu ou s’ils ont reçu un SMS d’une campagne SMS spécifique. Les filtres peuvent être définis à l’étape Utilisateurs cibles du créateur de campagne. 

**Filtrer par derniers SMS reçus**<br>
![Filtre de segmentation Dernier SMS reçu après le 8 décembre 2020.][2]

**Filtrer par messages reçus de la campagne par SMS**<br>
Filtre les utilisateurs qui ont reçu un message d’une campagne par SMS spécifique. Avec ce filtre, vous avez également la possibilité de filtrer ceux qui n’ont pas reçu de messages d’une campagne par SMS. <br>
![Filtre de segmentation A reçu un message de la campagne « Reciblage SMS ».][1]

### Déclencher des messages lorsque les utilisateurs reçoivent des SMS

Pour déclencher des messages lorsque les utilisateurs reçoivent des SMS d’une campagne spécifique, sélectionnez **Interagir avec la campagne** comme action de déclenchement pour une campagne par événement. Ensuite, sélectionnez **Recevoir un SMS** et la campagne par SMS que vous souhaitez utiliser.

![][3]

## Reciblage spécifique à la catégorie de mots-clés

Outre les trois catégories de mots-clés par défaut (Abonnement, Désabonnement et Aide), vous pouvez créer jusqu’à 25 catégories de mots-clés, et ainsi identifier les mots-clés et les réponses arbitraires. Ces catégories peuvent être utilisées pour filtrer et recibler. Pour en savoir plus sur les catégories de mots-clés SMS et comment les configurer, consultez la section [Reciblage des SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/). 

### Filtrer par récence

Filtrez la récence d’un utilisateur répondant à votre programme SMS. Ce filtre évalue la dernière date à laquelle un utilisateur a envoyé un SMS entrant appartenant à l’une des catégories de mots-clés. 

![Filtre de segmentation Dernier SMS envoyé au groupe d’abonnement « SMS marketing » avec le mot-clé « Abonnement » après le 11 août 2020.][6]

### Filtrer par attribution de campagne ou de Canvas

Filtrez les utilisateurs ayant répondu à une campagne par SMS ou un composant Canvas, une catégorie de mot-clé ou une balise spécifique.

**Filtrer par réponse à une catégorie de campagne spécifique**<br>
![Campagne avec le filtre « A répondu au SMS » pour la campagne « Promotion » « SMS-283 ». Dans le filtre, la fonction indique « Ce filtre expirera 25 mois après l’envoi du dernier message de « Promotion » s’il n’est utilisé dans aucune campagne active. »][12]

**Filtre selon la réponse à une campagne ou un Canvas avec la balise spécifique**
![ Campagne avec le filtre « À répondu au SMS » pour la campagne ou Canvas avec la balise « Service de messagerie Curbside C ».][13]

**Filtre selon la réponse à une étape spécifique**
![ Campagne avec le filtre « À répondu au SMS » pour l’étape « Double abonnement SMS » « Étape - Aide ».][11]

### Déclencher des messages par mot-clé

Les messages peuvent être déclenchés lorsque les utilisateurs envoient des messages entrants selon des catégories de mots-clés (l’utilisateur a envoyé l’un des mots-clés) ou d’autres mots-clés (l’utilisateur a envoyé un mot-clé n’appartenant à aucune catégorie existante). Ces déclencheurs sont définis lors de l’étape de livraison du créateur de campagne.

{% alert tip %} 
Si un Canvas par événement est déclenché par un SMS entrant, vous pouvez référencer les propriétés du SMS dans la première [étape de message]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/message_step/) du Canvas.
{% endalert %}

**Déclencher par catégorie de mots-clés entrants**<br>
![Campagne SMS par événement avec le filtre de segmentation Envoyer le mot-clé « Abonnement » au groupe d’abonnement « SMS marketing ».][7]{: style="margin-top:10px;"}

**Déclencher par mots-clés arbitraires**<br>
Remarque : lorsque vous déclenchez un message à une réponse de mot-clé « Autre », vous pouvez évaluer la correspondance exacte du texte du corps du mot-clé. Cette correspondance obéit aux mêmes règles indiquées : Seul le **message avec exactement un mot** est traité (_non sensible_ à la casse). Un mot-clé envoyé `Bonjour Braze !` ne correspond pas aux critères montrés dans l’exemple suivant. 
![Campagne SMS par événement avec la catégorie de mots-clés « Autre », où le corps du message est exactement « Bonjour » ou « Salut ».][8]{: style="margin-top:10px;"}

**Mots-clés de modèle**<br>
Lorsque vous déclenchez une campagne ou un composant Canvas sur un SMS ou MMS entrant, vous pouvez créer un modèle pour le texte ou les pièces jointes que votre utilisateur a envoyées dans le corps de votre campagne ou du Canvas avec Liquid. Vous pourrez accéder à la réponse de l’utilisateur et l’inclure dans votre réponse, puis appliquer une logique conditionnelle ou toute autre opération possible dans Liquid. 

{% raw %}

```liquid
Sorry, we didn't recognize {{sms.${inbound_message_body}}}. Text HELP for help or STOP to stop.
```

```liquid
{% if {{sms.${inbound_message_body}}} == "SNEAKERS" %}
OK, you're subscribed to updates on all our sneaker deals!
{% elsif {{sms.${inbound_message_body}}} == "SHIRTS" %}
Shirt deals coming up for you!
{% else %}
Want to receive a specific deal? Just text us the category you're interested in. For example SHIRTS or SNEAKERS.
{% endif %}
```

{% endraw %}

[1]: {% image_buster /assets/img/sms/filter1.png %}
[2]: {% image_buster /assets/img/sms/filter2.png %}
[3]: {% image_buster /assets/img/sms/trigger.png %} 
[6]: {% image_buster /assets/img/sms/retargeting1.png %}
[7]: {% image_buster /assets/img/sms/retargeting2.png %}
[8]: {% image_buster /assets/img/sms/retargeting3.png %}
[16]: {% image_buster /assets/img/keyword_example1.jpg %}
[17]: {% image_buster /assets/img/keyword_example2.jpg %}
[11]: {% image_buster /assets/img/sms/clicked_opened_step.png %}
[12]: {% image_buster /assets/img/sms/clicked_opened_campaign.png %}
[13]: {% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %} 
