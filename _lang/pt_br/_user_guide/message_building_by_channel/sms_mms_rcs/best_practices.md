---
nav_title: "Práticas recomendadas"
article_title: "Práticas recomendadas para SMS, MMS e RCS" 
page_order: 15
description: "Este artigo de referência aborda as práticas recomendadas para SMS/MMS."
alias: /sms_mms_rcs_best_practices/
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Práticas recomendadas para SMS, MMS e RCS 

> Saiba mais sobre as práticas recomendadas para SMS, MMS e RCS com o Braze, incluindo nossas recomendações para monitoramento de desativação e bombeamento de tráfego.

## Recomendações de monitoramento de recusa

A lei exige o cumprimento das solicitações dos destinatários para que optem por não receber comunicações. O não cumprimento das solicitações dos destinatários de SMS para desativar o canal pode incorrer em penalidades, inclusive multas, e pode levar a ações judiciais. O Braze possui recursos para permitir um gerenciamento robusto de opt-in e out de SMS e MMS, além de mecanismos para ajudar a garantir que as solicitações sejam processadas corretamente.

De acordo com seus contratos de assinatura conosco, nossos clientes são os únicos responsáveis pela conformidade com a legislação aplicável no uso de nossos serviços. Dessa forma, recomendamos enfaticamente que os clientes prestem muita atenção à configuração correta de suas definições de SMS e que testem essas configurações minuciosamente, tomem medidas para monitorar a conformidade com o opt-out e ajam prontamente caso identifiquem instâncias de não conformidade com solicitações de opt-out.

Ao configurar SMS e MMS no Braze para gerenciar opt-ins e opt-outs, consulte a lista de recursos a seguir:
* [Grupos de assinatura de SMS]({{site.baseurl}}/sms_rcs_subscription_groups/): Grupos de assinatura e métodos e status de opt-in/out.
* [APIs REST do grupo de assinaturas]({{site.baseurl}}/api/endpoints/subscription_groups): Como processar opt-ins e outs que eles recebem de uma fonte que não seja uma resposta direta a uma mensagem.
* [Processamento de palavras-chave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/): Explicações sobre como o Braze aborda o processamento e o gerenciamento de palavras-chave.
* [SMS double opt-in]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/): Exige que os usuários confirmem explicitamente sua intenção de adesão antes de poderem receber mensagens SMS. O double opt-in de SMS é um requisito para alguns países, portanto, a Braze recomenda a configuração desse recurso.
* [Envio de mensagens SMS]({{site.baseurl}}/sending_phone_numbers/): Fundamentos do envio de SMS no Braze, incluindo a importância dos grupos de assinatura, os requisitos para segmentos de SMS e corpos de mensagens e muito mais.

### Considerações

Quando o SMS e o MMS foram configurados em várias instâncias e, devido a uma configuração incorreta, uma campanha ou os cancelamentos do Canvas são enviados para o espaço de trabalho errado.

* A Braze possui um sistema de monitoramento para identificar tais casos. Se esse comportamento for sinalizado, o Braze repontuará os opt-outs para a instância correta e preencherá novamente todos os opt-outs que ocorreram durante o período.
* Recomendamos enfaticamente que os clientes testem os opt-outs para cada grupo de assinatura que tiverem no Braze. Identificar esse problema antes de lançar uma mensagem é melhor do que mitigá-lo depois que o problema foi identificado.

O Braze gerencia as assinaturas de SMS/MMS tanto no nível do perfil do usuário (`user_id`) quanto no nível do número de telefone (`channel_id`). Quando um número de telefone é ativado ou desativado, a atualização se aplica a todos os perfis que compartilham esse número. No caso de um usuário final que optou por um determinado número de telefone, mas depois mudou de número de telefone, o novo número de telefone herdará o status do grupo de assinatura do usuário. Assim, se um usuário final tiver optado por não participar, mas depois entrar novamente no aplicativo ou site com um novo número de telefone, ele não receberá mensagens indesejadas.

## Recomendações de bombeamento de tráfego

### O que é bombeamento de tráfego?

O bombeamento de tráfego é uma forma de fraude que ocorre quando um agente mal-intencionado usa um formulário on-line para acionar o envio de mensagens SMS em alto volume (por exemplo, mensagens de opt-in ou senhas de uso único). O malfeitor configura um número de telefone de tarifa premium para o qual essas mensagens são enviadas e reivindica uma participação na receita da operadora de celular com a qual o número de tarifa premium foi configurado, gerando assim uma receita ilícita.

### Como identificar o bombeamento de tráfego

* Os números de tarifa premium que dão suporte a esse tipo de golpe geralmente, mas nem sempre, são configurados em países fora de sua área geográfica normal de envio.
* Picos incomuns no envio de mensagens de formulários on-line podem indicar bombeamento de tráfego.
    * Recomendamos a configuração de [alertas de campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) para limitar e notificar se um número excessivamente alto de mensagens for enviado.
* Formulários on-line incompletos podem indicar o preenchimento de formulários programáticos.
* Ao criar formulários on-line, recomendamos definir regras para garantir que os formulários sejam totalmente preenchidos e usar ferramentas como o CAPTCHA para minimizar o risco.

### Impacto do bombeamento de tráfego

Os clientes são responsáveis por monitorar o tráfego que estão enviando e receberão uma fatura por todos os SMS enviados por meio de sua conta. Entre a Braze e o Cliente, o Cliente é a parte que está em melhor posição para detectar e evitar o bombeamento de tráfego.

