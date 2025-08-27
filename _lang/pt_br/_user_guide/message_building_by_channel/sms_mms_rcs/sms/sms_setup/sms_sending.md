---
nav_title: "Envio de mensagens SMS"
article_title: Visão geral do envio de mensagens SMS
page_order: 4
alias: /sms_message_sending/
description: "Este artigo de referência aborda os conceitos básicos e as práticas recomendadas de envio de SMS."
page_type: reference
channel:
  - SMS
  
---

# Envio de mensagens SMS

> O envio de mensagens pode ser complicado, mas não precisa ser. As seções a seguir listam os fundamentos do envio de mensagens SMS no Braze, incluindo a importância dos grupos de inscrições, os requisitos para segmentos de SMS e corpos de mensagens, bem como as opções avançadas de personalização disponíveis.

## Noções básicas de envio de SMS

### Selecione seu grupo de inscrições

As mensagens SMS devem ser enviadas de um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/). Um grupo de inscrições é uma coleção de números de telefone de envio (como códigos curtos, códigos longos e/ou IDs de remetente alfanuméricos) que são usados para um tipo específico de finalidade de envio de mensagens. É necessário designar um grupo de inscrições para garantir que apenas os usuários inscritos sejam direcionados. Alguns clientes podem descobrir que têm vários grupos de inscrições para diferentes casos de uso, como envio de mensagens SMS transacionais e mensagens SMS promocionais.<br><br>

### Corpo da mensagem de entrada

O corpo de uma mensagem SMS aceita até 1.600 caracteres, incluindo emojis, Liquid e Connected Content. Um único envio de campanha pode resultar em muitos envios de segmentos de mensagens. Os corpos das mensagens SMS do Braze podem ser criados com os padrões de codificação [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) ou [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). Caso um caractere UCS-2 (por exemplo, um Emoji) seja usado, o corpo da mensagem será formatado automaticamente para esse padrão de codificação.<br><br> 

### Compreender os segmentos de mensagens e os limites de caracteres

Os segmentos de mensagens SMS são a forma como o setor de SMS conta as mensagens. Um segmento de mensagem é um agrupamento de até um número definido de caracteres (160 para codificação GSM-7; 67 para codificação UCS-2) que será enviado em um único envio de SMS. Se você enviar um SMS com 161 caracteres usando a codificação GSM-7, verá que há dois (2) segmentos de mensagens que foram enviados. O envio de vários segmentos de mensagens pode resultar em cobranças adicionais.<br><br>

### Personalização de palavras-chave (opcional)

Os regulamentos exigem que haja respostas para todas as respostas de palavras-chave de SMS de aceitação, desativação e ajuda/informação. Com o Braze, você pode definir suas próprias palavras-chave para disparar respostas de aceitação, desativação e ajuda, gerenciar suas próprias respostas que são enviadas aos usuários e definir conjuntos de palavras-chave para diferentes idiomas. Para obter mais informações, consulte nossa coleção sobre [processamento de palavras-chave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/).

{% alert tip %}
Quer saber como criar uma campanha de SMS? Confira nosso guia passo a passo sobre como [criar uma campanha de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/create/).
{% endalert %}

## Práticas recomendadas de envio {#sending-best-practices}

### Envio de SMS para vários países

Algumas marcas podem desejar enviar para um grupo de usuários que tenham números de telefone de diferentes países. Para enviar uma mensagem SMS para um número de telefone em um determinado país, a melhor prática é usar um código longo ou curto que seja do mesmo país. Na verdade, os códigos curtos só podem enviar SMS para números de telefone do mesmo país em que o código curto foi criado. 

Para superar essa limitação, durante o [processo de configuração]({{site.baseurl}}/user_guide/message_building_by_channel/sms/sms_subscription_group/#setup-process) dos grupos de inscrições, os grupos podem ser configurados para conter códigos longos e curtos de vários países diferentes. Quando concluído, o envio de números de telefone com o mesmo código de país que o número de telefone do usuário de direcionamento será automaticamente usado no lançamento de uma campanha. Não será necessário criar campanhas separadas para usuários com números de telefone com códigos de país diferentes, o que lhe permite lançar uma campanha ou usar um componente do Canva para direcionamento a usuários relevantes.

![As cargas úteis de SMS são enviadas usando o mesmo código de país do número de telefone do usuário-alvo]({% image_buster /assets/img/sms/multi_country_subgroups.png %})

#### Melhores práticas

1. **Obter permissão**. Uma das regras mais importantes para usar o SMS como empresa é que você deve primeiro obter permissão dos clientes para entrar em contato com eles. Deixar de fazer isso pode prejudicar sua marca e resultar em altas taxas legais.<br><br>
2. **Escolha o número certo para seu caso de uso**. Três tipos principais de números de telefone podem enviar e receber mensagens SMS: códigos longos, códigos curtos e IDs de remetente alfanuméricos, e seus recursos e disponibilidade em diferentes regiões variam. Pense com antecedência se sua empresa será melhor atendida com um código personalizado. <br><br>
3. **Preste atenção ao tempo**. Lembre-se de que os clientes são mais receptivos aos materiais que são endereçados diretamente a eles. Um pouco de personalização ajuda muito, como usar o nome do destinatário ou adicionar um toque de conversa que reflita os interesses de seus clientes.<br><br>
4. **Engajar-se em conversas bidirecionais**. O SMS é um canal tão eficaz para engajamento com os clientes que é importante prever - e lidar de forma eficaz - com as respostas às suas mensagens. 85% dos consumidores não querem apenas receber informações, mas também responder às empresas ou se engajar em uma conversa.<br><br>
5. **Meça o que funciona**. Você está alcançando os clientes no momento certo, com a melhor frequência e usando as chamadas para ação mais eficazes? O uso das ferramentas de rastreamento corretas pode oferecer métricas diretas e mensuráveis que comprovam seu ROI. 

### Envio de grandes volumes

Planeja fazer envios de alto volume? Temos algumas práticas recomendadas para você garantir que tudo corra bem.

- Ajuste o limite de frequência da velocidade de entrega de sua campanha/canvas conforme necessário, com base no tamanho do público-alvo. Isso garantirá que você atinja o volume de envio de que precisa e que a Braze envie as mensagens na taxa que o Twilio espera e pode suportar.
- Certifique-se de respeitar o limite de 160 caracteres e esteja ciente de que os caracteres especiais são contados duas vezes (por exemplo, barras `\`, carets `^` e tildes `~`). 

