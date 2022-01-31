#!/bin/bash

echo 100 | sudo tee '/sys/devices/pwm-fan/target_pwm'
