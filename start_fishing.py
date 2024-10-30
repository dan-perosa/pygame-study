import time
import threading
import random
from inventory import inventory

inventory_lock = threading.Lock()

fishing_places = [
    {'location': 'pond',
     'activity_time': 2.4,
     'rewards': {range(90000, 100000): 'carp',
                 range(0,90000): 'trash 1'},
     },
    {'location': 'lake',
     'activity_time': 3.0,
     'rewards': {range(90000, 100000): 'carp',
                 range(0,90000): 'trash 2'},
     },
]

def start_fishing(chosen_place):
    activity = 'fishing'
    chosen = chosen_place
    for location in fishing_places:
        if location['location'] == chosen:
            rewards = location['rewards']
            activity_time = location['activity_time']
            
    activity_thread = threading.Thread(target=fishing, args=(rewards, activity_time))
    activity_thread.daemon = True
    activity_thread.start()
    
    
def fishing(rewards, activity_time):  
    while True:
        time.sleep(activity_time)
        random_number = random.randint(0, 100000)
        for key in rewards.keys():
            if random_number in key:
                with inventory_lock:
                    inventory.append(rewards[key])
                    print(inventory)
        
            
