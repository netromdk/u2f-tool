#!/bin/sh

OS=$(uname -s)
case "${OS}" in
  Darwin)
    brew install libusb
    ;;

  *)
    echo "Unknown how to setup deps for '${OS}'!"
    ;;
esac
