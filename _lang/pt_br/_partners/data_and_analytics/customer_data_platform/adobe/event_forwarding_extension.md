---
nav_title: Extensão de encaminhamento de eventos
article_title: Adobe
description: "Este artigo de referência aborda a extensão de encaminhamento de eventos do Braze que permite que você aproveite os dados capturados na Adobe Experience Platform Edge Network e os envie para o Braze na forma de eventos do lado do servidor."
page_type: partner
page_order: 2
search_tag: Partner

---

# Extensão de encaminhamento de eventos da API de rastreamento de eventos

> A extensão de [encaminhamento de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en) da API de eventos de monitoramento da Braze permite aproveitar os dados capturados na Adobe Experience Platform Edge Network e os enviar para a Braze na forma de eventos do lado do servidor usando a API [`/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).

Este documento aborda os casos de uso da extensão, como instalá-la em suas bibliotecas de encaminhamento de eventos e como empregar seus recursos em uma [regra](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de encaminhamento de eventos.

{% alert note %}
O envio de atributos à Braze pode aumentar o consumo de pontos de dados da Braze. Consulte seu gerente de conta Braze antes de enviar atribuições. Consulte a documentação da Braze sobre [pontos de dados faturáveis]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points/#billable-data-points) para saber mais.
{% endalert %}

## Casos de uso

Essa extensão deve usar dados da Edge Network no Braze para aproveitar seus recursos de análise de clientes e direcionamento.

Por exemplo, considere uma organização de varejo com presença multicanal (site e celular) e que captura entradas transacionais ou de conversação como dados de eventos de seu site e plataformas móveis. 

Usando várias regras de [tag](https://experienceleague.adobe.com/docs/experience-platform/tags/home.html?lang=en), esses dados são enviados para a Edge Network em tempo real. A partir daí, a extensão de encaminhamento de eventos do Braze envia automaticamente os eventos relevantes para o Braze do lado do servidor.

## Limites de frequência

| API | Limites de frequência |
| --- | --- |
| Rastreamento do usuário | 50.000 solicitações por minuto.<br><br>Consulte a [documentação da API de rastreamento de usuários]({{site.baseurl}}/api/endpoints/user_data/post_user_track#rate-limit) para obter detalhes.
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Reunir os detalhes de configuração necessários

Para conectar a Edge Network à Braze, são necessários os seguintes itens:

| Tipo de chave | Descrição |
| --- | --- |
| Instâncias da Braze | Sua instância do Braze pode ser obtida com seu gerente de integração do Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics/#endpoints). |
| chave da API REST Braze | Uma chave da API REST do Braze com todas as permissões. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

### Etapa 2: Criar um segredo

Crie um novo [segredo de encaminhamento de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/secrets.html?lang=en) e defina o valor como sua [chave de API do Braze](https://experienceleague.adobe.com/docs/experience-platform/tags/extensions/server/braze/overview.html?lang=en#configuration-details). Isso será usado para autenticar a conexão com sua conta e, ao mesmo tempo, manter o valor seguro.

### Etapa 3: Instalar e configurar a extensão Braze

1. Para instalar a extensão, [crie uma propriedade de encaminhamento de eventos](https://experienceleague.adobe.com/docs/experience-platform/tags/event-forwarding/overview.html?lang=en#properties) ou escolha uma propriedade existente para editar.
2. Em seguida, selecione **Extensions** (Extensões) na navegação à esquerda. Na guia **Catalog** (Catálogo ), selecione **Install** (Instalar) no cartão para a extensão Braze.
3. Na próxima tela, insira sua instância REST e a chave de API e selecione **Save** (Salvar) quando terminar.

### Etapa 4: Criar uma regra de evento de envio

Depois de instalar a extensão, crie uma nova [regra](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de encaminhamento de eventos e configure suas condições conforme desejado. Ao configurar as ações para a regra, selecione a extensão **Braze** e, em seguida, selecione **Send Event (Enviar evento)** para o tipo de ação.

![]({% image_buster /assets/img/efe.png %})

{% tabs local %}
{% tab Identificação do usuário %}

| Entrada | Descrição |
| --- | --- |
| ID de usuário externo | Um UUID ou GUID longo, aleatório e bem distribuído. Se você escolher um método diferente para nomear seus IDs de usuário, eles também deverão ser longos, aleatórios e bem distribuídos. Saiba mais sobre a [convenção de nomenclatura de ID de usuário sugerida]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| ID de usuário do Braze | Identificador de usuário do Braze. |
| Alias de usuário | Um alias serve como um identificador de usuário exclusivo alternativo. Use aliases para identificar usuários em dimensões diferentes da ID principal do usuário.<br><br>O objeto de alias de usuário consiste em duas partes: um `alias_name` para o próprio identificador e um `alias_label` indicando o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Para vincular o evento a um usuário, é necessário preencher o campo `External User ID`, o campo `Braze User Identifier` ou a seção `User Alias`.
{% endalert %}

{% endtab %}
{% tab Dados do evento %}

| Entrada | Descrição | Obrigatória |
| --- | --- | --- |
| Nome do evento | Nome do evento. | Sim |
| Hora do evento | Data-hora como string no formato ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Sim |
| Identificador do app | O identificador de aplicativo ou `app_id` é um parâmetro que associa a atividade a um app específico em seu espaço de trabalho. Ele designa com qual app dentro do espaço de trabalho você está interagindo. | Não |
| Propriedades do evento | Um objeto JSON que contém propriedades personalizadas do evento. | Não |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
A ação **Braze Send Event** requer apenas a especificação de um **Event Name (Nome do evento** ) e **Event Time (Hora do evento** ), mas você deve incluir o máximo de informações possível no campo de propriedades personalizadas. Consulte o [objeto de evento]({{site.baseurl}}/api/objects_filters/event_object/) para obter mais detalhes.
{% endalert %}

{% endtab %}
{% tab Atributo do usuário %}

As atribuições do usuário podem ser um objeto JSON que contém campos que criarão ou atualizarão um atributo com o nome e o valor fornecidos no perfil de usuário especificado. Há suporte para as seguintes propriedades:

| Atributo do usuário | Descrição |
| --- | --- |
| Nome | Nome do usuário. |
| Sobrenome | Sobrenome do usuário. |
| Telefone | Número de telefone do usuário. |
| E-mail | Endereço de e-mail do usuário. |
| Gênero | Uma das seguintes strings: "M", "F", "O" (outro), "N" (não aplicável), "P" (prefiro não dizer). |
| Cidade | A cidade do usuário. |
| País | O país do usuário como uma string no formato [ISO-3166-1 alfa-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Idioma | O idioma do usuário como uma string no formato [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Data de nascimento | Os dados de nascimento dos usuários em string no formato "YYYY-MM-DD" (por exemplo, 1980-12-21). |
| Fuso horário | Nome do fuso horário do [banco de dados de fuso horário da IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por exemplo, "America/New_York" ou "Eastern Time (US & Canada)"). |
| Facebook | Um hash contendo qualquer um dos seguintes itens: `id` (string), `likes` (vetor de strings), `num_friends` (inteiro). |
| X (antigo Twitter) | Hash contendo qualquer um dos seguintes itens: id (número inteiro), `screen_name` (string, identificador do X (antigo Twitter)), `followers_count` (número inteiro), `friends_count` (número inteiro), `statuses_count`(número inteiro). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Todas as atribuições adicionadas na configuração serão enviadas toda vez que o evento for enviado ao Braze, independentemente de o valor do atributo ter sido alterado. Ao configurar os dados de usuários, informe-se sobre como isso afetará o consumo de pontos de dados.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 5: Criar uma regra de evento de envio de compra

Depois de instalar a extensão, crie uma nova [regra](https://experienceleague.adobe.com/docs/experience-platform/tags/ui/rules.html?lang=en) de encaminhamento de eventos e configure suas condições conforme desejado. Ao configurar as ações para a regra, selecione a extensão **Braze** e, em seguida, selecione **Send Purchase Event (Enviar evento de compra** ) para o tipo de ação.

![]({% image_buster /assets/img/efe2.png %})

{% tabs local %}
{% tab Identificação do usuário %}

| Entrada | Descrição |
| --- | --- |
| ID de usuário externo | Um UUID ou GUID longo, aleatório e bem distribuído. Se você escolher um método diferente para nomear seus IDs de usuário, eles também deverão ser longos, aleatórios e bem distribuídos. Saiba mais sobre a [convenção de nomenclatura de ID de usuário sugerida]({{site.baseurl}}/developer_guide/platform_integration_guides/web/analytics/setting_user_ids#suggested-user-id-naming-convention). |
| ID de usuário do Braze | Identificador de usuário do Braze. |
| Alias de usuário | Um alias serve como um identificador de usuário exclusivo alternativo. Use aliases para identificar usuários em dimensões diferentes da ID principal do usuário.<br><br>O objeto de alias de usuário consiste em duas partes: um `alias_name` para o próprio identificador e um `alias_label` indicando o tipo de alias. Os usuários podem ter vários aliases com rótulos diferentes, mas apenas um `alias_name` por `alias_label`. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Para vincular o evento a um usuário, é necessário preencher o campo `External User ID`, o campo `Braze User Identifier` ou a seção `User Alias`.
{% endalert %}

{% endtab %}
{% tab Dados de compra %}

| Entrada | Descrição | Obrigatória |
| --- | --- | --- |
| ID do produto | Identificador da compra. (por exemplo, nome do produto ou categoria do produto) | Sim |
| Tempo de compra | Data-hora como string no formato ISO 8601 ou no formato `yyyy-MM-dd'T'HH:mm:ss:SSSZ`. | Sim |
| Moeda | Moeda como uma string no formato de código de moeda alfabético [ISO 4217](https://en.wikipedia.org/wiki/ISO_4217). | Sim |
| Preço | O preço do objeto. | Sim |
| Quantidade | A quantidade comprada. Se não for fornecida, o valor padrão será 1. O valor máximo deve ser inferior a 100. | Não |
| Identificador do app | O identificador de aplicativo ou `app_id` é um parâmetro que associa a atividade a um app específico em seu espaço de trabalho. Ele designa com qual app dentro do espaço de trabalho você está interagindo. | Não |
| Propriedades de compra | Um objeto JSON que contém propriedades personalizadas da compra. | Não |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

{% alert note %}
A ação **Enviar evento de compra** requer apenas a especificação de `Product ID`, `Purchase Time`, `Currency` e `Price`, mas você deve incluir o máximo de informações possível no campo de propriedades de compra. Consulte o [objeto de compra]({{site.baseurl}}/api/objects_filters/purchase_object/) para obter mais detalhes.
{% endalert %}

{% endtab %}
{% tab Atribuições do usuário %}

Você pode escolher se deseja enviar atribuições com cada evento na exibição de configuração.

As atribuições do usuário podem ser um objeto JSON que contém campos que criarão ou atualizarão um atributo com o nome e o valor fornecidos no perfil de usuário especificado. Há suporte para as seguintes propriedades:

| Atributo do usuário | Descrição |
| --- | --- |
| Nome | Nome do usuário. |
| Sobrenome | Sobrenome do usuário. |
| Telefone | Número de telefone do usuário. |
| E-mail | Endereço de e-mail do usuário. |
| Gênero | Uma das seguintes strings: "M", "F", "O" (outro), "N" (não aplicável), "P" (prefiro não dizer). |
| Cidade | A cidade do usuário. |
| País | O país do usuário como uma string no formato [ISO-3166-1 alfa-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2). |
| Idioma | O idioma do usuário como uma string no formato [ISO-639-1](https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes). |
| Data de nascimento | Os dados de nascimento dos usuários em string no formato "YYYY-MM-DD" (por exemplo, 1980-12-21). |
| Fuso horário | Nome do fuso horário do [banco de dados de fuso horário da IANA](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) (por exemplo, "America/New_York" ou "Eastern Time (US & Canada)"). |
| Facebook | Um hash contendo qualquer um dos seguintes itens: `id` (string), `likes` (vetor de strings), `num_friends` (inteiro). |
| X (antigo Twitter) | Hash contendo qualquer um dos seguintes itens: id (número inteiro), `screen_name` (string, identificador do X (antigo Twitter)), `followers_count` (número inteiro), `friends_count` (número inteiro), `statuses_count`(número inteiro). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert note %}
Todas as atribuições adicionadas na configuração serão enviadas toda vez que o evento for enviado ao Braze, independentemente de o valor do atributo ter sido alterado. Ao configurar os dados de usuários, informe-se sobre como isso afetará o consumo de pontos de dados.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 6: Validar dados no Braze

Se a coleta de eventos e a integração com a Adobe Experience Platform forem bem-sucedidas, você verá os eventos no console da Braze ao [visualizar os perfis de usuário]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/). Especificamente, os novos dados de eventos enviados ao Braze são refletidos na seção **Purchases (Compras** ) ou **Custom Events (Eventos personalizados** ) da [guia de visão geral]({{site.baseurl}}/user_guide/engagement_tools/segments/user_profiles/#overview-tab) de um determinado usuário.

