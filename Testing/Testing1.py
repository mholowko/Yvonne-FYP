from opentrons import containers, instruments, robot

trough2 = containers.create('trough2', grid=(1,2), spacing =(85, 63), diameter = 85, depth= 40)

trough = containers.load('trough2', 'C3', 'trough')
m200rack = containers.load('tiprack-200ul', 'B3', 'm200rack')
m200rack2 = containers.load('tiprack-200ul', 'B2', 'm200rack2')
trash2 = containers.load('point', 'D2', 'trash2')
plate2 = containers.load('96-PCR-flat', 'C2', 'plate2')

m200 = instruments.Pipette(name="m200", trash_container = trash2, tip_racks=[m200rack, m200rack2], min_volume=30, max_volume = 200, axis = "a", channels = 8)

m200.pick_up_tip(m200rack.well('A1'))
for row in plate2.rows():
	m200.distribute(30, trough('A1'), row, new_tip ='never',trash=False)
m200.return_tip()

for row in plate2.rows():
	m200.distribute(30, trough('A2'), row, new_tip = 'never', trash=False)

robot.run()