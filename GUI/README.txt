-----DOCUMENTATION TO USE GUI en Ubuntu22.04

First whe need to install cairo with python3.10
->sudo apt install libcairo2 libcairo2-dev
->pip3 install cairocffi
->sudo apt install --reinstall libxcb-xinerama0 libx11-xcb1 libxcb1 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxcb-xinerama0 libxcb-xkb1
->export QT_QPA_PLATFORM=wayland

Second with a venviroment install requiremets.txt
The output has to be succesfull 


Configuración:
	- GUI
	Instalar librerias cairo para GUI en Ubuntu

	- HAT RS-485
	Canviar de posicion las clavijas de los switches (1,2,3)

	- PLC RS-485
	Canviar de posicion las clavijas de los switches (TOP, RIGH)
	
	- Arduino IDE
	Configurar la placa y el modelo del IDE 
	Descagarse las librerias de industrialShield.

	
---------------------------------------------------------------------------------------
-----DOCUMENTATION TO USE GUI en Ubuntu22.04

First whe need to install cairo with python3.10
->sudo apt install libcairo2 libcairo2-dev
->pip3 install cairocffi
->sudo apt install --reinstall libxcb-xinerama0 libx11-xcb1 libxcb1 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-randr0 libxcb-render-util0 libxcb-shape0 libxcb-shm0 libxcb-sync1 libxcb-xfixes0 libxcb-xinerama0 libxcb-xkb1
->export QT_QPA_PLATFORM=wayland

Second with a venviroment install requiremets.txt
The output has to be succesfull 



---------------------------------------------------------------------------------------
---- CONFIGURATION OF THE HAT

-SW1
  1. OFF
  2. ON
  3. ON
  4. OFF

-SW2
  1. OFF
  2. OFF
  3. ON
  4. ON

-SW3 (Automatic send/recive)(multipoint master)
  1. ON
  2. OFF
  3. ON*
  4. ON*
 *Can be turned OFF to (send/recive control via GPIO18)



---------------------------------------------------------------------------------------
---- CONFIGURATION OF THE PLC
-Top switches
  1. ON
  2. OFF
  3. ON
  4. OFF
- Righ sitches
  1. OFF
  2. ON
  3. ON
  4. ON

  5. ON
  6. OFF
  7. ON
  8  OFF



---------------------------------------------------------------------------------------
---- ARDUINO IDE CONFIGURATION OF THE BOARD (ARDUINO ARBOX)

-Dowload the lybrary on idearduino of Industrial shield
	- Select the Family Board: Arbox Family
	- Selecte the Model: Ardbox Relay HF + RS 485 or Ardbox Relay HF w/RS 485

- Dowload from Git-Hub (Industrial-shield) the repo (arduino-Modbus)

