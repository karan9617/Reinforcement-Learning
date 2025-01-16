import gym
from main import SimpleGridWorld  # Import the environment

def run_environment():
    # Initialize the environment
    env = SimpleGridWorld()

    # Reset the environment to the initial state
    state = env.reset()

    # Render the initial state
    print("Initial State:")
    env.render()

    done = False
    total_reward = 0

    # Run an episode (loop through steps)
    while not done:
        # Randomly sample an action from the action space
        action = env.action_space.sample()

        # Take the action and receive the new state, reward, done flag, and info
        next_state, reward, done, info = env.step(action)

        # Accumulate the reward
        total_reward += reward

        # Render the environment (visualize the agent's position)
        print(f"Step {total_reward:.2f} - Action: {action}")
        env.render()

    # Print the total reward after the episode ends
    print(f"Total reward for the episode: {total_reward}")

    # Close the environment
    env.close()


# Run the environment
if __name__ == "__main__":
    run_environment()
