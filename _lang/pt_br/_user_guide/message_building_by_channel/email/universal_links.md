---
nav_title: Links universais e links de aplicativos
article_title: Links universais e links de aplicativos
page_order: 6.4
page_type: reference
description: "Este artigo de ajuda o orienta sobre como configurar os links universais da Apple e os app links do Android."
channel: email
---

# Links universais e links de aplicativos

Os links universais da Apple e os links de aplicativos Android são mecanismos criados para fornecer uma transição perfeita entre o conteúdo da Web e os aplicativos móveis. Embora os links universais sejam específicos para iOS, os links de app Android servem ao mesmo propósito para aplicativos Android.

## Como funcionam os links universais e os App Links

Os links universais (iOS) e os links de aplicativos (Android) são links padrão da Web (`http://mydomain.com`) que apontam para uma página da Web e para um conteúdo dentro de um app.

Quando um link universal ou App Link é aberto, o sistema operacional verifica se algum app instalado está registrado para esse domínio. Se um app for encontrado, ele será iniciado imediatamente, sem precisar carregar a página da Web. Se nenhum app for encontrado, o URL da Web será carregado no navegador da Web padrão do usuário, que também pode ser configurado para redirecionar para a App Store ou a Google Play Store, respectivamente.

De forma simples, os links universais permitem que um site associe suas páginas da Web a telas de aplicativos específicos, de modo que, quando um usuário clica em um link para uma página da Web que corresponde a uma tela de aplicativo, o aplicativo pode ser aberto diretamente (se o aplicativo estiver instalado no momento).

Esta tabela descreve as principais diferenças entre os links universais e os tradicionais deep linkings:

|                        | Links universais e links de aplicativos                                  | Deep linkings                   |
| ---------------------- | -------------------------------------------------------------- | ---------------------------- |
| Compatibilidade de plataforma | iOS (versão 9 e posterior) e Android (versão 6.0 e posterior)  | Usado em vários sistemas operacionais móveis    |
| Finalidade                | Vincule perfeitamente o conteúdo da Web e do app em dispositivos iOS e Android | Link para conteúdo específico do app |
| Função               | Direciona para páginas da Web ou conteúdo de app com base no contexto           | Abre telas específicas do app   |
| Instalação do app       | Abre o aplicativo se o aplicativo estiver instalado; caso contrário, abre o conteúdo da Web | Requer a instalação do app |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

## Casos de uso

Os links universais e os App Links são mais comumente usados em campanhas de e-mail, pois os e-mails podem ser abertos e clicados tanto no desktop quanto em dispositivos móveis.

Alguns canais não funcionam bem com esses links. Por exemplo, notificações por push, mensagens no app e cartões de conteúdo devem usar deep linkings baseados em esquemas (`mydomain://`).

{% alert note %}
Os links de apps para Android exigem um `IBrazeDeeplinkHandler` personalizado com lógica para lidar com links de seus domínios separadamente de outros URLs da Web. Em vez disso, pode ser mais fácil usar deep linking e manter as práticas de linking uniformes para outros canais além do envio de e-mail.
{% endalert %}

## Pré-requisitos

Para usar links universais e App Links:

- Seu site deve ser acessível via HTTPS
- Seu app deve estar disponível na App Store (iOS) ou na Google Play Store (Android)

## Configuração de links universais e App Links

Para que os aplicativos suportem links universais ou App Links, tanto o iOS quanto o Android exigem que um arquivo de permissões especial seja hospedado no domínio do link. Esse arquivo contém definições de quais apps podem abrir links desse domínio e, no caso do iOS, quais jornadas esses apps podem abrir:

- **iOS:** Arquivo da Apple App Site Association (AASA)
- **Android:** Arquivo de links de ativos digitais

Além desse arquivo de permissões, há definições codificadas de quais domínios de links o app tem permissão para abrir, que são configuradas dentro do app:

- **iOS:** Definir como "Domínios associados" no Xcode
- **Android:** Definido no arquivo `AndroidManifest.xml` do app

Essa associação domínio-app de duas partes é necessária para que um link universal ou App Link funcione e evita que qualquer aplicativo sequestre links de um domínio específico ou que qualquer domínio abra um aplicativo específico.

{% tabs %}
<!--iOS instructions-->
{% tab iOS %}

Estas etapas foram adaptadas da documentação do desenvolvedor da Apple. Para saber mais, consulte [Permitir que aplicativos e sites criem links para seu conteúdo](https://developer.apple.com/documentation/xcode/allowing-apps-and-websites-to-link-to-your-content?language=objc).

### Etapa 1: Configure os direitos do seu app

{% alert note %}
[No Xcode 13 e posterior](https://developer.apple.com/help/account/reference/provisioning-with-managed-capabilities/), o Xcode pode lidar automaticamente com o provisionamento de direitos para você. Provavelmente, você pode pular para a [etapa 1c](#step-1c) e consultar estas instruções se tiver problemas.
{% endalert %}

#### Etapa 1a: Registre seu app {#step-1a}

1. Acesse developer.apple.com e faça o registro.
2. Clique em **Certificates, Identifiers & Profiles (Certificados, Identificadores e Perfis**).
3. Clique em **Identificadores**.
4. Se ainda não tiver um identificador de app registrado, clique em + para criar um.
   a. Digite um **nome**. Pode ser o que você quiser.
   b. Digite a **ID do pacote**. Você pode encontrar o ID do pacote na guia **General (Geral** ) do seu projeto Xcode para obter o direcionamento de compilação adequado.

#### Etapa 1b: Ative os Domínios associados no identificador de seu app

1. No seu App Identifier existente ou recém-criado, localize a seção **App Services**.
2. Selecione **Domínios associados**.
3. Clique em **Salvar**.

![]({% image_buster /assets/img_archive/universal_links_1b.png %}){: style="max-width:75%;"}

#### Etapa 1c: Ative a opção Domínios Associados em seu projeto Xcode {#step-1c}

Antes de prosseguir, certifique-se de que o projeto do Xcode tenha a mesma equipe selecionada em que você acabou de registrar o App Identifier. 

1. No Xcode, acesse a guia **Recursos** de seu arquivo de projeto.
2. Ative a opção **Associated Domains (Domínios associados**).

##### Dica para solução de problemas

Se você vir o erro "Um App ID com o identificador 'your-app-id' não está disponível. Por favor, digite uma string diferente", faça o seguinte:

1. Verifique se você selecionou a equipe correta.
2. Verifique se o Bundle ID[(etapa 1a](#step-1a)) do seu projeto Xcode corresponde ao usado para registrar o identificador de apps.

#### Etapa 1d: Adicionar o direito de domínio

Na seção de domínios, adicione a tag de domínio apropriada. Você deve prefixá-la com `applinks:`. Nesse caso, você pode ver que adicionamos `applinks:yourdomain.com`.

![]({% image_buster /assets/img_archive/universal_links_1d.png %})

#### Etapa 1e: Confirme se o arquivo de direitos está incluído na compilação

No navegador de projetos, confira se o seu novo arquivo de direitos está selecionado em **Inscrição de destino**.

O Xcode deve lidar com isso automaticamente.

### Etapa 2: Configure seu site para hospedar o arquivo AASA

Para associar o domínio do seu site ao seu app nativo no iOS, é necessário hospedar o arquivo Apple App Site Association (AASA) em seu site. Esse arquivo serve como uma maneira segura de verificar a propriedade do domínio para o iOS. Antes do iOS 9, os desenvolvedores podiam registrar qualquer esquema de URI para abrir seus apps, sem nenhuma verificação. Entretanto, com a AASA, esse processo se tornou muito mais seguro e confiável.

O arquivo AASA contém um objeto JSON com uma lista de apps e as jornadas de URL no domínio que devem ser incluídas ou excluídas como links universais. Aqui está um exemplo de arquivo AASA:

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

- `appID`: Criado combinando o **ID** da **equipe** do seu app (acesse `https://developer.apple.com/account/#/membership/` para obter o ID da equipe) e o **identificador do pacote**. No exemplo acima, "JHGFJHHYX" é o ID da equipe e "com.facebook.ios" é o ID do pacote.
- `paths`: Matriz de strings que especificam quais jornadas são incluídas ou excluídas da associação. Você pode usar `NOT` antes do caminho para desativar as jornadas. Neste exemplo, todos os links nessa jornada acessarão a Web em vez de abrir o app. Você pode usar `*` como um curinga para ativar todas as jornadas em um diretório e `?` para corresponder a um único caractere (como /archives/201?/ para corresponder a todos os números de 2010-2019).

{% alert note %}
Essas strings diferenciam maiúsculas de minúsculas, e as strings de consulta e os identificadores de fragmento são ignorados.
{% endalert %}

### Etapa 3: Hospede o arquivo AASA em seu domínio

Quando o arquivo AASA estiver pronto, você poderá hospedá-lo em seu domínio em `https://<<yourdomain>>/apple-app-site-association` ou em `https://<<yourdomain>>/.well-known/apple-app-site-association`.

Faça upload do arquivo `apple-app-site-association` em seu servidor da Web HTTPS. Você pode colocar o arquivo na raiz do seu servidor ou no subdiretório `.well-known`. Não anexe `.json` ao nome do arquivo.

{% alert important %}
O iOS só tentará obter o arquivo AASA por meio de uma conexão segura (HTTPS).
{% endalert %}

Ao hospedar o arquivo da AASA, confira se ele segue estas diretrizes:

- É servido por HTTPS.
- Usa o tipo MIME `application/json`.
- Não excede 128 KB (requisito a partir do iOS 9.3.1)

### Etapa 4: Prepare seu app para lidar com links universais

Quando um usuário toca em um link universal em um dispositivo iOS, o dispositivo inicia o app e envia a ele um objeto [NSUserActivity](https://developer.apple.com/documentation/foundation/nsuseractivity). O app pode então consultar o objeto NSUserActivity para determinar como ele foi iniciado.

Para oferecer suporte a links universais em seu app, siga as etapas a seguir:

1. Adicione um direito que especifique os domínios que seu app suporta.
2. Atualize o delegado do app para responder adequadamente quando receber o objeto NSUserActivity.

No Xcode, abra a seção **Associated Domains (Domínios associados** ) na guia **Capabilities (Recursos)** e adicione uma entrada para cada domínio compatível com seu app, com o prefixo `applinks:`. Por exemplo, `applinks:www.mywebsite.com`.

{% alert note %}
A Apple recomenda limitar essa lista a não mais que 20 ou 30 domínios.
{% endalert %}

### Etapa 5: Teste seu link universal

Adicione o link universal a um e-mail e envie-o para um dispositivo de teste. Colar um link universal diretamente no campo de URL do Safari não fará com que o app seja aberto automaticamente. Se fizer isso, você terá que puxar manualmente o site para baixo para que apareça um prompt na parte superior solicitando que você abra o respectivo app.

{% endtab %}

<!--Android instructions-->
{% tab Android %}

Essas etapas foram adaptadas da documentação para desenvolvedores do Android. Para saber mais, consulte [Adicionar links de aplicativos Android](https://developer.android.com/training/app-links#add-app-links) e [Criar deep linking para o conteúdo do aplicativo](https://developer.android.com/training/app-links/deep-linking).

{% alert note %}
Os links de apps para Android exigem um `IBrazeDeeplinkHandler` personalizado com lógica para lidar com links de seus domínios separadamente de outros URLs da Web. Em vez disso, pode ser mais fácil usar deep linking e manter as práticas de linking uniformes para outros canais além do envio de e-mail.
{% endalert %}

### Etapa 1: Criar deep linking

Primeiro, você precisa criar deep links para seu app Android. Isso pode ser feito adicionando [filtros de intenção](https://developer.android.com/guide/components/intents-filters) em seu arquivo `AndroidManifest.xml`. O filtro de intenção deve incluir a ação `VIEW` e a categoria `BROWSABLE`, juntamente com o URL do seu site no elemento de dados.

### Etapa 2: Associe seu app ao seu site

Você precisa associar seu app ao seu site. Isso pode ser feito com a criação de um arquivo Digital Asset Links. Esse arquivo deve estar no formato JSON e inclui detalhes sobre os apps para Android que podem abrir links para o seu site. Ele deve ser colocado no diretório `.well-known` de seu site.

### Etapa 3: Atualize o arquivo de manifesto do app

Em seu arquivo `AndroidManifest.xml`, adicione um elemento de metadados dentro do elemento do aplicativo. O elemento de metadados deve ter uma atribuição `android:name` de "asset_statements" e uma atribuição `android:resource` que aponte para um arquivo de recursos com uma matriz de strings que inclua o URL de seu site.

### Etapa 4: Prepare seu app para lidar com deep linkings

No seu app para Android, você precisa lidar com os deep links recebidos. Você pode fazer isso obtendo a intenção que iniciou sua atividade e extraindo os dados dela.

### Etapa 5: Teste de seus deep links

Por fim, você pode testar seus deep linkings. Enviar um link para si mesmo por meio de um aplicativo de mensagens ou e-mail e clicar nele. Se tudo estiver configurado corretamente, ele deverá abrir seu app.

{% endtab %}
{% endtabs %}

## Links universais, links de apps e rastreamento de cliques

{% alert note %}
Os links de rastreamento de cliques geralmente são configurados como parte de sua integração para envio de e-mail. Se isso não tiver sido concluído durante a integração do cliente, entre em contato com seu gerente de conta para obter ajuda.
{% endalert %}

Nossos parceiros de envio de e-mail, SendGrid e SparkPost, usam domínios de rastreamento de cliques para envolver todos os links e incluir parâmetros de URL para rastreamento de cliques nos e-mails do Braze.

Por exemplo, um link como `https://www.example.com` se torna algo como `https://links.email.example.com/uni/wf/click?upn=abcdef123456…`.

Para permitir que os links de e-mail com rastreamento de cliques funcionem como links universais ou App Links, você precisará realizar algumas configurações adicionais. Certifique-se de adicionar o domínio de rastreamento de cliques (`links.email.example.com`) como um domínio que o app tem permissão para abrir. Além disso, o domínio de rastreamento de cliques deve servir os arquivos AASA (iOS) ou Digital Asset Links (Android). Isso ajudará a garantir que os links de e-mail com rastreamento de cliques funcionem perfeitamente.

Se não quiser que cada link de rastreamento de cliques seja um link universal ou um App Link, você poderá especificar quais links devem ser links universais com base no parceiro de envio de e-mail. Consulte as seções a seguir para saber mais.

### SendGrid

Para tratar um link de rastreamento de cliques da SendGrid como um link universal:

1. Configure seus valores pathPrefix do AASA ou do AndroidManifest para tratar apenas links com `/uni/` na jornada do URL como links universais.
2. Adicione a atribuição `universal="true"` à tag âncora de seu link (`<a>`). Isso altera a jornada do URL do link agrupado para incluir `/uni/`.

{% alert note %}
Para e-mails AMP, essa atribuição deve ser data-universal="true".
{% endalert %}

Por exemplo:

```html
<a href=”https://www.example.com” universal="true">
```

{:start="3"}
3\. Certifique-se de que seu app esteja configurado para lidar corretamente com os links agrupados. Consulte o artigo da SendGrid sobre [Resolução de links de rastreamento de cliques da SendGrid](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-sendgrid-click-tracking-links) e siga as etapas para seu sistema operacional. Este artigo contém um código de exemplo para [iOS](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-ios) e [Android](https://docs.sendgrid.com/ui/sending-email/universal-links#resolving-links-in-android).

Com essa configuração, os links com `/uni/` na jornada do URL funcionarão como links universais, enquanto todos os outros links funcionarão como links da Web.

### SparkPost

Para tratar um link de rastreamento de cliques do SparkPost como um link universal, adicione o seguinte atributo à seção Atributos do editor de arrastar e soltar para e-mail ou edite manualmente o HTML do link para incluir o seguinte atributo na tag âncora do seu link: `data-msys-sublink="custom_path"`.

Essa jornada personalizada permite que você trate seletivamente os URLs com esse valor como um link universal.

Por exemplo:

```html
<a href=”https://www.example.com” data-msys-sublink="open-in-app">
```

Em seguida, confira se seu app está configurado para lidar corretamente com a jornada personalizada. Consulte o artigo do SparkPost sobre [como usar o rastreamento de cliques do SparkPost em deep links](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#preferred-solution-using-sparkpost-click-tracking-on-deep-links). Este artigo contém um código de exemplo para [iOS](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#ios-swift-forwarding-clicks-to-sparkpost) e [Android](https://support.sparkpost.com/docs/tech-resources/deep-links-self-serve#forwarding-clicks-from-android-to-sparkpost).

### Desativar o rastreamento de cliques em uma base de link a link

É possível desativar o rastreamento de cliques para links específicos adicionando código HTML à mensagem de e-mail para o editor de HTML ou a um bloco HTML para o editor de arrastar e soltar.

#### SendGrid

Se o seu provedor de e-mail for o SendGrid, use o código HTML `clicktracking=off` desta forma:

```HTML
<a clicktracking=off href="[INSERT https LINK HERE]">click here</a>
```

#### SparkPost 

Se o seu provedor de serviço de e-mail for o SparkPost, use o código HTML `data-msys-clicktrack="0"` desta forma:

```HTML
<a data-msys-clicktrack="0" href="[INSERT https LINK HERE]">click here</a>
```

#### Amazon SES

Se o seu provedor de serviço de e-mail for o Amazon SES, use o código HTML `ses:no-track` desta forma:

```HTML
<a ses:no-track href="[INSERT https LINK HERE]">click here</a>
```

#### Editor de arrastar e soltar

Ao usar o editor de arrastar e soltar de e-mail, insira seu código HTML como um atributo personalizado se o link estiver anexado ao texto, a um botão ou a uma imagem.

##### Atributo personalizado para um link de texto

#### SendGrid

Selecione o seguinte para o atributo personalizado:

- **Nome:** `clicktracking`
- **Valor:** `off`

#### SparkPost

Selecione o seguinte para o atributo personalizado:

- **Nome:** `data-msys-clicktrack`
- **Valor:** `0`

![Um atributo personalizado para um link de texto.]({% image_buster /assets/img/text_click_tracking_off.png %}){: style="max-width:60%;"}

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

![Um atributo personalizado para um botão.]({% image_buster /assets/img/button_click_tracking_off.png %}){: style="max-width:60%;"}

### Solução de problemas de links universais com rastreamento de cliques

Se os links universais não estiverem funcionando como esperado em seus e-mails, por exemplo, navegando o destinatário do aplicativo de e-mail para o navegador da Web antes de finalmente ser redirecionado para o app, consulte estas dicas para solucionar problemas de configuração do link universal.

#### Verificar o local do arquivo de link

Certifique-se de que o arquivo AASA (iOS) ou o arquivo Digital Asset Links (Android) esteja localizado no lugar correto:

- **iOS:** `https://click.tracking.domain/.well-known/apple-app-site-association`
- **Android:** `https://click.tracking.domain/.well-known/assetlinks.json`

É importante garantir que esses arquivos estejam sempre acessíveis ao público. Se não conseguir acessá-los, talvez tenha perdido uma etapa na configuração de links universais para e-mail.

#### Verificar definições de domínio

Certifique-se de ter as definições corretas para os domínios que seu app tem permissão para abrir.

- **iOS:** Revise os domínios associados configurados no Xcode para seu app[(etapa 1c]({{site.baseurl}}/help/help_articles/email/universal_links/?tab=ios#step-1c)). Verifique se o domínio de rastreamento de cliques está incluído nessa lista.
- **Android:** Abra a página de informações do aplicativo (mantenha pressionado o ícone do aplicativo e clique em ⓘ). No menu de informações do app, localize **Abrir por padrão** e toque nele. Isso deve mostrar uma tela com todos os links verificados que o app tem permissão para abrir. Verifique se o domínio de rastreamento de cliques está incluído nessa lista.

