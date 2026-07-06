[![PyPI](https://img.shields.io/pypi/v/toshiba-ac-community.svg)](https://pypi.org/project/toshiba-ac-community/)
[![Github Release](https://img.shields.io/github/release/vmvelev/Toshiba-AC-control.svg)](https://github.com/vmvelev/Toshiba-AC-control/releases)
[![Github Open Issues](https://img.shields.io/github/issues/vmvelev/Toshiba-AC-control.svg)](https://github.com/vmvelev/Toshiba-AC-control/issues)
[![Github Open Pull Requests](https://img.shields.io/github/issues-pr/vmvelev/Toshiba-AC-control.svg)](https://github.com/vmvelev/Toshiba-AC-control/pulls)

# Toshiba AC control (community)

Python library to control Toshiba AC units over Toshiba's cloud service - HTTP login, device discovery, and real-time state updates over AMQP.

This is the community-maintained protocol library behind the [Toshiba AC (Community)](https://github.com/vmvelev/home-assistant-toshiba_ac) Home Assistant integration. It is published on PyPI as **`toshiba-ac-community`**; the Python import name is `toshiba_ac`.

Originally created by [Kamil Sroka (KaSroka)](https://github.com/KaSroka/Toshiba-AC-control) - full credit for the protocol work. This repository is maintained independently so fixes and improvements can ship on their own schedule.

## Installation

```
pip3 install toshiba-ac-community
```

> Note: this package pins the pre-release `azure-iot-device==2.15.0rc1`. Installers that refuse pre-release transitive dependencies (e.g. `uv`) need `azure-iot-device==2.15.0rc1` installed first, or pre-releases enabled.

### Installation for development

1. Clone this repository:

    `git clone https://github.com/vmvelev/Toshiba-AC-control.git`

2. Install the package (editable if you want to edit the code):

    `pip3 install -e .`

## Usage

```python
from toshiba_ac.device_manager import ToshibaAcDeviceManager

device_manager = ToshibaAcDeviceManager(username, password)
sas_token = await device_manager.connect()
devices = await device_manager.get_devices()
```

## Sample script

Sample GUI application `samples/toshiba_ac_gui.py` demonstrates usage of this package. It allows switching basic functionalities of the AC and shows current status.

It requires env variables with login information:

```
TOSHIBA_USER=<USER_NAME> TOSHIBA_PASS=<PASSWORD> python3 toshiba_ac_gui.py
```

## Reporting issues

- Library / device communication issues: [open an issue here](https://github.com/vmvelev/Toshiba-AC-control/issues)
- Home Assistant integration issues: [home-assistant-toshiba_ac](https://github.com/vmvelev/home-assistant-toshiba_ac/issues)

## License

[Apache-2.0](LICENSE.txt), same as the original project.
