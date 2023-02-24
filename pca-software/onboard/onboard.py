#####################
# NEXUS / MAIN LOOP #
#####################

def main():
    """Main loop: sequence of actions the propulsion system continuously does"""
    sensor_update()
    state_estimate_update()
    safety_watchdog()
    anomaly_watchdog()
    data_update()  # TODO: possibly move this to the end of the loop
    command_update()  # TODO: possibly move this to the front of the loop
    control_logic()
    control_update()


def sensor_update():
    """Updates sensor values from hardware"""
    pass


def state_estimate_update():
    """Updates estimated state of propulsion system based on models"""
    pass


def safety_watchdog():
    """Monitors propulsion system for unsafe conditions, and acts if needed"""
    # TODO: define "if needed" and determine how acting happens
    pass


def anomaly_watchdog():
    """Monitors system for deviations from expected performance"""
    # TODO: what anomalies can actually be monitored?
    pass


def data_update():
    """Pushes new data about the system to the CAN bus"""
    # TODO: what data? state, sensors, etc.?
    # TODO: what rate to prevent flooding the bus?
    pass


def command_update():
    """Processes incoming CAN messages into actionable commands & does them"""
    # TODO: does this call methods, set update, flags, etc.?
    pass


def control_logic():
    """High-level control algorithms and "business logic" for propulsion"""
    pass


def control_update():
    """Sets new values for control driving & updates calls to hardware"""
    pass


########
# CORE #
########

def update_sensor_translation_layer():
    """Read from physical sensors and translate values to unit-based ones"""
    # TODO: manage derviatives (velocity, acceleration, jerk)?
    # TODO: apply filtering (kalman)?
    # interesting article: https://en.wikipedia.org/wiki/Trajectory_optimization
    pass


def update_propellant_state_estimator():
    """Update physics-based estimate of propellant"""
    pass


def update_system_state_estimator():
    """Update physics-based estimate of propulsion system as a whole"""
    # TODO: what is the scope? errors? "business logic"? other?
    pass


def update_power_translation_layer():
    """Translate raw, intended heater/solenoid power states to hardware"""
    pass


###########
# DRIVERS #
###########

def read_digital_sensor():
    """Read abstract digital sensor. Placeholder for I2C etc. reads"""
    # TODO: part out into swappable interface e.g. i2c communication method?
    pass


def read_resistive_sensor():
    """Read analog pin voltage"""
    # purpose: read resistive sensors using a voltage divider
    pass


def write_digital_pin():
    """Write on/off to a digital pin"""
    # purpose: control high power channel
    pass


def receive_can_messages():
    """Returns new messages from CAN bus (filtered, relevant to propulsion)"""
    # TODO: how should ID filtering work?
    # TODO: how should checking for right length work?
    # TODO: where to put CAN bus state checking?

    # helpful websites:
    # https://en.wikipedia.org/wiki/CAN_bus
    # https://en.wikipedia.org/wiki/CANaerospace
    # https://en.wikipedia.org/wiki/Cubesat_Space_Protocol
    # https://learn.adafruit.com/using-canio-circuitpython/overview
    pass


def queue_can_message_for_sending():
    """Queues a message to be broadcast on the CAN bus"""
    pass
