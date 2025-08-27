---
nav_title: "Práticas recomendadas"
article_title: "Melhores Práticas para SMS, MMS e RCS" 
page_order: 15
description: "Este artigo de referência aborda as práticas recomendadas para SMS/MMS."
alias: /sms_mms_rcs_best_practices/
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
  
---

# Melhores práticas para SMS, MMS e RCS 

> Saiba mais sobre as melhores práticas para SMS, MMS e RCS com a Braze, incluindo nossas recomendações para monitoramento de opt-out e aumento de tráfego.

## Recomendações de monitoramento de aceitação

O cumprimento das solicitações dos destinatários para aceitação de comunicações é exigido por lei. O não cumprimento das solicitações dos destinatários de SMS para aceitação do canal pode incorrer em penalidades, inclusive multas, e pode levar a ações judiciais. A Braze possui recursos para ativar a gestão robusta de opt-in e opt-out de SMS e MMS, além de mecanismos para ajudar a garantir que os pedidos sejam processados corretamente.

De acordo com seus contratos de inscrição conosco, nossos clientes são os únicos responsáveis pela conformidade com a lei aplicável no uso de nossos serviços. Dessa forma, recomendamos enfaticamente que os clientes prestem muita atenção à configuração correta de suas definições de SMS e que testem essas configurações minuciosamente, tomem medidas para monitorar a conformidade com a aceitação e ajam prontamente caso identifiquem casos de não conformidade com pedidos de aceitação.

Ao configurar SMS e MMS na Braze para gerenciar opt-ins e opt-outs, consulte a seguinte lista de recursos:
* [Grupos de inscrições de SMS]({{site.baseurl}}/sms_rcs_subscription_groups/): Grupos de inscrições e métodos e status de aceitação/exclusão.
* [APIs REST de grupos de inscrições]({{site.baseurl}}/api/endpoints/subscription_groups): Como processar aceitações e desistências recebidas de uma fonte que não seja uma resposta direta a uma mensagem.
* [Processamento de palavras-chave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/): Explicações sobre como o Braze aborda o processamento e o gerenciamento de palavras-chave.
* [Aceitação dupla de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/double_opt_in/): Exige que os usuários confirmem explicitamente sua intenção de aceitação antes de poderem receber mensagens SMS. A aceitação dupla de SMS é um requisito para alguns países, portanto, a Braze recomenda configurá-la.
* [Envio de mensagens SMS]({{site.baseurl}}/sending_phone_numbers/): Fundamentos do envio de SMS no Braze, incluindo a importância dos grupos de inscrições, os requisitos para segmentos de SMS e corpos de mensagens e muito mais.

### Considerações

Onde SMS e MMS foram configurados em várias instâncias, e devido a uma má configuração, um opt-out de campanha ou Canvas é enviado para o espaço de trabalho errado.

* A Braze possui um sistema de monitoramento para identificar tais instâncias. Se esse comportamento for sinalizado, a Braze repontuará as aceitações para a instância correta e preencherá novamente todas as aceitações que ocorreram durante o período.
* Recomendamos enfaticamente que os clientes testem as aceitações para cada grupo de inscrições que tenham na Braze. Identificar esse problema antes de lançar uma mensagem é melhor do que fazer a mitigação depois que o problema foi identificado.

O Braze gerencia as inscrições de SMS/MMS tanto no nível do perfil do usuário (`user_id`) quanto no nível do número de telefone (`channel_id`). Quando um número de telefone é aceito ou excluído, a atualização se aplica a todos os perfis que compartilham esse número. No caso de um usuário final ter feito a aceitação com um determinado número de telefone, mas depois mudar de número de telefone, o novo número de telefone herdará o status do grupo de inscrições do usuário. Assim, se um usuário final tiver optado pela aceitação, mas depois entrar novamente no app ou no site com um novo número de telefone, ele não receberá mensagens indesejadas.

## Recomendações de bombeamento de tráfego

### O que é bombeamento de tráfego?

O traffic pumping é uma forma de fraude que ocorre quando um malfeitor usa um formulário on-line para disparar o envio de mensagens SMS em alto volume (por exemplo, mensagens de aceitação ou senhas de uso único). O malfeitor configura um número de telefone de tarifa premium para o qual essas mensagens são enviadas e reivindica uma participação na receita da operadora de celular com a qual o número de tarifa premium foi configurado, gerando assim uma receita ilícita.

### Como identificar o bombeamento de tráfego

* Os números de tarifa premium que dão suporte a esse tipo de golpe geralmente, mas nem sempre, são configurados em países fora de sua área geográfica normal de envio.
* Picos incomuns no envio de mensagens de formulários on-line podem indicar bombeamento de tráfego.
    * Recomendamos a configuração de [alertas de campanha]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) para limitar e notificar se um número excessivamente alto de mensagens for enviado.
* Formulários on-line incompletos podem indicar o preenchimento de formulários programáticos.
* Ao criar formulários on-line, recomendamos definir regras para garantir que os formulários sejam totalmente preenchidos e usar ferramentas como o CAPTCHA para minimizar o risco.

### Impacto do bombeamento de tráfego

Os clientes são responsáveis por monitorar o tráfego que estão enviando e receberão uma fatura por todos os SMS enviados por meio de sua conta. Entre o Braze e o Cliente, o Cliente é a parte que está em melhor posição para detectar e evitar o bombeamento de tráfego.

