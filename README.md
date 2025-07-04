# Raspberry Pi Cluster
## Sheffield Hallam University

##### Jonathan Zasada-James (GitHub: jzasjam)

-----------------------------------
## General Overview and Setup

Download or Clone the repository files to a chosen directory.

Follow the below Client and Server(s) cluster setup instructions for Raspberry Pi's & SenseHAT's with browser based UI to test the cluster by illuminating the LED's - based on the [OctaPi Client Setup Instructions](https://projects.raspberrypi.org/en/projects/build-an-octapi/3)

--------------------------------------------------------
## Client Install
**Install the below to a Raspberry Pi - this will be the 'Client' to distribute jobs to the 'Servers'**

If [Python](https://www.python.org/downloads) is not installed...

> Install [Python](https://www.python.org/downloads)

### Client: Cluster Management Dependencies

**Install the libraries which support distributing jobs to the cluster / servers / nodes**

Dispy: `sudo pip3 install dispy`

*Note: If issues with 'Managed Environment' run the below, then do 'sudo pip install package-name'...*

`sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.old`

### Client: UI Dependencies
**These installations are required to create the UI web server with NodeJS**

> Install [NodeJS](https://nodejs.org)...

`curl -sL https://deb.nodesource/setup_18.x | sudo -E bash -`

then: `sudo apt install -y nodejs`

check with: `node -v`

**Install NPM...**

`sudo apt-get -f install npm`

**Install NodeJS Modules...**

Node HTTP Server: `sudo npm install -g http-server`

Socket.io `sudo npm install socket.io`

Sense Hat LED: `sudo npm install sense-hat-led`

Python Shell `sudo npm install python-shell`

*NOTE: Check versions with the below (replacing the package-name)*
>`node -v package-name`

--------------------------------------------------------
## Server Install 
**Install the below to a Raspberry Pi - this will be a 'Server / Node' to execute distributed jobs from the 'Client'. You can then repeat these steps on other Raspberry Pi's or clone the SD to add additional Servers/Nodes to your cluster**

***NOTE: Each Server / Node will require any Python libraries or modules required for jobs to be pre-installed before running the cluster***

*Note: Servers / Nodes can be cloned (eg Raspberry Pi SD cards using an [SD Cloning Tool](https://etcher.balena.io))*

If [Python](https://www.python.org/downloads) is not installed...

> Install [Python](https://www.python.org/downloads)

### Server: Cluster Node Dependencies
**Install libraries which support the cluster / servers / nodes**

Dispy: 
`sudo pip3 install dispy`

PsUtil: 
`sudo pip3 install psutil`

*Note: If you have issues with 'Managed Environment' run the below, then do 'sudo pip install package-name'...*

`sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.old`

--------------------------------------------------------
## How To Use:

1. Have at least 1 Server / Node switched on and connected to the same network as the Client

2. In the terminal of the Client, cd to the directory you downloaded/extracted or moved the repository
*eg:* `cd Downloads/shu-pi-cluster`

3. Run The UI `node index.js` or double click `start-ui.sh` (you may need to make this executable `chmod +x start-ui.sh`)

4. In browser on same network as client, go to http://[YOUR-CLIENT-IP]:8080 or http://[YOUR-CLIENT-HOSTNAME]:8080 to view the UI
  This allows you to...

   - Test Fog Node cluster
   - Test Client LEDs

![SHU Pi Cluster UI](https://github.com/user-attachments/assets/d94687f8-10b3-4182-8c67-2aa6e0d4bc29)

or

1. Run the script

Test the Cluster / Nodes / Servers (Jobs illuminate the SenseHAT LEDs and sleep for a random number of seconds)
>`python cluster-leds.py`



--------------------------------------------------------
## Client Troubleshooting:

### **Stop Client Dispy Cluster** (if job gets stuck / servers not responding) ### 

1. Get the processID 
> `lsof -i:9700`

2. Kill the process 
> `kill -9 <ProcessID>`
--------------------------------------------------------

## Server Troubleshooting:

### **Start a Server Node** (if fails to start automatically) ### 

SSH to node, then (replacing IP for node IP) 
> `sudo dispynode.py -i 192.168.xxx.xxx --clean`
--------------------------------------------------------


### **Stop a Server Node** ### 

1. Get the process id (replacing IP for node IP) 
> `sudo dispynode.py -i 192.168.xxx.xxx`
or 
> `pgrep -f dispynode`

2. Kill the process 
> `sudo kill -9 <ProocessID>`
--------------------------------------------------------


### **Start / Stop Server Node on Startup** ### 
 
> Edit the last line of the user crontab file... `sudo nano /var/spool/cron/crontabs/Fognode1`

> Comment / Delete / Add... `@reboot sudo /home/pi/start_dispynode.sh`

> Reboot `sudo reboot now`

1. Create a startup script named ‘***start_dispynode.sh***’ and save somewhere like ‘***home/{username}/dispynode***’

2. Add the below to the file...
> #!/bin/sh -e

> sleep 30

> _IP=$(hostname -I | awk ‘{print $1}’)

> dispynode.py -i $_IP –-daemon

3. Make the script executable...
> chmod +x start_dispynode.sh

4. Open the user crontab file... 
> crontab -e

5. Add this to the final line of the file (editing the file path if needed) to start the server on boot or Comment / Delete to stop... 
> @reboot sudo /home/{username}/dispynode/start_dispynode.sh

6. Reboot… 
> sudo reboot now
--------------------------------------------------------
