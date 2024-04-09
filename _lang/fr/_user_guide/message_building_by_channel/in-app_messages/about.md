---
nav_title: "À propos des messages In-App"
article_title: À propos des messages In-App
page_order: 0
page_type: reference
description: "Cet article de référence donne un bref aperçu des messages in-app, des cas d’utilisation potentiels et des types de messages standard."
channel:
  - messages In-App
search_rank: 4.9
---

# [![Cours d’apprentissage Braze]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/messaging-channels-in-app-in-browser){: style="float:right;width:120px;border:0;" class="noimgborder"}À propos des messages In-App

> Les messages In-App sont utiles pour beaucoup de choses. De contenu riche, ils supposent d’une urgence moindre : l’utilisateur ne les reçoit pas hors de l’application de l’utilisateur et ils n’apparaissent pas sur son écran d’accueil. Les messages In-App se trouvent dans votre application (d’où leur nom), incluent un contexte et ne sont presque jamais indésirables ! Ils sont toujours livrés lorsque l’utilisateur est actif dans votre application.

Pour voir des exemples de messages In-App, consultez nos [études de cas][1].

## Cas d’usage potentiels

Grâce au contenu riche des messages In-App, vous pouvez exploiter ce canal pour une variété de cas d’utilisation :

| Cas d’utilisation | Explication |
| --- | --- |
| Amorçage de notification push | Lancez une campagne d’[amorçage de push][2] avec un message In-App riche afin de montrer à vos clients l’avantage de s’inscrire aux notifications push pour votre application ou votre site et de leur afficher une demande d’autorisation push.
| Soldes et promotions | Utilisez des messages In-App modaux pour offrir aux clients des contenus visuellement attrayants contenant des [codes de promotion][6] ou des offres. Incitez-les à faire des achats ou des conversions qu’ils n’auraient autrement pas faits. |
| Encouragement de l’adoption de fonctions | Encouragez les clients à utiliser d’autres parties de votre application ou à profiter d’un service. |
| Campagnes hautement personnalisées | Placez des messages In-App de façon à ce que vos clients les voient dès qu’ils entrent dans votre application ou votre site. Ajoutez des fonctionnalités de personnalisation Braze, telles que [Contenu connecté][3], pour forcer les utilisateurs à agir et donc optimiser votre portée.
{: .reset-td-br-1 .reset-td-br-2}

Autres cas d’utilisation à considérer :

- Nouvelles fonctionnalités de l’application
- Gestion de l’application
- Revues
- Mises à niveau ou mises à jour de l’application
- Concours et tirages au sort

## Types de messages standard

Les onglets suivants montrent ce que vos utilisateurs voient s’ils ouvrent l’un de nos types de messages standard intégrés : messages In-App slideup, modaux et plein écran.

{% tabs %}
{% tab Slideup %}

Les messages slideup apparaissent généralement en haut et en bas de l’écran de l’application (vous pouvez le définir à la création du message). Ils sont parfaits pour avertir vos utilisateurs de nouvelles conditions de service, cookies et autres extraits de code d’information.

![Message In-App slideup apparaissant en bas de l’écran de l’application. Le slideup comprend une image d’icône et un bref message.]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

Les modaux apparaissent au centre de l’écran de l’appareil avec une incrustation le démarquant de votre application en arrière-plan. Ils permettent d’intéressants appels à l’action et sont parfaits pour suggérer plus ou moins subtilement à votre utilisateur de profiter d’une vente ou d’un concours.

![Message In-App modal apparaissant au centre d’une application et d’un site Web comme boîte de dialogue. Le modal comprend une image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Fullscreen %}

Comme leur nom l’indique, les messages plein écran occupent tout l’écran de l’appareil Ce type de message est idéal lorsque vous avez vraiment besoin de toute l’attention de votre utilisateur, dans le cas par exemple de mises à jour obligatoires de l’application.

![Message In-App plein écran sur un écran d’application. Le message plein écran comprend une grande image, un en-tête, un corps de message et deux boutons.]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

Outre ces modèles de messages intégrés, vous pouvez personnaliser vos envois à l’aide de messages In-App HTML personnalisés, de modaux Web avec CSS ou de formulaires de capture d’e-mail Web. Pour plus d’informations, consultez [Personnalisation][4].

## Ressources supplémentaires

Avant de commencer à créer vos propres campagnes de messages In-App ou à utiliser des messages In-App dans une campagne multicanal, nous vous recommandons vivement de consulter notre [guide de préparation des messages In-App][5]. Ce guide couvre les questions de ciblage, de contenu et de conversion que vous devez prendre en compte lors de la création de messages In-App.


[1]: https://www.braze.com/customers
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/
[6]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/