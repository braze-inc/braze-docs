# Overview

The Braze Android SDK natively supports displaying in-app messages on OTT devices like Android TV or Fire Stick.

#### Key differences

Some key differences exist in the display of standard in-app messages between native and OTT devices.

For OTT devices:

* In-app messages that require touch mode (such as Slideup) are disabled on OTT.
* The currently selected/focused item, such as a button or close button, will be highlighted.
* Body clicks on the in-app message itself, i.e. not on a button, are not supported.


