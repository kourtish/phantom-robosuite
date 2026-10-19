import numpy as np

from robosuite.models.robots.manipulators.manipulator_model import ManipulatorModel
from robosuite.utils.mjcf_utils import xml_path_completion


class ARXR5(ManipulatorModel):
    """
    ARX R5 is a lightweight 6-DoF arm by ARX Robotics, typically used in bimanual setups.
    Model converted from ARX_Model/R5/R5a URDF.

    Args:
        idn (int or str): Number or some other unique identification string for this robot instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("robots/arx_r5/robot.xml"), idn=idn)

    @property
    def default_mount(self):
        return "PhantomMount"

    @property
    def default_gripper(self):
        return "ARXR5Gripper"

    @property
    def default_controller_config(self):
        return "default_arx_r5"

    @property
    def init_qpos(self):
        return np.array([0.0, 1.0, 1.2, -0.3, 0.0, 0.0])

    @property
    def base_xpos_offset(self):
        return {
            "bins": (-0.5, -0.1, 0),
            "empty": (-0.6, 0, 0),
            "table": lambda table_length: (-0.16 - table_length / 2, 0, 0),
        }

    @property
    def top_offset(self):
        return np.array((0, 0, 1.0))

    @property
    def _horizontal_radius(self):
        return 0.5

    @property
    def arm_type(self):
        return "single"
