---
nav_title: "Códigos curtos e longos de MMS"
article_title: Códigos curtos e longos de MMS
page_order: 1
description: "Este artigo de referência aborda as diferenças entre códigos curtos e códigos longos de SMS e MMS."
page_type: reference
alias: /mms_short_long_codes/
channel:
  - MMS
  
---

# Códigos curtos e longos de MMS

> MMS e SMS estão vinculados ao canal Braze SMS. O acesso ao MMS em sua conta requer a compra de SMS para aqueles que ainda não compraram o acesso. Os clientes de SMS existentes podem acessar o MMS depois de comprá-lo. 

Atualmente, o MMS é compatível com códigos curtos dos EUA (números de 5 a 6 dígitos), códigos longos dos EUA e Canadá (números de 10 dígitos) e números de clientes dos EUA e Canadá. O envio de MMS para números fora dos EUA/Canadá é possível, mas as mensagens MMS serão convertidas em uma mensagem SMS com um link para o ativo de mídia. Para saber mais, consulte [Códigos curtos e longos]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/).

## Códigos curtos de MMS

Alguns usuários podem não implementar ou usar códigos curtos de MMS, mas eles estarão disponíveis, se necessário, em uma data posterior.

Para os usuários que obtiveram seus códigos curtos antes de o Braze oferecer suporte a MMS, todos os clientes existentes com códigos curtos dos EUA estão qualificados para ativar instantaneamente o MMS. Entre em contato com o gerente de sucesso do cliente se essa situação se aplicar a você e se quiser ativar o MMS.

{% alert important %}
Ao ativar o MMS para códigos curtos que anteriormente não tinham o MMS ativado, os códigos curtos podem precisar ser reaprovados em um processo de aprovação que pode levar semanas. É importante levar em conta esse tempo ao decidir ativar o MMS.
{% endalert %}

### Práticas recomendadas de código curto MMS

- Na Braze, recomendamos enfaticamente manter separadas as mensagens de transação e promocionais, cada uma com códigos curtos diferentes. Como o MMS está vinculado ao canal de SMS, e o canal de SMS é altamente regulamentado, os clientes podem ser obrigados a pagar uma multa monetária pelo uso indevido do canal e ter seu código curto suspenso (o que é irreversível). Manter as mensagens transacionais e promocionais vinculadas a códigos curtos diferentes protege suas mensagens transacionais.
- Se os clientes já tiverem um código curto dedicado a mensagens promocionais e ele estiver habilitado para MMS, eles não precisarão de um código curto separado para MMS.

## Códigos longos MMS

Os clientes podem enviar MMS com códigos longos. Para fazer isso, você deve garantir que seus códigos longos estejam habilitados para MMS. Isso pode ser feito inicialmente durante a configuração ou posteriormente em sua conta. 

Observe que nossas mensagens MMS não podem ser enviadas com uma ID de remetente alfanumérica. Para saber mais sobre IDs alfanuméricas, consulte [ID alfanumérica do remetente]({{site.baseurl}}/user_guide/message_building_by_channel/sms/phone_numbers/sending_phone_numbers/#alphanumeric-sender-id).
