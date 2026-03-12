# SMS e remetentes RCS

> Este artigo fornece uma visão geral dos códigos e remetentes disponíveis para o envio de mensagens SMS e RCS.

## Tipos de remetentes SMS e RCS

{% tabs %}
{% tab RCS-Verified Sender %}

#### Remetente verificado RCS

RCS é um sistema de mensagens moderno que oferece mais recursos do que o SMS tradicional, introduzindo capacidades como IDs de remetente de marca, mídia rica e conteúdo interativo, como carrosséis roláveis, respostas rápidas, botões de CTA e mais. Ele é projetado para proporcionar uma experiência do usuário mais elegante e envolvente.  

##### Informações

| Componentes visuais | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| \- Nome da marca<br>\- logotipo<br>\- legenda opcional<br> \- selo verificado | 4 a 6 semanas para aprovação da operadora | A taxa de transferência e a entrega dependem do destinatário ter uma conexão de dados ativa (dados móveis ou Wi-Fi). RCS não depende de limites impostos por redes fixas como o SMS; as mensagens RCS são enviadas por redes de dados em vez dos canais de sinalização celular tradicionais usados pelo SMS. | N/D | 2 vias |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Prós e contras

| Prós |
| ---- |
| **Confiança e branding verificados**<br> Diferente do SMS tradicional, onde sua marca aparece como um código curto aleatório de 5 dígitos ou um código longo, o RCS permite perfis de remetente verificados. Esses perfis incluem o logotipo, nome e um símbolo de "verificado" da sua marca. |
| **Recursos de mensagens ricas**<br> O RCS suporta carrosséis, vídeos em alta resolução e botões de ação sugeridos (como "Reservar agora", "Rastrear pacote" ou "Pagar conta"). Os usuários podem completar tarefas complexas sem sair de seu aplicativo de mensagens, o que pode levar a taxas de conversão mais altas do que um link de texto simples. |
{: .reset-td-br-1 role="presentation"}

| Contras |
| ---- |
| **Suporte fragmentado**<br> Embora o Google tenha promovido fortemente o RCS para Android, e a Apple tenha recentemente introduzido suporte ao RCS para iOS, a implementação ainda pode ser desigual entre diferentes operadoras e regiões. Se o telefone ou a operadora de um usuário não suportar RCS, a mensagem geralmente é enviada como um SMS simples, perdendo, consequentemente, todos os recursos "ricos" do RCS. |
| **Inconsistências na plataforma**<br> A experiência do usuário do RCS varia dependendo da operadora do destinatário, do modelo do dispositivo e do aplicativo de mensagens que eles usam (por exemplo, Google Messages ou iMessage). |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Short Codes %}

#### Códigos curtos de SMS

Um código curto é um número de 5-6 dígitos que pode enviar e receber SMS de e para telefones móveis a taxas mais rápidas do que códigos longos. Códigos curtos são recomendados para envios de alto volume e sensíveis ao tempo.

Alguns países permitem que você escolha um número específico por uma taxa adicional. Esses códigos curtos são chamados de códigos curtos de vaidade. Se você estiver interessado em códigos curtos de vaidade, entre em contato com seu representante de conta da Braze para mais detalhes.

##### Informações

| Comprimento | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| 5-6 dígitos | Aplicação de 4-12 semanas| 100 mensagens por segundo ou mais | Sim | 2 vias |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Prós e contras

| Prós |
| ---- |
| **Velocidade e escalabilidade**<br> Códigos curtos são especificamente projetados para tráfego de alto volume. Eles podem enviar mensagens a taxas mais rápidas do que códigos longos e, como são pré-aprovados diretamente pelas operadoras, têm o menor risco de serem sinalizados por filtros de spam automatizados. |
| **Memorabilidade fácil para "Chamada à Ação"**<br> Para campanhas de marketing, (por exemplo, "Envie WIN para 55555"), um código curto é muito mais fácil para os usuários lembrarem e digitarem do que um número de 10 dígitos. Isso torna os códigos curtos o padrão ouro para anúncios de rádio, TV e outdoors, onde o usuário tem apenas alguns segundos para ver ou ouvir o número. |
{: .reset-td-br-1 role="presentation"}

| Contras |
| ---- |
| **Os códigos curtos estão disponíveis em menos países**<br> Códigos curtos não estão disponíveis em todos os países. Entre em contato com sua equipe de conta da Braze para perguntar sobre os países nos quais você planeja enviar mensagens. |
| **Processo de aplicação mais longo**<br> Ao contrário de códigos longos e IDs de remetente alfanuméricos, que podem ser provisionados em 1-2 semanas às vezes, um código curto pode levar de 4 a 12 semanas ou mais para ser provisionado. Todo grande operador deve aprovar manualmente sua aplicação específica antes que o código esteja ativo em sua rede. Se você tem um lançamento de marketing na próxima semana, um código curto não é uma opção. |
| **Maior custo**<br> Códigos curtos tendem a ser o tipo de remetente mais caro devido às taxas de configuração e aluguel anual. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Long Codes %}

#### Códigos longos de SMS

Um código longo é um número de telefone padrão usado para enviar e receber mensagens SMS. Esses números de telefone são tipicamente chamados de "códigos longos" (números longos de 10 dígitos em muitos países) quando comparados com códigos curtos de SMS (números de 5-6 dígitos).

##### Informações

| Comprimento | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| 10 dígitos | Aplicação de 4 a 6 semanas (pode ser mais curta ou mais longa para diferentes países) | Nos Estados Unidos, a capacidade de envio de códigos longos depende do seu score de confiança 10DLC; em mercados internacionais, a capacidade pode variar ou aumentar em algumas circunstâncias, mas normalmente começa em torno de 10 segmentos de mensagem por segundo (MPS). | Sim | 2 vias (dependendo de onde você está enviando) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Prós e contras

| Prós |
| ---- |
| **Familiaridade e confiança**<br> Códigos longos parecem números de telefone pessoais, frequentemente incluindo um código de área local. Para as marcas, isso representa um equilíbrio entre presença profissional e uma sensação pessoal e acessível. |
| **Maior disponibilidade mundial**<br>Códigos longos estão disponíveis em mais de 100 países importantes em todo o mundo. Entre em contato com seu gerente de sucesso do cliente ou [suporte da Braze]({{site.baseurl}}/braze_support/) para uma lista de países disponíveis.|
{: .reset-td-br-1}

| Contras |
| --- |
| **Velocidades de envio mais lentas e limites diários de mensagens**<br> Códigos longos não são feitos para marketing de "explosão" da mesma forma que os códigos curtos são. Se você tentar enviar uma venda relâmpago sensível ao tempo para 100.000 pessoas de uma só vez a partir de um código longo, pode levar horas para todas as mensagens serem entregues. Nos EUA, operadoras como a T-Mobile também podem impor limites diários de envio para 10DLC com base no score de confiança da sua marca. |
| **Risco de filtragem mais rigorosa**<br> Como os códigos longos parecem números de telefone pessoais, as operadoras os monitoram de perto para evitar que números "pessoa-a-pessoa" sejam usados para spam. Mesmo com uma campanha 10DLC registrada, se o conteúdo da sua mensagem for muito "spam" ou não seguir uma formatação rigorosa, você tem um risco muito maior de ser bloqueado pelas operadoras em comparação com um código curto pré-aprovado. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% tab SMS Alphanumeric Sender ID %}

#### ID de remetente alfanumérico de SMS

Um ID de remetente alfanumérico (frequentemente chamado de "alpha") é uma string reconhecível composta por qualquer combinação de letras e números (geralmente o nome da sua empresa ou marca) exibida como o ID do remetente para mensagens de texto unidirecionais.

Eles podem ter até 11 caracteres e conter letras maiúsculas (A-Z) e minúsculas (a-z), espaços e dígitos (0-9). Eles **não** podem conter apenas números.

##### Informações

| Comprimento | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| Até 11 caracteres | Disponível imediatamente se o pré-cadastro não for necessário. Caso contrário, 1-4 semanas na maioria dos países onde o registro é necessário. | Varia dependendo do país | Não | 1-via |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Prós e contras

| Prós | Contras |
| ---- | ---- | 
| {::nomarkdown} <ul><li> Reconhecimento de marca aprimorado </li><li> Em muitos mercados internacionais, as operadoras locais pré-cadastram e verificam remetentes alfanuméricos, para que suas mensagens tenham menos chances de serem capturadas em filtros de spam agressivos das operadoras que poderiam bloquear códigos longos aleatórios. </li><li> Disponível em 1 semana se o pré-cadastro não for necessário. </li></ul> {:/} | {::nomarkdown} <ul><li> <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>Comunicação bidirecional</a> não é suportada </li><li> Nem todos os países suportam esse recurso. Por exemplo, é suportado no Reino Unido, mas é bloqueado nos EUA. </li><li> Alguns países têm um extenso processo de pré-cadastro que requer a apresentação de documentação legal e prazos mais longos. </li></ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

Para saber mais sobre IDs de remetentes alfanuméricos, entre em contato com seu gerente de sucesso do cliente.
{% endtab %}
{% tab SMS toll-free numbers %}

#### Números gratuitos habilitados para SMS

Números gratuitos têm códigos de área distintos de três dígitos (por exemplo, 800, 888, 877 e 866), permitindo que os usuários entrem em contato com empresas sem serem cobrados. Amplamente utilizados para atendimento ao cliente, eles também podem lidar com todos os tipos de envio de mensagens A2P (aplicação para pessoa), incluindo marketing.

##### Informações

| Comprimento | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| 10 dígitos	 | Aplicação de 2 a 4 semanas | Começa em 3 MPS (segmentos por segundo), podendo ser aumentado por taxas adicionais. | Sim | 2 vias |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation"}

##### Prós e contras

| Prós |
| ---- |
| **Imagem profissional**<br> Números gratuitos são amplamente reconhecidos e confiáveis na América do Norte para comunicação empresarial, proporcionando um toque profissional e autoritário. |
| **Taxa de transferência flexível; sem limites de envio da operadora**<br> Ao contrário dos códigos longos padrão, que podem estabelecer limites de taxa de transferência ou limites de envio da operadora dependendo do país, os números gratuitos podem ter a taxa de transferência aumentada para ajudar a suportar volumes mais altos e não têm limites diários de envio da operadora nos EUA.|
{: .reset-td-br-1 role="presentation"}

| Contras |
| --- |
| **Imparcialidade e neutralidade geográfica**<br> Como os números gratuitos não têm um código de área local, podem parecer muito "corporativos" ou anônimos. Para um negócio de serviço local, um número gratuito pode ter um desempenho pior do que um código longo padrão, pois falta a conexão com a comunidade e às vezes pode ser confundido com uma linha de telemarketing aleatória. |
| **Camada Extra de Filtragem de STOP**<br> Os números gratuitos têm uma camada de gerenciamento de opt-out fora do Braze que não pode ser removida ou personalizada. Quando um usuário envia "STOP" para o seu número gratuito, o usuário será removido de futuras mensagens do seu número e receberá uma resposta automática gerada pela rede. Eles não receberão mais mensagens do seu número gratuito até que enviem "START" para serem removidos da lista de bloqueio do número gratuito. |
{: .reset-td-br-1 role="presentation"}

{% endtab %}
{% endtabs %}

## Configuração

Os requisitos e prazos de configuração variam de acordo com o tipo de remetente e o país em que o remetente está sendo provisionado.

{% tabs local %}
{% tab RCS-verified sender %}

### Remetente verificado RCS

Remetentes verificados pelo RCS são provisionados país a país. O processo de verificação e configuração foca no seu agente ou remetente— a persona digital que interage com os usuários. Você fornecerá ativos de marca e detalhes de verificação.

#### Ativos de marca

- **Nome verificado:** O nome que os usuários veem no topo da conversa. Deve ser um nome comercial reconhecível, não necessariamente o nome legal da sua empresa.
- **Logotipo:** Uma imagem de alta resolução que tem 224x224px. Isso é exibido em uma moldura circular, então mantenha os elementos críticos centralizados.
- **Banner (imagem principal):** Uma imagem de fundo para o seu cartão de perfil de negócios (semelhante a uma foto de capa do Facebook ou LinkedIn).
- **Cor da marca:** Um valor hex para os botões e elementos da interface do usuário que combine com o estilo da sua empresa.

#### Detalhes de verificação

- **Ponto de contato (POC):** Isso é crítico. Você deve fornecer um e-mail de um colaborador direto da marca (não um e-mail de agência). O Google ou a operadora enviará um e-mail para essa pessoa para confirmar que ela autorizou a Braze a agir em seu nome.
- **Website e política de privacidade:** Um site ativo e uma política de privacidade que explique como você lida com dados de usuários e envio de mensagens.
- **Descrição do caso de uso:** Uma explicação clara do que você está enviando (por exemplo, "Atualizações de entrega de pedidos e suporte ao cliente para compras no varejo").

Os prazos do RCS variam dependendo do país e à medida que mais operadoras adotam o canal. Atualmente, você pode esperar que um remetente RCS seja aprovado pelas operadoras dentro de 3 a 6 semanas após solicitar o lançamento.

{% endtab %}
{% tab SMS short codes %}

### Códigos curtos de SMS

Códigos curtos são provisionados país por país. Dependendo do país, o processo de aplicação para códigos curtos é notoriamente imprevisível. A Braze está aqui para ajudar você em cada etapa, então se você quiser um código curto, entre em contato com seu gerente de integração ou outro representante da Braze.

A Braze ajudará a reunir todos os materiais e informações necessárias para enviar uma aplicação e configurar um novo código curto. Os requisitos variam de país para país, mas muitos exigem pelo menos o seguinte:

| Material de aplicação    | Descrição    | Solicitações    |
|----------------------|----------------|-----------------|
| Chamada para Ação (Aceitação) | O principal objetivo das divulgações é confirmar que o usuário consente em receber mensagens de texto e entende a natureza do programa. | {::nomarkdown}<ul><li>Descrição do produto</li><li>Divulgação da frequência das mensagens</li><li>Termos e condições completos OU link para os termos e condições completos</li><li>Política de privacidade OU link para a política de privacidade</li><li>Palavra-chave STOP</li><li>"As tarifas de mensagem e dados podem ser aplicáveis" divulgação.</li></ul>{:/} |
| Termos e condições | Os termos e condições abrangentes podem ser apresentados completamente abaixo da chamada para ação ou acessíveis através de um link próximo à chamada para ação. | {::nomarkdown}<ul><li>Nome do programa (marca)</li><li>Divulgação da frequência das mensagens</li><li>Descrição do produto</li><li>Informações de contato do atendimento ao cliente</li><li>Informações de opt-out</li><li>"As tarifas de mensagem e dados podem ser aplicáveis" divulgação.</li></ul>{:/} |
| Fluxo de mensagens | Programas de mensagens recorrentes devem confirmar a aceitação com uma única mensagem de texto que declare explicitamente a qual programa o usuário se inscreveu e fornecer instruções claras de opt-out.<br><br> Braze processa aceitação, opt-out e mensagens de ajuda, atualizando automaticamente o estado do grupo de inscrições para o usuário e seu número de telefone associado em todas as solicitações recebidas.<br><br> Note que essas palavras-chave e respostas padrão também podem ser personalizadas. | {::nomarkdown}<ul><li>Confirmação de Aceitação:<ul><li>Nome do programa (marca) OU descrição do produto</li><li>Informações de opt-out</li><li>Informações de contato do atendimento ao cliente</li><li>Divulgação da frequência das mensagens</li><li>"As tarifas de mensagem e dados podem ser aplicáveis" divulgação.</li></ul></li><li>Resposta de AJUDA:<ul><li>Nome do programa (marca) OU descrição do produto</li><li>Informações de contato do atendimento ao cliente (e-mail ou número de telefone de suporte).</li></ul></li><li>Resposta de opt-out (STOP):<ul><li>Nome do programa (marca) OU descrição do produto</li><li>Confirmação de que nenhuma mensagem adicional será entregue.</li></ul></li></ul>{:/} |
| Mensagens do programa | As mensagens do programa são enviadas no curso normal do programa de Código Curto, após o usuário ter recebido uma confirmação de aceitação. | {::nomarkdown}<ul><li>Instruções de cancelamento devem ser fornecidas em intervalos regulares e pelo menos uma vez por mês.</li></ul>{:/} |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation"}

Quando todos os seus materiais de aplicação estiverem prontos, a Braze envia a aplicação em seu nome para nossos provedores. A aplicação é então revisada e aprovada por operadores locais que podem fornecer feedback adicional ou solicitar informações adicionais. Após todos os operadores darem aprovação, você pode imediatamente configurar o código curto para uso na Braze.

O prazo de revisão e aprovação do código curto varia, mas normalmente leva de 4 a 12 semanas, dependendo do país e da natureza do programa.

{% alert important %}
Se você já tem seu próprio código curto, entre em contato com seu gerente de sucesso do cliente durante o processo de integração para discutir a migração ou transferência do seu código curto.
{% endalert %}

{% endtab %}
{% tab SMS long codes and toll-free numbers %}

### Códigos longos de SMS (10DLC) e números gratuitos

Em muitos países, a configuração de códigos longos (também chamados de "10DLCs" ou "códigos longos de 10 dígitos") e números gratuitos para envio de SMS passou de um processo de "plug and play" para um sistema de verificação regulamentado. As operadoras querem saber exatamente quem você é e o que você planeja dizer antes de enviar.

Durante o processo de configuração do código longo, você pode esperar compartilhar detalhes sobre a identidade da sua marca e a intenção da campanha.

#### Identidade da marca

- **Nome da entidade legal:** Deve corresponder exatamente aos seus documentos fiscais (por exemplo, "Acme Corp LLC" não "Acme").
- **ID Fiscal:** Nos EUA, este é o seu Número de Identificação do Empregador (EIN). Internacionalmente, você precisará de um número de Imposto sobre Valor Agregado (IVA) ou um Número de Registro de Empresa local (BRN).
- **Presença digital:** Um site ativo e funcional. As operadoras podem verificar isso para confirmar que você não é uma empresa "fantasma".
- **Contato autorizado:** Nome, e-mail e número de telefone de uma pessoa responsável pela conta.

#### Intenção da campanha

- **Caso de uso:** Declare se você está enviando códigos 2FA, lembretes de compromissos, promoções de marketing ou outros.
- **Mensagens de exemplo:** Forneça de 2 a 5 exemplos do que você enviará.
- **Prova de aceitação:** Descreva (e muitas vezes mostre uma captura de tela) como um usuário se inscreve. Exemplos incluem um formulário na web com uma caixa de seleção ou uma palavra-chave "Texto INICIAR" em um cartaz.

A Braze trabalhará com você para coletar todos os detalhes necessários para provisionar seu código longo ou número gratuito, e então enviar os detalhes para nosso provedor para revisão e aprovação. Após a aprovação do programa pelo nosso provedor, configuramos imediatamente o código longo ou número gratuito na Braze.

O cronograma de configuração depende do país de provisionamento. Normalmente, códigos longos e números gratuitos levam entre 1 a 4 semanas para serem aprovados.

{% alert important %}
Todos os clientes que atualmente possuem e/ou usam códigos longos dos EUA para enviar para clientes dos EUA são obrigados a registrar seus códigos longos. Para ler mais sobre os detalhes do registro A2P 10DLC dos EUA e por que é necessário, visite nosso artigo dedicado [artigo 10DLC]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).
{% endalert %}

{% endtab %}
{% tab SMS alphanumeric sender ID %}

### ID de remetente alfanumérico de SMS

IDs de remetente alfanuméricos são altamente regulamentados porque podem ser facilmente falsificados para phishing. Enquanto alguns países permitem que qualquer um configure e envie de um nome, em muitos países você deve primeiro provar que possui a marca.

Você pode ser solicitado a fornecer os seguintes detalhes para configurar um ID de remetente alfanumérico.

- **ID preferido:** Uma string de até 11 caracteres. Ela contém pelo menos uma letra e não pode ser uma palavra genérica como "BANCO" ou "INFORMAÇÃO".
- **Comprovante de propriedade da marca:** Seu Certificado de Marca ou um Documento de Registro de Empresa (por exemplo, um Certificado de Constituição emitido nos últimos 12 meses).
- **Carta de autorização:** Uma carta assinada em papel timbrado da sua empresa autorizando a Braze e nosso provedor a enviar mensagens em seu nome usando aquele ID específico.
- **Modelos de mensagens:** Em várias regiões, você deve registrar os "modelos" exatos das mensagens que pretende enviar. Desvios nas mensagens reais podem causar falhas de entrega nesses países.

O prazo para configurar um ID de remetente alfanumérico depende muito se o país permite a configuração "Dinâmica" (imediata, sem registro necessário) ou exige "Pré-registro". Em países que exigem pré-registro, o prazo de configuração varia, mas geralmente leva entre 1 a 4 semanas.

{% endtab %}
{% endtabs %}

## Perguntas frequentes

Para respostas a perguntas frequentes sobre remetentes de SMS e RCS, consulte nossa página de [Perguntas frequentes sobre SMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/sms/faqs#frequently-asked-questions).