---
nav_title: Configuração inicial do SDK com o Eclipse
page_order: 1

page_type: update
description: "Este artigo arquivado descreve como realizar uma configuração inicial do SDK com o Eclipse. O Braze descontinuou o suporte ao Eclipse IDE."
---

# Configuração inicial do SDK com o Eclipse

{% alert update %}
A Braze removeu o suporte ao Eclipse IDE devido ao fato de [o Google ter encerrado o suporte ao plug-in do Eclipse Android Developer Tools](http://android-developers.blogspot.com/2015/06/an-update-on-eclipse-android-developer.html). Se precisar de ajuda com a integração com o Eclipse antes da migração, [envie um e-mail para o Suporte]({{site.baseurl}}/support_contact/) para obter assistência.
{% endalert %}

## Etapa 1
Em sua linha de comando, clone o [repositório GitHub da Braze para Android][03].

```bash
$ git clone git@github.com:braze-inc/braze-android-sdk.git
```

## Etapa 2
Importe o projeto Braze em seu espaço de trabalho local

Em Eclipse:

  - Acesse Arquivo > Importar.

    ![Importação de arquivos][04]
  - Selecione Android > Código Android existente no espaço de trabalho.

    ![Importação para Android][05]
  - Clique em "Navegar".

    ![Navegar][06]
  - Verifique a pasta do projeto Braze UI e a opção "copy project into workspace" e clique em "Finish".

    ![Selecione Android UI Project][07]

## Etapa 3
Faça referência ao Braze em seu próprio projeto.
Em Eclipse:

  - Clique com o botão direito do mouse em seu projeto e selecione "Propriedades".

    ![Clique em Propriedades][08]
  - Em "Android", clique em "Add..." (Adicionar...) na seção Library (Biblioteca) e adicione android-sdk-ui como uma biblioteca ao seu app.

    ![Braze Add][09]

## Etapa 4
Resolver erros de dependência e corrigir o direcionamento da compilação.

Nesse momento, você poderá ver erros no código da Braze, porque suas dependências não estão preenchidas e o direcionamento da compilação está possivelmente incorreto:

   - Clique com o botão direito do mouse no projeto Braze UI e selecione Properties->Android para garantir que o direcionamento da compilação esteja definido para a versão atual das ferramentas de compilação do Braze.

      ![Construir direcionamento][10]
   - Clique com o botão direito do mouse no projeto Braze UI e selecione Propriedades->Java Build Path->Adicionar JARs... e adicione 'android-support-v4.jar' do aplicativo principal como uma biblioteca.

      ![Suporte][11]

## Etapa 5

Adicione as peças finais.

  - Para a versão 1.10.0 ou superior do SDK, você precisará adicionar
  `<service android:name="com.appboy.services.AppboyDataSyncService" />`
  em seu site AndroidManifest.xml, pois o Eclipse não oferece suporte à mesclagem de manifestos.

  - Para a versão 1.7.0 ou superior do SDK, você precisará copiar "assets/fontawesome-webfont.ttf" do nosso projeto de biblioteca para o seu aplicativo. O Eclipse não inclui automaticamente a pasta de ativos das bibliotecas.

[03]: https://github.com/braze-inc/braze-android-sdk "Repositório GitHub do Appboy para Android"
[04]: {{site.baseurl}}/assets/img_archive/file_import.png
[05]: {{site.baseurl}}/assets/img_archive/android_import.png
[06]: {{site.baseurl}}/assets/img_archive/click_browse.png
[07]: {{site.baseurl}}/assets/img_archive/select_project_android.png
[08]: {{site.baseurl}}/assets/img_archive/click_properties.png
[09]: {{site.baseurl}}/assets/img_archive/add_appboy_ui.png
[10]: {{site.baseurl}}/assets/img_archive/build_target.png
[11]: {{site.baseurl}}/assets/img_archive/android_support_v4.png
