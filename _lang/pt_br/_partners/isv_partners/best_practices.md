---
nav_title: Práticas recomendadas
hidden: true
---

# Ciclo de vida do usuário e práticas recomendadas de identificadores

## Coleta de dados

Saiba mais sobre como o Braze coleta dados:
- [Coleta de dados do SDK]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/sdk_data_collection/)
- [Melhores práticas de coleta de dados]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/best_practices/)
- [Ciclo de vida do perfil do usuário]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_profile_lifecycle/)

## Identificadores de Braze

- `braze_id`: Um identificador atribuído pelo Braze que é imutável e associado a um usuário específico quando criado em nosso banco de dados.
- `external_id`: Um identificador atribuído pelo cliente, normalmente um UUID. Recomendamos que os clientes atribuam o endereço `external_id` quando o usuário puder ser identificado de forma exclusiva. Depois que um usuário é identificado, ele não pode ser revertido para anônimo.
- `user_alias`: Um identificador alternativo exclusivo que o cliente pode atribuir como um meio de fazer referência ao usuário por um ID antes de atribuir um `external_id`. Os aliases de usuário podem ser posteriormente mesclados com outros aliases ou com um `external_id` quando um estiver disponível por meio do endpoint [de identificação do usuário]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) do Braze.
    - No ponto de extremidade [User identify (Identificação do usuário]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/) ), o campo `merge_behavior` pode ser usado para especificar quais dados do perfil de alias de usuário devem persistir no perfil de usuário conhecido.
    - Observe que, para que o alias de usuário seja um perfil enviável, você ainda deve incluir e-mail e/ou telefone como atributo padrão no perfil.
- `device_id`: Um identificador específico do dispositivo, gerado automaticamente. Um perfil de usuário pode ter um número de `device_ids` associado a ele. Por exemplo, um usuário que tenha registrado sua conta no computador do trabalho, no computador de casa, no tablet e no app iOS teria 4 `device_ids` associados ao seu perfil.
- Endereço de e-mail e número de telefone:
    - Suportado como um identificador no ponto de extremidade do usuário de rastreamento da Braze. 
    - Ao usar o endereço de e-mail ou os números de telefone como identificador em uma solicitação, há três resultados possíveis:
        1. Se um usuário com esse e-mail/telefone não existir no Braze, será criado um perfil de usuário somente de e-mail/telefone e todos os dados da solicitação serão adicionados ao perfil.
        2. Se já existir um perfil com esse e-mail/telefone no Braze, ele será atualizado para incluir todos os dados enviados na solicitação.
        3. Em um caso de uso com mais de um perfil com esse e-mail/telefone, será priorizado o perfil atualizado mais recentemente.
    - Note que se existir um perfil de usuário somente de e-mail/telefone e, em seguida, for criado um perfil identificado com o mesmo e-mail/telefone (como outro perfil com o mesmo endereço de e-mail E uma ID externa), o Braze criará um segundo perfil. As atualizações subsequentes serão acessadas pelo perfil com a ID externa.
        - Os dois perfis podem ser mesclados usando o ponto de extremidade Braze [/merge/users]({{site.baseurl}}/api/endpoints/user_data/post_users_merge/) 

## Manipulação de usuários anônimos

Para um caso de uso em que você precisa criar ou atualizar um perfil de usuário no Braze sem ter acesso a um `external_id`, outro identificador, como um endereço de e-mail ou número de telefone, pode ser passado para o endpoint Braze [Export user by identifier]({{site.baseurl}}/api/endpoints/export/user_data/post_users_identifier/) para determinar se existe um perfil para o usuário no Braze. 

```json
{
 "email_address": "test@braze.com",
 "fields_to_export": ["braze_id", "user_aliases"]
}
```

Se existir um usuário no Braze com esse e-mail ou telefone, seu perfil será retornado. Caso contrário, será retornada uma matriz "users" vazia. A vantagem de usar o endpoint de exportação para determinar se já existe um usuário com esse endereço de e-mail é que isso permitirá determinar se algum perfil de usuário anônimo está associado ao usuário. Por exemplo, um perfil anônimo criado pelo SDK (que terá `braze_id`) ou um perfil de alias de usuário criado anteriormente. 

Se a solicitação não retornar um perfil de usuário, você poderá optar por criar um alias de usuário ou criar um usuário somente de e-mail:

### Alias de usuário

Use o ponto de extremidade de rastreamento de usuário para criar um alias de usuário, usando o identificador escolhido como o nome do alias. Ao incluir `_update_existing_only` como `false` no atributo, evento ou objeto de compra em que o novo alias de usuário é definido, é possível criar o perfil de alias e adicionar atributos, eventos e compras a esse perfil simultaneamente. 

Para que o alias de usuário seja um perfil que pode ser enviado, é necessário incluir o endereço de e-mail no campo `email`, conforme mostrado abaixo.

```json
{
   "attributes": [
   {
     "user_alias" : {
       "alias_name" : "test@braze.com",
       "alias_label" : "email"
     },
     "email": "test@braze.com",
     "_update_existing_only": false,
     "string_attribute": "sherman",
     "boolean_attribute_1": true,
     "integer_attribute": 25,
     "array_attribute": ["banana", "apple"]
   }
   ]
}
```

Posteriormente, você pode identificar e mesclar esse alias de usuário com um `external_id` quando um estiver disponível por meio do nosso endpoint [Identify users]({{site.baseurl}}/api/endpoints/user_data/post_user_identify/). 

### Criação de um usuário somente de e-mail

Use o endereço de e-mail como identificador no ponto de extremidade de rastreamento do usuário. 

```json
{
    "attributes": [
        {
            "email": "test@braze.com",
            "string_attribute": "fruit",
            "boolean_attribute_1": true,
            "integer_attribute": 25,
            "array_attribute": [
                "banana",
                "apple"
            ]
        }
    ]
}
```
{% alert important %}
Essa funcionalidade está atualmente em acesso antecipado.
{% endalert %}

## Sincronização de dados de perfis de usuários

[Rastreamento do usuário]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)
- É um endpoint acessível publicamente que pode criar e atualizar usuários no Braze, como registrar atributos no perfil do usuário. Esse endpoint tem um limite de frequência de 50.000 solicitações por minuto aplicado ao nível do espaço de trabalho.
- Ao usar esse endpoint, inclua a chave `partner` conforme mostrado na documentação do parceiro.

[Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/cloud_ingestion/overview/#what-is-cloud-data-ingestion)
- Semelhante ao endpoint de rastreamento do usuário, os dados podem ser sincronizados com os perfis de usuário por meio da ingestão de dados na nuvem. Ao usar essa ferramenta, atribuições, eventos e compras são registrados em perfis, configurando e conectando a tabela ou a visualização do data warehouse que você gostaria de sincronizar com o espaço de trabalho Braze desejado.

[Pontos de dados]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)
- O Braze tem um modelo de consumo de pontos de dados em que os pontos de dados são incorridos por "gravação" no perfil do usuário, independentemente de o valor ter sido alterado. Por esse motivo, recomendamos que apenas as atribuições que foram alteradas sejam enviadas à Braze. 

## Envio de públicos de usuários para o Braze

[Documentação do parceiro de sincronização de importação do coorte]({{site.baseurl}}/partners/isv_partners/cohort_import/)<br>
- Os públicos de usuários podem ser sincronizados com o Braze como um coorte usando os endpoints da API de importação de coorte do Braze. Em vez de esses públicos serem armazenados no perfil do usuário como atribuições do usuário, os clientes podem criar e direcionar esse coorte por meio de um filtro com a marca do parceiro em nossa ferramenta de segmentação. Isso pode tornar a localização e o direcionamento de um segmento específico de usuários mais fácil e simples para os clientes.
- Os pontos de extremidade de importação de coorte não são públicos e são específicos de cada parceiro. Por esse motivo, as sincronizações com os endpoints de coorte não serão contabilizadas nos limites de frequência do espaço de trabalho do cliente. 

[Rastreamento do usuário]({{site.baseurl}}/api/endpoints/user_data/post_user_track/)<br>
- Esse é um ponto de extremidade acessível ao público que pode ser usado imediatamente para criar usuários no Braze, denotando um usuário em um público específico por meio de uma atribuição de usuário. A principal diferença entre esse ponto de extremidade e o ponto de extremidade de importação de coorte é que os públicos enviados usando esse ponto de extremidade seriam armazenados no perfil do usuário, enquanto o ponto de extremidade de importação de coorte seria exibido como um preenchimento em nossa ferramenta de segmentação. Esse endpoint tem um limite de frequência de 50.000 solicitações por minuto aplicado ao nível do espaço de trabalho.
- Ao usar esse endpoint, verifique se você está incluindo a chave `partner`, conforme mostrado na [documentação do parceiro]({{site.baseurl}}/partners/isv_partners/api_partner).

[Pontos de dados]({{site.baseurl}}/user_guide/onboarding_with_braze/data_points#data-points)<br>
- O Braze tem um modelo de consumo de pontos de dados em que os pontos de dados são incorridos por "gravação" no perfil do usuário, independentemente de o valor ter sido alterado.
- Os pontos de dados são usados tanto pela importação de coorte quanto pelos endpoints de rastreamento do usuário.

## Análise de dados de engajamento transmitidos ao parceiro

### Currents

Currents é a ferramenta de análise de dados de engajamento com mensagens da Braze em tempo quase real. Isso enviará dados em nível de usuário sobre todos os envios, entregas, aberturas, cliques, etc., para campanhas e Canvas enviados do espaço de trabalho do cliente. Algumas coisas a serem notadas: Os preços do Currents são fixados por conector para o cliente, então todos os novos parceiros do Currents devem passar por um processo de acesso antecipado. Solicitamos que nossos parceiros tenham cinco clientes como parte do EA antes de criarmos a interface do usuário com marca personalizada e disponibilizarmos publicamente o conector. 
- [Documentação do parceiro]({{site.baseurl}}/partners/isv_partners/currents_integration/)
- [Eventos de engajamento com mensagens]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/message_engagement_events) \- todos os clientes que comprarem um conector Currents terão acesso a esses eventos.
- [Eventos de comportamento do usuário]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/event_glossary/customer_behavior_events) – nem todos os clientes que comprarem um conector do Current comprarão um conector "todos os eventos" que incluirá esses eventos. 

### Compartilhamento de dados do Snowflake

Os clientes que comprarem um conector Snowflake Data Share terão acesso automático aos eventos de engajamento com mensagens e de comportamento do usuário. Quando o Snowflake Data Share for usado como uma integração com parceiros, o Braze fornecerá um compartilhamento para a instância do Snowflake do parceiro em nome do cliente. Como observação, o compartilhamento de dados entre regiões tem um preço mais alto para nossos clientes, então pedimos que os parceiros que desejam se integrar ao Snowflake tenham uma conta em `US-EAST-1` e/ou `EU-CENTRAL-1`
- [Documentação do parceiro]({{site.baseurl}}/partners/isv_partners/currents_integration/)

## Criação e disparo de campanhas e Canvas

### Criação de ativos no Braze
O Braze oferece vários pontos de extremidade que permitem que clientes e parceiros criem/atualizem modelos de e-mail e blocos de conteúdo no espaço de trabalho do cliente. Esses modelos e blocos de conteúdo podem, por sua vez, ser usados nas campanhas e canvas da Braze do cliente.
- Modelos de e-mail
    - [Criar endpoint de modelo]({{site.baseurl}}/api/endpoints/templates/email_templates/post_create_email_template/)
    - [Atualizar o endpoint do modelo]({{site.baseurl}}/api/endpoints/templates/email_templates/post_update_email_template/#rate-limit)
- [Blocos de conteúdo]({{site.baseurl}}/user_guide/engagement_tools/templates_and_media/content_blocks#content-blocks) 
    - [Criar endpoint de bloco de conteúdo]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_create_email_content_block/)
    - [Atualizar endpoint de bloco de conteúdo]({{site.baseurl}}/api/endpoints/templates/content_blocks_templates/post_update_content_block/)

### Campanhas disparadas por API e Canvas

Os clientes podem configurar campanhas e Canvases para serem disparados pela API. As solicitações de API para disparar essas campanhas podem ser usadas para personalizar e segmentar ainda mais a campanha, passando as propriedades de API-trigger e os parâmetros de público ou destinatário. 
- [Como disparar campanhas via API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns/#request-body)
    - As campanhas são mensagens singulares, como e-mails individuais.
- [Acionamento de telas via API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases/#request-body)
    - O Canva é uma interface unificada na qual os profissionais de marketing podem criar campanhas com várias mensagens e etapas para formar uma jornada coesa. Ao disparar um Canvas, você está inserindo um usuário no fluxo do Canvas, onde ele continuará a receber envios de mensagens até que não se encaixe mais nos critérios do Canvas. 
- [Propriedades do disparador da API/propriedades de entrada da canva]({{site.baseurl}}/api/objects_filters/trigger_properties_object) 
    - Dados que podem ser preenchidos dinamicamente na mensagem no momento do envio.

### Campanhas da API
Ao criar campanhas de API (diferentes das campanhas disparadas por API mencionadas acima), o dashboard do Braze é usado apenas para gerar um `campaign_id`, que permite que o cliente rastreie a análise de dados para relatórios de campanha. A própria mensagem da campanha é definida na solicitação da API. 
- [Enviar campanha de API imediatamente]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_messages/)
- [Agendar uma campanha da API]({{site.baseurl}}/api/endpoints/messaging/schedule_messages/post_schedule_messages/)

### Enviar IDs
Use o endpoint do Braze para gerar um ID de envio que pode ser usado para dividir a análise de dados da campanha por envio. Por exemplo, se uma `campaign_id` (campanha de API) for criada por local, uma ID de envio poderá ser gerada por envio para rastrear o desempenho de diferentes envios de mensagens para um determinado local. 
- [Enviar IDs]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids/)

## Conteúdo conectado

O Connected Content pode ser usado em qualquer tipo de canal para fazer uma solicitação de API ao ponto de extremidade especificado no momento do envio e preencher a mensagem com o que é retornado na resposta.

A versatilidade do Connected Contents faz com que esse seja um recurso usado por muitos de nossos clientes para inserir conteúdo que não está ou não pode estar no Braze. Alguns dos casos de uso mais comuns que vemos são:
- Modelagem de conteúdo de blog ou artigo em mensagens
- Recomendações de conteúdo
- Metadados do produto
- Localização e tradução

Coisas que devem ser observadas:
- A Braze não cobra pelas chamadas de API e não será contabilizada em sua cota de dados.
- Há um limite de 1 MB para as respostas do conteúdo conectado.
- As chamadas do Connected Content ocorrerão quando a mensagem for enviada, exceto no caso de mensagens no app, que farão essa chamada quando a mensagem for visualizada.
- As chamadas de conteúdo conectado que não seguem redirects.Braze exigem que o tempo de resposta do servidor seja inferior a 2 segundos por motivos de performance; se o servidor demorar mais de 2 segundos para responder, o conteúdo não será inserido.
- Os sistemas da Braze podem fazer a mesma chamada à API de conteúdo conectado mais de uma vez por destinatário. Isso se deve ao fato de que a Braze pode precisar fazer uma chamada à API de conteúdo conectado para renderizar uma carga útil de mensagem, e as cargas úteis de mensagem podem ser renderizadas várias vezes por destinatário para validação, lógica de nova tentativa ou outros fins internos. 

Consulte estes artigos para saber mais sobre o conteúdo conectado:
- [Como fazer uma chamada de conteúdo conectado][1]
- [Abortar conteúdo conectado][2]
- [Outras tentativas no conteúdo conectado][3]

[1]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/making_an_api_call/
[2]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/aborting_connected_content
[3]: {{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/connected_content_retries
