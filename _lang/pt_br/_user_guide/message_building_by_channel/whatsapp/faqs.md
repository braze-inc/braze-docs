---
nav_title: PERGUNTAS FREQUENTES
article_title: Perguntas frequentes sobre o WhatsApp
page_order: 10
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem durante a configuração de campanhas do WhatsApp."
page_type: FAQ
channel:
  - WhatsApp

---

# Perguntas frequentes

> Nesta página, tentaremos responder às suas perguntas mais difíceis sobre o WhatsApp!<br><br>Estas Perguntas Frequentes não se destinam a fornecer, nem podem ser consideradas como aconselhamento jurídico. O uso do canal do WhatsApp está sujeito a requisitos específicos da Meta Platforms, Inc. Para garantir que esteja usando o canal do WhatsApp em conformidade com todos os requisitos aplicáveis e com todas as leis às quais possa estar especificamente sujeito, você deve procurar a orientação de seu advogado.

## Tópicos de perguntas frequentes
- [Contas comerciais do WhatsApp](#whatsapp-business-accounts)
- [Número de telefone da conta comercial do WhatsApp](#whatsapp-business-account-phone-numbers)
- [Gerenciamento de assinaturas e opt-in](#opt-in-and-subscription-management) 
- [Limites de mensagens](#messaging-limits) 
- [Modelos do WhatsApp](#whatsapp-templates)
- [Capacidade de entrega](#deliverability) 
- [Diversos](#miscellaneous)

### Contas comerciais do WhatsApp 

#### Como faço para criar uma conta comercial do WhatsApp? 
Recomendamos criar sua conta comercial do WhatsApp (WABA) por meio do fluxo de inscrição incorporado no painel do Braze. 

#### Eu já tenho uma conta comercial do Meta. Ainda preciso de uma conta comercial do WhatsApp? 
Sim, você ainda precisa criar uma conta comercial do WhatsApp. Recomendamos que você [aninhe sua WABA abaixo de sua conta comercial Meta principal]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/). 

#### Como faço para acessar minha conta comercial do WhatsApp? 
Depois de concluir o fluxo de inscrição incorporado, você pode acessar sua conta em business.facebook.com navegando até a [seção WhatsApp](https://business.facebook.com/wa/manage/home). 

#### Posso conectar várias WABAs ao Braze? 
Sim, você pode adicionar até 10 contas do WhatsApp Business por espaço de trabalho, e cada conta comercial pode ser aninhada em um Meta Business Manager diferente.

Diagrama do ecossistema Braze e WhatsApp, mostrando como os espaços de trabalho e as contas do WhatsApp Business se conectam entre si: você pode conectar um grupo de assinatura a um número de telefone, várias contas do WhatsApp Business a um espaço de trabalho e um espaço de trabalho a vários portfólios do Meta Business.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### Números de telefone da conta comercial do WhatsApp 

#### Preciso de um número de telefone para minha conta comercial do WhatsApp? 
Sim, você precisa de um número ao qual tenha acesso. Você será solicitado a verificar seu número de telefone com a autenticação de dois fatores ao passar pelo fluxo de inscrição incorporado. O número de telefone não pode ser usado para outras contas do WhatsApp (comerciais ou pessoais).

#### Que tipos de números de telefone são compatíveis com o WhatsApp? 
Consulte os requisitos do Meta para [números de telefone](https://developers.facebook.com/docs/whatsapp/phone-numbers) para obter mais informações. 

#### Posso usar um número de telefone em várias WABAs? 
Não. Um número de telefone não pode ser compartilhado entre várias WABAs. 

#### Preciso de um tipo específico de número de telefone para enviar mensagens para países específicos? 
Não. O WhatsApp permite enviar mensagens para usuários finais de qualquer número de telefone compatível em qualquer país. Consulte os requisitos do Meta para [números de telefone](https://developers.facebook.com/docs/whatsapp/phone-numbers) para obter mais informações. 

#### Preciso usar um número de telefone específico do país para enviar para determinados países?
Não. Com o WhatsApp, qualquer número de telefone compatível pode enviar para usuários finais em qualquer país compatível.

### Gerenciamento de assinaturas e opt-in 

#### Preciso coletar o opt-in para enviar mensagens de marketing aos usuários finais no WhatsApp? 
Sim, o WhatsApp exige que as empresas [coletem o consentimento](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para enviar mensagens de marketing aos usuários finais.

#### Posso enviar mensagens proativas aos usuários finais no WhatsApp para coletar o consentimento de adesão? 
Se você optar por enviar mensagens proativas aos usuários finais, a primeira mensagem iniciada pela empresa deverá perguntar ao usuário se ele deseja receber mensagens de marketing da sua empresa e deverá estar em conformidade com os requisitos do Meta para [obter o opt-in](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Lembre-se de que o WhatsApp monitorará a reputação de sua empresa no canal, portanto, a prática recomendada é ser explícito com os usuários finais e enviar apenas mensagens que eles tenham indicado que desejam receber.
 
#### Preciso coletar o número de telefone do usuário final quando obtenho o opt-in? 
É necessário ter o número de telefone do usuário final no perfil do Braze para enviar uma mensagem. 
- Se você já tiver o número do usuário, não precisará coletá-lo durante o opt-in. 
- Se você não tiver o número do usuário final, seu método de opt-in deverá incluir a captura do número de telefone. 

#### Como faço para atualizar o status da assinatura dos usuários finais que optaram por participar? 
O gerenciamento de assinaturas do canal WhatsApp funciona de forma semelhante à de outros canais Braze. Consulte [Gerenciamento de assinaturas de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/) para obter mais informações.  

#### Se eu já tiver uma lista de usuários que optaram por receber mensagens de marketing no WhatsApp, como faço para atualizar o status da assinatura deles no Braze? 
Você pode atualizar o status da assinatura por meio da [importação de usuários]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-custom-data). 

#### Que métodos devo usar para coletar opt-ins? 
A Braze recomenda consultar [as diretrizes do Meta para métodos de opt-in](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para manter a conformidade. Consulte o recurso a seguir para obter [ideias e sugestões de canais e opt-in](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit) do Braze.

#### O double opt-in é necessário para o WhatsApp? 
Não, o opt-in duplo não é necessário. 

#### Como meus usuários podem optar por não receber mensagens do WhatsApp? 
Seus usuários podem optar por não participar de duas maneiras:
1. Configure uma mensagem de entrada do WhatsApp com uma palavra específica de recusa e use um webhook para atualizar o status da assinatura do usuário.
2. Adicione uma resposta rápida de desativação no modelo do WhatsApp, com um webhook correspondente para atualização. 

### Limites de mensagens 

#### Quais são os limites das mensagens? 
Os limites de mensagens são um conceito de construção de integridade do WhatsApp. Eles determinam o número máximo de conversas iniciadas pela empresa que cada número de telefone pode iniciar em um período contínuo de 24 horas. Há quatro níveis de limite de mensagens: 1k, 10k, 100k e ilimitado.

#### Como faço para aumentar meu limite de mensagens? 
O WhatsApp aumentará seu limite de mensagens se você atender às seguintes condições:
1. [O status do número de telefone](https://www.facebook.com/business/help/896873687365001) é **Conectado** 
2. [A classificação da qualidade do número telefônico](https://www.facebook.com/business/help/896873687365001) é **Média** ou **Alta**
3. Nos últimos sete dias, você iniciou X ou mais conversas com usuários únicos, em que X é o seu limite atual de mensagens dividido por 2 

Portanto, para passar de 100 mil para ilimitado, você deve enviar pelo menos 50.000 conversas iniciadas por empresas em um período de 7 dias. 

#### Quanto tempo leva para aumentar meus limites de mensagens? 
Se todas as condições anteriores forem atendidas, você poderá aumentar seu limite de mensagens de 1k para ilimitado em 4 dias. 

#### Onde posso ver meu limite atual de mensagens? 
Você pode verificar seus limites atuais de mensagens no **Gerenciador do WhatsApp > Painel de visão geral >** guia **Insights**. 

#### O que acontece se eu tentar enviar mensagens quando já tiver atingido meu limite de mensagens?
Se você tentar enviar uma campanha ou Canvas para mais usuários únicos do que o limite atual permite, as mensagens não serão enviadas. O Braze continuará a tentar reenviar as mensagens se/quando seu limite de mensagens aumentar por até um dia. 

#### Meu limite de mensagens pode ser reduzido?
Sim, se a classificação de qualidade do seu número de telefone cair muito, você corre o risco de o WhatsApp diminuir seu limite de mensagens. A Braze recomenda que você se inscreva e seja notificado sobre atualizações relacionadas à qualidade do WhatsApp, incluindo atualizações do status do seu número de telefone e do nível de limite de mensagens. Você pode se inscrever para receber notificações diretamente no painel do WhatsApp Manager. 

#### Qual é o limite de taxa de transferência do Meta?
O Meta tem seu próprio limite de taxa de transferência separado do limite de mensagens WABA. O limite padrão suportado pela API da nuvem é de 80 mensagens por segundo. Se achar que suas campanhas excederão esse limite, você poderá [solicitar](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) o aumento do limite. A Meta recomenda que você envie essa solicitação pelo menos três dias antes do envio da campanha.

### Modelos do WhatsApp 

#### O que é um modelo do WhatsApp? 
O WhatsApp exige que todas as mensagens iniciadas por empresas comecem a usar um modelo aprovado. O modelo inclui o texto da mensagem, juntamente com mídia avançada opcional, como imagens, chamadas para ação e botões de resposta rápida. Depois que o WhatsApp aprovar os modelos, eles poderão ser usados para compor uma mensagem do WhatsApp no Braze. 

#### Onde posso criar, editar e gerenciar meus modelos do WhatsApp? 
Você criará, editará, gerenciará e enviará modelos para aprovação diretamente no WhatsApp Manager. Depois que sua WABA estiver conectada ao Braze, você verá todos os seus modelos no painel com um indicador de status. Se um modelo for rejeitado, você o reenviará diretamente por meio do gerenciador do WhatsApp. **Os modelos não podem ser criados ou editados diretamente no Braze.**

#### Quanto tempo o WhatsApp leva para analisar o envio de um modelo? 
O processo de aprovação pode levar até 24 horas, mas geralmente os modelos são processados em questão de horas ou minutos. 

#### Quantos modelos posso ter em um determinado momento? 
O limite do modelo de mensagem depende do status de verificação de sua empresa. Você pode verificar seu limite na página **Gerenciador do WhatsApp > Modelos de mensagem**. 

#### Como faço para personalizar a cópia do modelo e a mídia avançada no Braze? 
O WhatsApp permite que parâmetros variáveis sejam inseridos em modelos de mensagens. As mensagens não podem começar ou terminar com um parâmetro variável. Os parâmetros variáveis podem ser preenchidos com a lógica Liquid na plataforma Braze. Consulte a [composição de uma mensagem do WhatsApp no Braze]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#step-2-compose-your-whatsapp-message) para saber mais sobre parâmetros variáveis. 

#### Meu modelo foi rejeitado. O Braze pode me ajudar a obter a aprovação? 
A equipe do Braze não tem visibilidade das rejeições de modelos. Você deve trabalhar diretamente com seu gerente do WhatsApp Business para editar e reenviar o modelo. Certifique-se de fornecer um modelo de amostra quando necessário. Verifique se seu modelo segue as políticas [comerciais](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) ou [de](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) [negócios](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) da Meta.

#### A mídia avançada pode ser direcionada ou personalizada no Braze? 
As imagens podem ser carregadas da biblioteca de mídia, mas não podem ser direcionadas dinamicamente. Para URLs, a última parte do link pode ser preenchida dinamicamente usando o Liquid. 

### Capacidade de entrega 

#### Por que uma mensagem não seria entregue? 
Há vários motivos para uma mensagem não ser entregue, incluindo problemas de rede e o fato de o dispositivo estar desligado. 

#### Se uma mensagem não for entregue, serei cobrado? 
Não. Se uma mensagem não for entregue, você não será cobrado. 

#### O que acontece se um usuário final bloquear minha empresa? 
Se um usuário final bloquear sua empresa, as mensagens subsequentes que você tentar enviar não serão entregues e você não será cobrado. 

#### O que acontece se um usuário final relatar uma mensagem? 
Se um usuário final denunciar uma mensagem, você ainda poderá enviar mensagens subsequentes para esse usuário. No entanto, a denúncia pode afetar sua classificação de qualidade no canal. 

#### Se um usuário final bloquear ou denunciar minha empresa, o status da assinatura dele será atualizado no Braze? 
Não. Seu status de assinatura do Braze não será atualizado. 

### Diversos

#### O Braze oferece suporte a casos de uso de suporte ao cliente, como chatbots e chat assistido por humanos para o WhatsApp? 
Não oferecemos suporte a chatbots ou chat assistido por humanos no Braze ou por meio de integrações diretas. 

Se você já usa o WhatsApp como um canal de suporte ao cliente, recomendamos que mantenha a configuração atual e crie um novo WABA via Braze para mensagens de marketing. Essa WABA exigirá um novo número de telefone. 

#### Como posso "preencher a lacuna" entre minhas mensagens de suporte ao cliente e minhas mensagens de marketing via Braze? 
Você pode usar as propriedades do WhatsApp Liquid para encaminhar o conteúdo de mensagens recebidas do WhatsApp (incluindo o corpo da mensagem e os URLs de mídia) do Braze para outras plataformas, incluindo qualquer ferramenta de suporte ao cliente. Para obter detalhes, consulte nossas [etiquetas de personalização com suporte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). 

Para enviar informações para o Braze, por exemplo, para indicar que um usuário está em uma conversa de suporte ativa, você pode registrar um atributo personalizado (como um booleano "tem chat de suporte existente = verdadeiro/falso") e usá-lo como critério de segmentação em suas campanhas de marketing. Você também pode criar links diretos entre dois tópicos de bate-papo para direcionar os usuários para o tópico de suporte a partir do tópico de marketing e vice-versa. 

#### O Braze armazena as respostas dos usuários? 
As mensagens são armazenadas apenas pelo tempo suficiente para serem processadas. Para acessar as mensagens do usuário, use Currents. 

#### Como os números de telefone dos usuários precisam ser armazenados no Braze? 
Os números de telefone do usuário precisam ser armazenados no [formatoE.164 ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/#formatting).

#### Que tipo de mídia avançada é compatível com os modelos do WhatsApp? 
Você pode adicionar imagens, chamadas para ação (URL ou número de telefone) e botões de resposta rápida aos modelos do WhatsApp. Você pode adicionar esses elementos ao criar modelos diretamente no WhatsApp. 

#### Posso importar números de telefone de usuários? 
Sim. É possível [importar números de telefone de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/). 

#### O que é verificação de negócios? 
A verificação de negócios é um conceito do WhatsApp usado para garantir que a marca seja um negócio legítimo. Ela pode ser concluída no Gerenciador do WhatsApp. A verificação comercial também é necessária para dimensionar as mensagens. Sem a verificação comercial, os clientes só podem enviar até 250 usuários finais exclusivos em um período contínuo de 24 horas. 

#### O que é uma conta comercial oficial? 
O OBA lhe dá a marca de seleção verde ao lado do seu nome de exibição e é opcional. Você pode solicitar uma conta comercial oficial após concluir a verificação comercial. Observe que a verificação comercial e uma conta comercial oficial são conceitos diferentes do WhatsApp. 

#### Quais métricas estão disponíveis no painel de controle do Braze? 
Você pode ver destinatários exclusivos, envios, entregas, leituras e falhas no painel do Braze. Observe que os recibos de leitura dos usuários finais devem estar "Ativados" para que o Braze rastreie as leituras. Você também pode configurar eventos de conversão para monitorar o desempenho da campanha, de forma semelhante a outros canais. 

#### O que é uma conversa do WhatsApp? 
O WhatsApp é um canal focado em mensagens bidirecionais e, portanto, se concentra em conversas (em vez de no número de mensagens individuais). Uma conversa é um fio condutor de 24 horas entre uma empresa e um usuário final.

- **Conversa iniciada pela empresa**: Uma conversa em que a empresa começa enviando uma mensagem modelo aprovada para o usuário final. Assim que a empresa envia uma mensagem, começa a janela de 24 horas.
- **Conversa iniciada pelo usuário**: Uma conversa em que o usuário final envia uma mensagem para a empresa. Quando a empresa envia uma mensagem em resposta, começa a janela de 24 horas.

#### Quais fatores afetam a classificação de qualidade do número de telefone e o que acontece quando minha classificação de qualidade cai muito? 
Os fatores que afetam a classificação da qualidade do número de telefone incluem o bloqueio de uma empresa por um usuário final (e os motivos que ele apresenta quando bloqueia uma empresa) e a denúncia de uma empresa por um usuário final. 

Quando uma classificação de qualidade é baixa, o status do número de telefone muda de **Conectado** para **Sinalizado**. Se a qualidade não melhorar em sete dias, o status volta a ser **Conectado**. No entanto, o limite de mensagens diminuirá para o próximo nível. Por exemplo, um número de telefone que costumava ter um limite de 100.000 mensagens agora tem um limite de 10.000 mensagens.
