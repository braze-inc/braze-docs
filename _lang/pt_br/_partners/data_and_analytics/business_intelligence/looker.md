---
nav_title: Looker
article_title: Looker
alias: /partners/looker/
description: "Este artigo de referência descreve a parceria entre a Braze e o Looker, uma plataforma de business intelligence e análise de big data."
page_type: partner
search_tag: Partner

---

# [![Curso do Braze Learning] ({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/looker-integration-with-braze/){: style="float:right;width:120px;border:0;" class="noimgborder"}Looker

> A [Looker](https://looker.com/), uma plataforma de análise de dados e análises de big data, o capacita a explorar, analisar e compartilhar análises de business intelligence em tempo real sem problemas.

A integração entre o Braze e o Looker permite que os usuários do Braze aproveitem a sinalização de usuários dos [blocos do Looker](#looker-blocks) e do [Looker Actions](#looker-actions) por meio da API REST. Esses usuários sinalizados podem ser adicionados a segmentos para [direcionamento](#segment-users) de futuras campanhas ou canvas do Braze. Para usar o Looker com o Braze, recomendamos enviar seus dados do Braze para um data [warehouse usando o Braze Currents]({{site.baseurl}}/user_guide/data_and_analytics/braze_currents/available_partners/) e, em seguida, usar os blocos do Looker do Braze para modelar e visualizar rapidamente seus dados do Braze no Looker.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
|Conta Looker | É necessário ter uma [conta Looker](https://looker.com/) para usar a parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá da [URL do Braze para sua instância]({{site.baseurl}}/user_guide/data/braze_currents/how_braze_uses_currents/). |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

#### Limitações

- O processo só funciona com dados que não tenham sido dinamizados.
- A API processa um máximo de 100.000 linhas por vez.
- A contagem final da bandeira de um usuário pode ser menor devido a duplicatas ou não usuários.

## Integração

### Blocos do Looker

Nossos blocos do Looker ajudam os clientes do Braze a acessar rapidamente uma visão dos dados granulares que oferecemos via [Currents]({{site.baseurl}}/partners/braze_currents/about/). Nossos blocos fornecem visualizações e modelagens pré-fabricadas para os dados do Currents, de modo que os clientes do Braze possam implementar facilmente padrões analíticos, como retenção, avaliar a entregabilidade das mensagens, analisar mais detalhadamente o comportamento dos usuários e muito mais.

Para implementar os blocos do Looker, siga as instruções nos arquivos README do código do GitHub.
- [README do bloco de análise de dados de engajamento com mensagem](https://github.com/llooker/braze_message_engagement_block/blob/master/README.md)
- [README do bloco de análise de dados de comportamento do usuário](https://github.com/llooker/braze_retention_block/blob/master/README.md)

Ambas as integrações pressupõem que sua [integração inicial da Braze]({{site.baseurl}}/user_guide/onboarding_with_braze/integration/) e sua integração da Braze com um [data warehouse](https://looker.com/solutions/other-databases?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) compatível com o Looker estejam configuradas adequadamente para capturar e enviar os dados necessários.


{% alert important %}
A Braze criou nossos blocos do Looker usando o [Snowflake](https://www.snowflake.com/) como data warehouse. Embora nosso objetivo seja que nossos blocos funcionem com o maior número possível de data warehouses, algumas funções SQL podem diferir em disponibilidade, sintaxe ou comportamento entre dialetos.
{% endalert %}

{% alert warning %}
Esteja ciente das diferentes convenções de nomenclatura! Os nomes personalizados podem causar incongruências nos dados, a menos que você altere todos os nomes correspondentes. Se você personalizou algum nome de visualização/tabela ou modelo, renomeie cada um deles no LookML com o nome que você selecionou.
{% endalert %}

#### Blocos disponíveis

| Bloquear | Descrição |
|---|---|
| Bloco de análise de dados de engajamento com mensagens | Esse bloco inclui dados sobre push, e-mail, mensagens no app, webhook, conversão, entrada no Canva e eventos de inscrição no grupo de controle da campanha. <br><br>Saiba mais sobre este [bloco do Looker](https://looker.com/platform/blocks/source/message-engagement-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) ou confira o [código do GitHub](https://github.com/llooker/braze_message_engagement_block). |
| Bloco de análise de dados de comportamento do usuário | Este bloco inclui dados sobre eventos personalizados, compras, sessões, eventos locais e desinstalações.<br><br>Saiba mais sobre este [bloco do Looker](https://looker.com/platform/blocks/source/user-behavior-analytics-by-braze?latest&utm_campaign=7012R000000fxfC&utm_source=other&utm_medium=email&utm_content=brazedirectreferral&utm_term=braze_direct) ou confira o [código do GitHub](https://github.com/llooker/braze_retention_block). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Looker Actions

As Looker Actions permitem que você sinalize usuários no Braze por meio do endpoint da API REST de um Looker Look. As ações exigem que uma dimensão seja marcada com tags com `braze_id`. A ação anexará o valor sinalizado ao atributo personalizado `looker_export` do usuário.

{% alert important %}
Somente os usuários existentes serão sinalizados. Não é possível usar Looks articulados ao sinalizar dados no Braze.
{% endalert %}

#### Etapa 1: configurar uma ação do Looker da Braze

Configure uma ação do Looker da Braze com sua chave da API REST e o endpoint REST da Braze.

![A página de configuração do Looker Braze. Aqui, você pode encontrar campos para a chave da API do Braze e o endpoint da API REST do Braze.]({% image_buster /assets/img/braze-looker-action.png %})

#### Etapa 2: Configurar o Looker Develop

No Looker Develop, selecione as visualizações apropriadas. Adicione `braze_id` à tag dimensions e confirme as alterações.
A tag `braze_id` é usada para determinar qual campo é a chave exclusiva.

```json
dimension: external_id {
    type: string
    primary_key: yes
    sql: ${TABLE}.external_id ;;
    tags: ["braze_id"]
}
```

**Certifique-se de confirmar as alterações. A ação do Looker só funciona em configurações de produção.**

#### Etapa 3: Defina as atribuições do usuário nas tags

Opcionalmente, qualquer atributo pode ser definido usando uma tag `braze[]` com o nome do atributo entre colchetes. Por exemplo, se você quisesse que um atributo personalizado `user_segment` fosse enviado, a tag seria `braze[user_segment]`.

Observe as seguintes limitações:
- Os atributos só serão enviados se forem **incluídos como campo no look**.
- Os tipos suportados são `Strings`, `Boolean`, `Numbers` e `Dates`.
- Os nomes de atribuições diferenciam maiúsculas de minúsculas.
- As atribuições padrão também podem ser definidas, desde que correspondam exatamente aos nomes [de perfil de usuário padrão]({{site.baseurl}}/api/endpoints/user_data/#braze-user-profile-fields).
- A tag completa deve ser formatada entre aspas. Por exemplo, `tags: ["braze[first_name]"]`. Outras tags também podem ser atribuídas, mas serão ignoradas.
- Informações adicionais podem ser encontradas no [GitHub](https://github.com/looker/actions/tree/master/src/actions/braze).

#### Etapa 4: Enviar a ação Looker

1. Em um Look com uma dimensão `braze_id` selecionada, clique na engrenagem de configurações (<i class="fas fa-cog"></i>) no canto superior direito e selecione **Send...** (Enviar...).
2. Selecione a ação personalizada da Braze.
3. Em **Unique Key** (Chave única), forneça a chave de mapeamento do usuário primário para a conta Braze (`external_id` ou `braze_id`).
4. Dê um nome à exportação. Se nenhum for fornecido, será usado o endereço `LOOKER_EXPORT`.
5. Em **Advanced Options (Opções avançadas**), selecione **Results in Table (Resultados na tabela** ) ou **All Results (Todos os resultados** ) e, em seguida, **Send (Enviar**).<br><br>![]({% image_buster /assets/img/send-looker-action.png %})<br><br>Se a exportação tiver sido enviada corretamente, o endereço `LOOKER_EXPORT` deverá aparecer no perfil do usuário como um atributo personalizado com o valor inserido na ação.<br><br>![]({% image_buster /assets/img/custom-attributes-looker.png %})

##### Exemplo de API de saída

A seguir, confira um exemplo de uma chamada de API de saída, que será enviada para o [endpoint`/users/track/`]({{site.baseurl}}/api/endpoints/user_data/post_user_track/).

###### Cabeçalho
```
Authorization: Bearer [API_KEY]
```

###### Corpo
```json
{
   "attributes" : [
      {
        "external_id" : "user_01",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_02",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      {
        "external_id" : "user_03",
        "_update_existing_only" : true,
        "looker_export" : { "add" : ["LOOKER"] }
      },
      .....
   ]
}
```

### Usuários do segmento no Braze {#segment-users}

No Braze, para criar um segmento desses usuários sinalizados, navegue até **Segments (Segmentos** ) em **Engagement (Engajamento)**, nomeie seu segmento e selecione **Looker_Export** como o filtro. Em seguida, use a opção "includes value" (inclui valor) e forneça o sinalizador de atributo personalizado que você atribuiu no Looker.

![No criador de segmentos do Braze, o filtro "looker_export" está definido como "includes_value" e "Looker".]({% image_buster /assets/img/braze_segments.png %})

Depois de salvo, você pode fazer referência a esse segmento durante a criação do Canva ou da campanha na etapa de direcionamento de usuários.

## Solução de problemas
Se estiver tendo problemas com o Looker Actions, adicione um usuário teste aos [grupos internos]({{site.baseurl}}/user_guide/administrative/app_settings/developer_console/internal_groups_tab/) e verifique o seguinte:

* A chave de API tem as permissões `users.track`.
* O endpoint REST correto foi inserido, como `https://rest.iad-01.braze.com`.
* Uma tag `braze_id` é definida na visualização da dimensão.
* Sua consulta inclui a dimensão ou atributo Id como uma coluna.
* Os resultados do Looker não são dinamizados.
* A chave exclusiva foi selecionada corretamente. Normalmente, o `external_id`.
* `braze_id` na dimensão é diferente do `braze_id` na API. `braze_id` na dimensão é usado para indicar que é o campo `id` para a API do Braze. Para a maioria das finalidades, `external_id` é a chave primária no ato do envio.
* O usuário `external_id` existe na plataforma Braze.
* O campo `looker_export` é definido como `Automatically Detect` em `Braze Platform > Settings > Manage Settings > Custom Attributes`.
* As alterações são confirmadas para a produção. O Looker Actions funciona em configurações de produção.

