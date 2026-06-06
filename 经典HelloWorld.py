msg = "Hello my sucker!"
print(msg)

import numpy as np

print(f"here is a random num between 1 and 100: {np.random.randint(1,100)}")



if __name__ == "__main__": # pylint: disable=C0103
    print("This script is being run directly.")  
else :    
    print ("The module 'HelloWorld.py' has been imported in another program")     

