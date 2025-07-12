# HackPad
A simple pad of 8 switches for macros, using an RP2040 and Cherry MX switches.
Fun fact: designed everything in the lobby of GitHub HQ for HackClub Highway.
The firmware currently has the keys acting as if they were a numberpad 1-8.
The firmware should be modified for something more useful for whatever situation you want it to be used for.

## Overall HackPad
PCB is inside, but it's the same color
<img width="734" height="609" alt="image" src="https://github.com/user-attachments/assets/2d4e41d5-ba38-4df4-8e31-5185103ab2f3" />

## Schematic
<img width="370" height="716" alt="image" src="https://github.com/user-attachments/assets/57d081aa-57da-4466-8530-1de2986fbef6" />

## PCB Schem
<img width="930" height="268" alt="image" src="https://github.com/user-attachments/assets/f283cdde-3554-4b46-9bd7-75967ff80236" />

## Case assembly
I dont have a good screenshot, but you assemble the case by placing the PCB in the bottom and having it rest on the supports that are inside of it.

## Bill of Materials (BOM)

| Id | Designator                          | Footprint                         | Quantity | Designation       | Supplier and ref |
|----|-------------------------------------|-----------------------------------|----------|-------------------|------------------|
| 1  | U1                                  | XIAO-RP2350-DIP                   | 1        | XIAO-RP2040-DIP   |                  |
| 2  | SW8, SW7, SW6, SW5, SW4, SW3, SW2, SW1 | SW_Cherry_MX_1.00u_PCB           | 8        | SW_Push           |                  |
| 3  | D2, D1                               | LED_SK6812_PLCC4_5.0x5.0mm_P3.2mm | 2        | SK6812            |                  |

