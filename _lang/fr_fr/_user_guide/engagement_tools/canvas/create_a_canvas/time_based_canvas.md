---
nav_title: Fonctionnalités basées sur le temps
article_title: Fonctionnalités basées sur le temps pour Canvas
page_order: 1
tools: Canvas
page_type: reference
description: "Cet article de référence aborde les définitions, les fuseaux horaires et des exemples de fonctionnalités basées sur le temps pour Canvas."

---

# Fonctionnalités basées sur le temps pour Canvas

> Cet article de référence aborde les fonctionnalités basées sur le temps pour Canvas, pour proposer des stratégies, des résolutions de problèmes et répondre aux questions courantes. 

## Planifier un délai

{% alert important %}
Depuis le 28 février 2023, vous ne pouvez plus créer ou dupliquer de Canvas à l’aide de l’éditeur Canvas d’origine. Cette section est disponible à titre de référence lors de la modification de la planification d’un Canvas existant créé à l’aide du flux de travail Canvas d’origine. Pour les fonctionnalités basées sur le temps du flux de travail Canvas Flow, consultez le [composant Délai]({{site.baseurl}}/user_guide/engagement_tools/canvas/canvas_components/delay_step/).
{% endalert %}

### Envoyer immédiatement

| Définition |  Fuseau horaire |
| --- | --- |
| Envoyer un message dès que l’utilisateur reçoit l’étape précédente ou s’il s’agit de la première étape, dès que l’utilisateur accède à Canvas. | S.O. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][1]

### Envoyer après X jours

| Définition |  Fuseau horaire |
| --- | --- |
| Envoyer un message après un délai Vous pouvez indiquer un délai en secondes, minutes, heures, jours ou semaines.  | S.O. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][2]

### Envoyer le prochain [jour de la semaine] à l'heure X

| Définition |  Fuseau horaire |
| --- | --- |
| Envoyer un message le jour suivant indiqué de la semaine, à une heure sélectionnée de la journée.  | Sélectionnez l' **heure locale de l'utilisateur** ou l' **heure de l'entreprise**. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

Par exemple, supposons que vous sélectionniez « Envoyer samedi prochain à 15 h 15 ». Si un utilisateur accède à Canvas un samedi, il recevrait ce message le samedi suivant, dans sept jours. S’il y accède un vendredi, le samedi suivant serait dans un jour.

![][3]

### Envoyer dans X jours civils à Y heure

| Définition |  Fuseau horaire |
| --- | --- |
| Envoyer le message dans un nombre spécifique de jours, à une heure indiquée. | Sélectionnez l' **heure locale de l'utilisateur** ou l' **heure de l'entreprise**. |

Canvas calcule le délai comme suit : `day of the week` + `calendar days`, puis ajoute le`time`. Par exemple, supposons qu’un composant Canvas soit envoyé lundi à 21 h et que l’étape suivante soit programmée sur « Envoyer dans 1 jour à 9 h ». Ce message sera livré le mardi à 9 h, car le Canvas calcule le délai comme suit : `Monday` + `1 calendar day`, puis ajoute `9 am`.

![][4]

### Timing intelligent

| Définition | Fuseau horaire |
| ---------- | ----- |
| Le [timing intelligent]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/) calcule l'heure d'envoi optimale sur la base d'une analyse statistique des interactions passées de votre utilisateur avec votre message (par canal) et votre appli. | Si vous choisissez **une heure spécifique** comme [solution de repli]({{site.baseurl}}/user_guide/brazeai/intelligence/intelligent_timing/#fallback-options), celle-ci sera envoyée à l'heure locale de l'utilisateur. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

![][5]

## Limite de fréquence globale

| Définition | Fuseau horaire |
| --- | --- |
| Limiter le nombre de fois que chaque utilisateur doit recevoir le Canvas dans un certain délai, qui peut être mesuré en minutes, jours, semaines (sept jours) et mois. | Heure locale de l’utilisateur. Si le fuseau horaire de l’utilisateur n’est pas défini, le fuseau horaire de la société servira de base. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

La [limite de fréquence]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/rate-limiting/#frequency-capping) est basée sur des jours calendaires, et non sur une période de 24 heures. En d’autres termes, vous pourriez configurer une règle de limite de fréquence d’envoi, de pas plus d’une campagne par jour, mais si un utilisateur reçoit un message à 23 h dans son fuseau horaire, il peut toujours recevoir un autre message une heure plus tard (à minuit le jour civil suivant).

![][6]

{% alert note %}
Si vous disposez des [autorisations]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#managing-limited-and-team-role-permissions) nécessaires pour approuver les canevas, vous verrez apparaître une [étape de**résumé**]({{site.baseurl}}/user_guide/engagement_tools/canvas/managing_canvases/canvas_approval/#using-approvals) dans le flux de travail.
{% endalert %}


[1]: {% image_buster /assets/img_archive/schedule_delay_immediately.png %}
[2]: {% image_buster /assets/img_archive/schedule_delay_after.png %}
[3]: {% image_buster /assets/img_archive/schedule_delay_next.png %}
[4]: {% image_buster /assets/img_archive/schedule_delay_in.png %}
[5]: {% image_buster /assets/img_archive/schedule_delay_intelligent.png %}
[6]: {% image_buster /assets/img_archive/schedule_frequency_capping.png %}
