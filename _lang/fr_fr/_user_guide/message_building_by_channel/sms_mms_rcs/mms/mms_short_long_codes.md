---
nav_title: "Codes courts et longs des MMS"
article_title: Codes courts et longs des MMS
page_order: 1
description: "Cet article de référence présente les différences entre les codes courts et les codes longs des SMS et des MMS."
page_type: reference
alias: /mms_short_long_codes/
channel:
  - MMS
  
---

# Codes courts et longs des MMS

> Les MMS et les SMS sont tous deux liés au canal SMS de Braze. L'accès aux MMS sur votre compte nécessite l'achat de SMS pour ceux qui n'ont pas encore acheté l'accès. Les clients actuels du service SMS peuvent accéder au MMS après l'avoir acheté. 

Les MMS sont actuellement pris en charge pour les codes courts américains (numéros à 5-6 chiffres), les codes longs américains et canadiens (numéros à 10 chiffres) et les numéros de clients américains et canadiens. L'envoi de MMS à des numéros situés en dehors des États-Unis et du Canada est possible, mais les messages MMS seront convertis en messages SMS avec un lien vers la ressource. Pour en savoir plus, consultez les [codes courts et longs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Codes courts MMS

Il se peut que certains utilisateurs ne mettent pas en œuvre ou n'utilisent pas les codes courts MMS, mais ils seront disponibles si le besoin s'en fait sentir ultérieurement.

Pour les utilisateurs qui ont obtenu leur code court avant que Braze ne prenne en charge les MMS, tous les clients existants disposant d'un code court américain peuvent activer instantanément les MMS. Contactez votre gestionnaire satisfaction client si cette situation s'applique à vous et si vous souhaitez que les MMS soient activés.

{% alert important %}
Lorsque vous activez les MMS pour des codes courts qui ne l'étaient pas auparavant, il se peut que les codes courts doivent être réapprouvés dans le cadre d'une procédure d'approbation qui peut prendre des semaines. Il est important de tenir compte de ce délai lorsque vous décidez d'activer le MMS.
{% endalert %}

### Meilleures pratiques en matière de codes courts MMS

- Chez Braze, nous recommandons vivement de séparer les envois de messages transactionnels et promotionnels, chacun avec des codes courts différents. Comme les MMS sont liés au canal SMS, et que ce dernier est très réglementé, les clients peuvent être tenus de payer une pénalité monétaire en cas d'utilisation abusive du canal et de voir leur code court suspendu (ce qui est irréversible). Le fait de lier les envois de messages transactionnels et promotionnels à des codes courts différents protège leurs messages transactionnels.
- Si les clients disposent déjà d'un code court dédié à l'envoi de messages promotionnels et que celui-ci est compatible avec les MMS, ils n'ont pas besoin d'un code court distinct pour les MMS.

## Codes longs MMS

Les clients peuvent envoyer des MMS avec des codes longs. Pour ce faire, vous devez vous assurer que vos codes longs sont compatibles avec les MMS. Cette opération peut être effectuée initialement lors de la configuration ou ultérieurement à partir de votre compte. 

Notez que nos messages MMS ne peuvent pas être envoyés avec un ID d'expéditeur alphanumérique. Pour en savoir plus sur les ID [alphanumériques]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id), consultez la page [ID d'expéditeur alphanumérique]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id).
