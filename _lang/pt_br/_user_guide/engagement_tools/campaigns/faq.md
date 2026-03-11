---
nav_title: Perguntas frequentes
article_title: Perguntas Frequentes sobre Campanhas
page_order: 10
page_type: FAQ
description: "Esta página fornece respostas às perguntas frequentes sobre campanhas."
tool: Campaigns

---

# Perguntas frequentes

> Este artigo fornece respostas para algumas perguntas frequentes sobre campanhas.

### Como faço para criar uma campanha multicanal?

Para criar uma campanha multicanal, selecione **Envio de Mensagens** > **Campanhas**. Em seguida, selecione **Criar Campanha** > **Multicanal**. A partir daqui, você pode selecionar entre os seguintes canais de envio: Cartões de Conteúdo, e-mail, LINE, notificações por push, SMS/MMS/RCS, webhook ou WhatsApp.

### Posso adicionar um grupo de controle à minha campanha multicanal?

Não, os grupos de controle em campanhas são destinados ao envio de mensagens de canal único, como e-mail A versus e-mail B. Como alternativa, tente usar [canva]({{site.baseurl}}/user_guide/engagement_tools/canvas) para testar diferentes canais, conteúdo de envio de mensagens e tempo de entrega. 

### Quais são algumas maneiras de começar a testar e otimizar campanhas?

Campanhas multivariantes e execução de canvas com várias variantes são uma ótima maneira de começar! Por exemplo, você pode executar uma [campanha multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para testar uma mensagem que possui diferentes cópias ou linhas de assunto. Canvases com múltiplas variantes podem ajudar a testar fluxos de trabalho inteiros.

### Por que a taxa de abertura da minha campanha diminuiu?

As taxas de abertura baixas nem sempre estão correlacionadas a um problema técnico. Pode haver problemas com o recorte de e-mail, o que resulta em um pixel de rastreamento ausente. No entanto, também é possível que menos usuários estejam abrindo seus e-mails devido ao conteúdo ou mudanças no tamanho do público. 

### Como são avaliados os públicos da campanha?

Por padrão, as campanhas verificam os filtros de público no momento da entrada. Para campanhas baseadas em ação com postergação, há uma opção para reavaliar os critérios do segmento no momento do envio para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada. 

### Por que há uma diferença entre o número de destinatários únicos e o número de envios para uma determinada campanha ou canva?

Uma possível explicação pode ser que a campanha ou Canvas tenha a re-eligibilidade ativada, o que significa que usuários que se qualificam para o segmento e configurações de entrega poderão receber a mensagem mais de uma vez. Se a re-eligibilidade não estiver ativada, a provável explicação para a diferença entre envios e destinatários únicos pode ser devido a usuários com vários dispositivos, em diferentes plataformas, associados aos seus perfis. 

Por exemplo, se você tiver uma canva que tenha notificações push para iOS e web, um determinado usuário com dispositivos móveis e de desktop pode receber mais de uma mensagem.

### Por que o número de conversões pode exceder o número de usuários únicos em campanhas multicanal?

Para campanhas multicanal, a Braze conta conversões por canal, não por usuário. Quando um usuário realiza uma única ação de conversão dentro da janela de conversão, a Braze atribui essa conversão a cada canal do qual o usuário recebeu uma mensagem. Isso significa que se um usuário recebe mensagens em múltiplos canais (por exemplo, tanto e-mail quanto push) e converte, a Braze conta múltiplas conversões, uma para cada canal. Como resultado, a contagem total de conversões pode exceder o número de usuários únicos que converteram.

Por exemplo, se uma campanha multicanal envia tanto um e-mail quanto uma notificação por push para um usuário, e esse usuário realiza uma ação de conversão após receber ambas as mensagens e dentro da janela de conversão, a Braze conta isso como duas conversões, uma atribuída ao e-mail e uma atribuída ao push, mesmo que seja uma única ação do mesmo usuário.

### Por que minha campanha tem uma base de usuários alcançável menor do que o segmento que estou usando para a campanha?

Se você tiver um [grupo de controle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) configurado, isso impedirá que uma porcentagem do seu público alcançável receba campanhas. Isso significa que o número de usuários alcançáveis para o seu segmento pode às vezes ser maior do que o número de usuários alcançáveis para a sua campanha, mesmo que a campanha esteja usando esse mesmo segmento.

### O que a entrega no fuso local oferece?

A entrega no fuso local permite que você entregue campanhas de envio de mensagens para um segmento com base no fuso horário individual de um usuário. Sem entrega de fuso local, as campanhas serão agendadas com base nas configurações de fuso horário da sua empresa no Braze. 

Por exemplo, uma empresa com sede em Londres que envia uma campanha às 12h atingirá usuários na costa oeste da América às 4h. Se seu app estiver disponível apenas em certos países, isso pode não ser um risco para você. Caso contrário, recomendamos fortemente evitar enviar notificações por push de manhã cedo para sua base de usuários.

### Como o Braze reconhece o fuso horário de um usuário?

Braze determinará automaticamente o fuso horário de um usuário a partir de seu dispositivo. Isso garante a precisão do fuso horário e a cobertura total de seus usuários. Os usuários criados através da API de Usuário ou de outra forma sem um fuso horário terão o fuso horário da sua empresa como seu fuso horário padrão até serem reconhecidos em seu app pelo SDK. 

Você pode verificar o fuso horário da sua empresa nas [configurações da empresa]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) no dashboard.

### Quando o Braze avalia os usuários para a entrega no fuso local?

A Braze avalia os usuários para sua elegibilidade de entrada em:

- Horário de Samoa (UTC+13) ou UTC+14 durante o Horário de Verão
- O horário local do dia agendado

Para que um usuário seja elegível para entrada, ele deve ser elegível para ambas as verificações. Por exemplo, se um canva estiver programado para ser lançado em 7 de agosto de 2021 às 14h no fuso local, então direcionar um usuário localizado em Nova York exigiria as seguintes verificações de elegibilidade:

- Nova Iorque em 6 de agosto de 2021 às 21h
- Nova Iorque em 7 de agosto de 2021 às 14h

O usuário deve estar no segmento por 24 horas antes do lançamento. Se o usuário não for elegível na primeira verificação, então a Braze não tenta a segunda verificação.

Por exemplo, se uma campanha está programada para ser entregue às 19h UTC, começamos a enfileirar os envios da campanha assim que um fuso horário é identificado (como Samoa). Isso significa que estamos nos preparando para enviar a mensagem, não enviando a campanha. Se os usuários não corresponderem a nenhum filtro quando verificamos a elegibilidade, eles não farão parte do público-alvo.

Como outro exemplo, digamos que você queira criar duas campanhas agendadas para serem enviadas no mesmo dia—uma de manhã e outra à noite—e adicionar um filtro para que os usuários só possam receber a segunda campanha se já tiverem recebido a primeira. Com a entrega no fuso local, alguns usuários podem não receber a segunda campanha. Isso ocorre porque verificamos a elegibilidade quando o fuso horário do usuário é identificado, então, se o horário agendado ainda não ocorreu em seu fuso horário, eles não receberam a primeira campanha, o que significa que não serão elegíveis para a segunda campanha.

### Como faço para agendar uma campanha no fuso local?

Ao agendar uma campanha, escolha enviá-la em um horário designado e, em seguida, selecione **Enviar campanha para usuários em seu fuso horário local**.

A Braze recomenda fortemente que todas as campanhas em fuso horário local sejam agendadas com 24 horas de antecedência. Como tal campanha precisa ser enviada ao longo de um dia inteiro, agendá-la com 24 horas de antecedência garante que sua mensagem alcançará todo o seu segmento. No entanto, você pode agendar essas campanhas com menos de 24 horas de antecedência, se necessário. Tenha em mente que a Braze não enviará mensagens para nenhum usuário que tenha perdido o horário de envio por mais de 1 hora. 

Por exemplo, se for 13h e você agendar uma campanha de fuso local para as 15h, a campanha será enviada imediatamente para todos os usuários cujo fuso local seja das 15h às 16h, mas não para os usuários cujo fuso local seja 17h. Além disso, o horário de envio que você escolher para sua campanha ainda não deve ter ocorrido no fuso horário da sua empresa.

Editar uma campanha de fuso local que está programada para menos de 24 horas de antecedência não alterará o cronograma da mensagem. Se você decidir editar uma campanha de fuso local para enviar em um horário posterior (por exemplo, 19h em vez de 18h), os usuários que estavam no segmento alvo quando o horário de envio original foi escolhido ainda receberão a mensagem no horário original (18h). Se você editar um fuso local para enviar em um horário anterior (por exemplo, 16h em vez de 17h), a campanha ainda será enviada a todos os membros do segmento no horário original (17h). 

{% alert note %}
Para componentes de canva, os usuários não precisam estar no componente por 24 horas para receber o próximo componente na jornada do usuário para entrega no fuso local.
{% endalert %}

Se você permitiu que os usuários se tornassem re-elegíveis para a campanha, eles a receberão novamente no horário original (17h). Para todas as ocorrências subsequentes de sua campanha, no entanto, suas mensagens são enviadas apenas no seu horário atualizado.

### Quando as alterações nas campanhas de fuso local entram em vigor?

Os segmentos-alvo para campanhas de fuso local devem incluir pelo menos uma janela de 48 horas para quaisquer filtros baseados em tempo para garantir a entrega a todo o segmento. Por exemplo, considere um segmento direcionando usuários no seu segundo dia com os seguintes filtros:

- Usou o app pela primeira vez há mais de 1 dia
- Primeiro uso do app há menos de 2 dias

A entrega no fuso local pode não alcançar os usuários deste segmento com base no horário de entrega e no fuso local dos usuários. Isso ocorre porque um usuário pode deixar o segmento no momento em que seu fuso horário aciona a entrega.

### Quais mudanças posso fazer nas campanhas agendadas antes do lançamento?

Quando a campanha é agendada, você deve fazer edições em qualquer coisa além da composição da mensagem antes que coloquemos as mensagens na fila para envio. Como em todas as campanhas, você não pode editar eventos de conversão após o lançamento.

### Atualizei minha campanha agendada. Por que não lançou?

Isso pode acontecer quando uma campanha está programada para ser lançada exatamente no momento em que foi atualizada. Por exemplo, se atualmente são 15:10 e você mudou a campanha para ser lançada às 15:10 e selecionou **Atualizar campanha**, agora já passou das 15:10, o que significa que o horário agendado para o lançamento já passou. Em vez de agendar a campanha para o mesmo horário, selecione **Enviar assim que a campanha for lançada**.

### Qual é a "zona segura" antes que as mensagens em uma campanha agendada sejam enfileiradas?

Recomendamos fazer alterações nas mensagens dentro dos seguintes horários:

- **Campanhas agendadas únicas:** Edite até o horário de envio agendado.
- **Campanhas programadas recorrentes:** Edite até o horário de envio agendado.
- **Campanhas de fuso local:** Edite até 24 horas antes do horário de envio agendado.
- **Campanhas com tempo de envio ideal:** Edite até 24 horas antes do dia em que a campanha está agendada para ser enviada.

Se você fizer alterações em sua mensagem fora dessas recomendações, pode não ver as atualizações refletidas na mensagem enviada. Por exemplo, se você editar o horário de envio três horas antes de uma campanha estar agendada para ser enviada às 12h no horário local, o seguinte pode ocorrer:

- A Braze não envia mensagens para nenhum usuário que tenha perdido o horário de envio por mais de uma hora.
- Mensagens pré-enfileiradas ainda podem ser enviadas no horário originalmente enfileirado, em vez do horário ajustado.

Se você precisar fazer alterações, recomendamos parar a campanha atual (isso cancela qualquer mensagem enfileirada). Você pode então duplicar a campanha, fazer as alterações necessárias e lançar a nova campanha. Você pode precisar excluir usuários desta campanha que já receberam a primeira campanha. Reajuste os horários da campanha para permitir o envio no fuso horário.

### Por que nenhum usuário entrou na minha campanha programada diariamente no dia da mudança para o horário de verão?

Nos dias de transição para o horário de verão (DST), campanhas programadas diariamente podem ser executadas até uma hora mais cedo ou mais tarde do que o habitual, dependendo de os relógios adiantarem ou atrasarem. Se seu segmento depender de atributos personalizados ou eventos com timestamps que caem dentro de uma hora do horário programado de envio, esses usuários podem não se qualificar quando a campanha avalia a elegibilidade no dia do DST.

Por exemplo, suponha que os usuários normalmente recebam uma atualização de atributo personalizado às 15h UTC, e sua campanha é executada diariamente às 10h30 em Nova York (Horário da Costa Leste). Enquanto Nova York estiver no horário padrão (UTC-5), 10h30 ET corresponde a 15h30 UTC, então a campanha é executada após o atributo ser registrado. Quando Nova York muda para o horário de verão (UTC-4), 10h30 ET corresponde a 14h30 UTC, então no dia da mudança para o horário de verão a campanha pode ser executada antes da atualização do atributo às 15h UTC. Como o atributo qualificável ainda não existe, esses usuários são filtrados. Se a requalificação estiver desativada, usuários que entraram em dias anteriores não podem reentrar, resultando em zero entradas para aquele dia.

Para evitar isso, certifique-se de que suas atualizações de atributo personalizado ou evento ocorram mais de uma hora antes do horário programado de envio da campanha.

### Por que o número de usuários que entram em uma campanha não corresponde ao número esperado?

O número de usuários que entram em uma campanha pode diferir do seu número esperado por causa de como as audiências e os gatilhos são avaliados. Na Braze, um público é avaliado antes do disparador (a menos que esteja usando um disparador de [alteração de atribuição]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). Isso fará com que os usuários saiam da campanha se não forem inicialmente parte do seu público selecionado antes que quaisquer ações de disparo sejam avaliadas.

{% alert tip %}
Para mais assistência com a solução de problemas da campanha, entre em contato com o suporte da Braze dentro de 30 dias após a ocorrência do seu problema, pois temos apenas os últimos 30 dias de logs de diagnóstico.
{% endalert %}

### Qual é a diferença entre as opções CSV Export User Data e CSV Export Email Address na minha página de análise de campanha?

Selecionar a opção **CSV Export Email Addresses** baixa dados apenas para usuários com endereços de e-mail. Por exemplo, se você tiver um segmento de 100.000 usuários, mas apenas 50.000 desses usuários tiverem endereços de e-mail, e você clicar em **CSV Export Email Addresses**, a exportação conterá apenas 50.000 linhas de dados. Em comparação, selecionar **CSV Export User Data** exporta todos os dados dos usuários.

### Posso procurar uma campanha pelo seu identificador de API?

Sim, use o filtro `api_id:YOUR_API_ID` na página **Campanhas** para procurar uma campanha pelo seu identificador API. Consulte [procurando por campanhas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/) para saber mais.

### Por que o espaço em branco aparece de forma diferente em campos de entrada em comparação com o texto exibido? 

O tratamento de espaços em branco difere entre campos de entrada e componentes de texto exibido devido ao estilo CSS. Nos componentes de texto com o CSS padrão `white-space: normal`, múltiplos espaços consecutivos se colapsam em um único espaço quando exibidos. Esse é o comportamento padrão do HTML para texto renderizado. 

Os campos de entrada preservam múltiplos espaços exatamente como você os insere, porque você precisa ver e editar o espaçamento exato para uma entrada de dados precisa. Isso significa que o texto com múltiplos espaços pode aparecer de forma diferente quando visualizado em um campo de entrada (onde todos os espaços são preservados) em comparação com quando exibido em outras partes do dashboard (onde o CSS pode colapsar múltiplos espaços). 

Por exemplo, se você inserir um nome de campanha ou parâmetro UTM com múltiplos espaços em um campo de entrada, você verá todos os espaços preservados. No entanto, quando esse mesmo texto aparece nos resultados de busca, listas de campanhas ou outros componentes de texto, múltiplos espaços podem aparecer como um único espaço devido ao tratamento de espaços em branco do CSS. 

### Qual é a diferença entre campanhas de API e campanhas acionadas por API?

Campanhas acionadas por API permitem que você gerencie o texto da campanha, testes multivariantes e regras de reeligibilidade dentro do dashboard da Braze enquanto aciona a entrega desse conteúdo a partir de seus próprios servidores e sistemas. Essas mensagens também podem incluir dados adicionais a serem modelados nas mensagens em tempo real.

Campanhas de API são usadas para rastrear as mensagens enviadas usando a API. Ao contrário da maioria das campanhas, você não especifica a mensagem, os destinatários ou o cronograma, mas sim passa os identificadores em suas chamadas de API. 

### Qual é a diferença entre campanhas baseadas em ação e campanhas acionadas por API?

<style>
table th:nth-child(1) {
    width: 50%;
}
table th:nth-child(3) {
    width: 50%;
}
</style>

#### Baseado em ação

Campanhas de entrega baseada em ação ou campanhas disparadas por eventos são muito eficazes para mensagens transacionais ou baseadas em conquistas e permitem que você as dispare para enviar após um usuário completar um determinado evento. 

| Prós | Cons | 
| ---- | ---- |
| • Visibilidade das cargas úteis JSON recebidas na plataforma (se o evento for acionado por usuário teste) via o **Registro de Atividade de Mensagens**<br><br>• Elementos de personalização estão incluídos nas propriedades do evento personalizado<br><br>• Evento personalizado pode ser usado para criar Segmentos de usuários elegíveis para a mensagem | • Consome pontos de dados |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

#### Disparadas pela API

Campanhas acionadas por API e campanhas acionadas por servidor são ideais para lidar com transações mais avançadas, permitindo que você acione a entrega do conteúdo da campanha a partir de seus próprios servidores e sistemas. A solicitação da API para acionar a mensagem também pode incluir dados adicionais a serem modelados na mensagem em tempo real.

| Benefícios | Considerações | 
| ---- | ---- |
| • Não registra pontos de dados<br><br>• Elementos de personalização estão incluídos nas propriedades da carga útil JSON | • Não permite que você crie um segmento de usuários elegíveis para a mensagem nas propriedades da carga útil JSON<br><br>• Não é possível ver os payloads JSON recebidos com o **Registro de Atividade da Mensagem**|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

