---
nav_title: Perguntas frequentes
article_title: Perguntas frequentes sobre Currents
page_order: 9
page_type: reference
description: "Este artigo aborda algumas das perguntas mais frequentes que surgem ao configurar o Braze Currents."
tool: Currents
---

# Perguntas frequentes

> Esta página fornece respostas a algumas perguntas frequentes sobre o Currents.

### Como faço para obter dados históricos?

O Currents é um fluxo de dados ao vivo e em tempo real, o que significa que os eventos não podem ser reproduzidos. No entanto, é possível armazenar os dados do Currents em um data warehouse, como o [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/) ou o [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/), para que você possa agir com base em eventos passados conforme achar necessário. Os dados são retidos por 30 dias, mas para obter mais dados históricos, você pode consultar o [Snowflake]({{site.baseurl}}/user_guide/data/braze_currents/s3_to_snowflake/).

### Por que o Currents gera dados no formato Avro, e não em JSON?

O Avro, ao contrário do JSON sem esquema, suporta nativamente a evolução do esquema. Você também se beneficiará da capacidade de enviar arquivos Avro com menos largura de banda e economizar espaço de armazenamento, pois o Avro é altamente compactável.

### Como a Braze lida com a sobrecarga de arquivos?

Criamos um processo de extração, transformação e carga (ETL), que permite extrair grandes quantidades de dados de um banco de dados para colocá-los e armazená-los em outro.

### Onde devo armazenar esses dados para consulta?

A Braze tem parceria com vários data warehouses nos quais você pode armazenar seus dados para consulta. Recomendamos o uso de:
- [Amazon S3]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/amazon_s3/)
- [Microsoft Azure Blob Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents/)
- [Google Cloud Storage]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/google_cloud_storage_for_currents/).

### Qual é a confiabilidade dos dados do Currents?

O Currents garante a entrega "pelo menos uma vez" (at-least-once), o que significa que eventos duplicados podem ser gravados ocasionalmente no seu bucket de armazenamento. Se o seu caso de uso exigir entrega exatamente uma vez, você pode deduplicar eventos usando o campo de identificador único (`id`) enviado com cada evento. Para mais informações, consulte [Semântica de entrega de eventos]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/).

### Com que frequência os dados são sincronizados com o Currents?

Os dados são transmitidos continuamente. A Braze envia um lote de eventos sempre que há um lote completo para enviar, ou a cada 5 minutos, o que ocorrer primeiro. Para conectores de alto volume, os dados chegam quase em tempo real. Para conectores de baixo volume, espere que os dados cheguem entre 5 e 30 minutos. Para mais informações, consulte [Limite de gravação Avro]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/#avro-write-threshold).

{% alert note %}
Se um dispositivo não estiver conectado à internet, pode haver um atraso na criação do evento. Isso é mais comum para eventos de mensagens no app, já que mensagens no app podem ser disparadas offline.
{% endalert %}

### Como descubro quais eventos estão disponíveis para o Currents?

Para uma lista completa dos eventos que o Currents registra, consulte os glossários de [Eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/customer_behavior_events/) e [Eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/message_engagement_events/). Você pode filtrar esses glossários por tipo de evento (como envios, entregas ou aberturas).

### Todos os eventos de envio são registrados no Currents?

Todos os eventos são registrados no Currents. Não há cenários em que um evento seria intencionalmente suprimido do fluxo do Currents.

### Os dados podem ser corrompidos no Currents?

Em circunstâncias normais, os dados do Currents não são corrompidos. Embora sempre exista a possibilidade de um problema raro, não há condições conhecidas em que os dados seriam sistematicamente corrompidos.

### Por que vejo dados de eventos personalizados com datas anteriores à configuração da minha integração com o Currents?

A Braze não preenche retroativamente eventos no Currents. No entanto, eventos personalizados podem ser registrados com um timestamp passado (por exemplo, se um dispositivo estava offline quando o evento ocorreu e sincronizou depois). Nesses casos, o timestamp do evento reflete quando o evento ocorreu originalmente, o que pode ser antes da configuração da integração com o Currents.

### Posso incluir atributos personalizados nos eventos de envio do Currents?

Não. O Currents não inclui atributos personalizados nos eventos de envio. O Currents registra eventos personalizados e eventos de engajamento com mensagem. Para uma lista completa dos campos disponíveis, consulte os [glossários de eventos]({{site.baseurl}}/user_guide/data/braze_currents/event_glossary/).

### O Currents inclui tags de campanha ou pares chave-valor?

Não. O Currents não inclui tags de campanha ou pares chave-valor no nível da mensagem. Como alternativa, você pode usar um canal de webhook na campanha para enviar essas informações ao seu próprio endpoint, usando [Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid/) para modelar os dados de tags e pares chave-valor.

### Como a Braze notifica os clientes sobre mudanças no Currents?

Quando ocorrem mudanças no Currents (como novos campos de evento ou tipos de evento), a Braze envia um e-mail para todos os clientes com integrações ativas do Currents que usaram o dashboard nos últimos 30 dias. Você também pode consultar o [changelog do Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/currents_changelogs) para ver as últimas alterações.

### Quanto armazenamento eu preciso para os dados do Currents?

Os requisitos de armazenamento dependem do volume de eventos e dos tipos de eventos que você está exportando. A Braze fornece [exemplos de eventos no formato Avro](https://github.com/braze-inc/currents-examples/tree/master/sample-data) que você pode usar para estimar o tamanho dos arquivos para o seu caso de uso.

### Por que o nome da campanha ou o nome da etapa do canva está `NULL` nos meus dados do Currents?

Quando você cria uma nova campanha ou Canvas, o nome pode levar algum tempo para se propagar por todos os sistemas da Braze. Eventos enviados pelo Currents durante esse intervalo podem ter `NULL` nos campos de nome (como `campaign_name` ou `canvas_step_name`). Isso também é esperado se o nome foi modificado pouco antes dos eventos serem registrados. Para evitar isso, aguarde algum tempo após criar ou renomear uma campanha ou etapa do canva antes de enviar.

### O que acontece se meu bucket de armazenamento estiver indisponível quando o Currents tentar gravar dados?

Se o seu bucket de armazenamento estiver indisponível no momento da transferência de dados, esses dados serão perdidos. A Braze não consegue preencher retroativamente eventos que não foram entregues com sucesso. Para evitar perda de dados, certifique-se de que seu bucket de armazenamento esteja disponível e configurado corretamente o tempo todo.

### Com que frequência o ID do esquema é atualizado?

Os IDs de esquema são globais para todos os tipos de evento e incrementam sequencialmente. As atualizações podem ocorrer a qualquer momento, e a Braze notificará os clientes por e-mail sobre mudanças futuras. Cada vez que uma atualização de esquema ocorre para qualquer tipo de evento, o próximo ID global disponível é atribuído. Recomendamos ler os arquivos recursivamente a partir do caminho raiz para lidar com mudanças de ID de esquema. Para mais informações, consulte [Mudanças no esquema Avro]({{site.baseurl}}/user_guide/data/braze_currents/event_delivery_semantics/#avro-schema-changes).