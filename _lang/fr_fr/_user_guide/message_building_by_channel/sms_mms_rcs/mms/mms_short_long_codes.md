---
nav_title: "Codes courts et longs MMS"
article_title: Codes courts et longs MMS
page_order: 1
description: "Cet article de référence couvre les différences entre les codes courts et les codes longs SMS et MMS."
page_type: reference
alias: /mms_short_long_codes/
channel:
  - MMS
  
---

# Codes courts et longs MMS

> MMS et SMS sont tous deux liés au canal SMS de Braze. Pour accéder aux MMS sur votre compte, vous devez acheter l’option SMS si vous n’avez pas encore obtenu l’accès. Les clients SMS existants peuvent accéder aux MMS après les avoir achetés. 

Le MMS est actuellement pris en charge pour les codes courts (numéros à 5 à 6 chiffres) aux États-Unis et les codes longs (numéros à 10 chiffres) aux États-Unis et au Canada, ainsi que les numéros des clients provenant des États-Unis et du Canada. L'envoi de MMS à des numéros situés en dehors des États-Unis et du Canada est possible, mais les messages MMS seront convertis en messages SMS avec un lien vers la ressource. Pour en savoir plus, consultez [les codes courts et longs]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Codes courts MMS

Certains utilisateurs peuvent ne pas implémenter ou utiliser des codes courts MMS, mais ils seront disponibles si nécessaire à une date ultérieure.

Pour les utilisateurs qui ont obtenu leurs codes courts avant que Braze ne prenne en charge les MMS, tous les clients existants avec des codes courts américains sont éligibles pour activer instantanément les MMS. Contactez votre gestionnaire du succès des clients si cette situation vous concerne et que vous souhaitez activer les MMS.

{% alert important %}
Lors de l'activation des MMS pour des codes courts qui n'avaient pas précédemment les MMS activés, les codes courts devront peut-être être de nouveau approuvés dans un processus d'approbation qui peut prendre plusieurs semaines. Il est important de tenir compte de ce délai lors de l’activation ou non des MMS.
{% endalert %}

### Meilleures pratiques pour les codes courts MMS

- Chez Braze, nous recommandons fortement de séparer les messages de transaction des messages promotionnels, chacun ayant des codes courts différents. Étant donné que MMS est lié au canal SMS très réglementé, les clients peuvent être tenus de payer une sanction pécuniaire pour mauvais usage du canal et voir leur code court suspendu (opération irréversible). Garder les messages transactionnels et promotionnels liés à différents codes courts protège leurs messages transactionnels.
- Si les clients disposent déjà d’un code court dédié à la messagerie promotionnelle, et que MMS est activé, ils n’ont pas besoin d’un code court distinct pour MMS.

## Codes longs MMS

Les clients peuvent envoyer des MMS avec des codes longs. Pour ce faire, vous devez vous assurer que vos codes longs sont compatibles avec les MMS. Vérifiez-le initialement lors de la configuration, ou plus tard dans votre compte. 

Notez que nos messages MMS ne peuvent pas être envoyés avec un ID d’expéditeur alphanumérique. Pour en savoir plus sur les identifiants alphanumériques, consultez [ID d'expéditeur alphanumérique]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id).
