class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)  # Light gray background colordef
        
        ## bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)    
        self.bullets_allowed = 3000
        self.bullet_speed_factor = 10
        self.ship_speed_factor = 5
        self.ship_limit = 3
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        self.alien_speed_factor = 2 

# Other settings can be added here as needed    
