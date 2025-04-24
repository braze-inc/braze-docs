---
nav_title: Fonctionnalités basées sur le temps pour les campagnes
article_title: Fonctionnalités basées sur le temps pour les campagnes
page_order: 2
tool: Campaigns
page_type: reference
description: "Cet article de référence couvre les fonctionnalités basées sur le temps pour les campagnes telles que la livraison programmée, le timing intelligent et la livraison basée sur l'action."

---
# Fonctionnalités basées sur le temps pour les campagnes

> Lorsque vous utilisez des campagnes, vous pouvez vous servir des options de planification basées sur le temps pour atteindre votre audience. Ces fonctionnalités basées sur le temps incluent des campagnes programmées pour une livraison planifiée et une livraison basée sur l'action.

{% alert tip %}
Pour en savoir plus sur la réception/distribution des campagnes, consultez notre cours d'apprentissage Braze dédié à la [configuration des campagnes](https://learning.braze.com/campaign-setup-delivery-targeting-conversions).
{% endalert %}

## Livraison planifiée

Cette section couvre les options de planification et de livraison basées sur le temps pour les campagnes de [livraison programmée]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/scheduled_delivery/).

### Envoyer à un moment spécifié

| Définition | Fuseau horaire |
| ---------- | --------- |
| Envoie le message à un moment donné, à une date calendaire spécifique. | Fuseau horaire de la société. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Une campagne avec l’option « Envoyer à un moment spécifié » de sélectionnée pour envoyer une fois à partir de 9 h le 13 juillet 2021.][2]

### Timing intelligent

| Définition | Fuseau horaire |
| ---------- | --------- |
| Heure optimale de l’utilisateur. Chaque utilisateur recevra la campagne au moment où il est le plus susceptible de s’engager. Pour en savoir plus, consultez l’article sur [Intelligent Timing]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/). | Si vous sélectionnez une heure spécifique comme votre [solution de repli]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options), celle-ci sera envoyée à l'heure locale de l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Une campagne avec l’option « Timing intelligent » sélectionnée pour envoyer une fois à l’heure optimale le 13 juillet 2021 avec une heure de secours personnalisée réglée à 9 h pour les utilisateurs n’ayant pas suffisamment de données dans leurs profils pour calculer un moment optimal.][3]

### Envoyer une campagne aux utilisateurs dans leur fuseau horaire local

| Définition | Fuseau horaire |
| ---------- | --------- |
| Vous permet de livrer des messages à un segment en fonction du fuseau horaire [individuel de l'utilisateur]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#when-does-braze-evaluate-users-for-local-time-zone-delivery). | Heure locale de l’utilisateur. Si le fuseau horaire de l’utilisateur n’est pas défini, le fuseau horaire de la société servira de base. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Une campagne avec l’option « Envoyer à un moment spécifié » sélectionnée pour envoyer une fois à partir de 9 h le 13 juillet 2021 avec la case « Envoyer la campagne aux utilisateurs dans leur fuseau horaire local » de cochée.][4]

### Autoriser les utilisateurs à devenir rééligibles pour recevoir la campagne

| Définition | Fuseau horaire |
| ---------- | --------- |
| Une fois qu’un utilisateur a reçu un message de cette campagne, précisez quand il sera rééligible pour recevoir de nouveau la campagne. [En savoir plus.]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/) | S.O. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Une campagne avec la case « Autoriser les utilisateurs à devenir rééligibles pour recevoir la campagne » après une semaine de cochée.][5]

## Livraison par événement

Cette section couvre le retard de planification et les options de livraison pour les campagnes de [livraison basée sur l'action]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/).

### Planifier un délai

{% alert important %}
Lorsque vous choisissez la durée de votre délai, gardez à l'esprit que si vous définissez un délai supérieur à la [durée de la campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/#step-4-assign-duration), vos utilisateurs ne recevront pas votre campagne.
{% endalert %}

#### Envoyer immédiatement la campagne

| Définition | Fuseau horaire |
| ---------- | --------- |
| Envoyer le message immédiatement après que l’utilisateur a effectué l’action de déclenchement. | S.O. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Délai de planification défini pour envoyer la campagne immédiatement une fois que l’événement déclencheur a lieu.][6]

#### Envoyer une campagne après X jours

| Définition | Fuseau horaire |
| ---------- | --------- |
| Envoyer un message après un délai Vous pouvez indiquer un délai en secondes, minutes, heures, jours ou semaines. Pour les [campagnes d'envoi de messages in-app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/about), vous pouvez définir un délai allant jusqu'à deux heures seulement. | N/A |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Délai de planification défini pour envoyer la campagne un jour après l'événement déclencheur.][7]

#### Envoyer la campagne le prochain [jour de la semaine] à X heure

| Définition | Fuseau horaire |
| ---------- | --------- |
| Envoyer un message le jour suivant indiqué de la semaine, à une heure sélectionnée de la journée. | Sélectionnez l' **heure locale de l'utilisateur** ou l' **heure de l'entreprise**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Par exemple, supposons que vous sélectionniez « Envoyer samedi prochain à 15 h 15 ». Si un utilisateur effectue l’action de déclanchement un samedi, il recevrait ce message le samedi suivant, dans sept jours. S’il y accède un vendredi, le samedi suivant serait dans un jour.

![][8]

#### Envoyer dans X jours civils à Y heure

| Définition | Fuseau horaire |
| ---------- | --------- |
| Envoyer le message dans un nombre spécifique de jours, à une heure indiquée. | Sélectionnez entre **l'heure locale de l'utilisateur** ou **l'heure de l'entreprise** |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Braze calcule le délai comme suit : `day of the week` + `calendar days`, puis ajoute le `time`. Par exemple, imaginons que l’utilisateur effectue l’événement déclencheur le lundi à 21 h et que le délai planifié est défini sur « Envoyer la campagne dans 1 jour à 9 h ». Ce message sera livré le mardi à 9 h, car Braze calcule le délai comme suit : `Monday` + `1 calendar day`, puis ajoute `9 am`.

![][9]

### Heures calmes

| Définition | Fuseau horaire |
| ---------- | --------- |
| Empêche les messages d’être envoyés pendant les heures spécifiées. Si un message se déclenche pendant les heures de silence, vous pouvez choisir entre annuler le message ou l'envoyer au prochain moment disponible (comme l'envoyer à la fin de vos heures de silence). | Heure locale de l’utilisateur. Si le fuseau horaire de l’utilisateur n’est pas défini, le fuseau horaire de la société servira de base. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Une campagne avec des heures calmes activées. Dans cet exemple, les messages ne seront pas envoyés entre minuit et 8 h dans l’heure locale de l’utilisateur. Si un message se déclenche pendant les heures calmes, le message sera envoyé au prochain moment disponible.][10]

### Autoriser les utilisateurs à être rééligibles pour recevoir la campagne

| Définition | Fuseau horaire |
| ---------- | --------- |
| Après qu'un utilisateur a été contacté par cette campagne, spécifiez quand il deviendra [à nouveau éligible]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/reeligibility/#campaigns) pour recevoir la campagne à nouveau. | S.O. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![Une campagne avec la case « Autoriser les utilisateurs à devenir rééligibles pour recevoir la campagne » après une semaine de cochée.][5]

### Limite de fréquence globale

| Définition | Fuseau horaire |
| ---------- | --------- |
| Limiter le nombre de fois que chaque utilisateur doit recevoir la campagne dans un certain délai, qui peut être mesuré en minutes, jours, semaines (sept jours) et mois. Pour plus d'informations, consultez l’article sur la [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping). | Heure locale de l’utilisateur. Si le fuseau horaire de l’utilisateur n’est pas défini, le fuseau horaire de la société servira de base. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Par défaut, la limite de fréquence est désactivée pour les nouveaux Canvas. La limite de fréquence est appliquée au niveau de l’étape, pas à la base du Canvas.

La Limite de fréquence est basée sur des jours civils, non pas sur une période de 24h. En d’autres termes, vous pourriez configurer une règle de limite de fréquence d’envoi, de pas plus d’une campagne par jour, mais si un utilisateur reçoit un message à 23 h dans son fuseau horaire, il peut toujours recevoir un autre message une heure plus tard (à minuit le jour civil suivant). 

## Date limite de conversion

| Définition | Fuseau horaire |
| ---------- | --------- |
| Durée maximale pouvant s’écouler entre la réception de la campagne par l’utilisateur et le moment où il effectue l’action assignée pour qu’elle soit considérée comme une conversion. Pour plus d'informations, consultez l’article sur les [événements de conversion]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/conversion_events/). | S.O. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }



[2]: {% image_buster /assets/img_archive/time_designated.png %}
[3]: {% image_buster /assets/img_archive/time_intelligent_timing.png %}
[4]: {% image_buster /assets/img_archive/time_local.png %}
[5]: {% image_buster /assets/img_archive/time_reeligibility.png %}
[6]: {% image_buster /assets/img_archive/time_delay_immediately.png %}
[7]: {% image_buster /assets/img_archive/time_delay_after.png %}
[8]: {% image_buster /assets/img_archive/time_delay_on_the_next.png %}
[9]: {% image_buster /assets/img_archive/time_delay_in.png %}
[10]: {% image_buster /assets/img_archive/time_quiet_hours.png %}
