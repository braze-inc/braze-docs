---
nav_title: Perguntas frequentes
article_title: ""
page_order: 10
page_type: FAQ
description: "Esta página fornece respostas às perguntas frequentes sobre campanhas."
tool: Campaigns

---

# 

> Este artigo fornece respostas para algumas perguntas frequentes sobre campanhas.

### 

   

### Posso adicionar um grupo de controle à minha campanha multicanal?

Não, os grupos de controle em campanhas são destinados ao envio de mensagens de canal único, como e-mail A versus e-mail B. Como alternativa, tente usar [canva]({{site.baseurl}}/user_guide/engagement_tools/canvas) para testar diferentes canais, conteúdo de envio de mensagens e tempo de entrega. 

### Quais são algumas maneiras de começar a testar e otimizar campanhas?

Campanhas multivariantes e execução de canvas com várias variantes são uma ótima maneira de começar! Por exemplo, você pode executar uma [campanha multivariante]({{site.baseurl}}/user_guide/engagement_tools/testing/multivariant_testing/) para testar uma mensagem que possui diferentes cópias ou linhas de assunto. 

### Por que a taxa de abertura da minha campanha diminuiu?

As taxas de abertura baixas nem sempre estão correlacionadas a um problema técnico. Pode haver problemas com o recorte de e-mail, o que resulta em um pixel de rastreamento ausente. No entanto, também é possível que menos usuários estejam abrindo seus e-mails devido ao conteúdo ou mudanças no tamanho do público. 

### Como são avaliados os públicos da campanha?

Por padrão, as campanhas verificam os filtros de público no momento da entrada. Para campanhas baseadas em ação com postergação, há uma opção para reavaliar os critérios do segmento no momento do envio para garantir que os usuários ainda façam parte do público-alvo quando a mensagem for enviada. 

### Por que há uma diferença entre o número de destinatários únicos e o número de envios para uma determinada campanha ou canva?

Uma possível explicação para essa diferença pode ser devido à campanha ou canva ter a re-eligibilidade ativada. Ao ativar isso, os usuários que se qualificarem para o segmento e as configurações de entrega poderão receber a mensagem mais de uma vez. Se a re-eligibilidade não estiver ativada, a provável explicação para a diferença entre envios e destinatários únicos pode ser devido a usuários com vários dispositivos, em diferentes plataformas, associados aos seus perfis. 

Por exemplo, se você tiver uma canva que tenha notificações push para iOS e web, um determinado usuário com dispositivos móveis e de desktop pode receber mais de uma mensagem.

### Por que minha campanha tem uma base de usuários alcançável menor do que o segmento que estou usando para a campanha?

Se você tiver um [grupo de controle global]({{site.baseurl}}/user_guide/engagement_tools/testing/global_control_group/) configurado, isso impedirá que uma porcentagem do seu público alcançável receba campanhas. Isso significa que o número de usuários alcançáveis para o seu segmento pode às vezes ser maior do que o número de usuários alcançáveis para a sua campanha, mesmo que a campanha esteja usando esse mesmo segmento.

### O que a entrega no fuso local oferece?

A entrega no fuso local permite que você entregue campanhas de envio de mensagens para um segmento com base no fuso horário individual de um usuário. Sem entrega de fuso local, as campanhas serão agendadas com base nas configurações de fuso horário da sua empresa no Braze. 

Por exemplo, uma empresa com sede em Londres que envia uma campanha às 12h atingirá usuários na costa oeste da América às 4h. Se o seu app estiver disponível apenas em determinados países, isso pode não ser um risco para você, caso contrário, recomendamos fortemente evitar o envio de notificações por push de madrugada para sua base de usuários!

### Como o Braze reconhece o fuso horário de um usuário?

Braze determinará automaticamente o fuso horário de um usuário a partir de seu dispositivo. Isso garante a precisão do fuso horário e a cobertura total de seus usuários. Os usuários criados através da API de Usuário ou de outra forma sem um fuso horário terão o fuso horário da sua empresa como seu fuso horário padrão até serem reconhecidos em seu app pelo SDK. 

Você pode verificar o fuso horário da sua empresa nas [configurações da empresa]({{site.baseurl}}/user_guide/administrative/app_settings/company_settings/) no dashboard.

### Quando a Braze avalia os usuários para a entrega no fuso local?

Para entrega no fuso local, Braze avalia os usuários para sua elegibilidade de entrada durante essas duas instâncias:

- No horário de Samoa (UTC+13) do dia agendado
- No fuso local do dia agendado

Para que um usuário seja elegível para entrada, ele deve ser elegível para ambas as verificações. Por exemplo, se um canva estiver programado para ser lançado em 7 de agosto de 2021 às 14h no fuso local, então direcionar um usuário localizado em Nova York exigiria as seguintes verificações de elegibilidade:

- Nova Iorque em 6 de agosto de 2021 às 21h
- Nova York em 7 de agosto de 2021 às 14h

O usuário precisa estar no segmento por 24 horas antes do lançamento. Se o usuário não for elegível na primeira verificação, então a Braze não tentará a segunda verificação.

Por exemplo, se uma campanha está programada para ser entregue às 19h UTC, começamos a enfileirar os envios da campanha assim que um fuso horário é identificado (como Samoa).  

Como outro exemplo, digamos que você queira criar duas campanhas agendadas para serem enviadas no mesmo dia—uma de manhã e outra à noite—e adicionar um filtro para que os usuários só possam receber a segunda campanha se já tiverem recebido a primeira. Com a entrega no fuso local, alguns usuários podem não receber a segunda campanha. 

### Como faço para agendar uma campanha no fuso local?



A Braze recomenda fortemente que todas as campanhas no fuso local sejam agendadas com 24 horas de antecedência.  No entanto, você pode agendar essas campanhas com menos de 24 horas de antecedência, se necessário. Lembre-se de que a Braze não enviará mensagens para nenhum usuário que tenha perdido o horário de envio por mais de 1 hora. 

 Além disso, o horário de envio que você escolher para sua campanha ainda não deve ter ocorrido no fuso horário da sua empresa.

Editar uma campanha de fuso local que está programada para menos de 24 horas de antecedência não alterará o cronograma da mensagem. Se você decidir editar uma campanha de fuso local para enviar em um horário posterior (por exemplo, 19h em vez de 18h), os usuários que estavam no segmento alvo quando o horário de envio original foi escolhido ainda receberão a mensagem no horário original (18h). Se você editar um fuso local para enviar em um horário anterior (por exemplo, 16h em vez de 17h), a campanha ainda será enviada a todos os membros do segmento no horário original (17h). 

{% alert note %}
Para componentes de canva, os usuários não precisam estar no componente por 24 horas para receber o próximo componente na jornada do usuário para entrega no fuso local.
{% endalert %}

Se você permitiu que os usuários se tornassem re-elegíveis para a campanha, eles a receberão novamente no horário original (17h). 

### Quando as alterações nas campanhas de fuso local entram em vigor?

Os segmentos-alvo para campanhas de fuso local devem incluir pelo menos uma janela de 48 horas para quaisquer filtros baseados em tempo para garantir a entrega a todo o segmento. Por exemplo, considere um segmento direcionando usuários no seu segundo dia com os seguintes filtros:

- Usou o app pela primeira vez há mais de 1 dia
- Primeiro uso do app há menos de 2 dias

A entrega no fuso local pode não alcançar os usuários deste segmento com base no horário de entrega e no fuso local dos usuários. Isso ocorre porque um usuário pode deixar o segmento no momento em que seu fuso horário aciona a entrega.

### Quais mudanças posso fazer nas campanhas agendadas antes do lançamento?

Quando a campanha está agendada, edições em qualquer coisa além da composição da mensagem precisam ser feitas antes de colocarmos as mensagens na fila para envio. Como em todas as campanhas, você não pode editar eventos de conversão após o lançamento.

### Atualizei minha campanha agendada. Por que não lançou?

Isso pode acontecer quando uma campanha está programada para ser lançada exatamente no momento em que foi atualizada.  Em vez de agendar a campanha para o mesmo horário, selecione **Enviar assim que a campanha for lançada**.

### Qual é a "zona segura" antes que as mensagens em uma campanha agendada sejam enfileiradas?

Você pode fazer alterações com segurança nas mensagens dentro das seguintes zonas seguras:

- **Campanhas agendadas únicas** podem ser editadas até o horário de envio agendado.
- **Campanhas recorrentes agendadas** podem ser editadas até o horário de envio agendado.
- 
- 

### E se eu fizer uma edição no horário de envio dentro da "zona segura"?

Alterar o horário de envio das campanhas dentro desse período pode levar a um comportamento indesejado, por exemplo:

- A Braze não enviará mensagens para nenhum usuário que tenha perdido o horário de envio por mais de uma hora.
- Mensagens pré-enfileiradas ainda podem ser enviadas no horário originalmente enfileirado, em vez do horário ajustado.

### O que devo fazer se a "zona segura" já passou?

Para garantir que as campanhas operem conforme desejado, recomendamos parar a campanha atual (isso cancelará quaisquer mensagens enfileiradas).  Você pode precisar excluir usuários desta campanha que já receberam a primeira campanha.

Reajuste os horários da campanha para permitir o envio no fuso horário.

### Por que o número de usuários que entram em uma campanha não corresponde ao número esperado?

O número de usuários que entram em uma campanha pode diferir do seu número esperado por causa de como as audiências e os gatilhos são avaliados. Na Braze, um público é avaliado antes do disparador (a menos que esteja usando um disparador de [alteração de atribuição]({{site.baseurl}}/user_guide/engagement_tools/campaigns/building_campaigns/delivery_types/triggered_delivery/attribute_triggers/#change-custom-attribute-value)). 

{% alert tip %}

{% endalert %}

### Qual é a diferença entre as opções Exportar dados de usuários em CSV e Exportar endereço de e-mail em CSV na página de análise de dados da minha campanha?

Selecionar a opção **Exportar Endereços de E-mail em CSV** só vai baixar dados para usuários com endereços de e-mail. Por exemplo, se você tiver um segmento de 100.000 usuários, mas apenas 50.000 desses usuários tiverem endereços de e-mail, e você clicar em **Exportar Endereços de E-mail em CSV**, então você deve esperar ver apenas 50.000 linhas de dados no arquivo CSV. Em comparação, selecionar **Exportar dados de usuários em CSV** exportará todos os dados de usuários.

### Posso procurar uma campanha pelo seu identificador de API?

Sim, use o filtro `api_id:YOUR_API_ID` na página **Campanhas** para procurar uma campanha pelo seu identificador API. Consulte [procurando por campanhas]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns/) para saber mais.

### 

 

Campanhas de API são usadas para rastrear as mensagens que você envia usando a API.  

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

 

| Prós | Cons | 
| ---- | ---- |
| • Não consome pontos de dados<br><br>• Elementos de personalização estão incluídos nas propriedades da carga útil JSON | • Não permite que você crie um segmento de usuários elegíveis para a mensagem nas propriedades da carga útil JSON<br><br>|
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

