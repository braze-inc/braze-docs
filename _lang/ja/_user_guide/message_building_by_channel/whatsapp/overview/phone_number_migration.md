---
nav_title: WhatsApp電話番号の移行
article_title: WhatsApp電話番号の移行
page_order: 2
description: "この記事では、WhatsAppの電話番号を移行する方法について説明します。"
page_type: reference
channel:
  - WhatsApp
---

# WhatsApp電話番号の移行

> Metaの埋め込みサインアップを使用して、WhatsApp Businessアカウント間でWhatsAppの電話番号を移行します。

## 前提条件

お客様の電話番号は、移行の対象となるためにMetaの要件を満たしている必要があります。

- あなたのMetaビジネスアカウントは確認されました。
- お客様の既存のWhatsAppビジネスアカウントが承認されました。
- お客様の既存のWhatsAppビジネスアカウントには、**支払い設定**に有効な支払い方法があります。
- あなたのビジネス電話番号は二段階認証がオフになっています。WhatsApp ビジネスアカウントを所有している場合、WhatsApp マネージャーで番号の二段階認証をオフにすることができます。それ以外の場合は、ソリューションプロバイダーに依頼してオフにしてもらう必要があります。

WhatsAppの電話番号の移行に関する情報については、Metaの[埋め込みサインアップを介したWhatsAppビジネスアカウント間の電話番号の移行](https://developers.facebook.com/docs/whatsapp/business-management-api/guides/migrate-phone-to-different-waba/)に関するドキュメントを参照してください。

## WhatsApp電話番号の移行

1. WhatsAppマネージャーで、電話番号に関連付けられているWhatsAppビジネスアカウント（WABA）を選択し、**アカウントツール** > **電話番号**に移動します。
2. **二段階認証をオフにする**を選択し、続くステップを完了します。<br><br>![WhatsAppビジネスマネージャーが「電話番号」ページを開きました。][1]{: style="max-width:80%;"}<br><br> 電話番号を別のWhatsAppビジネスグループに移行していて、Metaの埋め込みサインアップで表示名が一致する必要がある場合は、**電話番号**ページに既存の表示名をメモしてください。次のステップでその名前を入力します。<br><br>![WhatsAppビジネスマネージャーの電話番号ページに、電話番号の横に「Braze」という表示名が記載されています。]({% image_buster /assets/img/whatsapp/phone_numbers.png %}){: style="max-width:80%;"}<br><br>
3. Metaの埋め込みサインアップワークフローを完了まで続けます。 

[1]: {% image_buster /assets/img/whatsapp/waba_manager.png %}