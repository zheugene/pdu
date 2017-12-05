#!/usr/bin/env python

from AM2315 import AM2315

thsen = AM2315()
print "T   ", thsen.read_temperature()
print "H   ", thsen.read_humidity()
print "H,T ", thsen.read_humidity_temperature()

