import gymnasium as gym
import numpy as np
import pyautogui
import time
import controller_setup as cs

actions = [
    0: "idle",
    1: "move_left",
    2: "move_right",
    3: "jump",
    4: "attack", # Neutral A
    5: "special", # Neutral B
    6: "shield",
    7: "grab",
    8: "smash_left",
    9: "smash_right",
    10: "smash_up",
    11: "smash_down",
]


class SmashBotEnv(gym.Env):
    def reset(self):
        self.state = self._get_obs()
        return self.state
    def step(self, action):
        self._send_action(action)

        new_state = self._get_obs()

        reward = self._compute_reward(self.state, new_state, action)

        done = self._check_done(new_state)

        self.state = new_state

        return new_state, reward, done, {}