from cowin_api import CoWinAPI

cowin = CoWinAPI()

states = cowin.get_states()
print(states)

# get the state id from above add it here
state_id = '12'
cowin = CoWinAPI()
districts = cowin.get_districts(state_id)
print(districts)
