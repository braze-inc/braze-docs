---
nav_title: PERGUNTAS FREQUENTES
article_title: Perguntas frequentes sobre campanhas
page_order: 10
page_type: FAQ
description: "Esta página fornece respostas a perguntas frequentes sobre campanhas."
tool: Campaigns

---

# Perguntas frequentes

> Este artigo fornece respostas a algumas perguntas frequentes sobre campanhas.

### Como faço para criar uma campanha multicanal?

Para criar uma campanha multicanal, selecione **Messaging** > **Campaigns**( **Mensagens** > **Campanhas**). Em seguida, selecione **Create Campaign** > **Multichannel**( **Criar campanha** > **Multicanal**). A partir daí, você pode selecionar os seguintes canais de mensagens: Cartões de conteúdo, e-mail, LINE, notificações por push, SMS/MMS/RCS, webhook ou WhatsApp.

### Posso adicionar um grupo de controle à minha campanha multicanal?

Não, os grupos de controle em campanhas são destinados a mensagens de canal único, como E-mail A versus E-mail B. Como alternativa, tente usar [o Canvas]({{site.baseurl}}/user_guide/engagement_tools/canvas) para testar diferentes canais, conteúdo de mensagens e tempo de entrega. 

### Quais são algumas maneiras de começar a testar e otimizar campanhas?

As campanhas multivariadas e a execução de Canvases com diversas variantes são uma ótima maneira de começar! Por exemplo, você pode executar uma [campanha multivariada]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para testar uma mensagem com diferentes cópias ou linhas de assunto. Telas com múltiplas variantes podem ajudar a testar fluxos de trabalho inteiros.

### Por que a taxa de abertura da minha campanha diminuiu?

As baixas taxas de abertura nem sempre estão relacionadas a um problema técnico. Pode haver problemas com o recorte de e-mail, o que resulta na falta de um pixel de rastreamento. No entanto, também é possível que menos usuários estejam abrindo seus e-mails devido ao conteúdo ou a mudanças no tamanho do público. 

### Como os públicos das campanhas são avaliados?

Por padrão, as campanhas verificam os filtros de público-alvo no momento da entrada. Para campanhas baseadas em ações com atraso, há uma opção para reavaliar os critérios de segmento no momento do envio para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada. 

### Por que há uma diferença entre o número de destinatários únicos e o número de envios de uma determinada campanha ou Canvas?

Uma possível explicação pode ser que a campanha ou o Canvas tenha a reelegibilidade ativada, o que significa que os usuários que se qualificam para o segmento e as configurações de entrega poderão receber a mensagem mais de uma vez. Se a reelegibilidade não estiver ativada, a explicação provável para a diferença entre os envios e os destinatários exclusivos pode ser devido ao fato de os usuários terem vários dispositivos, entre plataformas, associados aos seus perfis. 

Por exemplo, se você tiver um Canvas que tenha notificações push para iOS e Web, um determinado usuário com dispositivos móveis e desktop poderá receber mais de uma mensagem.

### Por que minha campanha tem uma base de usuários alcançável menor do que o segmento que estou usando para a campanha?

Se você tiver um [Grupo de controle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) configurado, isso impedirá que uma porcentagem do seu público-alvo alcançável receba campanhas. Isso significa que o número de usuários alcançáveis para o seu segmento pode, às vezes, ser maior do que o número de usuários alcançáveis para a sua campanha, mesmo que a campanha esteja usando o mesmo segmento.

### O que a entrega por fuso horário local oferece?

A entrega por fuso horário local permite a entrega de campanhas de mensagens a um segmento com base no fuso horário individual de um usuário. Sem a entrega por fuso horário local, as campanhas serão agendadas com base nas configurações de fuso horário de sua empresa no Braze. 

Por exemplo, uma empresa sediada em Londres que envia uma campanha às 12h alcançará usuários na costa oeste dos Estados Unidos às 4h. Se o seu aplicativo estiver disponível apenas em determinados países, isso pode não ser um risco para você. Caso contrário, é altamente recomendável evitar o envio de notificações push de manhã cedo para a sua base de usuários.

### Como o Braze reconhece o fuso horário de um usuário?

O Braze determinará automaticamente o fuso horário de um usuário a partir de seu dispositivo. Isso garante a precisão do fuso horário e a cobertura total dos seus usuários. Os usuários criados por meio da API do usuário ou de outra forma sem um fuso horário terão o fuso horário da sua empresa como fuso horário padrão até que sejam reconhecidos no seu aplicativo pelo SDK. 

Você pode verificar o fuso horário da sua empresa nas [configurações da empresa]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) no painel.

### Quando o Braze avalia os usuários para entrega no fuso horário local?

Para a entrega no fuso horário local, o Braze avalia a elegibilidade de entrada dos usuários durante essas duas instâncias:

- No horário de Samoa (UTC+13) do dia programado
- No horário local do dia programado

Para que um usuário seja elegível para participar, ele deve ser elegível para ambas as verificações. Por exemplo, se um Canvas estiver programado para ser lançado em 7 de agosto de 2021 às 14h do fuso horário local, a segmentação de um usuário localizado em Nova York exigiria as seguintes verificações de elegibilidade:

- Nova York em 6 de agosto de 2021 às 21 horas
- Nova York em 7 de agosto de 2021 às 14h

Observe que o usuário precisa estar no segmento por 24 horas antes do lançamento. Se o usuário não for elegível na primeira verificação, o Braze não tentará a segunda verificação.

Por exemplo, se uma campanha estiver programada para ser entregue às 19h UTC, começaremos a enfileirar os envios da campanha assim que um fuso horário for identificado (como Samoa). Isso significa que estamos nos preparando para enviar a mensagem, não para enviar a campanha. Se os usuários não corresponderem a nenhum filtro quando verificarmos a elegibilidade, eles não se enquadrarão no público-alvo.

Como outro exemplo, digamos que você queira criar duas campanhas programadas para serem enviadas no mesmo dia - uma pela manhã e outra à noite - e adicionar um filtro para que os usuários só possam receber a segunda campanha se já tiverem recebido a primeira. Com a entrega no fuso horário local, alguns usuários podem não receber a segunda campanha. Isso ocorre porque verificamos a elegibilidade quando o fuso horário do usuário é identificado; portanto, se o horário programado ainda não tiver ocorrido em seu fuso horário, ele não recebeu a primeira campanha, o que significa que não estará qualificado para a segunda campanha.

### Como programo uma campanha de fuso horário local?

Ao programar uma campanha, opte por enviá-la em um horário determinado e selecione **Enviar campanha para usuários em seu fuso horário local**.

A Braze recomenda enfaticamente que todas as campanhas de fuso horário local sejam agendadas com 24 horas de antecedência. Como essa campanha precisa ser enviada durante um dia inteiro, programá-la com 24 horas de antecedência garante que sua mensagem chegue a todo o segmento. No entanto, você pode agendar essas campanhas com menos de 24 horas de antecedência, se necessário. Lembre-se de que o Braze não enviará mensagens a nenhum usuário que tenha perdido o horário de envio por mais de 1 hora. 

Por exemplo, se for 13 horas e você programar uma campanha de fuso horário local para as 15 horas, a campanha será enviada imediatamente a todos os usuários cujo horário local esteja entre 15 e 16 horas, mas não aos usuários cujo horário local seja 17 horas. Além disso, o horário de envio escolhido para sua campanha precisa ainda não ter ocorrido no fuso horário de sua empresa.

A edição de uma campanha de fuso horário local programada com menos de 24 horas de antecedência não alterará a programação da mensagem. Se você decidir editar uma campanha de fuso horário local para enviar em um horário posterior (por exemplo, 19h em vez de 18h), os usuários que estavam no segmento segmentado quando o horário de envio original foi escolhido ainda receberão a mensagem no horário original (18h). Se você editar um fuso horário local para enviar em um horário anterior (por exemplo, 16h em vez de 17h), a campanha ainda será enviada a todos os membros do segmento no horário original (17h). 

{% alert note %}
Para os componentes do Canvas, os usuários não precisam estar no componente por 24 horas para receber o próximo componente na jornada do usuário para entrega no fuso horário local.
{% endalert %}

Se você permitiu que os usuários se tornassem reelegíveis para a campanha, eles a receberão novamente no horário original (17 horas). Para todas as ocorrências subsequentes de sua campanha, no entanto, suas mensagens são enviadas somente no horário atualizado.

### Quando as alterações nas campanhas de fuso horário local entram em vigor?

Os segmentos-alvo para campanhas de fuso horário local devem incluir pelo menos uma janela de 48 horas para qualquer filtro baseado em tempo, a fim de garantir a entrega a todo o segmento. Por exemplo, considere um segmento direcionado a usuários no segundo dia com os seguintes filtros:

- Aplicativo usado pela primeira vez há mais de 1 dia
- Primeiro uso do aplicativo há menos de 2 dias

A entrega por fuso horário local pode perder usuários nesse segmento com base no tempo de entrega e no fuso horário local dos usuários. Isso ocorre porque um usuário pode deixar o segmento no momento em que seu fuso horário aciona a entrega.

### Que alterações posso fazer nas campanhas programadas antes do lançamento?

Quando a campanha é programada, é necessário editar qualquer coisa que não seja a composição da mensagem antes de enfileirar as mensagens a serem enviadas. Como em todas as campanhas, você não pode editar os eventos de conversão após o lançamento.

### Atualizei minha campanha programada. Por que ele não foi lançado?

Isso pode acontecer quando uma campanha está programada para ser lançada no exato momento em que foi atualizada. Por exemplo, se no momento são 15h10 e você alterou a campanha para ser lançada às 15h10 e selecionou **Atualizar campanha**, agora já passa das 15h10, o que significa que o horário programado para o lançamento já passou. Em vez de programar a campanha para o mesmo horário, selecione **Enviar assim que a campanha for lançada**.

### Qual é a "zona de segurança" antes que as mensagens em uma campanha programada sejam enfileiradas?

Recomendamos fazer alterações nas mensagens nos seguintes horários:

- **Campanhas programadas únicas:** Editar até o horário de envio programado.
- **Campanhas programadas recorrentes:** Editar até o horário de envio programado.
- **Campanhas de tempo de envio local:** Edite até 24 horas antes do horário de envio programado.
- **Campanhas com tempo de envio ideal:** Edite até 24 horas antes do dia em que a campanha está programada para ser enviada.

Se você fizer alterações em sua mensagem fora dessas recomendações, talvez não veja as atualizações refletidas na mensagem enviada. Por exemplo, se você editar o horário de envio três horas antes de uma campanha ser programada para ser enviada às 12 horas, horário local, poderá ocorrer o seguinte:

- O Braze não enviará mensagens a nenhum usuário que tenha perdido o horário de envio por mais de uma hora.
- As mensagens pré-enfileiradas ainda podem ser enviadas no horário originalmente enfileirado, e não no horário ajustado.

Se você precisar fazer alterações, recomendamos interromper a campanha atual (isso cancelará todas as mensagens enfileiradas). Em seguida, você pode duplicar a campanha, fazer as alterações necessárias e lançar a nova campanha. Talvez seja necessário excluir dessa campanha os usuários que já tenham recebido a primeira campanha. Certifique-se de reajustar os horários do cronograma da campanha para permitir o envio por fuso horário.

### Por que o número de usuários que entram em uma campanha não corresponde ao número esperado?

O número de usuários que entram em uma campanha pode ser diferente do número esperado devido à forma como os públicos e os acionadores são avaliados. No Braze, um público é avaliado antes do acionador (a menos que seja usado um acionador de [alteração de atributo]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value) ). Isso fará com que os usuários saiam da campanha se não fizerem parte do público-alvo selecionado inicialmente, antes que qualquer ação de acionamento seja avaliada.

{% alert tip %}
Para obter mais assistência com a solução de problemas da campanha, entre em contato com o Suporte Braze em até 30 dias após a ocorrência do problema, pois só temos os registros de diagnóstico dos últimos 30 dias.
{% endalert %}

### Qual é a diferença entre as opções Exportar dados do usuário em CSV e Exportar endereço de e-mail em CSV na página de análise da minha campanha?

A seleção da opção **CSV Export Email Addresses (Exportar endereços de e-mail CSV** ) fará o download apenas dos dados de usuários com endereços de e-mail. Por exemplo, se você tiver um segmento de 100.000 usuários, mas apenas 50.000 desses usuários tiverem endereços de e-mail, e você clicar em **CSV Export Email Addresses**, deverá esperar ver apenas 50.000 linhas de dados no arquivo CSV. Em comparação, selecionar **CSV Export User Data** exportará todos os dados do usuário.

### Posso pesquisar uma campanha por seu identificador de API?

Sim, use o filtro `api_id:YOUR_API_ID` na página **Campaigns** para pesquisar uma campanha por seu identificador de API. Consulte a [pesquisa de campanhas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/) para saber mais.

### Qual é a diferença entre campanhas de API e campanhas acionadas por API?

As campanhas acionadas por API permitem que você gerencie o texto da campanha, os testes multivariados e as regras de reelegibilidade no painel do Braze e, ao mesmo tempo, acione a entrega desse conteúdo a partir de seus próprios servidores e sistemas. Essas mensagens também podem incluir dados adicionais a serem modelados nas mensagens em tempo real.

As campanhas de API são usadas para rastrear as mensagens enviadas usando a API. Ao contrário da maioria das campanhas, você não especifica a mensagem, os destinatários ou a programação, mas passa os identificadores para as chamadas de API. 

### Qual é a diferença entre campanhas baseadas em ações e campanhas acionadas por API?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Baseado em ações

As campanhas de entrega baseadas em ações ou campanhas acionadas por eventos são muito eficazes para mensagens transacionais ou baseadas em conquistas e permitem acioná-las para envio depois que um usuário concluir um determinado evento. 

| Prós | Contras | 
| ---- | ---- |
| \- Visibilidade das cargas úteis de JSON recebidas na plataforma (se o evento for acionado pelo usuário de teste) por meio do **registro de atividade de mensagens**<br><br>\- Os elementos de personalização estão incluídos nas propriedades do evento personalizado<br><br>\- O evento personalizado pode ser usado para criar segmentos de usuários qualificados para a mensagem | \- Consome pontos de dados |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Acionado por API

As campanhas acionadas por API e por servidor são ideais para lidar com transações mais avançadas, permitindo que você acione a entrega do conteúdo da campanha a partir de seus próprios servidores e sistemas. A solicitação da API para acionar a mensagem também pode incluir dados adicionais a serem modelados na mensagem em tempo real.

| Benefícios | Considerações | 
| ---- | ---- |
| \- Não registra pontos de dados<br><br>\- Os elementos de personalização estão incluídos nas propriedades da carga útil JSON | \- Não permite que você crie um segmento de usuários qualificados para a mensagem nas propriedades da carga útil JSON<br><br>\- Não é possível ver as cargas úteis de JSON recebidas com o **Registro de atividades de mensagens**|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

