import ctypes

# Constants for power management
ES_SYSTEM_REQUIRED = 0x00000001
ES_DISPLAY_REQUIRED = 0x00000002


# Function to put the system to sleep (suspend)
def suspend_system():
    ctypes.windll.powrprof.SetSuspendState(0, 1, 0)


# Call the function to put the system to sleep
suspend_system()
