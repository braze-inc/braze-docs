---
nav_title: Sheetlabs
article_title: Sheetlabs
description: "Este artigo de referência descreve a parceria entre o Braze e a Sheetlabs, um serviço que permite personalizar suas campanhas de marketing com dados provenientes de planilhas."
alias: /partners/sheetlabs/
page_type: partner
search_tag: Partner
---

# Sheetlabs

> O [Sheetlabs](https://sheetlabs.com/) é uma plataforma que permite transformar planilhas em APIs poderosas e bem documentadas. Você pode importar dados do Google Sheets ou do Excel, transformá-los em uma API e, em seguida, usar essa API em outros aplicativos, como a Braze.
_Essa integração é mantida pela Sheetlabs._

## Sobre a integração

A integração entre a Sheetlabs e o Braze permite que você aproveite o [Connected Content]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/connected_content/about_connected_content/) para incluir APIs da Sheetlabs em suas campanhas de marketing do Braze. Isso é normalmente usado para fornecer uma ponte entre uma planilha do Google (que é atualizada diretamente pela equipe de marketing) e os modelos do Braze. Isso permite que você faça mais com os modelos do Braze, como traduções ou conjuntos maiores de atributos personalizados.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta Sheetlabs | É necessário ter uma [conta Sheetlabs](https://sheetlabs.com/) para aproveitar essa parceria. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Casos de uso

A integração entre a Braze e a Sheetlabs permite executar os seguintes casos de uso:

1. **Separar o acesso do profissional de marketing do acesso à campanha do Braze**: Algumas equipes desejam evitar dar a todos os funcionários acesso para configurar diretamente os modelos e o conteúdo do Braze. Em vez disso, eles querem que a equipe atualize o conteúdo de marketing em uma planilha. O Sheetlabs faz a ponte entre as planilhas eletrônicas e o Braze e pode ser atualizado em tempo real.
2. **Traduções**: Os modelos Braze não oferecem suporte nativo a traduções. Se quiser oferecer suporte a vários idiomas, você deverá criar vários modelos. Ao usar a Sheetlabs em conjunto com a Braze, você pode ter um único modelo da Braze traduzido para vários idiomas.
3. **Extensão de atributos personalizados**: O Braze fornece um certo número de atributos personalizados que podem ser configurados. Ao usar o Sheetlabs em conjunto com o Braze, você pode adicionar outros atributos personalizados além dessa atribuição inicial.

Consulte o [Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/) para obter mais informações sobre esses casos de uso.

## Integração

### Etapa 1: Importar sua planilha para o Sheetlabs

No Sheetlabs, faça upload de uma planilha do Excel ou vincule sua conta do Google e importe uma planilha do Google. 

- Para importar uma planilha do Excel, clique em **Data Tables (Tabelas de dados** ) na barra de menus e, em seguida, em **Import from CSV/Excel**.
- Para importar do Planilhas Google, clique em **Tabelas de dados** na barra de menus e, em seguida, em **Importar do Google**. Em seguida, você precisará fornecer suas credenciais de login do Google e importar a planilha.

Você também pode aceitar manter sua Planilha Google sincronizada, o que significa que o Sheetlabs buscará automaticamente os dados mais recentes de sua Planilha Google quando eles forem alterados.

Certifique-se de incluir o ID de usuário do Braze em sua planilha ou outra coisa que possa ser usada como pesquisa posteriormente.

### Etapa 2: Criar uma API no Sheetlabs

Em seguida, na Sheetlabs, acesse **APIs > Create API** (APIs > Criar API) e dê um nome à sua API. É provável que você queira permitir consultas por meio de um campo de pesquisa da sua planilha, como o ID de usuário do Braze.

Nesse ponto, você deve ser capaz de acessar sua API com um link como:<br> [`https://sheetlabs.com/ACME/email1_translations?country=en`](https://sheetlabs.com/ACME/email1_translations?country=en).

### Etapa 3: use a API no conteúdo conectado da Braze

Agora que sua API está acessível, você pode usá-la em suas chamadas de conteúdo conectado. Aqui está um exemplo de como um modelo de tradução pode se parecer:

{% raw %}
```js
{% connected_content https://sheetlabs.com/ACME/email1_translations?country={{${country}}} :save translations %}

{{translations[0].greeting}} {{${first_name}}},

{{translations[0].message_body}}
```
{% endraw %}
{% alert tip %}
Para obter mais exemplos e conselhos sobre a integração com a Sheetlabs, consulte a [documentação da Sheetlabs](https://app.sheetlabs.com/docs/producers/braze/).
{% endalert %}
