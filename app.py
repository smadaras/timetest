"""
Calculating maximum time resolution
"""
import time

"""
class TimeRecorder:
    def __init__(self):
        self.times = []
        self.start_time = time.time()

    def record_time(self):
        while (time.time() - self.start_time) < 1:
            current_time = int(time.time() * 1000)
            self.times.append(str(current_time))
            # Introduce a small delay to simulate real-time recording
            time.sleep(0.001)
"""

def main():
    sFilename: str = "current_times.txt"
    iDuration_ms: int = 1000 ; fDuration_s: float = float(iDuration_ms) / 1_000
    iPause_ms: int = 20 ; fPause_s: float = float(iPause_ms) / 1_000

    lTimes: list = []
    lDelta: list = []

    fStartTime: float = time.time()
    print(f"Start:{fStartTime}")
    fStopTime: float = fStartTime + fDuration_s
    print(f"Stop:{fStopTime}")
    while True:
        fCurrentTime: float = time.time()
        if fCurrentTime > fStopTime:
            break
        lTimes.append(fCurrentTime)
        if iPause_ms:
            time.sleep(fPause_s)

    for iIndex in range(1, len(lTimes)):
        lDelta.append(lTimes[iIndex]-lTimes[iIndex - 1])

    if iPause_ms:
        print(f" {lTimes}\n {lDelta}\n Count: {len(lTimes)}")
    else:
        print(f"Count: {len(lTimes)}")
    
    try:
        print(f"Max: {max(lDelta)}, Min: {min(lDelta)}")
    except:
        print("Couldn't start during the given duration.")

    """
    
    recorder = TimeRecorder()


    try:
        while (time.time() - recorder.start_time) < 1:
            pass
    except KeyboardInterrupt:
        print("Stopping recording...")
    
    recorder.record_time()
    with open(sFilename, 'w') as file:
        for time in recorder.times:
            file.write(time + "\n")
    """

if __name__ == "__main__":
    main()
    exit()
