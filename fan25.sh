#!/bin/bash

echo 48 | sudo tee '/sys/devices/pwm-fan/target_pwm'
