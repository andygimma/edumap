import logging
import hashlib
import random
from datetime import datetime




def get_hash(string = None):
    logging.debug("get_hash")
    seed = "4b9bb860b4934a7fa17d1bedf31b78679ed3fe5f"
    random_number = random.random()
    random_string = str(random_number)
    time = str(datetime.now())
    
    h = ""
    if string:
        hash_string = time + seed + string
        h = hashlib.sha1(seed + string)
    else:
        h = hashlib.sha1(time + random_string)
    new_hash = h.hexdigest()

    return new_hash
        
        