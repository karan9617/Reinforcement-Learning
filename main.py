import gym
from gym import spaces
import numpy as np

class SimpleGridWorld(gym.Env):
    def __init__(self):
        super(SimpleGridWorld,self).__init__()
        self.action_space = spaces.Discrete(4)
        self.observation_space = spaces.Discrete(25)
        self.state = 0
        self.goal = 24

    def reset(self):
        self.state = 0
        return self.state
    def step(self,action):
        if action == 0:
            if self.state >= 5:
                self.state -= 5
        elif action == 1:
            if self.state < 20:
                self.state += 5
        elif action == 2:
            if self.state %5 != 0:
                self.state -= 1
        elif action == 3:
            if self.state %5 != 4:
                self.state += 1
        done = self.state == self.goal
        reward = 1 if done else -0.01
        return self.state, reward, done, {}

    def render(self):
        # Render the grid (visualize the current state)
        grid = np.zeros((5, 5), dtype=int)
        grid[self.state // 5, self.state % 5] = 1  # Mark agent's position
        grid[self.goal // 5, self.goal % 5] = 2  # Mark goal position
        print(grid)

    def close(self):
        pass  # Cleanup resources if necessary
