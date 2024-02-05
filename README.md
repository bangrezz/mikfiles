<p align="center">
  <a href="" rel="noopener">
 <img width=400px height=100px src="img/Screenshot_20240131_110445.png" alt="Project logo"></a>
</p>

<h3 align="center">mikfiles</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/bangrezz/mikfiles)](https://github.com/bangrezz/The-Documentation-Compendium/issues)
![GitHub closed issues](https://img.shields.io/github/issues-closed/bangrezz/mikfiles?color=purple)
![GitHub Release](https://img.shields.io/github/v/release/bangrezz/mikfiles?color=teal)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> MikroTik downloader for log file, configuration file, and backup file with automatic cron.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Built Using](#built_using)
- [Authors](#authors)
- [Gallery]()
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
![Alt text](img/Screenshot_20240131_110818.png)

Mikfiles can download :
- Log file
- Configuration file
- Backup file 
#### And support for automation download with Linux cron
![Alt text](img/Screenshot_20240131_111819.png)
This can add, edit, delete, enable, disable cron configuration. But, "add" menu only can 1 cron to add.

## 🏁 Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

Mikfiles currently full worked on Linux. Because it using cron to unlock feature automatic schedule downloading file. But you can try to downloading file with mikfiles using Windows, macOS, and Android (Termux) if possible.

### Installing

A step by step series of examples that tell you how to get a development env running.

Install the python on your system :
- Ubuntu/Debian
```
sudo apt install python3
```
- Fedora/RedHat
```
sudo dnf install python3
```
- Arch/Manjaro
```
pacman -S python
```
- Other OS visit ` https://www.python.org/downloads/` to spesific version


Say what the step will be

```
cd mikfiles/
pip install -r requirements.txt
```

End with an example of getting some data out of the system or using it for a little demo.

## 🎈 Usage <a name="usage"></a>

### How to use mikfiles to downloading file
- if you using Linux and want to edit cron
```
sudo python3 mikfiles.py
```
- if you using Linux, Windows, macOS, or Android (via Termux)
```
python3 mikfiles.py
```
Then follow all instructions on mikfiles

## ⛏️ Built Using <a name = "built_using"></a>

- 🐍 [Python](https://www.python.com/) - All code using python

## ✍️ Authors <a name = "authors"></a>

- [@bangrezz](https://github.com/bangrezz) - Idea & Initial work

## 🖼️ Gallery Mikfiles
![Alt text](img/Screenshot_20240131_110818.png)  
![Alt text](img/Screenshot_20240201_103310.png)
![Alt text](img/Screenshot_20240201_103434.png)
![Alt text](img/Screenshot_20240201_083443.png)  
![Alt text](img/Screenshot_20240201_103620.png)
## Automatic Download with Cron - mikfiles feature
![Alt text](img/Screenshot_20240131_111819.png) 
![Alt text](img/Screenshot_20240201_104154.png) 
![Alt text](img/Screenshot_20240205_090657.png) 
![Alt text](img/Screenshot_20240205_090848.png) 
![Alt text](img/Screenshot_20240205_090933.png) 
![Alt text](img/Screenshot_20240205_091053.png)

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- MikfoTik Wiki https://wiki.mikrotik.com/wiki/Main_Page
