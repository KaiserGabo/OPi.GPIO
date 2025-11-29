# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa Zero3
(see https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface)
Usage:

.. code:: python
   import radxa.zero3
   from OPi import GPIO

   # Choose pin numbering mode
   GPIO.setmode(radxa.zero3.BOARD) # Column Physical in table below
   GPIO.setmode(radxa.zero3.BCM) # Column GPIO in table below


+------+-----+----------+--------+---+   PI3B   +---+--------+----------+-----+------+
| GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
+------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
|      |     |     3.3V |        |   |  1 || 2  |   |        | 5V       |     |      |
|  140 |   0 |    SDA.2 |     IN | 1 |  3 || 4  |   |        | 5V       |     |      |
|  141 |   1 |    SCL.2 |     IN | 1 |  5 || 6  |   |        | GND      |     |      |
|  147 |   2 |    PWM15 |     IN | 0 |  7 || 8  | 1 | ALT1   | RXD.2    | 3   | 25   |
|      |     |      GND |        |   |  9 || 10 | 1 | ALT1   | TXD.2    | 4   | 24   |
|  118 |   5 | GPIO3_C6 |     IN | 0 | 11 || 12 | 1 | IN     | GPIO3_C7 | 6   | 119  |
|  128 |   7 | GPIO4_A0 |     IN | 0 | 13 || 14 |   |        | GND      |     |      |
|  130 |   8 |    TXD.7 |     IN | 0 | 15 || 16 | 0 | IN     | RXD.7    | 9   | 131  |
|      |     |     3.3V |        |   | 17 || 18 | 0 | IN     | GPIO4_A1 | 10  | 129  |
|  138 |  11 | SPI3_TXD |     IN | 0 | 19 || 20 |   |        | GND      |     |      |
|  136 |  12 | SPI3_RXD |     IN | 0 | 21 || 22 | 0 | IN     | TXD.9    | 13  | 132  |
|  139 |  14 | SPI3_CLK |     IN | 0 | 23 || 24 | 0 | IN     | SPI3_CS1 | 15  | 134  |
|      |     |      GND |        |   | 25 || 26 | 0 | IN     | GPIO4_A7 | 16  | 135  |
|   32 |  17 |    SDA.3 |   ALT2 | 1 | 27 || 28 | 1 | ALT2   | SCL.3    | 18  | 33   |
|  133 |  19 |    RXD.9 |     IN | 0 | 29 || 30 |   |        | GND      |     |      |
|  124 |  20 | GPIO3_D4 |     IN | 0 | 31 || 32 | 0 | IN     | PWM11    | 21  | 144  |
|  127 |  22 | GPIO3_D7 |     IN | 0 | 33 || 34 |   |        | GND      |     |      |
|  120 |  23 | GPIO3_D0 |     IN | 0 | 35 || 36 | 0 | IN     | GPIO3_D5 | 24  | 125  |
|  123 |  25 | GPIO3_D3 |     IN | 0 | 37 || 38 | 0 | IN     | GPIO3_D2 | 26  | 122  |
|      |     |      GND |        |   | 39 || 40 | 0 | IN     | GPIO3_D1 | 27  | 121  |
+------+-----+----------+--------+---+----++----+---+--------+----------+-----+------+
| GPIO | wPi |   Name   |  Mode  | V | Physical | V |  Mode  | Name     | wPi | GPIO |
+------+-----+----------+--------+---+   PI3B   +---+--------+----------+-----+------+

"""


# Orange Pi 3b physical board pin to GPIO pin
BOARD = {
    3: 32,  # SDA.2/GPIO1_A0
    5: 33,  # SCL.2/GPIO1_A1
    7: 116,  # PWM14_M0/GPIO3_C4
    8: 25,  # RXD.2/GPIO0_D1
    10: 24,  # TXD.2/GPIO0_D0
    11: 97,  # GPIO3_A1
    12: 99,  # I2S3_SCLK_M0/GPIO3_A3
    13: 98,  # I2S3_MCLK_M0/GPIO3_A2
    15: 104,  # GPIO3_B0
    16: 105,  # PWM8_M0/UART4_RX_M1/GPIO3_B1
    18: 106,  # PWM9_M0/UART4_TX_M1/GPIO3_B2
    19: 147,  # PWM15_IR_M1/I2S3_SCLK_M1/SPI3_MOSI_M1/GPIO4_C3
    21: 149,  # UART9_TX_M1	PWM12_M1/I2S3_SDO_M1/SPI3_MISO_M1/GPIO4_C5
    22: 113,  # I2S1_SDO2_M2/GPIO3_C1
    23: 146,  # PWM14_M1/I2S3_MCLK_M1/SPI3_CLK_M1
    24: 150,  # I2S3_SDI_M1/UART9_RX_M1/PWM13_M1/SPI3_CS0_M1/GPIO4_C6
    # 26: 135,  # GPIO4_A7/NC
    27: 138,  # I2C4_SDA_M0/I2S2_SDI_M1/GPIO4_B2
    28: 139,  # I2S2_SDO_M1/I2C4_SCL_M0/GPIO4_B3
    29: 107,  # I2C5_SCL_M0/GPIO3_B3
    31: 108,  # I2C5_SCD_M0/GPIO3_B4
    32: 114,  # I2S1_SDO3_M2/UART5_TX_M1/GPIO3_C2
    33: 115,  # UART5_RX_M1/I2S1_SCLK_RX_M2/GPIO3_C3
    35: 100,  # I2S3_LRCK_M0/GPIO3_A4	
    36: 103,  # GPIO3_A7
    37: 36,   # GPIO1_A4	
    38: 102,  # I2S3_SDI_M0/GPIO3_A6
    40: 121,  # I2S3_SDO_M0/GPIO3_A5
}

# Orange Pi 3b physical board pin to WiringPi GPIO pin
# WIRINGPI = {
#     3: 0,  # SDA.2/GPIO4_B4
#     5: 1,  # SCL.2/GPIO4_B5
#     7: 2,  # PWM15/GPIO4_A4
#     8: 3,  # RXD.2/GPIO0_D1
#     10: 4,  # TXD.2/GPIO0_D0
#     11: 5,  # GPIO3_C6
#     12: 6,  # GPIO3_C7
#     13: 7,  # GPIO4_A0
#     15: 8,  # TXD.7/GPIO4_A2
#     16: 9,  # RXD.7/GPIO4_A3
#     18: 10,  # GPIO4_A1
#     19: 11,  # SPI3_TXD/GPIO4_B2
#     21: 12,  # SPI3_RXD/GPIO4_B0
#     22: 13,  # TXD.9/GPIO4_B1
#     23: 14,  # SPI3_CLK/GPIO4_B3
#     24: 15,  # SPI3_CS1/GPIO4_A6
#     26: 16,  # GPIO4_A7
#     27: 17,  # SDA.3/GPIO4_A0
#     28: 18,  # SCL.3/GPIO1_A1
#     29: 19,  # RXD.9/GPIO4_A5
#     31: 20,  # GPIO3_D4
#     32: 21,  # PWM11/GPIO4_C0
#     33: 22,  # GPIO3_D7
#     35: 23,  # GPIO3_D0
#     36: 24,  # GPIO3_D5
#     37: 25,  # GPIO3_D3
#     38: 26,  # GPIO3_D2
#     40: 27,  # GPIO3_D1
# }

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
