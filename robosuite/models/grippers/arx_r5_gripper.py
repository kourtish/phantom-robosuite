"""
Gripper for the ARX R5 arm (two parallel fingers, 0-44 mm travel each).
"""
import numpy as np

from robosuite.models.grippers.gripper_model import GripperModel
from robosuite.utils.mjcf_utils import xml_path_completion


class ARXR5Gripper(GripperModel):
    """
    Parallel-jaw gripper of the ARX R5. Each finger is position-controlled in meters of travel:
    finger 1 in [0, 0.044], finger 2 in [-0.044, 0] (0 = closed).

    With direct_gripper_control robosuite sends [a, -a] to the two actuators (see robots/manipulator.py),
    where a is the per-finger opening in meters.

    Args:
        idn (int or str): Number or some other unique identification string for this gripper instance
    """

    def __init__(self, idn=0):
        super().__init__(xml_path_completion("grippers/arx_r5_gripper.xml"), idn=idn)

    def format_action(self, action):
        """
        Maps continuous action into finger commands (only used without direct_gripper_control)
        -1 => open, 1 => closed

        Args:
            action (np.array): gripper-specific action

        Raises:
            AssertionError: [Invalid action dimension size]
        """
        assert len(action) == self.dof
        return np.array([-action[0], action[0]])

    @property
    def init_qpos(self):
        return np.array([0.022, -0.022])

    @property
    def dof(self):
        return 1

    @property
    def _important_geoms(self):
        return {
            "left_finger": ["finger1_collision"],
            "right_finger": ["finger2_collision"],
            "left_fingerpad": ["finger1_collision"],
            "right_fingerpad": ["finger2_collision"],
        }
