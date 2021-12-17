---
nav_title: "À propos des messages In-App"
article_title: À propos des messages In-App
page_order: 0
page_type: reference
description: "Cet article de référence donne un bref aperçu des messages dans l'application."
channel:
  - messages intégrés à l'application
---

# À propos des messages dans l'application

> Cet article fournit un aperçu des messages dans l'application, y compris les types de messages disponibles et certains cas d'utilisation potentiels. En plus du contenu couvert ici, nous vous recommandons également de consulter notre cours LAB [Messages In-App et In-Browser](https://lab.braze.com/messaging-channels-in-app-in-browser).

Les messages intégrés sont bons pour beaucoup de choses. Ils sont riches en contenu et ont un sens faible de l'urgence, car ces messages ne sont pas distribués en dehors de l'application de l'utilisateur et ne s'immiscent pas sur son écran d'accueil. Les messages dans l'application existent dans votre application (d'où le nom), viennent avec contexte et ne sont presque jamais indésirables ! Ils sont toujours livrés lorsque l'utilisateur est actif dans votre application.

Pour voir des exemples de messages dans l'application, consultez notre [Études de cas][1].

## Cas d'utilisation potentiels

Avec le niveau de contenu riche offert par les messages dans l'application, vous pouvez tirer parti de ce canal pour une variété de cas d'utilisation :

| Cas d'utilisation                         | Explication                                                                                                                                                                                                                                                                                                                                 |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amorçage du Push                          | Lancez une campagne [d'amorçage de][2] à l'aide d'un message riche dans l'application pour montrer à vos clients l'avantage de choisir de pousser pour votre application ou votre site, et les présenter avec une prompte à accorder la permission push.                                                                                    |
| Ventes et promotions                      | Utilisez des messages modaux dans l'application pour accueillir les clients avec des médias visuellement attrayants contenant des [codes promotionnels][6] ou des offres. Les inciter à faire des achats ou des conversions alors qu'ils ne l'auraient pas autrement.                                                                       |
| Favoriser l'adoption de la fonctionnalité | Encouragez les clients à utiliser d'autres parties de votre application ou à profiter d'un service.                                                                                                                                                                                                                                         |
| Campagnes hautement personnalisées        | Placez des messages dans l'application comme première chose que vos clients voient lorsqu'ils entrent dans votre application ou votre site. Ajoutez certaines fonctionnalités de personnalisation de Braze, telles que [Contenu connecté][3], pour obliger les utilisateurs à prendre des mesures et donc rendre votre accès plus efficace. |
{: .reset-td-br-1 .reset-td-br-2}

Les autres cas d'utilisation à considérer incluent les éléments suivants :

- Nouvelles fonctionnalités de l'application
- Gestion des applications
- Revues
- Mises à jour ou mises à jour de l'application
- Cadeaux et loteries

## Types de messages standard

Les onglets suivants montrent à quoi ressemblent vos utilisateurs pour ouvrir un de nos types de messages intégrés - glissement, modal et plein écran dans l'application.

{% tabs %}
{% tab Slideup %}

Les diapositives apparaissent généralement en haut et en bas de l'écran de l'application (vous pouvez le définir lorsque vous créez votre message). Ils sont parfaits pour avertir vos utilisateurs des nouvelles conditions de service, des cookies et d'autres extraits d'informations.

![Comportement de glissement]({% image_buster /assets/img/slideup-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Modal %}

Les modales apparaissent au centre de l'écran de l'appareil avec une superposition d'écran qui l'aide à se démarquer de votre application en arrière-plan. Ce sont des appels à action géniaux. Ils sont parfaits pour suggérer à votre utilisateur de profiter d'une vente ou d'un don.

![Comportement modal]({% image_buster /assets/img/modal-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% tab Full-Screen %}

Les messages en plein écran sont exactement ce à quoi vous vous attendiez — ils prennent tout l’écran de l’appareil ! Ce type de message est parfait lorsque vous avez vraiment besoin de l'attention de votre utilisateur, comme pour les mises à jour obligatoires de l'application.

![Comportement plein écran]({% image_buster /assets/img/full-screen-behavior.gif %}){: style="border:0px;"}

<br>

{% endtab %}
{% endtabs %}

En plus de ces modèles de messages hors de la boîte, vous pouvez également personnaliser votre messagerie en utilisant des messages HTML personnalisés dans l'application, des modes web avec CSS ou des formulaires de capture de courriels Web. Pour plus d'informations, reportez-vous à [Personnalisation][4].

## Plus de ressources

Avant de commencer à créer vos propres campagnes de messages dans l'application—ou à utiliser des messages dans l'application dans une campagne multi-canal—nous vous recommandons fortement de consulter notre [guide de préparation des messages dans l'application][5]. Ce guide couvre les questions de ciblage, de contenu et de conversion que vous devriez considérer lors de la création de messages dans l'application.


[1]: https://www.braze.com/customers
[2]: {{site.baseurl}}/user_guide/message_building_by_channel/push/best_practices/creating_custom_opt-in_prompts/
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/
[4]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/customize/
[5]: {{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/best_practices/prep_guide/
[6]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/promotion_codes/