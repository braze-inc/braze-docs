
# SMS e remetentes RCS

> Este artigo explicará os conceitos importantes envolvidos no envio de números de telefone com a Braze.

## Tipos de remetentes SMS e RCS

{% tabs %}
{% tab Remetente RCS Verificado %}

#### remetente RCS verificado

Um remetente RCS verificado é uma representação visual da sua marca que inclui um nome de marca, logotipo, legenda opcional e um selo de verificação. Isso proporciona ao remetente RCS verificado uma vantagem significativa sobre os códigos SMS em termos de estabelecer a confiança do usuário.  

![Um exemplo de remetente RCS verificado em uma mensagem RCS chamada "Cat Failz Cafe".]{% image_buster /assets/img/rcs/rcs_sender.png %}{: style="max-width:60%;"}

##### Informações

| Componentes visuais | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| \- Nome da marca<br>\- logotipo<br>\- legenda opcional<br> \- selo de verificação | 4 a 6 semanas para uma aplicação (pode variar) | Aproximadamente 100 mensagens por remetente por segundo. As taxas de transferência reais podem variar com base no fornecedor, nas condições da rede e nos detalhes específicos da implementação. | Não | 2 vias |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

##### Prós e contras

| Prós |
| ---- |
| **Estabelecendo confiança**<br> Os remetentes RCS verificados são muito mais eficazes em estabelecer a confiança do usuário do que os códigos SMS, dada sua natureza altamente visual, bem como sua verificação explícita pela operadora. 
<br><br>**Recursos de mensagens ricas**<br>Os remetentes RCS verificados ativam o envio de mensagens com capacidades de mensagens mais ricas do que SMS, incluindo mídia rica, como arquivos de imagem e botões interativos. |
{: .reset-td-br-1}

| Contras |
| ---- |
| **Novidade e natureza dinâmica do mercado**<br> RCS é um protocolo relativamente novo, o que significa que a cobertura das operadoras, a entregabilidade e os preços estão evoluindo em ritmos diferentes em diferentes regiões. No entanto, o recente acordo da Apple para suportar o RCS significa que a grande maioria dos usuários de smartphones agora pode ser alcançada por este protocolo. <br><br>**Maior custo de envio de mensagens ricas**<br> As mensagens RCS que utilizam muitas capacidades de envio de mensagens ricas tendem a custar mais por mensagem do que as mensagens SMS. Isso não é surpreendente, dado os benefícios dos recursos ricos, mas pode ser importante notar para o seu orçamento de marketing. |
{: .reset-td-br-1}

{% endtab %}
{% tab Códigos Curtos SMS %}

#### códigos curtos SMS

Um código curto é uma sequência memorável de 5 a 6 dígitos que permite que os remetentes enviem mensagens a taxas mais altas do que os códigos longos. Isso torna os códigos curtos perfeitos para envios em grande volume e sensíveis ao tempo.

##### Informações

| Comprimento | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| 5-6 dígitos | aplicação de 8 a 12 semanas| 100 mensagens por segundo ou mais | Sim | 2 vias |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Prós e contras

| Prós |
| ---- |
| **Velocidade e escalabilidade**<br> Códigos curtos oferecem velocidade e escalabilidade com taxas de envio de 100 segmentos por segundo, 6.000 segmentos por minuto, 360 mil segmentos por hora e 1 milhão de segmentos a cada 2 horas. Os códigos curtos podem atingir taxas tão altas devido à verificação que é necessária durante o processo de solicitação do código curto.<br><br>**MMS habilitado para alguns códigos curtos**<br>Alguns códigos curtos podem ser compatíveis com MMS, também conhecido como Serviço de Mensagens Multimídia, permitindo que você envie mensagens contendo ativos multimídia (JPEG, GIF, PNG) para telefones celulares. Para saber mais sobre MMS na Braze, consulte [Sobre MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/about_mms/). |
{: .reset-td-br-1}

| Contras |
| ---- |
| **Os códigos curtos estão disponíveis em menos países**<br> Os códigos curtos estão atualmente disponíveis em certos países, incluindo os EUA, Reino Unido e Canadá.<br><br>**Processo de aplicação mais longo**<br> Um processo de aplicação envolvente onde os casos de uso devem ser delineados em grande detalhe é necessário. Isso é necessário para permitir a entregabilidade porque, após a concessão de um código curto, as operadoras auditarão códigos curtos, mas **não** filtrarão mensagens, permitindo taxas de envio mais altas. O comprimento deste processo varia dependendo do país.<br><br>**Maior custo**<br> Os códigos curtos custam mais do que os códigos longos e levam mais tempo para serem aprovados. No entanto, após obter um código curto, você é considerado "pré-aprovado" para enviar mensagens a taxas melhores e mais rápidas e está sujeito a menos requisitos durante o processo de envio, uma vez que você terá passado por todas as verificações durante sua solicitação do código curto. |
{: .reset-td-br-1}

{% endtab %}
{% tab Códigos Longos SMS %}

#### códigos longos SMS

Um código longo é um número de telefone padrão usado para enviar e receber chamadas de voz e mensagens SMS. Os números de telefone são tipicamente chamados de "códigos longos" (números de 10 dígitos em muitos países) quando comparados com os códigos curtos de SMS (números de 5-6 dígitos).

##### Informações

| Comprimento | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| 10 dígitos | Aplicação de 4 a 6 semanas (pode ser mais curta ou mais longa para diferentes países) | Nos EUA, a capacidade depende do seu escore de confiança 10DLC; em mercados internacionais, a capacidade pode variar ou ser aumentada em algumas circunstâncias. | Sim | 2 vias (dependendo de onde você está enviando) |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Prós e contras

| Prós |
| ---- |
| **Pode ser usado imediatamente para enviar mensagens (para certos países)**<br>Códigos longos proporcionam uma experiência de cliente localizada e pessoal ao enviar mensagens para casos de uso de pessoa para pessoa. Ao contrário dos códigos curtos de SMS, adquirir um código longo é um processo bastante rápido para alguns países. (Para outros países, leva tanto tempo quanto ou mais do que um código curto.) Códigos longos também podem ser definidos como um número de fallback se um código curto falhar.<br><br>**Maior disponibilidade mundial**<br>Códigos longos estão disponíveis em mais de 100 países importantes em todo o mundo. Por favor, entre em contato com seu gerente de sucesso do cliente ou [suporte]({{site.baseurl}}/braze_support/) da Braze para uma lista de países disponíveis.<br><br>**MMS habilitado para certos países**<br>Compatível com MMS, também conhecido como Serviço de Mensagens Multimídia, permitindo que você envie mensagens contendo ativos multimídia (JPEG, GIF, PNG) para telefones celulares. Para saber mais sobre MMS na Braze, confira nossa documentação [aqui]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/about_mms/).|
{: .reset-td-br-1}

| Contras |
| --- |
| **Velocidades de envio mais lentas**<br>Códigos longos não correspondem à velocidade e ao envio de códigos curtos. As taxas de envio de SMS dependem da sua pontuação de confiança 10DLC nos EUA. |
{: .reset-td-br-1}

{% endtab %}
{% tab Código Curto Vanity SMS %}

#### códigos curtos vanity SMS

Um código curto personalizado é um número de telefone de 5 a 6 dígitos que é especificamente selecionado por uma marca. Os códigos personalizados são marcados e mais fáceis para os consumidores lembrarem, embora sejam geralmente mais caros. Por exemplo:
- O departamento de saúde de NYC tem um código curto personalizados de `692-692` que soletra NYC-NYC em um teclado de telefone.
- A Amazon usa um código curto de `262-966` que soletra AMA-ZON para atualizações de rastreamento de remessas.
- O PayPal usa um código curto de `729-725` que soletra PAY-PAL para comandos de mensagem de texto.<br><br>

##### Informações

| Comprimento | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| 5-6 dígitos | aplicação de 8 a 12 semanas | 100 mensagens por segundo | Sim | 2 vias |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Prós e contras

| Prós |
| ---- |
| **Velocidade e escalabilidade**<br> Códigos curtos oferecem velocidade e escalabilidade com taxas de envio de 100 segmentos por segundo, 6.000 segmentos por minuto, 360 mil segmentos por hora e 1 milhão de segmentos a cada 2 horas. Os códigos curtos podem atingir taxas tão altas devido à verificação que é necessária durante o processo de solicitação do código curto.<br><br>**MMS habilitado**<br>Compatível com MMS, também conhecido como Serviço de Mensagens Multimídia, permitindo que você envie mensagens contendo ativos multimídia (JPEG, GIF, PNG) para telefones celulares. Para saber mais sobre MMS na Braze, consulte [Sobre MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/mms/about_mms/). |
{: .reset-td-br-1}

| Contras |
| ---- |
| **Os códigos curtos não estão disponíveis em todos os lugares**<br> Os códigos curtos estão atualmente disponíveis apenas no **Estados Unidos e Canadá (CA)**.<br><br>**Processo de aplicação mais longo**<br> Um processo de aplicação de 8 a 12 semanas, onde os casos de uso devem ser descritos em grande detalhe, é necessário. Este processo é necessário para permitir a entregabilidade porque, após a concessão de um código curto, as operadoras auditarão os códigos curtos, mas **não** filtrarão mensagens, permitindo taxas de envio mais altas.<br><br>**Maior custo nos EUA**<br> Não há custo adicional para códigos curtos no CA, mas nos EUA, os códigos curtos custam mais do que os códigos longos e levam mais tempo para serem aprovados. No entanto, após obter um código curto, você é considerado "pré-aprovado" para enviar mensagens a taxas melhores e mais rápidas e está sujeito a menos requisitos durante o processo de envio, uma vez que você terá passado por todas as verificações durante sua solicitação do código curto. |
{: .reset-td-br-1}

{% endtab %}
{% tab ID do Remetente Alfanumérico SMS %}

#### ID do remetente alfanumérico SMS

Os IDs do remetente são os códigos curtos ou longos que aparecem no topo de uma mensagem SMS e indicam de quem a mensagem foi enviada. Se um usuário não estiver familiarizado com um ID de Remetente, ele pode optar por ignorar essas mensagens completamente. Através do uso de IDs de remetente alfanuméricos, os usuários conseguem identificar rapidamente de quem estão recebendo mensagens, aumentando as taxas de abertura. 

Os IDs de remetente alfanuméricos permitem que você defina o nome da sua empresa ou marca (como "Kitchenerie" ou "CashBlastr") como o ID do remetente ao enviar mensagens unidirecionais para usuários móveis. Eles podem ter até 11 caracteres e aceitam letras maiúsculas (A-Z) e minúsculas (a-z), espaços e dígitos (0-9). **Pode não haver** apenas números. 

##### Informações

| Comprimento | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| Até 11 caracteres | Disponível imediatamente se a pré-inscrição não for necessária | Varia dependendo do país | Não | 1-via |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Prós e contras

| Prós | Contras |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> Sem custo adicional para implementar </li> <li> Melhora a conscientização da marca </li> <li> Aumenta as taxas de abertura de SMS </li> <li> A velocidade de envio de correspondências de números de telefone dentro do grupo de inscrições </li> <li> Disponível imediatamente se a pré-inscrição não for necessária </li> </ul> {:/} | {::nomarkdown} <ul> <li> <a href='/docs/user_guide/message_building_by_channel/sms/keywords/#two-way-messaging-custom-keyword-responses/'>Comunicação bidirecional</a> não é suportada </li> <li> Nem todos os países aceitam esse recurso </li> <li> Alguns países exigem processos de aprovação adicionais </li> <li> MMS não está habilitado </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2}

Para saber mais sobre o ID do Remetente Alfanumérico, entre em contato com seu gerente de sucesso do cliente.
{% endtab %}
{% tab Número Gratuito SMS %}

#### Número gratuito habilitado para SMS

Um número de telefone gratuito, ou um número de telefone livre, é um número de telefone que é cobrado por todas as chamadas recebidas em vez de incorrer em encargos para o assinante do telefone de origem. Números gratuitos nos EUA e no Canadá são habilitados para SMS, onde os assinantes são cobrados por mensagens de texto recebidas e enviadas.

##### Informações

| Comprimento | Acesso | Throughput | MMS habilitado | 1-via vs. 2 vias |
| --- | --- | --- | --- | --- |
| 10 dígitos	 | Aplicação de 2 a 4 semanas | Depende da sua aprovação e pode ser aumentado pagando mais | Não | 2 vias |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 }

##### Prós e contras

| Prós | Contras |
| ---- | ---- | 
| {::nomarkdown} <ul> <li> Deve ser registrado antes de enviar. </li> </ul> {:/} | {::nomarkdown} <ul> <li> Números gratuitos são apenas nos EUA e no Canadá </li><li> MMS não está habilitado </li> </ul> {:/} |
{: .reset-td-br-1 .reset-td-br-2} 

{% endtab %}
{% endtabs %}

{% alert important %}
Se a taxa de transferência for excedida, algumas mensagens podem falhar.
{% endalert %}

Além dessas diferenças, saiba que uma marca geralmente terá um código curto, mas vários códigos longos de backup, dependendo de quantos destinatários eles planejam enviar SMS.

{% alert important %}
Quer saber o que são os códigos curtos compartilhados? Para saber mais sobre por que recomendamos evitar códigos curtos compartilhados, visite o tópico em nosso [FAQ de SMS]({{site.baseurl}}/sms_faq/).
{% endalert %}

## números de telefone de envio SMS

Códigos curtos e longos são o número de telefone de onde você envia mensagens para seus usuários ou clientes. Eles podem ser códigos curtos de 5 a 6 dígitos ou códigos longos de 10 dígitos. Cada tipo de código oferece benefícios específicos e todos os fatores devem ser considerados antes de escolher se você deseja um código curto, que tipo de código curto você pode querer, além do código longo que você já será atribuído.

## Como posso obter um código curto SMS?

Passar pelo processo de aplicação de código curto pode ser um processo longo. No entanto, pode ser uma experiência que vale a pena! Se você gostaria de um código curto, entre em contato com seu gerente de integração ou outro representante da Braze. Depois que você fizer isso, eles vão se inscrever para você - eles vão pedir algumas informações básicas que ajudarão você a se qualificar. Agora é só esperar.

### Aplicação de código curto

Enquanto Braze é responsável por realmente solicitar o código curto, há algumas informações que precisamos de você. Recomendamos revisar estas perguntas antes de entrar em contato com a Braze. 

As regulamentações exigem que haja respostas para todas as respostas de palavras-chave de aceitação, exclusão e ajuda/informação. Você precisará nos informar os fluxos de mensagens específicos (as respostas que você deseja enviar aos usuários após eles enviarem um [palavra-chave]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/keywords/optin_optout/)) que você deseja para as seguintes situações.

| Fluxo Necessário | Tipo | Exemplo |
| ----------- | ---- | ------- |
| Aceitação <br><br>Aceitação dupla| SMS | `Welcome to our SMS system! Reply "YES" to receive updates from our company. Respond "STOP" to opt-out and "HELP" for more info.` |
| Aceitação | Website | `Hi there, would you like to sign up for SMS? Text "START" to "23456". Or, enter your number below.` |
| Cancelamentos de inscrição | SMS | `Sorry to see you go! If this was a mistake, text back "UNSTOP". Text "HELP" for more information.` |
| Ajuda | N/D | `Our company is a company that does this and that. For more info on the company, let us know here. Or, you can contact support at 1-800-111-1111.` |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3}

Dependendo da sua situação, você pode precisar fornecer mais ou menos fluxos como os listados na tabela anterior. Você também terá que nos informar **três exemplos gerais** de mensagens que você planeja enviar via SMS. Sinta-se à vontade para pedir orientação ao seu representante da Braze.

Você também deve nos informar, independentemente de qual número você usar, quantas mensagens por mês você planeja enviar.

{% alert important %}
Se você tiver seu próprio código curto, entre em contato com seu gerente de sucesso do cliente durante o processo de integração para discutir a migração ou transferência do seu código curto. Os códigos curtos devem ser configurados pelo gerente de sucesso do cliente.
{% endalert %}

## Códigos Longos de Aplicação para Pessoa SMS de 10 Dígitos (A2P 10DLC)

A2P 10DLC refere-se a um sistema nos Estados Unidos que permite que as empresas enviem mensagens do tipo aplicativo para pessoa (A2P) por meio de um número de telefone padrão de código longo de 10 dígitos (10DLC). Os códigos longos de 10 dígitos foram tradicionalmente projetados para o tráfego de pessoa para pessoa (P2P), fazendo com que as empresas sejam restringidas por uma taxa de transferência limitada e por uma filtragem maior. Este serviço ajuda a aliviar esses problemas, melhorando a entregabilidade geral das mensagens, permitindo que as marcas enviem mensagens em grande escala, incluindo links e chamadas para ação, e ajudando a proteger ainda mais os consumidores de mensagens indesejadas. 

Todos os clientes que atualmente possuem e/ou usam códigos longos dos EUA para enviar para clientes dos EUA são obrigados a registrar seus códigos longos para 10DLC. Este processo leva de 4 a 6 semanas. Para saber mais sobre os detalhes do 10DLC e por que ele é necessário, acesse nosso [artigo dedicado ao 10DLC]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/user_phone_numbers/10dlc/).

## Perguntas frequentes

### Como a taxa de transferência de mensagens RCS se compara à taxa de transferência de mensagens SMS?

A taxa de transferência de mensagens RCS não é tão estritamente definida ou controlada pela operadora como é com SMS. Porque as mensagens RCS são enviadas por redes de dados em vez dos canais de sinalização celular tradicionais usados pelo SMS, o RCS não depende de limites impostos pela rede fixa como o SMS. 

### Os remetentes verificados pelo RCS suportam alta taxa de mensagens como um código curto?

Não. Os remetentes verificados pelo RCS não têm a opção de uma alta taxa de mensagens separada.

### Um remetente verificado pelo RCS pode ser compartilhado entre vários grupos de inscrições? 

Não. Semelhante a um remetente de SMS, um remetente verificado pelo RCS só pode ser usado com um único grupo de inscrições.

### Um remetente de fallback de SMS pode ser compartilhado entre grupos de inscrições de SMS?

Não. Os remetentes de fallback de SMS só podem ser usados com um único grupo de inscrições.


