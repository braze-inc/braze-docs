---
nav_title: Reciblage utilisateur
article_title: Reciblage utilisateur par SMS
description: "Cet article de référence explique comment les utilisateurs peuvent recibler leurs messages via les interactions par SMS."
page_type: reference
tool:
  - Campaigns
channel:
  - SMS

---

# Reciblage utilisateur

> En plus de modifier l'état d'abonnement de l'utilisateur et d'envoyer des réponses automatiques en fonction des mots-clés entrants, Braze enregistrera également les interactions avec le profil utilisateur afin de filtrer et de déclencher des messages.<br><br>Ces filtres et déclencheurs vous permettent de filtrer les utilisateurs ayant reçu des SMS et de déclencher des messages lorsque les utilisateurs reçoivent des SMS d’une campagne par SMS spécifique. 

{% alert tip %}
Pour en savoir plus sur les mots-clés personnalisés et sur la manière de mettre en place un envoi de messages bidirectionnel pour tirer parti de ces options de reciblage, consultez notre article sur les [mots-clés personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/).
{% endalert %}  

## Options de reciblage

{% alert note %}
Lorsque vous créez des audiences avec le reciblage utilisateur, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la protection de la vie privée, telles que le droit "Ne pas vendre ou partager" en vertu de la CUP. Les marketeurs doivent mettre en œuvre les filtres pertinents pour l'éligibilité des utilisateurs au sein de leurs critères d'entrée dans le canvas et/ou la campagne.
{% endalert %}

### Filtrer les utilisateurs par SMS

Les utilisateurs peuvent être filtrés par le dernier SMS reçu ou s’ils ont reçu un SMS d’une campagne SMS spécifique. Les filtres peuvent être définis à l’étape Utilisateurs cibles du créateur de campagne. 

**Filtrer sur le dernier SMS reçu**<br>
![Filtre de segmentation Dernier SMS reçu après le 8 décembre 2020.][2]

**Filtre sur les messages reçus dans le cadre d'une campagne de communication par SMS**<br>
Filtre les utilisateurs qui ont reçu un message d’une campagne par SMS spécifique. Avec ce filtre, vous avez également la possibilité de filtrer ceux qui n’ont pas reçu de messages d’une campagne par SMS. <br>
![Filtre de segmentation A reçu un message de la campagne « Reciblage SMS ».][1]

### Déclencher des messages lorsque les utilisateurs reçoivent des SMS {#trigger-messages}

Pour déclencher des messages lorsque les utilisateurs reçoivent des SMS d'une campagne spécifique, sélectionnez **Interagir avec la campagne** comme action déclenchante pour une campagne basée sur des actions. Sélectionnez ensuite **Recevoir des SMS** et la campagne SMS que vous souhaitez utiliser.

![][3]

### Filtrer par liens de suivi avancé

Recibler les utilisateurs qui ont cliqué sur les campagnes avec des [liens de suivi avancés]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/link_shortening/).
Seules les campagnes où le suivi avancé est activé apparaîtront dans les listes déroulantes suivantes :

**Recibler les utilisateurs qui ont cliqué sur une campagne SMS spécifique**
1. Créez un segment à l'aide du filtre **Campagne cliquée/ouverte.** 
2. Sélectionnez les **sms cliqués**.
3. Choisissez la campagne souhaitée.

![][15]

**Recibler les utilisateurs qui ont cliqué sur une étape de canvas spécifique**
1. Créez une segmentation à l'aide du filtre **Étape cliquée/ouverte.** 
2. Sélectionnez les **sms cliqués**.
3. Choisissez le Canvas ou l'étape de Canvas souhaités.

![][16]

## Reciblage spécifique à la catégorie de mots-clés

Outre les trois catégories de mots-clés par défaut (Abonnement, Désabonnement et Aide), vous pouvez créer jusqu’à 25 catégories de mots-clés, et ainsi identifier les mots-clés et les réponses arbitraires. Ces catégories peuvent être utilisées pour filtrer et recibler. Pour en savoir plus sur les catégories de mots-clés par SMS et sur la manière de les mettre en place, reportez-vous à la rubrique [reciblage par SMS.]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/retargeting/) 

### Filtrer par récence

Filtrez la récence d’un utilisateur répondant à votre programme SMS. Ce filtre évalue la dernière date à laquelle un utilisateur a envoyé un SMS entrant appartenant à l’une des catégories de mots-clés. 

![Filtre de segmentation Dernier SMS envoyé au groupe d’abonnement « SMS marketing » avec le mot-clé « Abonnement » après le 11 août 2020.][6]

### Filtrer par attribution de campagne ou de Canvas

Filtrez les utilisateurs ayant répondu à une campagne par SMS ou un composant Canvas, une catégorie de mot-clé ou une balise spécifique.

**Filtrer en fonction des réponses à une catégorie de campagne spécifique**<br>
![Campagne avec le filtre « A répondu au SMS » pour la campagne « Promotion » « SMS-283 ». Dans le filtre, la fonction indique « Ce filtre expirera 25 mois après l’envoi du dernier message de « Promotion » s’il n’est utilisé dans aucune campagne active. »][12]

**Filtrer en fonction des réponses à une campagne ou à un canvas avec une étiquette spécifique**
![Campagne avec le filtre « A répondu au SMS » pour la campagne ou le Canvas avec la balise « Service de messagerie Curbside C ».][13]

**Filtrer en répondant à une étape spécifique**
![Campagne avec le filtre « A répondu au SMS » pour l’étape « Double abonnement SMS » « Étape - Aide ».][11]

### Déclencher des messages par mot-clé

Les messages peuvent être déclenchés lorsque les utilisateurs envoient des messages entrants selon des catégories de mots-clés (l’utilisateur a envoyé l’un des mots-clés) ou d’autres mots-clés (l’utilisateur a envoyé un mot-clé n’appartenant à aucune catégorie existante). Ces déclencheurs sont définis lors de l’étape de livraison du créateur de campagne.

Lorsque l'on évalue si un message entrant répond à un événement déclencheur défini, les espaces de début et de fin sont supprimés avant le début de l'évaluation.

{% alert tip %}
Si un canvas basé sur une action est déclenché par un message SMS entrant, vous pouvez faire référence aux propriétés du SMS dans n'importe quelle étape du canvas jusqu'au prochain parcours d'action.
{% endalert %}

**Déclencheur par catégorie de mots-clés entrants**<br>
![Campagne SMS par événement avec le filtre de segmentation Envoyer le mot-clé « Abonnement » au groupe d’abonnement « SMS marketing ».][7]{: style="margin-top:10px;"}

**Déclenchement par mots-clés arbitraires**<br>
Remarque : lorsque vous déclenchez un message à une réponse de mot-clé « Autre », vous pouvez évaluer la correspondance exacte du texte du corps du mot-clé. Cette correspondance obéit aux mêmes règles indiquées : Seul le **message avec exactement un mot** est traité (_non sensible_ à la casse). Un mot-clé envoyé `Hello Braze!` ne correspond pas aux critères montrés dans l’exemple suivant.
![Campagne SMS par événement avec la catégorie de mots-clés « Autre », où le corps du message est exactement « Bonjour » ou « Salut ».][8]{: style="margin-top:10px;"}

**Mots clés du modèle**<br>
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
[15]: {% image_buster /assets/img/sms/retargeting5.png %}
[16]: {% image_buster /assets/img/sms/retargeting4.png %}
