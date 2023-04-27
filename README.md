# Helicoprion Keyboard

The Helicoprion Keyboard is a 44-key diodeless, flippable, choc spaced, hotswap, aggressive column staggered, split keyboard powered by Pro Micro pin compatible board, eg a nice!nano or a KB2040.
It does not have battery support, but you can use a nice!nano wired if you want.

I made this after having build and attempetd to use a sweep. Tha lack of dedicated modifier keys kept being a problem for me. The normal tucky thumb keys are hard to reach for me so I came up with this that I think feels better.
I don't expect this to by my last iteration on a keyboard so it is made to allow me to recycle the MCU and the switches in a next iteration.

![left](https://github.com/ofweb/helicoprion/blob/main/images/3d-left.png)
![right](https://github.com/ofweb/helicoprion/blob/main/images/3d-right.png)


# Testing
If you want to see if this is right for you you can start with printing a paper tester. If you have access to a 3d-printer you can print the step file form the repo and add you switches, this should give you a better indication on if it is right.

# Inspiration

* [Sweep](https://github.com/davidphilipbarr/Sweep) The main inspiration is from the ferris sweep I started trying to used I needed more keys.
* [Hillside](https://github.com/mmccoyd/hillside) The very pretty promicro foot print and how to wire it.
* [Torn](https://github.com/rtitmuss/torn) For not be afraid of showing th components and that look can be very sexy.

## Features

* Pro Micro MCU - Many options
* Sweep inspired layout - Ergonomic strong column staggering for short pinkies.
* Flippable PCBs - Cheaper to order the PCBs
* Hotswap low profile choc switches - Experiment with different key switches with the hotswap sockets.
* Very large thumb cluster - Let your thumb do more of the work.
* Both SMD and THT diodes - Pick if you want the easier to solder or the smaller diodes.

## Bill of Materials (BOM)

Quantity | Item
--- | ---
2 | Helicoprion PCB
2 | Pro Micro pin compatable comtrollers
44 | Kailh choc v1 PG1350 switches
44 | Choc v1 keycaps
44 | Kahli hotswap sockets for choc v1 PG1350
2 | TRRS jack PJ-320A (not needed for nice!nano)
1 | 3.5mm TRRS cable (not needed for nice!nano)
4 | Pin headers (20 pin) or sockets
2 | Reset Button (optional) ALPS SKHLLCA010 or footprint compatible

# PCB layout and schematic
![front](https://github.com/ofweb/helicoprion/blob/main/images/front.png)
![back](https://github.com/ofweb/helicoprion/blob/main/images/back.png)
![schematic](https://github.com/ofweb/helicoprion/blob/main/images/schematic.png)

## External footprints and symbols used

External symbols and footprints are not covered by the LICENSE in this repo.

* [Keebio-Parts.pretty](https://github.com/keebio/Keebio-Parts.pretty) is licensed under the MIT License.
* [keyswitches.pretty](https://github.com/daprice/keyswitches.pretty) is licensed under the Creative Commons Attribution-ShareAlike 4.0 International License.
* [Hillside](https://github.com/mmccoyd/hillside) is licensed under the MIT License.