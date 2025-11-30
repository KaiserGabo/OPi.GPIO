# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa Zero3, can also be used for Rock 3C
(see https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface)
Usage:

.. code:: python
   import radxa.zero3
   from OPi import GPIO

   # Choose pin numbering mode
   GPIO.setmode(radxa.zero3.BOARD) # Column Physical in table below
   GPIO.setmode(radxa.zero3.BCM) # Column GPIO in table below

"""


# Radxa Zero 3 physical board pin to GPIO pin
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
    # 26:  ,  # NC
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

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
