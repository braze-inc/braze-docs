---
nav_title: Estilo Personalizado
article_title: Estilo de Cartão de Conteúdo Personalizado para iOS
platform: iOS
page_order: 1
description: "Este artigo cobre as opções de estilo personalizado do cartão de conteúdo para seu aplicativo iOS."
channel:
  - content cards
noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Estilo Personalizado

## Substituição de imagens padrão

{% alert important %}
A integração de `SDWebImage` é necessária se você planeja usar nossa UI do Braze para exibir imagens em mensagens no aplicativo iOS ou Cartões de Conteúdo.
{% endalert %}

Braze permite que os clientes substituam as imagens padrão existentes por suas próprias imagens personalizadas. Para realizar isso, crie um novo arquivo `png` com a imagem personalizada e adicione-o ao pacote de imagens do app. Em seguida, renomeie o arquivo com o nome da imagem para substituir a imagem padrão em nossa biblioteca. Além disso, faça o upload das versões `@2x` e `@3x` das imagens para acomodar diferentes tamanhos de telefone. Imagens disponíveis para substituição em Cartões de Conteúdo incluem:

- Imagem de espaço reservado: `appboy_cc_noimage_lrg`
- Imagem do ícone fixado: `appboy_cc_icon_pinned`

Como os Cartões de Conteúdo têm um tamanho máximo de 2 KB para o conteúdo que você insere no dashboard (incluindo texto da mensagem, URLs de imagens, links e todos os pares chave-valor), verifique o tamanho antes de enviar. Exceder esse valor impedirá o cartão de enviar.

{% alert important %}
Substituir imagens padrão atualmente não é permitido em nossa integração Xamarin iOS.
{% endalert %}

## Desativação do modo escuro

Para evitar que a interface do cartão de conteúdo adote o estilo do tema escuro quando o dispositivo do usuário estiver com o modo escuro ativado, defina a propriedade `ABKContentCardsTableViewController.enableDarkTheme`. Você pode acessar a propriedade `enableDarkTheme` diretamente em uma instância `ABKContentCardsTableViewController` ou através da propriedade `ABKContentCardsViewController.contentCardsViewController` para melhor atender à sua própria interface de usuário.

{% tabs %}
{% tab OBJECTIVE C %}

```objc
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
- (IBAction)presentModalContentCards:(id)sender {
  ABKContentCardsViewController *contentCardsVC = [ABKContentCardsViewController new];
  contentCardsVC.contentCardsViewController.enableDarkTheme = NO;
  ...
  [self.navigationController presentViewController:contentCardsVC animated:YES completion:nil];
}

// Accessing enableDarkTheme directly.
- (IBAction)presentNavigationContentCards:(id)sender {
  ABKContentCardsTableViewController *contentCardsTableVC = [[ABKContentCardsTableViewController alloc] init];
  contentCardsTableVC.enableDarkTheme = NO;
  ...
  [self.navigationController pushViewController:contentCardsTableVC animated:YES];
}
```

{% endtab %}
{% tab swift %}

```swift
// Accessing enableDarkTheme via ABKContentCardsViewController.contentCardsViewController.
@IBAction func presentModalContentCards(_ sender: Any) {
  let contentCardsVC = ABKContentCardsViewController()
  contentCardsVC.contentCardsViewController.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsVC, animated: true, completion: nil)
}

// Accessing enableDarkTheme directly.
@IBAction func presentNavigationContentCards(_ sender: Any) {
  let contentCardsTableVC = ABKContentCardsTableViewController()
  contentCardsTableVC.enableDarkTheme = false
  ...
  self.navigationController?.present(contentCardsTableVC, animated: true, completion: nil)
}
```

{% endtab %}
{% endtabs %}

