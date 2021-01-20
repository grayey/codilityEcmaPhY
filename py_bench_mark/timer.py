import time

class Timer():
    
    def __init__(self,sol):
        print('Started..')
        self.seconds = time.time();
        self.sol = sol;
    
    def stop(self):
        print('Finished..')
        print(f"Time taken to run Solution {self.sol}: {time.time() - self.seconds} Seconds")




