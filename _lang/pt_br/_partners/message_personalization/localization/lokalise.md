---
nav_title: Lokalise
article_title: Lokalise
description: "Este artigo de referência descreve a parceria entre a Braze e o Lokalise, um serviço de gerenciamento de tradução para equipes ágeis."
alias: /partners/lokalise/
page_type: partner
search_tag: Partner

---

# Lokalise

> O [Lokalise](https://lokalise.com) é um serviço de gerenciamento de tradução para equipes ágeis.

_Esta integração é mantida pelo Lokalise._

## Sobre a integração

A integração entre a Braze e o Lokalise usa o conteúdo conectado para permitir que você insira facilmente conteúdo traduzido nas suas campanhas da Braze com base nas configurações de idioma do usuário.

## Pré-requisitos

| Requisito | Descrição |
| ----------- | ----------- |
| Conta do Lokalise | É necessário ter uma conta do Lokalise para usar essa parceria. |
| Projeto de tradução do Lokalise | Um projeto de tradução do Lokalise deve ser criado antes de configurar essa integração. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Criar um novo projeto do Lokalise

Para criar um novo projeto de tradução, registre-se no Lokalise e selecione **New Project**. Em seguida, nomeie seu projeto, escolha um **idioma base** (o idioma a partir do qual você traduzirá), adicione um ou mais **idiomas de direcionamento** e escolha o tipo de projeto de **localização de software**. Quando estiver pronto, clique em **Proceed (Continuar**).

## Integração

No Lokalise, você criará um código de tradução para cada uma das variáveis do conteúdo conectado definidas na Braze. Quando as traduções estiverem prontas, você poderá gerar um arquivo JSON por idioma e publicá-lo nos URLs que servirão seu Connected Content.

### Etapa 1: Configuração de idiomas do usuário

Se ainda não tiver feito isso, abra o dashboard do Braze e vá para **Usuários > Importação de usuário.** Aqui, você pode importar seus usuários. Ao preparar um arquivo CSV para importação, certifique-se de incluir uma coluna de idioma com os idiomas dos usuários. Esse campo de idioma será usado posteriormente na exibição de traduções. 

{% alert important %}
Os códigos de idioma usados devem corresponder tanto no Braze quanto no Lokalise.
{% endalert %}
### Etapa 2: prepare suas traduções no Lokalise

Em seguida, para preparar suas traduções no Lokalise, você precisará criar manualmente as chaves de tradução com o mesmo nome que está usando nas variáveis do Braze Connected Content. 

Por exemplo, vamos criar um código de tradução simples, `description`:
1. Abra seu projeto do Lokalise, clique em **Add Key (Adicionar chave**) e digite "description" (descrição) no campo **Key (chave)**.
2. Digite "Demo description" (Descrição da demonstração) no campo **Base Language Value (Valor do idioma base** ).
3. Adicione "Web" no menu suspenso **Platforms (Plataformas** ). 
4. Quando estiver pronto, clique em **Salvar**.

![]({% image_buster /assets/img/lokalise/1_add_key.png %}){: style="max-width:60%"}

Seu código de tradução deve aparecer no editor de projetos:

![]({% image_buster /assets/img/lokalise/2_translation_key_added.png %}){: style="max-width:90%"}

#### Problemas conhecidos

- Suas chaves devem ser atribuídas à plataforma **da Web**.
- Evite usar chaves que contenham pontos (`.`) ou a string `_on`. Por exemplo, use `this_is_the_key` em vez de `this.is.the.key`, e use `join_us_instagram` em vez de `join_us_on_instagram`.

### Etapa 3: Configuração do app Braze no Lokalise

Abra seu projeto do Lokalise e clique em **Apps**. Procure e instale o app da Braze. Você verá a seguinte tela:

![Configuração do Braze na lista do Lokalise com o ID do projeto e a URL dos arquivos de tradução.]({% image_buster /assets/img/lokalise/3_lokalise_braze_app.png %})

No **URL do arquivo de tradução**, o Lokalise publica um arquivo JSON contendo todas as traduções para suas chaves no projeto. Você obterá um URL de arquivo de tradução para cada idioma-alvo do projeto. É por isso que os URLs de arquivo de tradução resultantes têm duas partes:

1. A primeira parte do caminho do URL é comum a todos os idiomas.
2. O nome do arquivo JSON no final do URL é baseado no código do idioma.

O URL do arquivo de tradução é o URL de que você precisará ao configurar uma campanha do Braze. Você pode atualizar o conteúdo do arquivo JSON clicando em **Refresh** (Atualizar). Note que o URL permanecerá o mesmo, e você não precisará alterar sua chamada de conteúdo conectado na Braze.

### URL de teste

Para testar esse URL, copie-o e substitua {% raw %}`{{${language}}}`{% endraw %} por um código de idioma (por exemplo, `en`) e abra esse URL no seu navegador. Você verá um arquivo JSON com suas chaves e traduções:

![]({% image_buster /assets/img/lokalise/4_testing_json_lokalise.png %})

### Etapa 4: Uso de traduções na campanha do Braze

#### Inserir chamada de conteúdo conectado

Quando estiver com tudo pronto, retorne à Braze e abra uma campanha existente ou crie uma nova. Criaremos uma nova campanha de e-mail com conteúdo de amostra para este exemplo. Clique em **Edit Email Body (Editar corpo do e-mail**).

Para inserir suas traduções, você precisa adicionar a solicitação Connected Content no HTML, na parte superior do documento ou logo antes do primeiro local em que a tradução é necessária. Isso pode ser feito inserindo o seguinte markup:

{% raw %}
`{% connected_content https://exports.live.lokalise.cloud/braze/123abc/456xyz/{{${language}}}.json :save translations %}`
{% endraw %}

Substitua o URL `https://exports.live.lokalise.cloud/...` pelo URL do arquivo de tradução obtido na etapa anterior.

{% raw %}

- `{{${language}}}` significa "inserir o idioma do usuário nessa posição". Caso prefira, é possível codificar seu código de idioma. Exemplo: `en.json`.
  - Para garantir que o arquivo JSON traduzido apropriado seja recuperado para cada usuário, é necessário colocar o atributo de perfil `{{${language}}}` ou outro atributo personalizado semelhante que contenha o idioma do usuário no final do URL dos arquivos de tradução. (por exemplo, `/{{${language}}}.json`) Os valores contidos nesses atributos devem corresponder ao prefixo de cada um dos arquivos JSON traduzidos. Isso garantirá que o arquivo de tradução correto será retornado para cada usuário.
- `:save translations` salvará o conteúdo JSON na variável translations.

#### Exibir traduções

Agora use a variável translations para exibir as traduções desejadas por suas chaves.

Por exemplo, para exibir a chave `description`, use`{{ translations.description }}`.

{% endraw %}
![]({% image_buster /assets/img/lokalise/6_integration_usage_sample.png %})

Por fim, salve o modelo de e-mail e faça uma prévia. Você deverá ver sua tradução sendo exibida.

## Perguntas frequentes

**O que acontecerá se eu excluir sem querer uma chave do Lokalise?**<br>
A string correspondente no Braze não terá mais uma tradução.

**Se eu tiver uma localidade `en` e substituí-la por `en-US` no Lokalise, a Braze a lerá como `en-US`?**<br>
Não, os códigos ISO de localização devem corresponder no Braze e no Lokalise.

**Podemos usar a flag `:rerender` ao conectar o conteúdo do Lokalise?**<br>
Sim, claro. Você pode consultar os documentos do Braze para saber como adicionar esse sinalizador.

**Depois de atualizar o arquivo de tradução no Lokalise, por que não consigo ver nenhuma alteração no conteúdo traduzido na Braze?**<br>
A Braze armazena em cache o conteúdo traduzido, que pode levar alguns minutos para ser atualizado. Se estiver testando suas campanhas e precisar ver os resultados das traduções imediatamente, poderá usar o parâmetro `:cache_max_age`, conforme explicado neste artigo de referência.


