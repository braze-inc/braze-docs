---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre o WhatsApp
page_order: 80
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem ao configurar campanhas do WhatsApp."
page_type: FAQ
channel:
  - WhatsApp

---

# Perguntas frequentes

> Nesta página, tentaremos responder às suas perguntas mais difíceis sobre o WhatsApp!<br><br>Estas Perguntas Frequentes não se destinam a fornecer, nem podem ser consideradas como aconselhamento jurídico. O uso do canal do WhatsApp está sujeito a requisitos específicos da Meta Platforms, Inc. Para garantir que esteja usando o canal do WhatsApp em conformidade com todos os requisitos aplicáveis e com todas as leis às quais possa estar especificamente sujeito, você deve procurar o conselho de seu advogado.

## Tópicos de perguntas frequentes
- [Contas comerciais do WhatsApp](#whatsapp-business-accounts)
- [Número de telefone da conta empresarial do WhatsApp](#whatsapp-business-account-phone-numbers)
- [Gerenciamento de aceitação e inscrição](#opt-in-and-subscription-management) 
- [Limites de envio de mensagens](#messaging-limits) 
- [Modelos do WhatsApp](#whatsapp-templates)
- [Entregabilidade](#deliverability) 
- [Diversos](#miscellaneous)

### Contas comerciais do WhatsApp 

#### Como faço para criar uma conta do WhatsApp Business? 
Recomendamos que você crie sua conta do WhatsApp Business (WABA) por meio do fluxo de inscrição incorporado no dashboard do Braze. 

#### Eu já tenho uma conta comercial do Meta. Ainda preciso de uma conta do WhatsApp Business? 
Sim, você ainda precisa criar uma conta do WhatsApp Business. Recomendamos que você [aninhe seu WABA abaixo de sua conta comercial principal da Meta]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/overview/). 

#### Como posso acessar minha conta do WhatsApp Business? 
Depois de concluir o fluxo incorporado de inscrição, você pode acessar sua conta em business.facebook.com > [seção WhatsApp](https://business.facebook.com/wa/manage/home). 

#### Posso conectar várias WABAs ao Braze? 
Sim, você pode adicionar até 10 contas do WhatsApp Business por espaço de trabalho, e cada conta comercial pode ser aninhada em um Meta Business Manager diferente.

![Diagrama do ecossistema do Braze e do WhatsApp, mostrando como os espaços de trabalho e as contas do WhatsApp Business se conectam entre si: você pode conectar um grupo de inscrições a um número de telefone, várias contas do WhatsApp Business a um espaço de trabalho e um espaço de trabalho a vários portfólios do Meta Business.]({% image_buster /assets/img/whatsapp/whatsapp_braze_ecosystem.png %}) 

### Números de telefone da conta empresarial do WhatsApp 

#### Preciso de um número de telefone para minha conta do WhatsApp Business? 
Sim, você precisa de um número ao qual tenha acesso. Será solicitado que você verifique seu número de telefone com a autenticação de dois fatores ao passar pelo fluxo de inscrição incorporado. O número de telefone não pode ser usado para outras contas do WhatsApp (comerciais ou pessoais).

#### Que tipos de números de telefone são compatíveis com o WhatsApp? 
Para saber mais, consulte os requisitos da Meta para [números telefônicos](https://developers.facebook.com/docs/whatsapp/phone-numbers). 

#### Posso usar um número de telefone em várias WABAs? 
Não. Um número de telefone não pode ser compartilhado entre várias WABAs. 

#### Preciso de um tipo específico de número de telefone para enviar mensagens para países específicos? 
Não. O WhatsApp permite o envio de mensagens para usuários finais de qualquer número de telefone compatível em qualquer país. Para saber mais, consulte os requisitos da Meta para [números telefônicos](https://developers.facebook.com/docs/whatsapp/phone-numbers). 

#### Preciso usar um número de telefone específico do país para enviar para determinados países?
Não. Com o WhatsApp, qualquer número de telefone compatível pode enviar para usuários finais em qualquer país compatível.

### Gerenciamento de aceitação e inscrição 

#### Preciso coletar a aceitação para enviar mensagens de marketing para os usuários finais no WhatsApp? 
Sim, o WhatsApp Business exige que as empresas [coletem o consentimento de aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para enviar mensagens de marketing aos usuários finais.

#### Posso enviar mensagens de forma proativa aos usuários finais no WhatsApp para coletar o consentimento de aceitação? 
Se optar por enviar mensagens aos usuários finais de forma proativa, a primeira mensagem iniciada pela empresa deve perguntar ao usuário se ele deseja receber mensagens de marketing da sua empresa e deve estar em conformidade com os requisitos do Meta para [obter a aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/). Lembre-se de que o WhatsApp monitorará a reputação da sua empresa no canal, portanto, a prática recomendada é ser explícito com os usuários finais e enviar apenas mensagens que eles tenham indicado que desejam receber.
 
#### Preciso coletar o número de telefone do usuário final quando obtenho a aceitação? 
É necessário ter o número de telefone do usuário final no perfil do Braze para enviar mensagens a ele. 
- Se você já tiver o número do usuário, não precisará coletá-lo durante a aceitação. 
- Se não tiver o número do usuário final, seu método de aceitação deverá incluir a captura do número de telefone. 

#### Como faço para atualizar o status da inscrição dos usuários finais com aceitação? 
O gerenciamento de inscrições do canal WhatsApp funciona de forma semelhante à de outros canais Braze. Para saber mais, consulte [Gerenciando inscrições de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_subscription/).  

#### Se eu já tiver uma lista de usuários que fizeram a aceitação para receber mensagens de marketing no WhatsApp, como atualizo o status da inscrição deles no Braze? 
É possível atualizar o status da inscrição por meio da [importação de usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-custom-data). 

#### Que métodos devo usar para coletar aceitações? 
A Braze recomenda consultar as [diretrizes da Meta para métodos de aceitação](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/) para manter a conformidade. Consulte o recurso a seguir para obter [ideias e sugestões de canais e aceitação](https://docs.google.com/document/d/1rNKnKN2oIn-e9bXdYEvnwdlzlCsEOKs-xREcdVvPBE8/edit) do Braze.

#### A aceitação dupla é necessária para o WhatsApp? 
Não, a aceitação dupla não é necessária. 

#### Como meus usuários aceitam o envio de mensagens do WhatsApp? 
Seus usuários podem fazer a aceitação de duas maneiras:
1. Configure uma mensagem de entrada do WhatsApp com uma palavra específica de aceitação e use um webhook para atualizar o status da inscrição do usuário.
2. Adicione uma resposta rápida de aceitação no modelo do WhatsApp, com um webhook correspondente para atualização. 

### Limites de envio de mensagens 

#### Quais são os limites de envio de mensagens? 
Os limites de envio de mensagens são um conceito de construção de integridade do WhatsApp. Eles determinam o número máximo de conversas iniciadas pela empresa que cada número de telefone pode iniciar em um período contínuo de 24 horas. Há quatro níveis de limite de envio de mensagens: 1k, 10k, 100k e ilimitado.

#### Como faço para aumentar meu limite de envio de mensagens? 
O WhatsApp aumentará seu limite de envio de mensagens se você atender às seguintes condições:
1. [O status do número de telefone](https://www.facebook.com/business/help/896873687365001) é **Conectado** 
2. [A classificação da qualidade do número telefônico](https://www.facebook.com/business/help/896873687365001) é **Média** ou **Alta**
3. Nos últimos sete dias, você iniciou X ou mais conversas com usuários únicos, em que X é o seu limite atual de envio de mensagens dividido por 2 

Portanto, para acessar de 100 mil a ilimitado, é necessário enviar pelo menos 50.000 conversas iniciadas por empresas em um período de 7 dias. 

#### Quanto tempo leva para aumentar meus limites de envio de mensagens? 
Se todas as condições anteriores forem atendidas, você poderá aumentar seu limite de envio de mensagens de 1k para ilimitado em 4 dias. 

#### Onde posso ver meu limite atual de envio de mensagens? 
Você pode verificar seus limites atuais de envio de mensagens no **Gerenciador do WhatsApp > Painel de visão geral > guia Insights.**  

#### O que acontece se eu tentar enviar mensagens quando já tiver atingido meu limite de envio de mensagens?
Se tentar enviar uma campanha ou um Canva para mais usuários únicos do que o limite atual permite, as mensagens não serão enviadas. O Braze continuará tentando reenviar as mensagens se/quando seu limite de mensagens aumentar por até um dia. 

#### Meu limite de envio de mensagens pode ser reduzido?
Sim, se a classificação de qualidade do seu número de telefone cair muito, você corre o risco de o WhatsApp diminuir seu limite de mensagens. O Braze recomenda que você se inscreva e seja notificado sobre atualizações relacionadas à qualidade do WhatsApp, incluindo atualizações do status do seu número de telefone e do nível do limite de envio de mensagens. Você pode se inscrever para receber notificações diretamente no dashboard do WhatsApp Manager. 

#### Qual é o limite de taxa de transferência da Meta?
A Meta tem seu próprio limite de taxa de transferência separado do limite de envio de mensagens do WABA. O limite padrão suportado pela API da nuvem é de 80 mensagens por segundo. Se achar que suas campanhas excederão esse limite, você poderá [solicitar](https://developers.facebook.com/docs/whatsapp/cloud-api/overview/#throughput) o aumento do limite. A Meta recomenda que você envie essa solicitação pelo menos três dias antes do envio da campanha.

### Modelos do WhatsApp 

#### O que é um modelo do WhatsApp? 
O WhatsApp exige que todas as mensagens iniciadas por empresas comecem a usar um modelo aprovado. O modelo inclui o texto da mensagem, juntamente com mídia avançada opcional, como imagens, chamadas para ação e botões de resposta rápida. Depois que o WhatsApp aprovar os modelos, eles poderão ser usados para compor uma mensagem do WhatsApp no Braze. 

#### Onde posso criar, editar e gerenciar meus modelos do WhatsApp? 
Você criará, editará, gerenciará e enviará modelos para aprovação diretamente no WhatsApp Manager. Depois que sua WABA estiver conectada ao Braze, você verá todos os seus modelos no dashboard com um indicador de status. Se um modelo for rejeitado, você o reenviará diretamente por meio do gerenciador do WhatsApp. **Os modelos não podem ser criados ou editados diretamente no Braze.**

#### Quanto tempo o WhatsApp leva para analisar o envio de um modelo? 
O processo de aprovação pode levar até 24 horas, mas muitas vezes os modelos são processados em questão de horas ou minutos. 

#### Quantos modelos posso ter em um determinado momento? 
O limite do modelo de mensagem depende do status de verificação de sua empresa. Você pode verificar seu limite na página **Gerenciador do WhatsApp > Modelos de mensagens**. 

#### Como faço para personalizar a cópia do modelo e a mídia avançada no Braze? 
O WhatsApp permite que parâmetros variáveis sejam inseridos em modelos de mensagens. As mensagens não podem começar ou terminar com um parâmetro variável. Os parâmetros variáveis podem ser preenchidos com a lógica Liquid na plataforma Braze. Consulte o artigo [Criador de uma mensagem do WhatsApp no Braze]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/whatsapp_campaign/create#step-2-compose-your-whatsapp-message) para saber mais sobre parâmetros variáveis. 

#### Meu modelo foi rejeitado. O Braze pode me ajudar a obter a aprovação? 
A equipe do Braze não tem visibilidade das rejeições de modelos. Fale diretamente com seu gerente do WhatsApp Business para editar e reenviar o modelo. Forneça um modelo de amostra quando necessário. Verifique novamente se seu modelo segue as políticas [comerciais](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) ou [de](https://www.whatsapp.com/legal/commerce-policy/?fbclid=IwAR3bzN3LTZ-7kO-wnO7X3smtPKGy0asxaFod-U1Ub8B9JUpnrfy1_y7LpAQ) [negócios](https://www.whatsapp.com/legal/business-policy/?fbclid=IwAR2qWg6yFKdyjDMxJkbNSM38FLGsxXxffC1qStY2gaHOyp-gl_8g72rZNIw) da Meta.

#### A mídia avançada pode ser direcionada ou personalizada no Braze? 
É possível fazer upload de imagens a partir da biblioteca de mídia, mas não é possível direcioná-las dinamicamente. Para URLs, a última parte do link pode ser preenchida dinamicamente usando o Liquid. 

### Entregabilidade 

#### Por que uma mensagem não seria entregue? 
Há vários motivos para uma mensagem não ser entregue, incluindo problemas de rede e o fato de o dispositivo estar desligado. 

#### Se uma mensagem não for entregue, serei cobrado? 
Não. Se uma mensagem não for entregue, você não será cobrado. 

#### O que acontece se um usuário final bloquear meu negócio? 
Se um usuário final bloquear sua empresa, as mensagens subsequentes que você tentar enviar não serão entregues e você não será cobrado. 

#### O que acontece se um usuário final relatar uma mensagem? 
Se um usuário final denunciar uma mensagem, ainda será possível enviar mensagens subsequentes a esse usuário. No entanto, a denúncia pode afetar sua classificação de qualidade no canal. 

#### Se um usuário final bloquear ou denunciar minha empresa, o status da inscrição dele será atualizado no Braze? 
Não. Seu status de inscrição no Braze não será atualizado. 

### Diversos

#### O Braze oferece suporte a casos de uso de suporte ao cliente, como chatbots e bate-papo assistido por humanos para o WhatsApp? 
Não oferecemos suporte a chatbots ou chat assistido por humanos no Braze ou por meio de integrações diretas. 

Se você já usa o WhatsApp como canal de suporte de clientes, recomendamos que mantenha sua configuração atual e crie um novo WABA via Braze para envio de mensagens de marketing. Essa WABA exigirá um novo número de telefone. 

#### Como posso "preencher a lacuna" entre o envio de mensagens do meu suporte ao cliente e o envio de mensagens de marketing via Braze? 
Você pode usar as propriedades do WhatsApp Liquid para encaminhar o conteúdo das mensagens recebidas do WhatsApp (incluindo o corpo da mensagem e os URLs de mídia) do Braze para outras plataformas, incluindo qualquer ferramenta de suporte ao cliente. Para saber mais, consulte nossas [tags de personalização com suporte]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/supported_personalization_tags/). 

Para enviar informações para o Braze, por exemplo, para indicar que um usuário está em uma conversa de suporte ativa, é possível registrar um atributo personalizado (como um booleano "tem chat de suporte existente = verdadeiro/falso") e usá-lo como critério de segmentação em suas campanhas de marketing. Também é possível fazer um deep linking entre dois tópicos de bate-papo para direcionar os usuários para o tópico de suporte a partir do tópico de marketing e vice-versa. 

#### O Braze armazena as respostas dos usuários? 
As mensagens só ficam armazenadas pelo tempo suficiente para serem processadas. Para acessar as mensagens do usuário, use Currents. 

#### Como os números de telefone dos usuários precisam ser armazenados no Braze? 
Os números de telefone do usuário precisam ser armazenados no [formatoE.164 ]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/#formatting).

#### Que tipo de mídia avançada é compatível com os modelos do WhatsApp? 
Você pode adicionar imagens, chamadas para ação (URL ou número de telefone) e botões de resposta rápida aos modelos do WhatsApp. Você pode adicionar esses elementos ao criar modelos diretamente no WhatsApp. 

#### Posso fazer a importação de números de telefone de usuários? 
Sim. É possível [fazer a importação de números de telefone de usuários]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/user_phone_numbers/). 

#### O que é verificação de negócios? 
A verificação de negócios é um conceito do WhatsApp usado para garantir que a marca seja um negócio legítimo. Ela pode ser concluída no WhatsApp Manager. A verificação comercial também é necessária para dimensionar o envio de mensagens. Sem a verificação comercial, os clientes só podem enviar até 250 usuários finais exclusivos em um período contínuo de 24 horas. 

#### O que é uma conta comercial oficial? 
O OBA concede a marca de seleção verde ao lado do seu nome de exibição e é opcional. Você pode solicitar uma conta comercial oficial após concluir a verificação comercial. É importante frisar que a verificação comercial e uma conta comercial oficial são conceitos diferentes no WhatsApp. 

#### Quais métricas estão disponíveis no dashboard do Braze? 
Você pode ver destinatários exclusivos, envios, entregas, leituras e falhas no dashboard do Braze. Note que os recibos de leitura dos usuários finais devem estar "Ligados" para que a Braze rastreie as leituras. Você também pode configurar eventos de conversão para monitorar a performance da campanha, de forma semelhante a outros canais. 

#### O que é uma conversa do WhatsApp? 
O WhatsApp é um canal focado no envio de mensagens bidirecionais e, portanto, se concentra nas conversas (em vez de no número de mensagens individuais). Uma conversa é um fio condutor de 24 horas entre uma empresa e um usuário final.

- **Conversa iniciada pela empresa**: Uma conversa em que a empresa começa enviando uma mensagem de modelo aprovado para o usuário final. Assim que a empresa envia uma mensagem, começa o período de 24 horas.
- **Conversa iniciada pelo usuário**: Uma conversa em que o usuário final envia uma mensagem para a empresa. Quando a empresa envia uma mensagem em resposta, começa o período de 24 horas.

#### Quais fatores afetam a classificação de qualidade do número de telefone e o que acontece quando minha classificação de qualidade cai muito? 
Os fatores que afetam a classificação da qualidade do número de telefone incluem o bloqueio de uma empresa por um usuário final (e os motivos que ele apresenta quando bloqueia uma empresa) e a denúncia de uma empresa por um usuário final. 

Quando uma classificação de qualidade é baixa, o status do número de telefone muda de **Conectado** para **Sinalizado**. Se a qualidade não melhorar em sete dias, o status volta a ser **Conectado**. No entanto, o limite de envio de mensagens diminuirá para o próximo nível. Por exemplo, um número de telefone que costumava ter um limite de 100.000 envios de mensagens agora tem um limite de 10.000 envios de mensagens.
