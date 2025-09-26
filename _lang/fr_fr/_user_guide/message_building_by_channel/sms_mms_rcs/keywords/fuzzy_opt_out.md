---
nav_title: Désabonnement vague
article_title: Désabonnement vague
description: "Cet article de référence explique comment configurer le fuzzy opt-out, un paramètre qui tente de reconnaître lorsqu'un message entrant ne correspond pas à un mot-clé d'opt-out."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 1

---

# Désabonnement vague

![Chat iOS qui affiche des messages d'exclusion sortants en réponse à l'exclusion floue entrante "Please stoppppp".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Les utilisateurs qui envoient des SMS, MMS et RCS avec Braze doivent respecter les lois, réglementations et normes industrielles applicables qui sont définies. Concernant un désabonnement, la loi demande que, lorsqu’un utilisateur envoie le message « STOP », alors tous les messages liés à ce programme d’envoi de messages s’arrêteront. Braze traite ces messages automatiquement et désinscrit l’utilisateur.<br><br>Le désabonnement vague tente de déterminer lorsqu’un message entrant ne correspond pas à un [mot-clé de désabonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), mais en indique l’intention. Si l'option fuzzy opt-out est activée et qu'une réponse par mot-clé entrant est jugée "floue", Braze répondra automatiquement par un message de réponse qui demandera aux utilisateurs de se désabonner.

Actuellement, seuls les mots-clés de désabonnement créés en utilisant l'anglais comme [langue locale]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support) sont pris en charge.

## Qu’est-ce qui est considéré comme vague ?

Les critères permettant de considérer une réponse entrante comme étant « vague » sont les suivants :
- Si inverser une lettre avec la lettre immédiatement à droite ou à gauche sur un clavier QWERTY entraîne un mot-clé de désabonnement correspondant.
- Une sous-chaîne de caractères dans le message correspond au mot-clé de désabonnement.

Par exemple, « Stpo » ou « Please stopppp » seront considérés comme vague et une réponse de désabonnement vague sera envoyée. Si l'utilisateur répond ensuite par un mot-clé d'abonnement, un événement de désabonnement se déclenche.

## Paramétrer le désabonnement vague

Pour configurer le désabonnement vague, rendez-vous sur la page de gestion de mots-clés de groupe d’abonnement.

1. Allez dans **Audience** > **Abonnements** et sélectionnez un groupe d'abonnement **SMS/MMS/RCS**.

{:start="2"}
2\. Dans les **mots-clés globaux**, recherchez la catégorie d'**abonnement** et sélectionnez l'icône en forme de crayon.
3\. Activez le **désabonnement vague** en activant la bascule.
4\. Modifiez la réponse du désabonnement vague comme vous le désirez. 

![]({% image_buster /assets/img/sms/fuzzy2.png %}){: style="max-width:70%;"}


