{% multi_lang_include developer_guide/prerequisites/android.md %}

## About TV and OTT support

The Android Braze SDK natively supports displaying in-app messages on OTT devices like Android TV or Fire Stick. However, there's some key differences between native Android and OTT in-app messages. For OTT devices:

- In-app messages that require touch mode, such as slideup, are disabled on OTT.
- The currently selected or focused item, such as a button or close button, will be highlighted.
- Body clicks on the in-app message itself, such as not on a button, are not supported.
