#!/bin/bash

echo 225 | sudo tee '/sys/devices/pwm-fan/target_pwm'
