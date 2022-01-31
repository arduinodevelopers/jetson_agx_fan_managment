#!/bin/bash

echo 150 | sudo tee '/sys/devices/pwm-fan/target_pwm'
