---
nav_title: "Codes courts et longs MMS"
article_title: Codes courts et longs MMS
page_order: 1
description: "Cet article de référence couvre les différences entre les codes courts SMS et MMS et les codes longs."
page_type: Référence
channel:
  - MMS
---

# Codes court et long MMS

Les MMS et les SMS sont tous deux liés au canal SMS de Braze. Pour accéder aux MMS de votre compte nécessite l'achat de SMS pour ceux qui n'ont pas encore acheté d'accès. Les clients SMS existants peuvent accéder aux MMS une fois qu'ils l'ont acheté.

Les MMS sont actuellement supportés pour les codes courts américains et canadiens (5-6 chiffres) et les codes longs (10 chiffres), ainsi que les numéros de clients des États-Unis et du Canada. L'envoi de numéros à des numéros en dehors des États-Unis/Canada est possible, mais les messages MMS seront convertis en un message SMS avec un lien vers l'actif média. Pour en savoir plus sur les codes courts et longs, consultez [cette documentation]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/).

## Codes courts MMS

Toutes les nouvelles applications de code court incluront les MMS par défaut. Généralement, les codes courts doivent être explicitement demandés lors de l'application de code court, mais sont maintenant inclus par défaut. Certains utilisateurs peuvent ne pas implémenter ou utiliser cette fonctionnalité, mais seront disponibles si nécessaire à une date ultérieure.

Pour les utilisateurs qui ont obtenu leurs codes courts avant que Braze ne prenne en charge les MMS, tous les clients actuels des États-Unis et du Canada ayant des codes abrégés américains et canadiens sont admissibles à activer instantanément les MMS. Veuillez contacter votre CSM si cette situation s'applique à vous et si vous souhaitez que les MMS soient activés.

### Meilleures pratiques de code court MMS

- Chez Braze, nous vous recommandons fortement de séparer les transactions et les messages promotionnels, chacun avec des codes courts différents. Parce que le MMS est lié au canal SMS, et que le canal SMS est fortement réglementé, les clients peuvent être tenus de payer une pénalité monétaire pour avoir mal utilisé le canal et avoir leur code court suspendu (ce qui est irréversible). Gardez les transactions et les messages promotionnels liés à des codes courts différents protège leur message transactionnel.

- Si les clients ont déjà un code court dédié à la messagerie promotionnelle, et il est MMS activé, ils n'ont pas besoin d'un code court séparé pour les MMS.

## Codes longs MMS

Les clients peuvent envoyer des MMS avec des codes longs. Pour ce faire, vous devez vous assurer que vos codes longs sont activés MMMS. Cela peut être fait initialement pendant la configuration, ou plus tard à partir de votre compte.

Notez que nos MMS ne peuvent pas être envoyés avec un identifiant alphanumérique de l'expéditeur. Pour en savoir plus sur les identifiants alphanumériques, consultez [l'identifiant de l'expéditeur alphanumérique]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id).
