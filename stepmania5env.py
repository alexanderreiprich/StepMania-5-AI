## This .py file is used to register the custom environment to gymnasium

class StepManiaEnv(Env):

    # Setup
    def __init__(self):
        
        super().__init__()
        # Define action space
        self.action_space = Discrete(5)

        # Observation Array
        self.observation_space = Box(
            low=0, 
            high=255, 
            shape=(1, 135, 100),
            dtype=np.uint8
        )
        
        # Define extraction parameters for the game
        self.screenshot_helper = Screenshot()
        self.input_sending_helper = SendInput()
        self.pattern_recog_helper = RecognizePattern()
        self.capture = mss()
        self.steps = 0
        self.previous_reward = 0
        self.window_location = {'top': 35, 'left': 10, 'width': 410, 'height': 230}
        self.game_location = {'top': 15, 'left': 20, 'width': 100, 'height': 185}
        self.score_location = {'top': 215, 'left': 280, 'width': 100, 'height': 25}
        self.done_location = {'top': 0, 'left': 0, 'width': 90, 'height':25}
        self.past_arrows_location = {'top': 45, 'left': 50, 'width': 140, 'height': 2}
        self.cur_held_buttons = {'a': False, 's': False, 'w': False, 'd': False}
        self.action_map = {
            0: "no_op",
            1:'a',
            2:'s',
            3:'w',
            4:'d',
        }
        
        # Adjust window position and size
        win = pygetwindow.getWindowsWithTitle('StepMania')[1]
        win.size = (450, 290)
        win.moveTo(0, 0)

    # One iteration of the environment
    def step(self, action):

        # Manage input based on action parameter
        if action != 0:
            if (list(self.cur_held_buttons.values())[action - 1]):
                self.cur_held_buttons[list(self.cur_held_buttons)[action - 1]] = False
                self.input_sending_helper.releaseKey(self.action_map[action])
            else:
                self.cur_held_buttons[list(self.cur_held_buttons)[action - 1]] = True
                self.input_sending_helper.holdKey(self.action_map[action])
     
        # Take screenshot for done, observation and reward functions
        screenshot = np.array(self.capture.grab(self.window_location))[:,:,:-1].astype(np.uint8)
        downscaled_screenshot = self.screenshot_helper.downscaleImageBinary(screenshot, (225, 150), (1, 150, 225))
        self.steps += 1
        
        # Checking if the game is over
        done = self.get_over(screenshot)
        
        # Get the next observation
        new_observation = self.get_observation(downscaled_screenshot)

        # Use score as reward
        reward = self.get_reward(screenshot, action)
        info = {}

        return new_observation, reward, done, info

    # Quits result screen and selects new song
    def reset(self):

        # Exit to menu, select new song and start
        time.sleep(5)
        pydirectinput.press('enter')
        time.sleep(6)
        pydirectinput.press('d')
        time.sleep(2)
        pydirectinput.press('enter')

        # Edge Case - 'Roulette' is selected
        time.sleep(1.5)
        pydirectinput.press('enter')
        time.sleep(3)
        pydirectinput.press('enter')

        # Reset variables
        self.previous_reward = 0
        self.steps = 0

        # Take screenshot to pass to observation
        screenshot = np.array(self.capture.grab(self.window_location))[:,:,:-1].astype(np.uint8)
        downscaled_screenshot = self.screenshot_helper.downscaleImageBinary(screenshot, (225, 150), (1, 150, 225))

        return self.get_observation(downscaled_screenshot)

    # Returns image of gameplay
    def get_observation(self, img):

        # Crop gameplay part of the window screenshot
        obs = img[:, self.game_location['top']:(self.game_location['top'] + self.game_location['height']), self.game_location['left']:(self.game_location['left'] + self.game_location['width'])]

        return obs
            

    # Returns the current score as a reward
    def get_reward(self, img, action):

        # Crop score part of the window screenshot and top of the gameplay section
        score_img = img[self.score_location['top']:(self.score_location['top'] + self.score_location['height']), self.score_location['left']:(self.score_location['left'] + self.score_location['width'])]
        past_arrows_img = img[env.past_arrows_location['top']:(env.past_arrows_location['top'] + env.past_arrows_location['height']), env.past_arrows_location['left']:(env.past_arrows_location['left'] + env.past_arrows_location['width'])]

        # If no input should have occured, give negative reward
        if (self.pattern_recog_helper.input_expected(past_arrows_img, action) == False):
            return -1

        # If the score increased, give positive reward
        new_reward = self.pattern_recog_helper.analyze_score(score_img)
        if (new_reward > self.previous_reward):
            # Set the current reward as the previous reward for the next iteration
            self.previous_reward = new_reward
            return 5
            
        # If the score didn't change, and no action has taken place, give a neutral reward
        else:
            return 0

    # Checks if the game is over
    def get_over(self, img):

        # Crop done part of the window screenshot
        obs = img[self.done_location['top']:(self.done_location['top'] + self.done_location['height']), self.done_location['left']:(self.done_location['left'] + self.done_location['width'])]
        
        return self.pattern_recog_helper.analyze_results(obs)