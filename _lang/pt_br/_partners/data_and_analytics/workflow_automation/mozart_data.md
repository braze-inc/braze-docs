---
nav_title: Mozart Data
article_title: Mozart Data
description: "Este artigo de referência descreve a parceria entre o Braze e a Mozart Data, uma plataforma de dados moderna e completa, permitindo que você use o Fivetran para importar dados para o Snowflake, criar transformações, combinar dados e muito mais."
alias: /partners/mozart_data/
page_type: partner
search_tag: Partner

---

# Mozart Data

{% multi_lang_include video.html id="HU6dSOClcQ0" align="right" %}

> A [Mozart Data](https://mozartdata.com/) é uma plataforma de dados moderna e completa, com tecnologia Fivetran, Portable e Snowflake.

A integração entre a Braze e a Mozart Data permite:
- Use o Fivetran para importar dados do Braze para o Snowflake
- Crie transformações combinando dados do Braze com dados de outros aplicativos e analise efetivamente o comportamento dos usuários
- Importar dados do Snowflake para o Braze para criar novas oportunidades de engajamento de clientes
- Combine os dados do Braze com os dados de outros aplicativos para obter uma compreensão mais holística do comportamento dos usuários
- Integrar com uma ferramenta de business intelligence para explorar ainda mais os dados armazenados no Snowflake

## Pré-requisitos

<style>
table th:nth-child(1) {
    width: 25%;
}
table th:nth-child(2) {
    width: 75%;
}
table td {
    word-break: break-word;
}
</style>

| Requisito | Descrição |
| ----------- | ----------- |
| Conta de dados da Mozart | É necessário ter uma conta Mozart Data para aproveitar essa parceria. [Inscreva-se aqui.](https://app.mozartdata.com/signup)|
| Conta Snowflake<br>Opção 1: Nova conta | Selecione **Criar uma nova conta do Snowflake** durante o processo de criação da conta da Mozart Data para que a Mozart Data provisione uma nova conta do Snowflake para você. |
| Conta Snowflake<br>Opção 2: Conta existente | Se sua organização já tiver uma conta do Snowflake, você poderá usar a opção "Mozart Data Connected" (Dados conectados da Mozart).<br><br>Selecione a opção **Já tenho uma conta Snowflake** para conectar uma conta Snowflake existente. Para usar essa opção, um usuário com permissões no nível da conta deve [seguir estas etapas](https://help.mozartdata.com/docs/setting-up-data-warehouse#existingsnowflakeaccount). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

A integração é suportada tanto para a sincronização de dados do [Braze com o Mozart Data](#syncing-data-from-braze-to-mozart-data) quanto do [Mozart Data com o Braze](#syncing-data-from-mozart-data-to-braze).

### Sincronização de dados do Braze com o Mozart Data

#### Etapa 1: Configurar o conector Braze

1. No Mozart Data, acesse **Connectors (Conectores** ) e clique em **Add Connector (Adicionar conector**).
2. Procure por "Braze" e selecione o cartão conector.
3. Digite um nome de esquema de destinos onde todos os dados sincronizados do Braze serão armazenados. Recomendamos usar o nome do esquema padrão `braze`.
4. Clique em **Add Connector**.

#### Etapa 2: Preencha o formulário do conector Fivetran

Você será redirecionado para a página do conector Fivetran. Nessa página, preencha os campos indicados. Em seguida, clique em **Continue** > **Save & Test** (Continuar > Salvar e testar) para concluir o conector Fivetran.

O Fivetran começará a sincronizar os dados da sua conta da Braze com o data warehouse do Snowflake. Você pode acessar os dados de consulta do Mozart Data depois que o conector tiver concluído a sincronização. 

### Sincronização de dados do Mozart Data para o Braze

#### Etapa 1: configurar um data warehouse do Snowflake

Siga as instruções de [ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data_and_analytics/cloud_ingestion/integrations/?tab=snowflake) para configurar uma tabela, um usuário e uma permissão na interface do Snowflake. Note que essa etapa requer acesso de administrador ao Snowflake.

#### Etapa 2: Configure sua integração com o Snowflake no Braze

Depois de configurar seu data warehouse do Snowflake, na Mozart Data, acesse a página **Integration** (Integração) e selecione **Braze**. Aqui você encontra as credenciais necessárias para fornecer à Braze.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-integrationpage.png %}){: style="max-width:80%;"}

Em seguida, com login feito na Braze, acesse **Integrações > Parceiros de tecnologia > Snowflake** para iniciar o processo de integração. Copie as credenciais da Mozart Data e adicione-as à página de importação "Dados do Snowflake". Clique em **Configurar detalhes de sincronização** e insira sua conta do Snowflake e as informações da tabela de origem. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-snowflakecredentials.png %}){: style="max-width:80%;"}

Em seguida, escolha um nome para a sincronização, forneça os e-mails dos contatos e selecione um tipo de dados e uma frequência de sincronização. 

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-importsync.png %}){: style="max-width:80%;"}

#### Etapa 3: Adicione uma chave pública ao usuário do Braze
Nesse ponto, você precisará voltar ao Snowflake para concluir a configuração. Adicione a chave pública exibida no dashboard do Braze ao usuário que você criou para que o Braze se conecte ao Snowflake.

Para obter mais informações sobre como fazer isso, consulte a [documentação do Snowflake](https://docs.snowflake.com/en/user-guide/key-pair-auth.html). Se você quiser alternar as chaves a qualquer momento, a Mozart Data poderá gerar um novo par de chaves e fornecer a você a nova chave pública.

```json
ALTER USER BRAZE_INGESTION_USER SET rsa_public_key='Braze12345...';
```

#### Etapa 4: Conexão de teste

Depois que o usuário for atualizado com a chave pública, retorne ao dashboard da Braze e clique em **Testar conexão**. Se o teste for bem-sucedido, você verá uma prévia dos dados. Se, por algum motivo, a conexão não for bem-sucedida, será exibida uma mensagem de erro para ajudar a solucionar o problema.

![]({% image_buster /assets/img/mozartdata/mozartdata-braze-testsyncpublickey.png %}){: style="max-width:80%;"}

{% alert note %}
Você deve testar com êxito uma integração antes que ela possa passar do estado Rascunho para o estado Ativo. Se você precisar sair da página de criação, sua integração será salva e você poderá acessar novamente a página de detalhes para fazer alterações e testes.  
{% endalert %}

## Usando essa integração

### Como acessar os dados do Braze como um usuário do Mozart Data
Após a criação bem-sucedida de uma conta na Mozart Data, você poderá acessar seus dados da Braze sincronizados com seu data warehouse do Snowflake a partir da Mozart Data.

#### Transformações
O Mozart Data oferece uma camada de transformação SQL para permitir que os usuários criem uma visualização ou uma tabela. É possível criar uma tabela de dimensão no nível do usuário (por exemplo, `dim_users`) para resumir os dados de uso do produto de cada usuário, o histórico de mensagens e as atividades de engajamento com mensagens do Braze. 

#### Análise
Usando os modelos de transformação ou os dados brutos sincronizados do Braze, é possível analisar o engajamento dos usuários com as mensagens do Braze. Além disso, é possível combinar os dados do Braze com outros dados do aplicativo e analisar como os insights obtidos com a interação dos usuários com as mensagens do Braze se relacionam com outros dados que você possa ter sobre os usuários. Por exemplo, informações demográficas, histórico de compras, uso de produtos e engajamento no atendimento ao cliente. 

Isso pode ajudá-lo a tomar decisões mais informadas sobre estratégias de engajamento para melhorar a retenção de usuários. Tudo isso pode ser feito na interface do Mozart Data usando a ferramenta Consulta, onde você pode exportar os resultados para uma planilha do Google ou CSV para preparar uma apresentação.

#### Business intelligence (BI)
Pronto para visualizar e compartilhar seus insights com outros membros da equipe? A Mozart Data se integra a quase todas as ferramentas de BI. Se você ainda não tem uma ferramenta de BI, entre em contato com a Mozart Data para configurar uma conta gratuita da Metabase. 