import gym
import pygame
import random

random.seed(1234)

streets = gym.make("Taxi-v3", render_mode="human").env #New versions keep getting released; if -v3 doesn't work, try -v2 or -v4
streets.reset()
streets.render()