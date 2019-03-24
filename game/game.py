#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""Class definition for Bellgame
"""

import uuid

class NoPlayersFound(Exception):
    pass

class Trial(object):

    def __init__(self,
                 players=None,
                 gameId=None):

        self.points = 0

class Player(object):
    pass

class Game(object):

    def __init__(self,
                 players=None,
                 unplayedTrials=None,
                 gameId=None):

        self.playedTrials = []
        self.strategy = None
        self.score = 0
        if players is None:
            self.players = set()
        if unplayedTrials is None:
            self.unplayedTrials = []
        if gameId is None:
            self.gameId = uuid.uuid4()
        else:
            self.get_trials()

    def add_player(self, player):
        """Add a player to the game
        """
        self.players.add(player)

    def new_trial(self):
        """Add an unplayed trial to the game
        """
        trial = Trial(players=self.players,
                      gameId=self.gameId)
        self.unplayedTrials.append(trial)
        return trial

    def get_score(self):
        """Calculate score from played trials

        If no trials have been played, returns 0
        """
        self.score = 0
        for trial in self.playedTrials:
            self.score += trial.points
        return self.score

    def set_strategy(self, strategy):
        """Set strategy for the game. Strategy is always optional
        """
        self.strategy = strategy

    def create_room(self):
        """Create room ID and assign it to self
        """

    def get_trials(self):
        """Query database to get all trials
        """

    def __repr__(self):
        return "Game; players: {self.players}, trials: {len(self.trials)}," \
                "score: {self.get_score()}"
