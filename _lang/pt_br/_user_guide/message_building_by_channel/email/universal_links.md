---
nav_title: Links universais e links de aplicativos
article_title: Links universais e links de aplicativos
page_order: 6.4
page_type: reference
description: "Este artigo de ajuda o orienta sobre como configurar os links universais da Apple e os links de aplicativos do Android."
channel: email
---

# Links universais e links de aplicativos

Os links universais da Apple e os links de aplicativos do Android são mecanismos criados para proporcionar uma transição perfeita entre o conteúdo da Web e os aplicativos móveis. Embora os links universais sejam específicos do iOS, os Android App Links têm a mesma finalidade para os aplicativos Android.

## Como funcionam os links universais e os App Links

Os links universais (iOS) e os links de aplicativos (Android) são links padrão da Web (`http://mydomain.com`) que apontam para uma página da Web e para um conteúdo dentro de um aplicativo.

Quando um link universal ou App Link é aberto, o sistema operacional verifica se algum aplicativo instalado está registrado para esse domínio. Se um aplicativo for encontrado, ele será iniciado imediatamente, sem nunca carregar a página da Web. Se nenhum aplicativo for encontrado, o URL da Web será carregado no navegador da Web padrão do usuário, que também pode ser configurado para redirecionar para a App Store ou a Google Play Store, respectivamente.

De forma simples, os links universais permitem que um site associe suas páginas da Web a telas de aplicativos específicos, de modo que, quando um usuário clica em um link para uma página da Web que corresponde a uma tela de aplicativo, o aplicativo pode ser aberto diretamente (se o aplicativo estiver instalado no momento).

Esta tabela descreve as principais diferenças entre os links universais e os links diretos tradicionais:

|                        | Links universais e links de aplicativos                                  | Links profundos                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Compatibilidade de plataforma | iOS (versão 9 e posterior) e Android (versão 6.0 e posterior)  | Usado em vários sistemas operacionais móveis    |
| Finalidade                | Vincule perfeitamente o conteúdo da Web e do aplicativo em dispositivos iOS e Android | Link para conteúdo específico do aplicativo |
| Função               | Direciona para páginas da Web ou conteúdo de aplicativos com base no contexto           | Abre telas específicas do aplicativo   |
| Instalação do aplicativo       | Abre o aplicativo se o aplicativo estiver instalado; caso contrário, abre o conteúdo da Web | Requer a instalação do aplicativo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

Os links universais e os links de aplicativos são mais comumente usados para campanhas de e-mail, pois os e-mails podem ser abertos e clicados tanto no desktop quanto em dispositivos móveis.

Alguns canais não funcionam bem com esses links. Por exemplo, notificações push, mensagens no aplicativo e cartões de conteúdo devem usar deep links baseados em esquemas (`mydomain://`).

{% alert note %}
Os links de aplicativos Android exigem um `IBrazeDeeplinkHandler` personalizado com lógica para tratar os links de seus domínios separadamente de outros URLs da Web. Em vez disso, pode ser mais fácil usar links diretos e manter as práticas de vinculação uniformes para outros canais além do e-mail.
{% endalert %}

## Pré-requisitos

Para usar links universais e App Links:

- Seu site deve ser acessível via HTTPS
- Seu aplicativo deve estar disponível na App Store (iOS) ou na Google Play Store (Android)

## Configuração de links universais e App Links

Para que os aplicativos suportem links universais ou App Links, tanto o iOS quanto o Android exigem que um arquivo de permissões especial seja hospedado no domínio do link. Esse arquivo contém definições de quais aplicativos podem abrir links desse domínio e, no caso do iOS, quais caminhos esses aplicativos podem abrir:

- **iOS:** Arquivo da Associação de Sites de Aplicativos da Apple (AASA)
- **Android:** Arquivo de links de ativos digitais

Além desse arquivo de permissões, há definições codificadas de quais domínios de links o aplicativo tem permissão para abrir, que são configuradas no aplicativo:

- **iOS:** Definir como "Domínios associados" no Xcode
- **Android:** Definido no arquivo `AndroidManifest.xml` do aplicativo

Essa associação domínio-app de duas partes é necessária para que um link universal ou App Link funcione e evita que qualquer aplicativo sequestre links de um domínio específico ou que qualquer domínio abra um aplicativo específico.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Essas etapas foram adaptadas da documentação do desenvolvedor da Apple. Para obter mais informações, consulte [Permitir que aplicativos e sites sejam vinculados ao seu conteúdo](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Etapa 1: Configure os direitos do aplicativo

{% alert note %}
[No Xcode 13 e posterior](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), o Xcode pode lidar automaticamente com o provisionamento de direitos para você. Provavelmente, você pode pular para a [etapa 1c](#step-1c) e consultar estas instruções se tiver problemas.
{% endalert %}

#### Etapa 1a: Registre seu aplicativo {#step-1a}

1. Acesse developer.apple.com e faça login.
2. Clique em **Certificates, Identifiers (Certificados, Identificadores) & Profiles (Perfis**).
3. Clique em **Identificadores**.
4. Se ainda não tiver um App Identifier registrado, clique em + para criar um.
   a. Digite um **nome**. Pode ser o que você quiser.
   b. Digite o **ID do pacote**. Você pode encontrar o ID do pacote na guia **General (Geral** ) do seu projeto Xcode para obter o alvo de compilação adequado.

#### Etapa 1b: Ative os domínios associados no identificador do aplicativo

1. No seu App Identifier existente ou recém-criado, localize a seção **App Services**.
2. Selecione **Domínios associados**.
3. Clique em **Salvar**.

\![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Etapa 1c: Ative a opção Associated Domains em seu projeto Xcode {#step-1c}

Antes de prosseguir, certifique-se de que o projeto do Xcode tenha a mesma equipe selecionada na qual você acabou de registrar o App Identifier. 

1. No Xcode, vá para a guia **Capabilities (Recursos** ) do seu arquivo de projeto.
2. Ative a opção **Associated Domains (Domínios associados**).

##### Dica para solução de problemas

Se você vir o erro "Uma ID de aplicativo com o identificador 'your-app-id' não está disponível. Digite uma cadeia de caracteres diferente", faça o seguinte:

1. Verifique se você selecionou a equipe correta.
2. Verifique se o Bundle ID[(etapa 1a](#step-1a)) do seu projeto Xcode corresponde ao usado para registrar o App Identifier.

#### Etapa 1d: Adicionar o direito de domínio

Na seção de domínios, adicione a tag de domínio apropriada. Você deve prefixá-lo com `applinks:`. Nesse caso, você pode ver que adicionamos `applinks:yourdomain.com`.

\![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Etapa 1e: Confirme se o arquivo de direitos está incluído na compilação

No navegador de projetos, certifique-se de que seu novo arquivo de direitos esteja selecionado em **Target Membership**.

O Xcode deve lidar com isso automaticamente.

### Etapa 2: Configure seu site para hospedar o arquivo AASA

Para associar o domínio do seu site ao seu aplicativo nativo no iOS, você precisa hospedar o arquivo Apple App Site Association (AASA) no seu site. Esse arquivo serve como uma maneira segura de verificar a propriedade do domínio para o iOS. Antes do iOS 9, os desenvolvedores podiam registrar qualquer esquema de URI para abrir seus aplicativos, sem nenhuma verificação. No entanto, com a AASA, esse processo se tornou muito mais seguro e confiável.

O arquivo AASA contém um objeto JSON com uma lista de aplicativos e os caminhos de URL no domínio que devem ser incluídos ou excluídos como links universais. Aqui está um exemplo de arquivo AASA:

```json
{
  "applinks": {
    "apps": [],
    "details": [
      {
        "appID": “JHGFJHHYX.com.facebook.ios",
        "paths": [
          "*"
        ]
      }
    ]
  }
}
```

- `appID`: Criado combinando o **ID** da equipe do seu aplicativo (acesse `https://developer.apple.com/account/#/membership/` para obter o ID da equipe) e o **Bundle Identifier (Identificador do pacote**). No exemplo acima, "JHGFJHHYX" é o ID da equipe e "com.facebook.ios" é o ID do pacote.
- `paths`: Matriz de cadeias de caracteres que especificam quais caminhos são incluídos ou excluídos da associação. Você pode usar `NOT` antes do caminho para desativar os caminhos. Neste exemplo, todos os links nesse caminho irão para a Web em vez de abrir o aplicativo. Você pode usar `*` como curinga para habilitar todos os caminhos em um diretório e `?` para corresponder a um único caractere (como /archives/201?/ para corresponder a todos os números de 2010-2019).

{% alert note %}
Essas strings diferenciam maiúsculas de minúsculas, e as strings de consulta e os identificadores de fragmentos são ignorados.
{% endalert %}

### Etapa 3: Hospede o arquivo AASA em seu domínio

Quando o arquivo AASA estiver pronto, você poderá hospedá-lo em seu domínio em `https://<<yourdomain>>/apple-app-site-association` ou em `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Faça upload do arquivo `apple-app-site-association` em seu servidor da Web HTTPS. Você pode colocar o arquivo na raiz do seu servidor ou no subdiretório `.well-known`. Não anexe `.json` ao nome do arquivo.

{% alert important %}
O iOS só tentará buscar o arquivo AASA por meio de uma conexão segura (HTTPS).
{% endalert %}

Ao hospedar o arquivo da AASA, certifique-se de que o arquivo siga estas diretrizes:

- É servido por HTTPS.
- Usa o tipo MIME `application/json`.
- Não excede 128 KB (requisito no iOS 9.3.1 em diante)

### Etapa 4: Prepare seu aplicativo para lidar com links universais

Quando um usuário toca em um link universal em um dispositivo iOS, o dispositivo inicia o aplicativo e envia a ele um objeto [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity). O aplicativo pode então consultar o objeto NSUserActivity para determinar como ele foi iniciado.

Para oferecer suporte a links universais em seu aplicativo, execute as seguintes etapas:

1. Adicione um direito que especifique os domínios que seu aplicativo suporta.
2. Atualize o delegado do aplicativo para responder adequadamente quando receber o objeto NSUserActivity.

No Xcode, abra a seção **Associated Domains (Domínios associados** ) na guia **Capabilities (Recursos)** e adicione uma entrada para cada domínio compatível com seu aplicativo, com o prefixo `applinks:`. Por exemplo, `applinks:www.mywebsite.com`.

{% alert note %}
A Apple recomenda limitar essa lista a não mais que 20 ou 30 domínios.
{% endalert %}

### Etapa 5: Teste seu link universal

Adicione o link universal a um e-mail e envie-o para um dispositivo de teste. Colar um link universal diretamente no campo de URL do Safari não fará com que o aplicativo seja aberto automaticamente. Se fizer isso, você terá que puxar manualmente o site para baixo para que apareça um aviso na parte superior solicitando que você abra o respectivo aplicativo.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Essas etapas foram adaptadas da documentação do desenvolvedor do Android. Para obter mais informações, consulte [Adicionar links de aplicativos Android](https://developer.android.com/training/app-links#add-app-links) e [Criar links diretos para o conteúdo do aplicativo](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Os links de aplicativos Android exigem um `IBrazeDeeplinkHandler` personalizado com lógica para tratar os links de seus domínios separadamente de outros URLs da Web. Em vez disso, pode ser mais fácil usar links diretos e manter as práticas de vinculação uniformes para outros canais além do e-mail.
{% endalert %}

### Etapa 1: Criar links diretos

Primeiro, você precisa criar deep links para seu aplicativo Android. Isso pode ser feito adicionando [filtros de intenção](https://developer.android.com/guide/components/intents-filters) em seu arquivo `AndroidManifest.xml`. O filtro de intenção deve incluir a ação `VIEW` e a categoria `BROWSABLE`, juntamente com o URL do seu site no elemento de dados.

### Etapa 2: Associe seu aplicativo ao seu site

Você precisa associar seu aplicativo ao seu site. Isso pode ser feito com a criação de um arquivo Digital Asset Links. Esse arquivo deve estar no formato JSON e inclui detalhes sobre os aplicativos Android que podem abrir links para o seu site. Ele deve ser colocado no diretório `.well-known` de seu site.

### Etapa 3: Atualize o arquivo de manifesto do aplicativo

Em seu arquivo `AndroidManifest.xml`, adicione um elemento de metadados dentro do elemento do aplicativo. O elemento de metadados deve ter um atributo `android:name` de "asset_statements" e um atributo `android:resource` que aponte para um arquivo de recurso com uma matriz de strings que inclua o URL do seu site.

### Etapa 4: Prepare seu aplicativo para lidar com deep links

Em seu aplicativo Android, você precisa lidar com os deep links de entrada. Você pode fazer isso obtendo a intenção que iniciou sua atividade e extraindo os dados dela.

### Etapa 5: Teste de seus deep links

Por fim, você pode testar seus links diretos. Enviar a si mesmo um link por meio de um aplicativo de mensagens ou e-mail e clicar nele. Se tudo estiver configurado corretamente, ele deverá abrir seu aplicativo.

{% endtab %}
{% endtabs %}

## Links universais, links de aplicativos e rastreamento de cliques

{% alert note %}
Os links de rastreamento de cliques geralmente são configurados como parte de sua integração para e-mail. Se isso não tiver sido concluído durante a integração do cliente, entre em contato com o gerente da sua conta para obter ajuda.
{% endalert %}

Nossos parceiros de envio de e-mail, SendGrid e SparkPost, usam domínios de rastreamento de cliques para envolver todos os links e incluir parâmetros de URL para rastreamento de cliques nos e-mails do Braze.

Por exemplo, um link como `https://www.example.com` se torna algo como `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Para permitir que os links de e-mail com rastreamento de cliques funcionem como links universais ou App Links, você precisará realizar algumas configurações adicionais. Certifique-se de adicionar o domínio de rastreamento de cliques (`links.email.example.com`) como um domínio que o aplicativo tem permissão para abrir. Além disso, o domínio de rastreamento de cliques deve servir os arquivos AASA (iOS) ou Digital Asset Links (Android). Isso ajudará a garantir que os links de e-mail com rastreamento de cliques funcionem perfeitamente.

Se não quiser que cada link de rastreamento de cliques seja um link universal ou um App Link, você poderá especificar quais links devem ser links universais com base no parceiro de envio de e-mail. Consulte as seções a seguir para obter detalhes.

### SendGrid

Para tratar um link de rastreamento de cliques da SendGrid como um link universal:

1. Configure os valores pathPrefix do AASA ou do AndroidManifest para tratar apenas os links com `/uni/` no caminho do URL como links universais.
2. Adicione o atributo `universal="true"` à tag âncora de seu link (`<a>`). Isso altera o caminho do URL do link agrupado para incluir `/uni/`.

{% alert note %}
Para e-mails AMP, esse atributo deve ser data-universal="true".
{% endalert %}

Por exemplo:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\. Certifique-se de que seu aplicativo esteja configurado para lidar corretamente com os links agrupados. Consulte o artigo da SendGrid sobre [Resolução de links de rastreamento de cliques da SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) e siga as etapas para seu sistema operacional. Este artigo contém um código de exemplo para [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) e [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Com essa configuração, os links com `/uni/` no caminho do URL funcionarão como links universais, enquanto todos os outros links funcionarão como links da Web.

### SparkPost

Para tratar um link de rastreamento de cliques do SparkPost como um link universal, adicione o seguinte atributo à seção Atributos do editor de arrastar e soltar para e-mail ou edite manualmente o HTML do link para incluir o seguinte atributo na tag de âncora do seu link: `data-msys-sublink="custom_path"`.

Esse caminho personalizado permite que você trate seletivamente os URLs com esse valor como um link universal.

Por exemplo:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Em seguida, certifique-se de que seu aplicativo esteja configurado para lidar corretamente com o caminho personalizado. Consulte o artigo do SparkPost sobre [como usar o rastreamento de cliques do SparkPost em deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Este artigo contém um código de exemplo para [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) e [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

### Desativar o rastreamento de cliques em uma base de link a link

Você pode desativar o rastreamento de cliques para links específicos adicionando código HTML à sua mensagem de e-mail para o editor de HTML ou a um bloco HTML para o editor de arrastar e soltar.

#### SendGrid

Se o seu provedor de serviços de e-mail for o SendGrid, use o código HTML `clicktracking=off` da seguinte forma:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost 

Se o seu provedor de serviços de e-mail for o SparkPost, use o código HTML `data-msys-clicktrack="0"` da seguinte forma:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Se o seu provedor de serviços de e-mail for o Amazon SES, use o código HTML `ses:no-track` da seguinte forma:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Editor de arrastar e soltar

Ao usar o editor de e-mail do tipo arrastar e soltar, insira seu código HTML como um atributo personalizado se o link estiver anexado a um texto, um botão ou uma imagem.

##### Atributo personalizado para um link de texto

#### SendGrid

Selecione o seguinte para o atributo personalizado:

- **Nome:** `clicktracking`
- **Valor:** `off`

#### SparkPost

Selecione o seguinte para o atributo personalizado:

- **Nome:** `data-msys-clicktrack`
- **Valor:** `0`

\![Um atributo personalizado para um link de texto.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

##### Atributo personalizado para um botão ou imagem

#### SendGrid

Selecione o seguinte para o atributo personalizado:

- **Nome:** `clicktracking`
- **Valor:** `off`
- **Tipo:** Link

#### SparkPost

Selecione o seguinte para o atributo personalizado:

- **Nome:** `data-msys-clicktrack`
- **Valor:** `0`
- **Tipo:** Link

\![Um atributo personalizado para um botão.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Solução de problemas de links universais com rastreamento de cliques

Se os seus links universais não estiverem funcionando como esperado em seus e-mails, como navegar o destinatário do aplicativo de e-mail para o navegador da Web antes de finalmente redirecionar para o aplicativo, consulte estas dicas para solucionar problemas de configuração do link universal.

#### Verificar o local do arquivo de link

Certifique-se de que o arquivo AASA (iOS) ou o arquivo Digital Asset Links (Android) esteja localizado no local correto:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

É importante garantir que esses arquivos estejam sempre acessíveis ao público. Se não conseguir acessá-los, talvez tenha perdido uma etapa na configuração de links universais para e-mail.

#### Verificar definições de domínio

Verifique se você tem as definições corretas para os domínios que seu aplicativo pode abrir.

- **iOS:** Revise os domínios associados configurados no Xcode para seu aplicativo[(etapa 1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c)). Verifique se o domínio de rastreamento de cliques está incluído nessa lista.
- **Android:** Abra a página de informações do aplicativo (mantenha pressionado o ícone do aplicativo e clique em ⓘ). No menu de informações do aplicativo, localize **Abrir por padrão** e toque nele. Isso deve mostrar uma tela com todos os links verificados que o aplicativo tem permissão para abrir. Verifique se o domínio de rastreamento de cliques está incluído nessa lista.

