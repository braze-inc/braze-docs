---
nav_title: Nexla
article_title: Nexla
description: "Este artigo de referência descreve a parceria entre Braze e Nexla, uma plataforma unificada de operações de dados que permite que os usuários do Braze Currents extraiam, transformem e carreguem dados do data lake para outros locais em um formato personalizado."
alias: /partners/nexla/
page_type: partner
search_tag: Partner

---

# Nexla

> A [Nexla](https://www.nexla.com) é líder em operações de dados unificados e é uma das principais fornecedoras da Gartner em 2021. A plataforma Nexla simplifica a criação de fluxos de dados dimensionáveis, proporcionando operações de dados governadas e com atrito zero, melhor colaboração e agilidade para as equipes de negócios e de dados. As equipes que trabalham com dados obtêm uma experiência unificada com pouco ou nenhum código para integrar, transformar, provisionar e monitorar dados para qualquer caso de uso. 

A integração Braze e Nexla permite que os clientes que usam o [Currents]({{site.baseurl}}/user_guide/data/braze_currents/setting_up_currents/) aproveitem o Nexla para extrair, transformar e carregar dados do data lake em outros locais em um formato personalizado, tornando os dados facilmente acessíveis em todo o seu ecossistema.

## Pré-requisitos

| Requisito | Descrição |
|---|---|
| Conta Nexla | É necessário ter uma [conta Nexla](https://www.nexla.com/get-demo) para aproveitar essa parceria. |
| Chave da API REST do Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Ponto de extremidade REST do Braze  | Sua URL de endpoint REST. Seu endpoint dependerá do [URL do Braze para sua instância]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints)). |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

Os dados como produto da Nexla, [Nexsets](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information), facilitam o trabalho com dados de qualquer formato sem se preocupar com metadados. Quando você configura seus fluxos de dados de ou para o Braze com o Nexla, as ferramentas sem código facilitam e disponibilizam tudo em minutos. Depois que o fluxo de dados for definido para um destino, a Nexla monitorará seu fluxo e o dimensionará para qualquer quantidade de dados.

## Integração

### Etapa 1: Criar uma conta Nexla

Se você ainda não tem uma conta Nexla, acesse [o site](https://www.nexla.com) da Nexla para solicitar uma demonstração e um teste gratuitos. Em seguida, registre-se em [www.dataops.nexla.io](https://www.dataops.nexla.io) e faça login com suas novas credenciais.

### Etapa 2: adicione sua fonte

#### Se o Braze for sua fonte de dados
1. Na plataforma Nexla, navegue até **Fluxos > Criar um novo fluxo** na barra de ferramentas à esquerda.
2. Clique em **Create New Source** (Criar nova fonte), selecione o conector Braze e clique em **Next** (Avançar). 
3. Selecione **Add a New Credential** (Adicionar uma nova credencial), nomeie a credencial, adicione sua chave da API da Braze e o endpoint REST e **salve**.
4. Por fim, selecione seus dados e clique em **Save (Salvar)**. 

A Nexla agora pesquisará na fonte todos os dados que encontrar e gerará um [Nexset](https://nexla.zendesk.com/hc/en-us/articles/360052999674-Dataset-Information) para transformação ou envio aos destinos.

#### Se o Braze é seu destino

Visite a documentação da Nexla sobre como [conectar fontes à Nexla](https://nexla.zendesk.com/hc/en-us/sections/115001685927-Create-a-Data-Source).

### Etapa 3: Transformar (opcional)

Se quiser realizar [transformações](https://nexla.zendesk.com/hc/en-us/sections/115001686007-Transformations) personalizadas em seus dados ou usar os conetores pré-construídos da Nexla, clique no botão **Transformar** no conjunto de dados para acessar o Transform Builder. Orientações sobre como usar o Transform Builder podem ser encontradas na [documentação da Nexla](https://nexla.zendesk.com/hc/en-us/articles/360000590468-How-to-Transform-your-Data).

### Etapa 4: enviar para destinos

Para enviar dados para um destino, clique na seta **Send to Destination (Enviar para destino** ) no conjunto de dados e selecione qualquer um dos conectores de destinos do Nexla ou do Braze, se você tiver uma origem diferente. Insira suas credenciais, configure as opções de destinos e clique em **Save** (Salvar). Os dados começarão a fluir instantaneamente no formato que você especificou para o destino de sua escolha.

## Usando esta integração

Depois que o fluxo é configurado, nada mais é necessário. O Nexla tratará de todas as alterações nos dados de origem, dimensionará para todos os novos dados e notificará você sobre quaisquer alterações de esquema ou erros para triagem. Se quiser fazer alterações nas transformações, na origem ou no destino, você pode clicar nessas opções e fazer a alteração, e o Nexla atualizará o fluxo instantaneamente.

