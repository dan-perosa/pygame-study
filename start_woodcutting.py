import time
import threading
import random
from inventory import inventory

inventory_lock = threading.Lock()

woodcutting_places = [
    {'location': 'forest',
     'activity_time': 2.4,
     'rewards': {range(90000, 100000): 'log',
                 range(0,90000): 'stick'},
     },
    {'location': 'jungle',
     'activity_time': 3.0,
     'rewards': {range(90000, 100000): 'wood',
                 range(0,90000): 'trash 3'},
     },
]

def start_woodcutting(chosen_place):
    activity = 'woodcutting'
    chosen = chosen_place
    for location in woodcutting_places:
        if location['location'] == chosen:
            rewards = location['rewards']
            activity_time = location['activity_time']
            
    activity_thread = threading.Thread(target=woodcutting, args=(rewards, activity_time))
    activity_thread.daemon = True
    activity_thread.start()
    
    
def woodcutting(rewards, activity_time):  
    while True:
        time.sleep(activity_time)
        random_number = random.randint(0, 100000)
        for key in rewards.keys():
            if random_number in key:
                with inventory_lock:
                    inventory.append(rewards[key])
                    print(inventory)
        
            
