---
nav_title: "Codes courts et longs MMS"
article_title: Codes courts et longs MMS
page_order: 1
description: "Cet article de référence couvre les différences entre les codes courts et les codes longs SMS et MMS."
page_type: reference
channel:
  - MMS
  
---

# Codes courts et longs MMS

> MMS et SMS sont tous deux liés au canal SMS de Braze. Pour accéder aux MMS sur votre compte, vous devez acheter l’option SMS si vous n’avez pas encore obtenu l’accès. Les clients SMS existants peuvent utiliser les MMS une fois l’option achetée. 

Le MMS est actuellement pris en charge pour les codes courts (numéros à 5 à 6 chiffres) et les codes longs (numéros à 10 chiffres) aux États-Unis et au Canada, ainsi que les numéros des clients provenant des États-Unis et du Canada. Il est possible d’envoyer des messages à des numéros en dehors des États-Unis et du Canada, mais les messages MMS seront convertis en SMS avec un lien vers la ressource média. Pour en savoir plus, consultez notre section [Codes courts et longs]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/).

## Codes courts MMS

Toutes les nouvelles applications de code court incluront les MMS par défaut. Généralement, les codes courts doivent être explicitement demandés pendant l’application de code court, mais ils sont désormais inclus par défaut. Certains utilisateurs ne peuvent pas implémenter ou utiliser cette fonctionnalité, qui sera disponible si nécessaire à une date ultérieure.

Pour les utilisateurs qui ont obtenu leurs codes courts avant la prise en charge des MMS par Braze, tous les clients existants situés aux États-Unis ou au Canada, avec des codes courts provenant de ces mêmes pays, sont éligibles pour activer instantanément les MMS. Contactez votre gestionnaire du succès des clients si cette situation vous concerne et que vous souhaitez activer les MMS. 

### Meilleures pratiques pour les codes courts MMS

- Chez Braze, nous recommandons fortement de séparer les messages de transaction des messages promotionnels, chacun ayant des codes courts différents. Étant donné que MMS est lié au canal SMS très réglementé, les clients peuvent être tenus de payer une sanction pécuniaire pour mauvais usage du canal et voir leur code court suspendu (opération irréversible). En séparant les messages transactionnels de ceux promotionnels liés à des codes courts distincts, vous protégez votre messagerie transactionnelle. 

- Si les clients disposent déjà d’un code court dédié à la messagerie promotionnelle, et que MMS est activé, ils n’ont pas besoin d’un code court distinct pour MMS.

## Codes longs MMS

Les clients peuvent envoyer des MMS avec des codes longs. Pour ce faire, vous devez vous assurer que vos codes longs sont compatibles avec les MMS. Vérifiez-le initialement lors de la configuration, ou plus tard dans votre compte. 

Notez que nos messages MMS ne peuvent pas être envoyés avec un ID d’expéditeur alphanumérique. Pour en savoir plus sur les ID alphanumériques, consultez la section [ID d’expéditeur alphanumérique]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id).
