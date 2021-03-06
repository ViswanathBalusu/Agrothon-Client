<div align="center">
<h1>Agrothon Client</h1>
<h3>A Client for Agrothon Running in Raspberry Pi</h3>
<a href="https://pypi.org/project/AgroClient"><img alt="PyPI" src="https://img.shields.io/pypi/v/AgroClient?style=for-the-badge"></a>
<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/AgroClient?style=for-the-badge">
<img alt="PyPI - Wheel" src="https://img.shields.io/pypi/wheel/AgroClient?style=for-the-badge">
<img alt="PyPI - Implementation" src="https://img.shields.io/pypi/implementation/AgroClient?style=for-the-badge">
<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/AgroClient?style=for-the-badge">
<a href="https://github.com/viswanathbalusu/Agrothon-Client/blob/main/LICENSE"><img alt="GitHub license" src="https://img.shields.io/github/license/ViswanathBalusu/Agrothon-Client?style=for-the-badge"></a>
<a href="https://github.com/ViswanathBalusu/Agrothon-Client/issues"><img alt="GitHub issues" src="https://img.shields.io/github/issues/ViswanathBalusu/Agrothon-Client?style=for-the-badge"></a>
<a href="https://github.com/ViswanathBalusu/Agrothon-Client/network"><img alt="GitHub forks" src="https://img.shields.io/github/forks/ViswanathBalusu/Agrothon-Client?style=for-the-badge"></a>
<a href="https://github.com/ViswanathBalusu/Agrothon-Client/stargazers"><img alt="GitHub stars" src="https://img.shields.io/github/stars/ViswanathBalusu/Agrothon-Client?style=for-the-badge"></a>

</div>

## Installation
- First Install the dependencies
    ```
    sudo apt-get update
    sudo apt-get install python3-opencv python3-rpi.gpio
    ```
- from Pypi

    ```
    pip3 install AgroClient
    ```
- From git

  ```
  pip3 install -U git+https://github.com/viswanathbalusu/Agrothon-Client
  ```
- Using Docker
  - First install docker
  
    ```
    curl -sSL https://get.docker.com | sudo sh
    sudo usermod -aG docker ${USER}
    ```
  - Get the `docker-compose.yml` and `agrothonclient.env` to a local directory

    ```
    wget -q https://raw.githubusercontent.com/viswanathbalusu/Agrothon-Client/main/docker-compose.yml
    wget -q https://raw.githubusercontent.com/viswanathbalusu/Agrothon-Client/main/agroclient-sample.env -O agroclient.env
    ```
  - Edit the Variables in agroclient.env and start docker container

    ```
    pip3 -q install docker-compose
    docker-compose up -d
    ```
  - Docker method only works on `linux/arm/v7`, `linux/arm64/v8`, `linux/amd64` (CPU) architecture

## Usage

```
usage: AgroClient [-h] -y HOSTNAME -a APIKEY [-u USB] [-p1 PIR1] [-p2 PIR2]
                  [-p3 PIR3] [-p4 PIR4] [-br BAUDRATE] [-r RELAY]

optional arguments:
  -h, --help, show this help message and exit
  -y, --hostname HOSTNAME, API Server host name
  -a, --apikey APIKEY, API Key of host
  -u, --usb USB, USB Port of Arduino
  -p1, --pir1 PIR1, GPIO Pin of PIR1
  -p2, --pir2 PIR2, GPIO Pin of PIR2
  -p3, --pir3 PIR3, GPIO Pin of PIR3
  -p4, --pir4 PIR4, GPIO Pin of PIR4
  -br, --baudrate BAUDRATE, Baud rate of USB Port to read sensor data
  -r, --relay RELAY, Relay Signalling GPIO pin
```

## Circuit Diagram

![Circuit](https://raw.githubusercontent.com/viswanathbalusu/Agrothon-Client/main/images/CircuitDiagram.jpg)

## Hardware

![Hardware](https://raw.githubusercontent.com/viswanathbalusu/Agrothon-Client/main/images/projecthardware.jpg)
## Pin Configuration (Default)

- **Raspberry Pi**

    | GPIO | Device | Use | Mode |
    | :---: | :---: | :---: | :---: |
    | `12` | Relay | To Switch on/off Relay | OUT |
    | `25` | PIR1 | Motion Detection | IN |
    | `8` | PIR2 | Motion Detection | IN |
    | `7` | PIR3 | Motion Detection | IN |
    | `1` | PIR3 | Motion Detection | IN |

- **Arduino nano**

    | Pin | Device | Device pin | Mode |
    | :---: | :---: | :---: | :---: |
    | `A0` | Moisture Sensor* | Analog Out | IN |
    | `D12` | DHT11 | Signal | IN |
  
    ```* For multiple sensors use differnet Analog pins```

- Connect the Pi camera to CSI Port
- Use SSH to access the terminal and run the Python Code
- Connect all the `Vdd's` and `GND's` to 5V and GND (or as per instructions given in spec sheet)

## Note
- To get the USB Device ID, Use
    ```
    ls /dev/tty*
    ```
    Most Probably the Value will be `/dev/ttyUSB0`

- Sensor data should be sent in the following pattern
  
    ```
    mositure1,moisture2,moisture3, .... ,moistureN, Temperature,Humidity
    ex : 55.29,52.59,32.5,65.26
    ```
