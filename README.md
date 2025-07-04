# Raspberry Pi Cluster
## Sheffield Hallam University

##### Jonathan Zasada-James (GitHub: jzasjam)

-----------------------------------
## General Overview and Setup

Download or Clone the repository files to a chosen directory.

--------------------------------------------------------
## Client Install Dependencies
Basic Reqirements or the project and UI

> Install [Python](https://www.python.org/downloads)

> Install [NodeJS](https://nodejs.org)

Note: If issues with 'Managed Environment' run the below, then do 'sudo pip install package-name'...

> `sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.old`

### Client: Cluster Management Dependencies
Libraries which support distributing jobs to the cluster / servers / node - following the [OctaPi Client Setup Instructions](https://projects.raspberrypi.org/en/projects/build-an-octapi/3)

> Dispy: `sudo pip3 install dispy`

> nmap: `sudo apt-get install nmap`


### Client: UI Dependencies
The UI gives you access to the script in this repository. These installations are required to create the UI web server with NodeJS

Install [NodeJS](https://nodejs.org)
> eg: `curl -sL https://deb.nodesource/setup_18.x | sudo -E bash -`

> then: `sudo apt install -y nodejs`

> then: `sudo apt-get -f install npm`

> check with: `node -v`

Install NodeJS Modules
> Node HTTP Server: `sudo npm install -g http-server`

> Socket.io `sudo npm install socket.io`

> Sense Hat LED: `sudo npm install sense-hat-led`

> Python Shell `sudo npm install python-shell`

> NOTE: Check versions with `node -v package-name`node

--------------------------------------------------------
## Server Install Dependencies
***NOTE: Each Server / Node requires any libraries required for jobs to be pre-installed***

Note: If issues with 'Managed Environment' run the below, then do 'sudo pip install package-name'...

> `sudo mv /usr/lib/python3.11/EXTERNALLY-MANAGED /usr/lib/python3.11/EXTERNALLY-MANAGED.old`

If [Python](https://www.python.org/downloads) is not installed...

> Install [Python](https://www.python.org/downloads)

### Server: Cluster Node Dependencies
Libraries which support the cluster / servers / nodes - following the [OctaPi Server Setup Instructions](https://projects.raspberrypi.org/en/projects/build-an-octapi/4)

> Dispy: `sudo pip3 install dispy`

> PsUtil: `sudo pip3 install psutil`

Note: Servers / Nodes can be cloned (eg Raspberry Pi SD cards using an [SD Cloning Tool](https://etcher.balena.io))

--------------------------------------------------------
## Usage:

1. Have at least 1 Server / Node switched on and connected to the same network as the Client.

2. In the terminal of the Client, cd to the directory you downloaded/extracted or moved it
> *eg:* `cd Downloads/shu-pi-cluster`

3. Run The UI
> `node index.js`

4. In browser on same network as client, go to http://[YOUR-CLIENT-IP]:8080 or http://[YOUR-CLIENT-HOSTNAME]:8080 to view the UI
  This allows you to...

   - Test Fog Node cluster
   - Test Client LEDs


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
