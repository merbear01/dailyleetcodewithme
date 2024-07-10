class Solution(object):
    def largestAltitude(self, gain):
        altitude = 0
        highest_altitude = 0
        for i in gain:
            altitude += i #updates altitude based on items in gain
            highest_altitude = max(altitude, highest_altitude)
                
        return highest_altitude
        