---
nav_title: PERGUNTAS FREQUENTES
article_title: PERGUNTAS FREQUENTES SOBRE SMS
page_order: 12
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem durante a configuração de campanhas de SMS."
page_type: FAQ
alias: /sms_faq/
channel:
  - SMS
  
---

# Perguntas frequentes

> Nesta página, tentaremos responder às suas perguntas mais rigorosas sobre o SMS!

### Você pode incluir links em um SMS?

Você pode incluir qualquer link em qualquer campanha de SMS que desejar. Entretanto, há algumas preocupações a serem consideradas:

- Os links podem ocupar grande parte do limite de 160 caracteres do SMS. Se você incluir um link e um texto, isso poderá resultar em duas mensagens SMS em vez de apenas uma.
- As empresas costumam usar encurtadores de links para limitar o impacto do número de caracteres de um link. No entanto, se enviar um link encurtado por meio de um código longo, as operadoras podem bloquear ou negar a mensagem, pois podem suspeitar do redirecionamento do link.
- O uso de um [código curto]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/short_and_long_codes/) seria o tipo de número mais confiável para incluir links.

O Braze também tem seu próprio recurso de encurtamento de links, que encurta os links e fornece análises de cliques automaticamente. Consulte [Encurtamento de links]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/link_shortening/) para obter mais informações.

### As mensagens de texto de teste contam para os limites?

Sim, eles têm. Tenha isso em mente ao testar as mensagens.

### Um usuário precisa fazer parte de um grupo de assinatura de SMS para receber mensagens de teste de SMS?

Sim, eles têm. Os usuários devem ter um número de telefone válido e fazer parte do grupo de assinatura de SMS usado para o envio do teste.

### Você precisa limitar a velocidade de envio de mensagens SMS?

A taxa de simultaneidade e a taxa de transferência padrão permitem cerca de 360.000 mensagens por hora por código curto. Uma taxa de transferência adicional requer códigos curtos adicionais.

### Como posso evitar excedentes?

Embora não possamos prometer que você não terá um excedente ocasionalmente, você pode seguir estas precauções para diminuir as chances de ultrapassar os limites alocados:

- Preste atenção ao número de caracteres em seu SMS. O envio não intencional de mais de um segmento pode causar excessos. Para obter mais detalhes, consulte nosso [detalhamento por segmento]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown).
- Calcule cuidadosamente os caracteres do SMS para levar em conta o conteúdo líquido ou conectado. O compositor Braze SMS em seu painel não estima nem leva em consideração o uso de nenhum desses recursos.
- Considere o tipo de codificação que a sua mensagem usa - se a sua mensagem usar a codificação GSM-7, você geralmente pode estimar que pode enviar uma mensagem com 128 caracteres por segmento de mensagem. Se a sua mensagem usar a codificação [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set), você geralmente pode estimar que pode enviar uma mensagem com 67 caracteres por segmento de mensagem.
- Teste, teste e teste! Sempre teste suas mensagens SMS antes do lançamento, especialmente ao usar Liquid e Connected Content.

### Quais são as melhores práticas de envio para evitar a detecção de spam para SMS?

1. Certifique-se de que as instruções de opt-in e opt-out estejam claras.
2. Certifique-se de que você (a marca) tenha um relacionamento com o cliente.
3. Certifique-se de que o conteúdo seja relevante para o relacionamento e para o que o usuário optou por receber.

Para obter mais orientações sobre como evitar a detecção de spam, visite [as diretrizes de leis e regulamentos de SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/laws_and_regulations/).

### Como criar uma lógica para opt-ins seletivos para SMS para que os usuários estejam no grupo de assinatura correto?

As palavras-chave personalizadas seriam escritas como eventos personalizados, portanto, você deve criar segmentos com base nas palavras-chave que os clientes podem digitar. Por exemplo, se um usuário optar por receber SMS para mensagens VIP, mas não para alertas, você poderá criar um segmento VIP e um segmento de alertas e, em seguida, atribuir o usuário ao segmento apropriado.

### Quantos caracteres um emoji usa?

Os emojis podem ser complicados, pois não há uma contagem padrão de caracteres em todos os emojis. Há o risco de o emoji exceder o limite de caracteres e dividir o SMS em várias mensagens, apesar de ser exibido como uma única mensagem no compositor do Braze. Ao testar suas mensagens, você pode verificar melhor se uma mensagem será dividida usando nossa [calculadora de segmentos]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-calculator).

### Se um usuário enviar uma mensagem de texto "Stop" para o nosso código curto, ele terá cancelado a assinatura do grupo de assinaturas?

Qual é a aparência disso no perfil do usuário? O grupo de assinaturas será revertido para 2 traços (- -) e haverá eventos personalizados para assinar e cancelar a assinatura.

### Existe uma maneira de verificar se existe um alias em um perfil de usuário?

Os aliases não são visíveis no perfil do usuário. Você precisaria usar os pontos de extremidade [Exportar dados do usuário]({{site.baseurl}}/api/endpoints/export/) para confirmar a definição dos aliases.

### O que são códigos curtos compartilhados?

Com um código curto compartilhado, todas as mensagens de texto, independentemente da empresa ou organização que as envia, chegam ao dispositivo móvel do consumidor a partir do mesmo número de telefone de 5 a 6 dígitos. Embora os códigos curtos compartilhados sejam de custo relativamente baixo e estejam imediatamente disponíveis, isso significa que sua empresa não terá um código curto dedicado.

Algumas desvantagens dessa abordagem incluem:

- Se seus clientes optarem por não receber as mensagens de outra empresa que tenha um código curto compartilhado com você, eles também terão optado por não receber suas mensagens.
- Se uma empresa violar as regras, as mensagens de todas as empresas serão suspensas.
- Problemas de segurança

### Como você permite listar URLs para SMS?

Antes de enviar mensagens SMS contendo URLs para usuários em determinados países (por exemplo, Suécia ou países nórdicos), é necessário registrar esses URLs na operadora. Entre em contato com seu gerente de atendimento ao cliente Braze para obter ajuda. Esse processo levará cerca de cinco dias.  

### O que acontece se vários usuários tiverem o mesmo número de telefone?

Quando vários perfis de usuários que compartilham um número de telefone (habilitado para SMS) estiverem qualificados para uma campanha baseada em ação ou um componente do Canvas ao mesmo tempo, acionados pelo evento de um SMS recebido, o Braze fará a deduplicação dos usuários no nível do componente do Canvas. Isso impedirá que os usuários recebam mais de um texto SMS para um componente do Canvas, mesmo que vários usuários compartilhem o mesmo número de telefone. 

{% alert note %}
O Braze não faz deduções por número de telefone para Canvases agendados.
{% endalert %}

O Braze usará o seguinte fluxo para determinar o perfil do destinatário:
- Verifique qual perfil recebeu SMS mais recentemente (até 7 dias atrás); se houver um, envie-o para esse usuário.
- Se nenhum dos dois tiver recebido SMS até 7 dias atrás, envie para o usuário que tiver um alias de usuário "phone" que corresponda ao número de telefone.
- Se não houver nenhum deles, envie para um perfil aleatório entre os disponíveis. 

Se você receber uma palavra-chave "START" ou "STOP" do número de telefone compartilhado, todos os perfis de usuário serão inscritos e ativados para SMS ou cancelados. Isso também se aplica às alterações de estado da API. Por exemplo, se vários perfis com IDs externos diferentes tiverem os mesmos números de telefone, uma alteração no estado do grupo de assinaturas por meio da API atualizará todos os perfis com esse número de telefone, mesmo que apenas um ID externo seja especificado.

{% alert important %}
Se você escalonar seus usuários em um Canvas e tiver horários de agendamento diferentes para cada componente do Canvas, poderá enviar mensagens duplicadas a um usuário com o mesmo e-mail ou telefone.
{% endalert %}

### As propriedades do evento SMS capturarão palavras-chave em uma frase?

Para que uma palavra-chave seja reconhecida em uma frase (por exemplo, "por favor, pare de me enviar mensagens de texto"), você precisará usar uma declaração líquida na mensagem para reconhecer a palavra específica. As propriedades do evento têm um limite de 256 caracteres; caso contrário, não há limite de caracteres.

### Por que o painel de controle do Braze está me avisando que posso ser cobrado por segmentos de mensagens adicionais quando minha mensagem tem menos de 160 (GCM-7) ou 70 (UCS-2) caracteres?

Poderão ser cobrados segmentos de mensagem adicionais se você tiver a personalização Liquid incluída em sua mensagem. O modelo do Content Block não ocorre até que a mensagem esteja se preparando para ser enviada. Quando você está editando um SMS com um Content Block, o Braze não sabe o que o Content Block conterá, mas fornece uma estimativa aproximada. Recomendamos que os usuários usem o painel de teste para visualizar a mensagem e entender melhor o que esperar.

### O que é um `app_id` no objeto da API de SMS?

A chave da API do identificador do aplicativo ou `app_id` é um parâmetro que associa a atividade a um aplicativo específico em seu espaço de trabalho. Ele designa com qual aplicativo dentro do espaço de trabalho você está interagindo. Por exemplo, você verá que terá um `app_id` para seu aplicativo iOS, um `app_id` para seu aplicativo Android e um `app_id` para sua integração na Web. 

Você pode encontrar seu `app_id` navegando até **Configurações** > **Configurações do aplicativo** e localizando a seção **Identificação**.

### Como serei cobrado pelo SMS?

Além das tarifas para códigos curtos e longos, o Braze oferece uma cota de mensagens SMS para diferentes países. Ou seja, trabalhamos com você para definir um determinado número de segmentos de mensagens para diferentes países, que você usará para enviar campanhas de SMS. O faturamento é feito pelo número de segmentos de mensagens enviados por país. Para saber mais sobre como os segmentos de mensagem são calculados, consulte nosso guia [Segmentos de mensagem e limites de cópia]({{site.baseurl}}/user_guide/message_building_by_channel/sms/campaign/segments/#segment-breakdown). Seu gerente de conta entrará em contato para informá-lo se você estiver próximo de atingir o máximo, fornecendo relatórios relevantes para ajudá-lo a se manter informado. Para mais perguntas sobre excedentes, entre em contato com seu representante Braze.

### Se uma mensagem for enviada para um telefone fixo, ela ainda será contabilizada na minha contagem de envios de SMS?

Nos EUA, Canadá e Reino Unido:
- Se um SMS for enviado para um telefone fixo, ele será marcado como **Não entregue**. Observe que o Twilio ainda cobrará pela tentativa de entrega, portanto, as mensagens marcadas como **Enviadas**, **Entregues** ou **Não entregues** em seus registros de mensagens serão cobradas.
- No Reino Unido, algumas operadoras converterão o SMS em um correio de voz, entregando a mensagem.

Em outros países:
- O Twilio emitirá um erro e você não será cobrado pela tentativa de envio da mensagem SMS. 

### Se um usuário tiver optado por não participar e enviar uma palavra-chave para nosso código curto e longo, ele receberá a resposta que configuramos para essa palavra-chave no Braze?

Se um usuário tiver optado por não participar e enviar uma palavra-chave de uma das [categorias de palavras-chave padrão]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/), ele receberá a resposta para essa palavra-chave. Se um usuário for excluído e enviar uma [palavra-chave personalizada]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/keyword_handling/), ele não receberá a resposta para essa palavra-chave. 
