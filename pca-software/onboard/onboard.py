import struct
import time

# someone else did circuitpython mocks/tests, documented in blog post:
# https://ntoll.org/article/circuitpython-tests/

# more on mocking:
# https://learn.adafruit.com/clue-sensor-plotter-circuitpython/testing
# https://docs.python.org/3/library/unittest.mock.html

# TODO: connect mocks to simulation somehow
MOCK_HARDWARE = True

# https://circuitpython.org/board/feather_m4_can/
if MOCK_HARDWARE:
    import mockboard as board
    import mockcanio as canio
    import mockdigitalio as digitalio
else:
    import board  # type: ignore
    import canio  # type: ignore
    import digitalio  # type: ignore


# TODO: sphinx documentation system? https://www.sphinx-doc.org/en/master/

#####################
# NEXUS / MAIN LOOP #
#####################

def main():
    """Main loop: sequence of actions the propulsion system continuously does"""
    # pull in all new commands from satellite's CAN bus
    pull_commands_from_can_bus()

    # update the propulsion system's understanding of its current state
    poll_sensors()
    update_state_estimate()

    # check that the current state is safe and expected
    safety_watchdog()
    anomaly_watchdog()

    # update the propulsion system's "plan" and execution of "plan"
    update_control_logic()
    update_control_outputs()

    # write out data to satellite's CAN bus
    push_data_to_can_bus()


def poll_sensors():
    """Updates sensor values from hardware"""
    pass


def update_state_estimate():
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


def push_data_to_can_bus():
    """Pushes new data about the system to the CAN bus"""
    # TODO: what data? state, sensors, etc.?
    # TODO: what rate to prevent flooding the bus?
    pass


def pull_commands_from_can_bus():
    """Processes incoming CAN messages into actionable commands & does them"""
    # TODO: does this call methods, set update, flags, etc.?
    pass


def update_control_logic():
    """High-level control algorithms and "business logic" for propulsion"""
    pass


def update_control_outputs():
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
    # TODO: 
    pass


# https://learn.adafruit.com/circuitpython-essentials/circuitpython-analog-in
def read_resistive_sensor():
    """Read analog pin voltage"""
    # purpose: read resistive sensors using a voltage divider
    # TODO: return signature: should this return a voltage float or int?
    # TODO: add pin to function input signature
    pass


def write_digital_pin() -> None:
    """Write on/off to a digital pin"""
    # purpose: control high power channel
    # TODO: add pin to function input signature
    pass


def receive_can_messages() -> list[canio.Message]:
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


def queue_can_message_for_sending(message: canio.Message) -> None:
    """Queues a message to be broadcast on the CAN bus"""
    pass
