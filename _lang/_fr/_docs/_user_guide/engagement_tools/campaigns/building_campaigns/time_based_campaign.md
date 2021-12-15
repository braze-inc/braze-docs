---
nav_title: Fonctionnalités basées sur le temps pour les campagnes
article_title: Fonctionnalités basées sur le temps pour les campagnes
page_order: 2
tool: Campagnes
page_type: Référence
description: "Cet article de référence couvre les fonctionnalités basées sur le temps pour les campagnes."
---

# Fonctionnalités basées sur le temps pour les campagnes

> Cet article de référence couvre les fonctionnalités basées sur le temps pour les campagnes d'aide aux stratégies, de dépannage et de répondre à des questions courantes. Vous pouvez également consulter notre cours de LAB [Configuration de la campagne](https://lab.braze.com/campaign-setup-delivery-targeting-conversions) pour en savoir plus sur la livraison de la campagne.

## Livraison planifiée

Cette section couvre les options de planification et de livraison basées sur le temps pour les campagnes de [Livraison planifiée]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/scheduled_delivery/).

### Envoyer à une heure désignée

| Définition                                                                 | Fuseau horaire                |
| -------------------------------------------------------------------------- | ----------------------------- |
| Envoyer un message à une heure désignée, à une date précise du calendrier. | Fuseau horaire de la société. |
{: .reset-td-br-1 .reset-td-br-2}

!\[Envoyer à une heure désignée\]\[2\]

### Timing Intelligent

| Définition                                                                                                                                                                                                   | Fuseau horaire                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Temps optimal de l'utilisateur. Chaque utilisateur recevra la campagne au moment où il est le plus susceptible de s'engager. [En savoir plus]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/). | Si vous sélectionnez **une heure spécifique** comme votre [repli]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/#fallback-options), cela sera envoyé à l'heure locale de l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

!\[Intelligent Timing\]\[3\]

### Envoyer une campagne aux utilisateurs dans leur fuseau horaire local

| Définition                                                                                                                                                                                                                         | Fuseau horaire                                                                                                                               |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Vous permet de livrer des messages à un segment en fonction du fuseau horaire individuel d'un utilisateur. [En savoir plus]({{site.baseurl}}/user_guide/engagement_tools/campaigns/faq/#what-does-local-time-zone-delivery-offer). | Heure locale des utilisateurs. Si le fuseau horaire d'un utilisateur n'est pas défini, cela retombera sur le fuseau horaire de l'entreprise. |
{: .reset-td-br-1 .reset-td-br-2}

!\[Fuseau horaire local\]\[4\]

### Autoriser les utilisateurs à devenir rééligibles pour recevoir une campagne

| Définition                                                                                                                                                                                                                                                                      | Fuseau horaire |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Après qu'un utilisateur soit envoyé par cette campagne, spécifiez quand il deviendra de nouveau éligible pour recevoir la campagne. [En savoir plus]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/#campaigns). | N/A            |
{: .reset-td-br-1 .reset-td-br-2}

!\[Re-eligibility\]\[5\]

## Livraison basée sur l'action

Cette section couvre le délai de planification et les options de livraison pour les [campagnes de livraison par action-Based Delivery]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/).

### Planifier un retard

{% alert important %}
En choisissant votre longueur de retard, notez que si vous définissez un délai qui est plus long que la [durée de la campagne]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/triggered_delivery/#step-4-assign-duration), aucun utilisateur ne recevra votre campagne.
{% endalert %}

#### Envoyer la campagne immédiatement

| Définition                                                                                   | Fuseau horaire |
| -------------------------------------------------------------------------------------------- | -------------- |
| Envoyer un message immédiatement après que l'utilisateur effectue l'action de déclenchement. | N/A            |
{: .reset-td-br-1 .reset-td-br-2}

!\[Envoyer immédiatement\]\[6\]

#### Envoyer une campagne après X jours

| Définition                                                                                                         | Fuseau horaire |
| ------------------------------------------------------------------------------------------------------------------ | -------------- |
| Envoyer un message après un délai. Vous pouvez spécifier un délai en secondes, minutes, heures, jours ou semaines. | N/A            |
{: .reset-td-br-1 .reset-td-br-2}

!\[Envoyer après X jours\]\[7\]

#### Envoyer une campagne le [jour de la semaine] suivant en X

| Définition                                                                            | Fuseau horaire                                                                  |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Envoyer un message le jour suivant spécifié de la semaine, à une heure de la journée. | Sélectionnez entre **heure locale de l'utilisateur** ou **heure de la société** |
{: .reset-td-br-1 .reset-td-br-2}

!\[Envoyer le lendemain (jour) à X heure\]\[8\]

Par exemple, supposons que vous sélectionnez "Envoyer le samedi suivant à 15h15". Si un utilisateur effectue l'événement de déclenchement un samedi, il recevra ce message le samedi suivant dans 7 jours. S'ils y entrent un vendredi, le samedi suivant serait dans 1 jour.

#### Envoyer en X jours du calendrier à l'heure Y

| Définition                                                               | Fuseau horaire                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Envoyer un message dans un nombre de jours spécifique à un moment donné. | Sélectionnez entre **heure locale de l'utilisateur** ou **heure de la société** |
{: .reset-td-br-1 .reset-td-br-2}

!\[Envoyer en X jours à l'heure Y\]\[9\]

Braze calcule le délai comme `jour de la semaine` + `jours du calendrier`, puis ajoute le `temps`. Par exemple, supposons que l'utilisateur exécute l'événement de déclenchement le lundi à 21h, et le délai de programmation est réglé sur "Envoyer la campagne dans 1 jour à 9h". Ce message sera envoyé mardi à 9h, parce que Braze calcule le délai comme `lundi` + `1 jour du calendrier`, puis ajoute le `9am`.

### Heures silencieuses

| Définition                                                                                                                                                                                                                                                           | Fuseau horaire                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Empêcher l'envoi de messages pendant les heures spécifiées. Si un message se déclenche pendant les heures silencieuses, vous pouvez choisir entre abandonner le message ou l'envoyer à l'heure disponible suivante (i.e. Envoyer à la fin de vos heures de silence). | Heure locale de l'utilisateur. Si le fuseau horaire d'un utilisateur n'est pas défini, cela retombera sur le fuseau horaire de l'entreprise. |
{: .reset-td-br-1 .reset-td-br-2}

!\[Heures silencieures\]\[10\]

### Autoriser les utilisateurs à être rééligibles pour recevoir une campagne

| Définition                                                                                                                                                                                                                                                                      | Fuseau horaire |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Après qu'un utilisateur soit envoyé par cette campagne, spécifiez quand il deviendra de nouveau éligible pour recevoir la campagne. [En savoir plus]({{site.baseurl}}/user_guide/engagement_tools/campaigns/scheduling_and_organizing/delivery_types/reeligibility/#campaigns). | N/A            |
{: .reset-td-br-1 .reset-td-br-2}

!\[Re-eligibility\]\[5\]

### Plafond global de fréquence

| Définition                                                                                                                                                                                                                                                                                                     | Fuseau horaire                                                                                                                               |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Limiter le nombre de fois que chaque utilisateur doit recevoir la campagne dans un certain laps de temps, qui peuvent être mesurées en minutes, jours, semaines (7 jours) et mois. [En savoir plus]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping). | Heure locale de l'utilisateur. Si le fuseau horaire d'un utilisateur n'est pas défini, cela retombera sur le fuseau horaire de l'entreprise. |
{: .reset-td-br-1 .reset-td-br-2}

Le plafonnement de fréquence est basé sur les jours de calendrier, et non sur une période de 24 heures. Cela signifie que vous pouvez mettre en place une règle de plafonnement de fréquence d'envoi pas plus d'une campagne par jour, mais si un utilisateur reçoit un message à 23h dans son heure locale, ils peuvent toujours recevoir un autre message une heure plus tard (à minuit le jour suivant du calendrier).

## Date limite de conversion

| Définition                                                                                                                                                                                                                                                                | Fuseau horaire |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Le temps maximum qui peut passer entre un utilisateur recevant une campagne et effectuant l'action assignée pour qu'il soit considéré comme une conversion. [En savoir plus]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/conversion_events/). | N/A            |
{: .reset-td-br-1 .reset-td-br-2}
[2]: {% image_buster /assets/img_archive/time_designated.png %} [3]: {% image_buster /assets/img_archive/time_intelligent_timing.png %} [4]: {% image_buster /assets/img_archive/time_local. ng %} [5]: {% image_buster /assets/img_archive/time_reeligibility.png %} [6]: {% image_buster /assets/img_archive/time_delay_immediately. ng %} [7]: {% image_buster /assets/img_archive/time_delay_after.png %} [8]: {% image_buster /assets/img_archive/time_delay_on_the_next. ng %} [9]: {% image_buster /assets/img_archive/time_delay_in.png %} [10]: {% image_buster /assets/img_archive/time_quiet_hours.png %}
