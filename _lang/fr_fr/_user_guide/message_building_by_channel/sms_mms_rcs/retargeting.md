---
nav_title: Reciblage des utilisateurs
article_title: Reciblage des utilisateurs
description: "Cet article de référence traite de la manière dont les utilisateurs peuvent recibler leurs messages en fonction des interactions SMS et RCS d'un utilisateur."
page_type: reference
page_order: 4
alias: /sms_mms_rcs_user_retargeting/
tool:
  - Campaigns
channel:
  - SMS
  - MMS
  - RCS

---

# Reciblage des utilisateurs

> En plus de modifier l'état d'abonnement de l'utilisateur et d'envoyer des réponses automatiques en fonction des mots-clés entrants, Braze enregistrera également les interactions avec le profil utilisateur afin de filtrer et de déclencher des messages.<br><br>Ces filtres et déclencheurs vous permettent de filtrer les actions en fonction des utilisateurs qui ont été envoyés ou ont répondu à des campagnes SMS, MMS et RCS, ou d'engager davantage les utilisateurs qui ont cliqué sur des URL raccourcies.

{% alert tip %}
Pour en savoir plus sur les mots-clés personnalisés et sur la manière de mettre en place un envoi de messages bidirectionnel pour tirer parti de ces options de reciblage, consultez notre article sur les [mots-clés personnalisés]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/).
{% endalert %}  

## Options de reciblage

{% alert note %}
Lorsque vous créez des audiences avec le reciblage utilisateur, vous pouvez souhaiter inclure ou exclure certains utilisateurs en fonction de leurs préférences, et afin de respecter les lois sur la protection de la vie privée, telles que le droit "Ne pas vendre ou partager" en vertu de la CUP. Les marketeurs doivent mettre en œuvre les filtres pertinents pour l'éligibilité des utilisateurs au sein de leurs critères d'entrée dans le canvas et/ou la campagne.
{% endalert %}

### Filtrer les utilisateurs par SMS, MMS et RCS

Les utilisateurs peuvent être filtrés en fonction de la date à laquelle ils ont reçu pour la dernière fois un SMS, un MMS ou un RCS, ou en fonction de la date à laquelle ils ont reçu un SMS, un MMS ou un RCS dans le cadre d'une campagne spécifique. Les filtres peuvent être définis dans l'étape " **Audiences cibles"** du générateur de campagne. 

**Filtre sur le dernier SMS/MMS/RCS reçu**<br>
\![Filtre de segmentation Dernier SMS reçu après le 8 décembre 2020.]({% image_buster /assets/img/sms/filter2.png %})

**Filtre sur les messages reçus dans le cadre d'une campagne SMS/MMS/RCS**<br>
Filtre les utilisateurs qui ont reçu un message d'une campagne spécifique. Avec ce filtre, vous avez également la possibilité de filtrer les personnes qui n'ont pas reçu de messages d'une campagne. <br>
\![Le filtre de segmentation a reçu un message de la campagne "SMS reciblage".]({% image_buster /assets/img/sms/filter1.png %})

### Déclenchez des messages lorsque les utilisateurs reçoivent des SMS, des MMS ou des RCS. {#trigger-messages}

Pour déclencher des messages lorsque les utilisateurs reçoivent des messages SMS, MMS ou RCS d'une campagne spécifique, sélectionnez **Interagir avec la campagne** comme action de déclenchement pour une campagne basée sur des actions. Ensuite, sélectionnez **Recevoir des SMS** et la campagne SMS, MMS ou RCS que vous souhaitez utiliser.

\![]({% image_buster /assets/img/sms/trigger.png %})

### Filtre sur les liens de suivi avancés

Recibler les utilisateurs qui ont cliqué sur les campagnes avec des [liens de suivi avancés]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/).
Seules les campagnes pour lesquelles le suivi avancé est activé apparaîtront dans les listes déroulantes suivantes :

**Recibler les utilisateurs qui ont cliqué sur un SMS, un MMS ou une campagne RCS spécifique.**
1. Créez un segment à l'aide du filtre **Campagne cliquée/ouverte.** 
2. Sélectionnez le **lien SMS raccourci cliqué**.
3. Choisissez la campagne souhaitée.

\![]({% image_buster /assets/img/sms/retargeting5.png %})

**Recibler les utilisateurs qui ont cliqué sur une étape du canvas.**
1. Créez une segmentation à l'aide du filtre **Étape cliquée/ouverte**.
2. Sélectionnez le **lien SMS raccourci cliqué**.
3. Choisissez la toile et l'étape du canvas souhaitées.

\![]({% image_buster /assets/img/keyword_example1.jpg %})

## Reciblage par catégorie de mots clés

Outre les trois catégories de mots-clés par défaut (Abonnement, Désabonnement et Aide), vous pouvez créer jusqu'à 25 catégories de mots-clés qui vous sont propres, ce qui vous permet d'identifier des mots-clés et des réponses arbitraires. Ces catégories peuvent être utilisées pour le filtrage et le reciblage. Pour en savoir plus sur les catégories de mots-clés globales et sur la manière de les configurer, reportez-vous à la section [Traitement des mots-clés]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/). 

### Filtrer par récence

Filtrez la récurrence de la réponse d'un utilisateur à votre programme SMS, MMS ou RCS. Ce filtre évalue la dernière date à laquelle un utilisateur a envoyé un message entrant entrant dans l'une des catégories de mots-clés. 

\![Filtre de segmentation Dernier SMS envoyé au groupe d'abonnement "Marketing sms" avec le mot-clé "Abonnement" après le 11 août 2020.]({% image_buster /assets/img/sms/retargeting1.png %})

### Filtrer par attribution de campagne ou de canvas.

Filtre pour les utilisateurs qui ont répondu à une campagne SMS, MMS ou RCS spécifique ou à un composant Canvas, à une catégorie de mots clés ou à une étiquette.

**Filtrer les réponses à une campagne spécifique par catégorie de mots-clés**<br>
\![Campagne avec le filtre "A répondu au SMS" pour la campagne "SMS-283" "Promotion". Sous le filtre, la fonctionnalité mentionne "Ce filtre expirera 25 mois après l'envoi du dernier message de "Promotion" s'il n'est pas utilisé dans le cadre d'une campagne active."]({% image_buster /assets/img/sms/clicked_opened_campaign.png %})

**Filtrer en fonction des réponses à une campagne ou à un canvas avec une étiquette spécifique.**
\![Campagne avec le filtre "A répondu au SMS" pour la campagne ou le Canvas avec l'étiquette "Curbside Messaging Service C".]({% image_buster /assets/img/sms/clicked_opened_campaign_canvas_tag.png %})

**Filtrer en répondant à une étape spécifique**
Campagne avec le filtre "A répondu au SMS" pour l'étape "SMS Double Opt" "Étape - Aide".]({% image_buster /assets/img/sms/clicked_opened_step.png %})

### Déclencher des messages par mot-clé

Les messages peuvent être déclenchés lorsque les utilisateurs envoient des messages entrants sur la base de catégories de mots-clés (l'utilisateur a envoyé l'un des mots-clés) ou d'autres mots-clés (l'utilisateur a envoyé un mot-clé qui n'entre pas dans l'une des catégories existantes). Ces déclencheurs sont définis dans l'étape de réception/distribution du générateur de campagne.

Lorsque l'on évalue si un message entrant répond à un événement déclencheur défini, les espaces de début et de fin sont supprimés avant le début de l'évaluation.

{% alert tip %}
Si un Canvas basé sur une action est déclenché par un message SMS ou MMS entrant, vous pouvez faire référence aux [propriétés de liquide SMS prises en charge]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/) dans n'importe quelle étape du Canvas jusqu'au prochain chemin d'action.
{% endalert %}

**Déclencheur par catégorie de mots-clés entrants**<br>
!Campagne SMS basée sur l'action avec le filtre de segmentation Mot-clé envoyé "Opt-in" vers le groupe d'abonnement "Marketing SMS".]({% image_buster /assets/img/sms/retargeting2.png %}){: style="margin-top:10px;"}

**Déclenchement par mots-clés arbitraires**<br>
Notez que lorsque vous déclenchez un message sur une réponse par mot-clé "Autre", vous avez la possibilité d'évaluer le corps du mot-clé sur la base d'une correspondance textuelle exacte. Ce match suit les mêmes règles que celles mentionnées ci-dessus : Seul le **message exact, composé d'un seul mot,** sera traité ( _insensible à la_ casse). Un mot-clé envoyé à `Hello Braze!` ne correspondrait pas aux critères de l'exemple suivant.
Campagne SMS basée sur l'action avec la catégorie de mots clés "Autre" et dont le corps du message est exactement "Bonjour" ou "Hey".]({% image_buster /assets/img/sms/retargeting3.png %}){: style="margin-top:10px;"}

**Mots clés du modèle**<br>
Lorsque vous déclenchez une campagne ou un composant Canvas sur un SMS ou un MMS entrant, vous pouvez, si vous le souhaitez, insérer dans le corps de votre campagne ou de votre Canvas un modèle de texte ou de pièces jointes média que votre utilisateur a envoyées avec Liquid. Cela vous permettra d'accéder à la réponse de l'utilisateur que vous pourrez ensuite inclure dans votre réponse, appliquer une logique conditionnelle ou tout ce que vous pouvez faire avec Liquid. 

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

[16] : {% image_buster /assets/img/keyword_example1.jpg %}
[16] : {% image_buster /assets/img/sms/retargeting4.png %}
