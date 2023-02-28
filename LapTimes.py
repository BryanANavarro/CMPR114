# Bryan Navarro
# CMPR114 - Python
# February 27, 2023

currentLap = 0
fastestLap = 0
slowestLap = 0
total = 0

laps = int(input("\nHow many laps have you ran? "))

for times in range(laps):
	currentLap = int(input("\nEnter the time of the lap: "))
	
	if times == 0:
		fastestLap = currentLap
		slowestLap = currentLap

	total += currentLap

	if currentLap < fastestLap:
		fastestLap = currentLap

	if currentLap > slowestLap:
		slowestLap = currentLap

average = total/laps
# Display the Fastest, Slowest, and Average Lap Times
print(f"\nFasted Lap: {fastestLap}.")
print(f"\nSlowest Lap: {slowestLap}.")
print(f"\nAverage Lap: {average}.")