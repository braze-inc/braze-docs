---
nav_title: Perguntas frequentes sobre fraudes de bombeamento de tráfego por SMS
permalink: "/sms_traffic_pumping_fraud/"
description: "Este artigo de referência aborda as perguntas frequentes sobre fraudes de bombeamento de tráfego por SMS."
hidden: true
---

# Perguntas frequentes sobre fraudes de bombeamento de tráfego por SMS 

### O que é fraude de bombeamento de tráfego de SMS? 

O bombeamento de tráfego de SMS é uma ameaça crescente no espaço de SMS. Isso ocorre quando os fraudadores encontram uma maneira de disparar envios de mensagens SMS para números de telefone que não estão associados a clientes reais, a fim de coletar receita vinculada ao envio fraudulento de mensagens. Na maioria das vezes, eles disparam envios de SMS de alto volume usando formulários on-line, como formulários para aceitação de SMS ou senhas de uso único para redefinição de senha ou login de conta.  

Por exemplo, se uma marca tiver um formulário de inscrição para SMS em seu site para que os clientes aceitem receber mensagens de texto, um fraudador inserirá números de telefone fraudulentos no formulário para disparar mensagens SMS. O fraudador usa números de telefone de tarifa premium para essas mensagens e reivindica uma participação na receita da operadora de telefonia móvel local, que é responsável pela entrega das mensagens aos usuários finais. Esse esquema gera cobranças fraudulentas para a marca. 

### O que a Braze faz para mitigar a fraude de bombeamento por SMS?

Atualmente, o Braze mantém uma lista de bloqueio de SMS para países embargados pelos EUA, bem como para países conhecidos como de alto risco para bombeamento de tráfego, que pode ser consultada em [nossa documentação]({{site.baseurl}}/sms_country_blocklist). Todas as tentativas de envio para números de telefone com esses códigos de país são bloqueadas.

Além disso, o Braze está introduzindo uma lista de permissões geográficas de SMS, que protegerá ainda mais contra o comportamento fraudulento, impondo controles sobre os países para os quais você pode enviar.

### Como posso proteger minha marca contra fraudes de bombeamento de SMS? 

Há várias maneiras de se proteger, inclusive: 
- **Monitore seus volumes diários de envio de SMS em busca de picos e anormalidades:**
    - Recomendamos a definição de [limites de campanha e alertas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/campaign_alerts/) para limitar e notificar se um número excepcionalmente alto de mensagens for enviado.
    - Picos incomuns no envio de mensagens podem indicar bombeamento de tráfego.
    - Um número excepcionalmente alto de aceitações em um curto período de tempo (fora das estratégias intencionais para impulsionar as aceitações) pode indicar um bombeamento de tráfego.
- **Melhore a segurança dos formulários on-line de captura de números de telefone:**
    - [Os modelos de formulário de inscrição de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture) da Braze oferecem medidas de segurança prontas para uso, como a validação do comprimento e do formato do número de telefone. Também é possível configurar o formulário para coletar apenas números de telefone com códigos de país alinhados aos seus clientes-alvo:
        - Por exemplo, se você só faz negócios nos EUA e no Reino Unido, configure o formulário para coletar apenas números com código de país +1 e +44 (os detalhes técnicos podem ser encontrados em [nossa documentação]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/drag_and_drop/templates/phone_number_capture/#step-2-customize-your-phone-number-input-component)).
    - Se estiver criando uma captura de número de telefone personalizada no seu site, recomendamos definir regras para validar o tamanho e o formato do número de telefone e garantir que os formulários estejam totalmente completos antes de coletar os números de telefone. Certifique-se de trabalhar com a sua equipe técnica ou de engenharia para validar as entradas do formulário tanto no lado do cliente quanto no lado do servidor para obter o máximo de proteção.
        - Além disso, considere o uso de ferramentas como o CAPTCHA para garantir que o formulário seja enviado por um ser humano e não por um processo automatizado. A exigência de um CAPTCHA nos formulários de inscrição por SMS pode ajudar a reduzir o número de inscrições fraudulentas.

### Minha marca opera nos EUA, e os EUA estão em minha lista de permissões de permissão geográfica de SMS. Meus clientes ainda receberão meus envios de mensagens SMS quando viajarem para fora dos EUA? 

Sim, desde que seus clientes tenham um número de telefone com código de área dos EUA, eles ainda receberão suas mensagens enquanto estiverem viajando. 

{% alert important %}
Se tiver outras dúvidas sobre o bombeamento de tráfego de SMS e como essas alterações no produto podem afetar o envio de SMS, entre em contato com o gerente de sucesso do cliente.
{% endalert %}
