#!/usr/bin/env python3
import usb.core as C

print("Detecting YubiKeys..")
yubikeys = list(C.find(idVendor=0x1050, find_all=1))
if len(yubikeys) > 0:
  for yubikey in yubikeys:
    print("  {} (0x{:x}) from {} (0x{:x}) with ID=0x{:0x}".format(
      yubikey.product, yubikey.iProduct, yubikey.manufacturer, yubikey.iManufacturer,
      yubikey.idProduct))
else:
  print("None found..")
