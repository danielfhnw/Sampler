# Sampler

Easy Sampler in Python for Raspberry Pi. The program is tested on Raspberry Pi Model 3 B Plus and should also work for newer versions. It is based on the pygame library.

## Setting up Raspberry Pi (headless)


### 1. Flash your SD-Card with the Raspberry Pi OS (e.g. using Raspberry Pi Imager).

![image](https://user-images.githubusercontent.com/93777297/161608871-dadaef1f-ea0a-4146-a9c7-dcb367de33fa.png)


### 2. Copy an empty file named "ssh" into the boot folder. This will enable SSH on the Pi.


### 3. Copy a file named "wpa_supplicant.conf" into the boot folder. 
Change NAME to your WiFi SSID and PASS to your password. Also change XX to your countrys specific two letter code (e.g. Switzerland -> CH). This will connect the Pi to your WiFi on startup.

![image](https://user-images.githubusercontent.com/93777297/161609782-7703b352-44a9-4259-9409-90ade6945108.png)


### 4. Insert the SD-Card into your Pi and connect it to power.


### 5. Scan your WiFi network to get the IP address of your Pi (e.g. logging into your router and see connected devices).


### 6. Connect to your Pi via SSH (e.g. using PuTTY).

![image](https://user-images.githubusercontent.com/93777297/161613134-0d3ddf04-3193-4243-adfb-2d191b2a7399.png)

```
user: pi
password: raspberry
```


### 7. Go to raspi-config and enable VNC

```
sudo raspi-config
```

![image](https://user-images.githubusercontent.com/93777297/161611145-80c041c3-aa2e-41bc-a096-09033062c8b7.png)
![image](https://user-images.githubusercontent.com/93777297/161610897-0b939bb1-9fa6-4df3-9382-dcc302493e75.png)


### 8. Connect to your Pi via VNC (e.g. using VNC Viewer by RealVNC).

![image](https://user-images.githubusercontent.com/93777297/161613721-c311ff74-c689-465e-9155-87d50238d046.png)


### 9. Go through the initialisation settings.


### 10. Set the screen resolution in the settings.

![image](https://user-images.githubusercontent.com/93777297/161612843-ee4a26e1-947e-4353-8a54-b7da659550b6.png)

## Installing the Sampler


### 1. Copy the sounds, background image and python files in this repository into a folder on your Pi (e.g. /home/pi/Samper).

![image](https://user-images.githubusercontent.com/93777297/161614584-e61b3730-9255-46b1-99af-9ed8c6ecc500.png)

If you are a fan of git, then you can of course also clone the repository. ;)


### 2. Edit the startup script for desktop environements.

```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
Add the following line at the end:
```
@lxterminal -e python3 /home/pi/Sampler/sampler.py
```
This will start the sampler right when the desktop is loaded.


### 3. Disable automatic display of options when inserting a USB Drive. 
If this is not disabled and you are running the Sampler and disconnect the USB and insert it back while still running, the filesystem gets messed up and does no longer discover your USB Drive.

![image](https://user-images.githubusercontent.com/93777297/161615584-61594568-3130-4ed0-85c2-fe9c7f642d52.png)

If your Sampler does not "see" the USB when executing try removing all the Drives and remove the References with:
```
sudo rm /media/pi/SAMPLER
```


### 4. Install necessary python libraries.
```
pip3 install pygame
```

## Create own WiFi
If you do not want to supply the Pi with a WiFi network just to do some troubleshooting, the Pi can generate its own wireless network.


### 1. Install RaspAP.

```
curl -sL https://install.raspap.com | bash
```

This installation needs a few inputs (y/n) wheter you want to install additional features.

![image](https://user-images.githubusercontent.com/93777297/161617222-13bd9d0a-42ac-4df2-a91f-42256ed26404.png)


### 2. Change SSID and password in the settings (go to 10.3.141.1 in your browser).

![image](https://user-images.githubusercontent.com/93777297/161617427-2ed4b00e-f688-44bb-a72d-1f92f7b2a448.png)


### 3. Test VNC connection with new hotspot

Connect to the Sampler WiFi and open a VNC connection to 10.3.141.1.

## Sample away

### 1. Format a USB drive and name it "SAMPLER".

### 2. Load all your desired sounds to your USB drive. Do not use folders if you want to keep things easy.

### 3. Edit the SamplerConfig.csv file to your desires (e.g. using Excel). 
Take a look at the "Bedienungsanleitung" if you are having trouble.

### 4. Connect your USB drive to the Pi.

### 5. Connect a wireless numeric keypad (e.g. LogiLink ID0120)

![image](https://user-images.githubusercontent.com/93777297/161619455-37b84bea-a0ae-454f-94d8-fb0b780d6caa.png)

### 6. Connect loudspeakers to the AUX Port. 
You can alternatively connect your loudspeakers via Bluetooth.

### 7. Connect your Pi to power and wait for it to say "Hello".

### 8. Enjoy. :D
- You do not have to be connected to your Pi with a smartphone or a laptop to use it as a Sampler.
- You can close the Sampler when connected via VNC with the X in the top right corner. Then your Pi behaves like any other until you restart it.
- You can see the program output in the commandline when connected to the pi via VNC, if you move the Window to the side.
- If you want your changes in the SamplerConfig to take effect, you have to restart the Sampler.
