name: Build APK

on:
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-22.04

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          sudo apt-get update
          sudo apt-get install -y build-essential ccache git libncurses5:i386 libstdc++6:i386 libgtk2.0-0:i386 libpangox-1.0-0:i386 libpangoxft-1.0-0:i386 libidn11:i386 python3-dev zlib1g-dev openjdk-17-jdk autoconf libtool pkg-config patch
          python -m pip install --upgrade pip
          pip install --upgrade buildozer cython==0.29.36 kivy

      - name: Build with Buildozer
        run: |
          buildozer -v android debug

      - name: Upload APK Artifact
        uses: actions/upload-artifact@v4
        with:
          name: shipra-original-apk
          path: bin/*.apk
