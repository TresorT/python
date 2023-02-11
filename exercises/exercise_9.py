"""

In this exercise, we will continue working on the ‘Bad Ambiance!’ app.
Along with being able to play the game in story mode, completing missions, it is also possible to
play a couple of silly side games such as ‘Hyper Hurdles’ and ‘We Have Lift-off!’.
Although these may seem like silly side games, a game player can actually unlock weapons and
missions by achieving certain milestones in these side games. For instance, if the Hyper Hurdles
game is completed in 10 seconds or under, or the Car rises off the ground by more than 11
centimetres when going over a hill at speed, a new weapon is unlocked in story mode. If both of the
above criteria has been met (hurdles in 10 seconds or under and height is over 11 centimetres), a
new mission is unlocked.
You have been given the following sample data:
  hurdle_time = 9.95
  height_from_road = 10.75

You have been tasked with writing two expressions to check if the game player has managed to
unlock weapons and/or missions.
 The expression to determine if both criteria has been met, should store the result in a
variable called unlock_mission
 The expression to determine if either of the criteria has been met, should be stored in a
variable called unlock_weapon

"""
hurdle_time = 9.95
height_from_road = 10.75

unlock_mission = hurdle_time and height_from_road
unlock_weapon = hurdle_time or height_from_road