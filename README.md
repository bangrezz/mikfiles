<p align="center">
  <a href="" rel="noopener">
 <img width=400px height=100px src="img/Screenshot_20240131_110445.png" alt="Project logo"></a>
</p>

<h3 align="center">mikfiles</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
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
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>
![Alt text](img/Screenshot_20240131_110818.png)
Mikfiles can download :
- Log file
- Configuration file
- Backup file 
#### And support for automation download with Linux cron


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

How to use mikfiles to downloading file
- if you using Linux and want to edit cron
```
sudo python3 mikfiles.py
```
- if you using Linux, Windows, macOS, or Android (via Termux)
```
python3 mikfiles.py
```
First select format hostname, 1 or 2. Then select menu for downloading files. Example to download export file and backup file, select 2.
<video src="img/select%20menu.mp4" controls title="Title"></video>
Next input username, password, port, and IP Address. You can input port and IP Address more than 1 with split by ','. Default port is 22 and you can press enter if default port.
<video src="img/Attempt%20to%20login%201.mp4" controls title="<vid>"></video>
<video src="img/Attempt%20to%20login%202.mp4" controls title="Title"></video>
Finally the files has been downloaded. You can export again, download other file (Example log or other), and exit.

## ⛏️ Built Using <a name = "built_using"></a>

- 🐍 [Python](https://www.python.com/) - All code using python

## ✍️ Authors <a name = "authors"></a>

- [@bangrezz](https://github.com/kylelobo) - Idea & Initial work

See also the list of [contributors](https://github.com/kylelobo/The-Documentation-Compendium/contributors) who participated in this project.

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- MikfoTik Wiki https://wiki.mikrotik.com/wiki/Main_Page
