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

![Chat de messages iOS qui affiche des messages d'opt-out sortants en réponse à l'opt-out flou entrant "Please stopppppp".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Les utilisateurs qui envoient des SMS, MMS et RCS avec Braze doivent respecter les lois, réglementations et normes industrielles applicables qui sont définies. Concernant un désabonnement, la loi demande que, lorsqu’un utilisateur envoie le message « STOP », alors tous les messages liés à ce programme d’envoi de messages s’arrêteront. Braze traite ces messages automatiquement et désinscrit l’utilisateur.<br><br>Le désabonnement vague tente de déterminer lorsqu’un message entrant ne correspond pas à un [mot-clé de désabonnement]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), mais en indique l’intention. Si l'option fuzzy opt-out est activée et qu'une réponse par mot-clé entrant est jugée "floue", Braze répondra automatiquement par un message de réponse qui demandera aux utilisateurs de se désabonner.

Actuellement, seuls les mots-clés de désabonnement créés en utilisant l'anglais comme [langue locale]({{site.baseurl}}/user_guide/message_building_by_channel/sms/keywords/keyword_handling/#multi-language-support) sont pris en charge.

## Qu’est-ce qui est considéré comme vague ?

Les critères permettant de considérer une réponse entrante comme étant « vague » sont les suivants :
- Si inverser une lettre avec la lettre immédiatement à droite ou à gauche sur un clavier QWERTY entraîne un mot-clé de désabonnement correspondant.
- Une sous-chaîne de caractères dans le message correspond au mot-clé de désabonnement.

Par exemple, « Stpo » ou « Please stopppp » seront considérés comme vague et une réponse de désabonnement vague sera envoyée. Si l'utilisateur répond ensuite par un mot-clé d'abonnement, un événement de désabonnement se déclenche.

## Paramétrer le désabonnement vague

Pour configurer le désabonnement vague, rendez-vous sur la page de gestion de mots-clés de groupe d’abonnement.

1. Allez dans **Audience** > **Gestion des abonnements** et sélectionnez un groupe d'abonnement **SMS/MMS/RCS**.
2. Dans les **mots-clés globaux**, recherchez la catégorie d'**abonnement** et sélectionnez l'icône en forme de crayon.
3. Activez le **désabonnement vague** en activant la bascule.
4. Modifiez la réponse du désabonnement vague comme vous le désirez. 

![Section permettant de modifier les mots-clés d'abonnement.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Meilleures pratiques pour les messages d'abandon flous

Pour garantir une expérience claire, conforme et positive à vos abonnés, il est essentiel de configurer votre message d'envoi de messages d'abonnement flous de manière réfléchie. L'objectif principal du message d'abonnement flou est de **guider les utilisateurs qui envoient un message similaire, mais pas exactement, à votre mot-clé d'abonnement désigné.** Le message indique aux utilisateurs comment se désinscrire avec succès.

### Considérations critiques

{% alert warning %}
**NE** configurez **PAS** votre message d'abonnement flou pour confirmer un désabonnement. Votre message d'envoi de messages de désabonnement flous ne doit pas contenir de termes laissant entendre que l'utilisateur s'est déjà désabonné avec succès. Par exemple, **n'** utilisez **pas** "Vous avez été désabonné", "Vous ne recevrez plus de messages de ce numéro" ou "Vous êtes maintenant désabonné".
{% endalert %}

Le message d'abandon flou est envoyé avant que l'utilisateur n'ait exercé son droit d'abandon. L'utilisation d'un langage de confirmation induit l'abonné en erreur en lui faisant croire qu'il s'est désabonné alors que ce n'est pas le cas, ce qui entraîne la persistance de messages non désirés, la frustration de l'abonné et des risques importants en matière de conformité.

{% alert warning %}
**NE** configurez **PAS** votre message d'exclusion flou de manière à ce qu'il soit identique ou similaire à votre mot-clé d'exclusion exact.
{% endalert %}

Si votre message flou est identique ou trop proche de votre mot-clé exact de désabonnement (par exemple, si "STOP" est votre mot-clé exact et que votre message flou est "Envoyez STOP pour vous désabonner"), cela peut créer une confusion quant à savoir si le message initial de l'utilisateur a réellement abouti à un désabonnement ou s'il doit entreprendre une autre action. Le message flou doit toujours préciser l'action que l'utilisateur doit entreprendre.

### Exemples d'envois de messages d'abonnement flous

Se concentrer sur l'orientation des utilisateurs. Par exemple, si votre mot-clé d'abonnement est "STOP", voici de bons et de mauvais exemples d'envois de messages d'abonnement flous que vous pourriez créer :

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemples <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Mauvais exemples <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Pour vous désabonner de tous les messages, veuillez répondre en indiquant le mot STOP."</td>
      <td>"Vous avez été désabonné avec succès. Vous ne recevrez plus aucun message de ce numéro. Répondez à START pour vous réabonner" (il s'agit d'une confirmation directe du désabonnement, ce qui est trompeur dans un scénario d'abonnement flou).</td>
    </tr>
    <tr>
      <td>"Nous avons reçu votre message. Si vous souhaitez ne plus recevoir de textos, envoyez STOP".</td>
      <td>"STOP" (il s'agit simplement du mot-clé exact, qui ne guide pas l'utilisateur).</td>
    </tr>
    <tr>
      <td>"Vouliez-vous vous désinscrire ? Répondez STOP pour vous abonner à tous les messages futurs."</td>
      <td>"(Si "STOP" est également votre mot-clé exact, ce message est redondant et ne clarifie pas l'action si le message initial était flou).</td>
    </tr>
  </tbody>
</table>
