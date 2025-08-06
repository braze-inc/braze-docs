---
nav_title: Grouparoo
page_order: 1
description: "Este artigo descreve a parceria entre o Braze e o Grouparoo, uma ferramenta de ETL reversa de código aberto que facilita a alimentação de suas ferramentas de marketing, vendas e suporte usando os dados de seu data warehouse."
page_type: update

---

# Grouparoo

{% alert update %}
O suporte ao Grouparoo foi descontinuado a partir de abril de 2022.
{% endalert %}

> O [Grouparoo](https://www.grouparoo.com/) é uma ferramenta de ETL reversa de código aberto que facilita a alimentação de suas ferramentas de marketing, vendas e suporte usando os dados de seu data warehouse. A configuração é feita em uma interface de usuário centrada no modelo, possibilitando que membros não técnicos da equipe configurem e programem sincronizações de dados para apoiar as operações.

A integração da Braze com o Grouparoo facilita a operacionalização dos dados armazenados em um data warehouse, enviando-os para a Braze. Quando você configura agendas de sincronização automática, pode melhorar consistentemente as comunicações com os clientes com informações atualizadas.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta e projeto do Grouparoo | É necessário ter uma conta e um projeto do Grouparoo para aproveitar essa parceria.<br><br>Essa integração pode ser usada com a edição comunitária gratuita e com as soluções empresariais fornecidas pelo Grouparoo. A instalação ocorrerá na interface de usuário de configuração do Grouparoo. |
| Chave da API REST do Braze | Uma chave da API REST do Braze com usuários e permissões de rastreamento. <br><br> Isso pode ser criado no dashboard do Braze em **Configurações** > **Chaves de API**. |
| Endpoint REST do Braze | [Sua URL de endpoint REST.](https://www.grouparoo.com/) Seu endpoint dependerá do URL do Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Integração

### Etapa 1: Criar um app Braze no Grouparoo

No Grouparoo, navegue até **Apps** e selecione **Braze** para criar um novo aplicativo Braze. Na janela modal exibida, informe sua chave de API da Braze e o endpoint REST.

![]({% image_buster /assets/img/grouparoo/add-app.png %})

### Etapa 2: Configurar um modelo e uma fonte de dados

Essa integração requer que você tenha um modelo existente e uma fonte de dados configurada antes de prosseguir para a próxima etapa. Se você não tiver essa configuração, visite a documentação do Grouparoo para saber como configurar um [modelo](https://www.grouparoo.com/docs/config/models) e uma [fonte de dados](https://www.grouparoo.com/docs/config/sources).

### Etapa 3: Criar um destino Braze no Grouparoo

#### Selecionar o modo de sincronização

No Grouparoo, selecione seu modelo na barra de navegação. Em seguida, vá até a seção **Destinations (Destinos)** e clique em **Add new Destination (Adicionar novo destino)**.

Em seguida, selecione o app **Braze** que você criou, nomeie os destinos e selecione o modo de sincronização desejado entre os seguintes:
- **Sincronização**: Adicione, atualize e remova usuários do Braze conforme necessário. Essa opção procura novos registros, alterações em registros existentes e exclusões.
- **Aditivo**: Adicione e atualize os usuários da Braze conforme necessário, mas não remova ninguém. Essa opção procura novos usuários para adicionar ao Braze e alterações nos usuários existentes do Braze, mas não controla as exclusões.
- **Enriquecer**: Atualize apenas os usuários que já existem no Braze. Não adicione ou remova usuários. Essa opção atualizará apenas os usuários existentes no Braze.

#### Mapeamento do campo de propriedade

Em seguida, você deve mapear os campos de propriedade do Grouparoo para os campos de propriedade do Braze. 

![Exemplo de campos de mapeamento de propriedades. O userID do Grouparoo é definido para mapear para external_id. e-mail, firstName e lastName são definidos como campos equivalentes de "e-mail", "first_name" e "last_name" do Grouparoo.]({% image_buster /assets/img/grouparoo/mapping.png %}){: style="max-width:80%;"}

Certifique-se de que o campo `external_id` do Braze esteja mapeado para a chave primária em sua tabela de origem. Mapeie o restante dos campos conforme necessário para seu caso de uso.

**Enviar seção Propriedades do registro**: Uma lista de campos de perfil de usuário predefinidos disponíveis para mapear dados. Qualquer um deles pode ser sincronizado a partir das propriedades do Grouparoo.

Seção de **campos opcionais do perfil de usuário do Braze**: Crie campos de perfil de usuário Braze personalizados opcionais. Se você clicar em **Add New Braze User Profile Field (Adicionar novo campo de perfil de usuário Braze)**, verá todas as propriedades disponíveis que podem ser mapeadas para o Braze. O nome de qualquer novo campo que você criar será o mesmo da propriedade Grouparoo, mas poderá ser renomeado.

#### Grupos Grouparoo

Além do mapeamento, você também pode optar por adicionar grupos do Grouparoo a grupos de inscrições do Braze. 

![Em "Braze Subscription Groups" na janela de configuração de destinos do Grouparoo, o grupo do Grouparoo "High value with recent automotive purchase" será adicionado ao grupo de inscrições do Braze "High value with recent automotive purchase".]({% image_buster /assets/img/grouparoo/lists.png %}){: style="max-width:80%;"}

{% alert important %}
Mais detalhes e atualizações sobre essa integração podem ser encontrados na [documentação do Grouparoo](https://www.grouparoo.com/docs/integrations/grouparoo-braze).
{% endalert %}

