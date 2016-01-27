from automission import automission

lat,lon=41.0831324,29.0515797
alt=100


my_mission=automission('copter')
my_mission.do_set_home(lat,lon)

increase=0.001
for i in range(20):
	my_mission.spline_waypoint(lat,lon,alt)
	lat+=increase if i in range(0,20,4) else 0
	lon+=increase if i in range(1,20,4) else 0
	lat-=increase if i in range(2,20,4) else 0
	lon-=increase if i in range(3,20,4) else 0
	increase-=0.00005
	
my_mission.land()	
my_mission.write(name='vortex')
