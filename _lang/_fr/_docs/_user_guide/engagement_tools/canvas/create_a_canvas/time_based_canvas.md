---
nav_title: Fonctionnalités basées sur le temps pour Canvas
article_title: Fonctionnalités basées sur le temps pour Canvas
page_order: 1
tools: Toile
page_type: Référence
description: "Cet article de référence couvre les définitions, les fuseaux horaires et les exemples de fonctionnalités basées sur le temps pour Canvas."
---

# Fonctionnalités basées sur le temps pour Canvas

> Cet article de référence couvre les fonctionnalités basées sur le temps pour Canvas pour aider les stratégies, le dépannage et répondre aux questions courantes.

## Planifier un retard

### Envoyer immédiatement

| Définition                                                                                                                                                                               | Fuseau horaire |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------- |
| Envoyer un message immédiatement après que l'utilisateur ait reçu l'étape précédente, ou s'il s'agit de la première étape, immédiatement après l'entrée de l'utilisateur dans le Canvas. | N/A            |
{: .reset-td-br-1 .reset-td-br-2}

!\[Envoyer immédiatement\]\[1\]

### Envoyer après X jours

| Définition                                                                                                         | Fuseau horaire |
| ------------------------------------------------------------------------------------------------------------------ | -------------- |
| Envoyer un message après un délai. Vous pouvez spécifier un délai en secondes, minutes, heures, jours ou semaines. | N/A            |
{: .reset-td-br-1 .reset-td-br-2}

!\[Envoyer après X jours\]\[2\]

### Envoyer le [jour de la semaine] suivant à X heure

| Définition                                                                            | Fuseau horaire                                                                  |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| Envoyer un message le jour suivant spécifié de la semaine, à une heure de la journée. | Sélectionnez entre **heure locale de l'utilisateur** ou **heure de la société** |
{: .reset-td-br-1 .reset-td-br-2}

Par exemple, supposons que vous sélectionnez "Envoyer le samedi suivant à 15h15". Si un utilisateur entre sur Canvas un samedi, il recevra ce message le samedi suivant dans 7 jours. S'ils y entrent un vendredi, le samedi suivant serait dans 1 jour.

!\[Envoyer le prochain \]\[3\]

### Envoyer en X jours du calendrier à l'heure Y

| Définition                                                               | Fuseau horaire                                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| Envoyer un message dans un nombre de jours spécifique à un moment donné. | Sélectionnez entre **heure locale de l'utilisateur** ou **heure de la société** |

Canvas calcule le délai comme `jour de la semaine` + `jours du calendrier`, puis ajoute le `temps`. Par exemple, supposons qu'une étape de Canvas soit envoyée le lundi à 21h, et que l'étape suivante soit programmée pour « Envoyer dans 1 jour à 9h ». Ce message sera envoyé mardi à 9h, parce que Canvas calcule le délai comme `lundi` + `1 jour de calendrier`, puis ajoute le `9am`.

!\[Envoyer en X jours\]\[4\]

### Timing Intelligent

| Définition                                                                                                                                                                                                                                                             | Fuseau horaire                                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Braze calcule le temps d'envoi optimal basé sur une analyse statistique des interactions passées de votre utilisateur avec votre messagerie (sur une base par canal) et l'application. [En savoir plus]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/). | Si vous sélectionnez **une heure spécifique** comme votre [repli]({{site.baseurl}}/user_guide/intelligence/intelligent_timing/#fallback-options), cela sera envoyé à l'heure locale de l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2}

!\[Timing intelligent\]\[5\]

## Plafond global de fréquence

| Définition                                                                                                                                                                                                                                                                                                  | Fuseau horaire                                                                                                                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Limite le nombre de fois que chaque utilisateur doit recevoir le Canvas dans un certain laps de temps, qui peuvent être mesurées en minutes, jours, semaines (7 jours) et mois. [En savoir plus]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping). | Heure locale de l'utilisateur. Si le fuseau horaire d'un utilisateur n'est pas défini, cela retombera sur le fuseau horaire de l'entreprise. |
{: .reset-td-br-1 .reset-td-br-2}

Le plafonnement de fréquence est basé sur les jours de calendrier, et non sur une période de 24 heures. Cela signifie que vous pouvez mettre en place une règle de plafonnement de fréquence d'envoi pas plus d'une campagne par jour, mais si un utilisateur reçoit un message à 23h dans son heure locale, ils peuvent toujours recevoir un autre message une heure plus tard (à minuit le jour suivant du calendrier).

!\[Cappage Fréquence\]\[6\]
[1]: {% image_buster /assets/img_archive/schedule_delay_immediately.png %} [2]: {% image_buster /assets/img_archive/schedule_delay_after.png %} [3]: {% image_buster /assets/img_archive/schedule_delay_next. ng %} [4]: {% image_buster /assets/img_archive/schedule_delay_in.png %} [5]: {% image_buster /assets/img_archive/schedule_delay_intelligent. ng %} [6]: {% image_buster /assets/img_archive/schedule_frequency_capping.png %}
