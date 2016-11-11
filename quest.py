from enum import Enum

class State(Enum):
    pass


class Quest(object):
    def __init__(self, name, quest_giver, gold_reward, item_reward, goals):
        self.name = name
        self.quest_giver = quest_giver
        self.gold_reward = gold_reward
        self.item_reward = item_reward
        self.goals = goals
        self.on_completion = None


class QuestGoal(object):
    def __init__(self):
        self.is_complete = False
        self.number_to_kill = 0
        self.number_to_gather = 0
        self.item_to_gather = None

    def completion_check(self, game_state):
        for category in game_state.player.items:
            if self.item_to_gather in game_state.player.items[category]:
                self.is_complete = True


class HasYeflaske(QuestGoal):
    def __init__(self):
        super().__init__()
        self.is_complete = False
        self.item_to_gather = "Ye Flaske"

    def completion_check(self, game_state):
        for category in game_state.player.items:
            for each in game_state.player.items[category]:
                if each.name == self.item_to_gather:
                    self.is_complete = True


def end_quest(quest_giver, quest_name):
    del quest_giver.dialogue[quest_name]


def start_ye_flaske(quest_giver):
    del quest_giver.dialogue["Searching for something"]
    find_ye_flaske = (None, ["Good.  It must be around here somewhere...",
                             "Return to me when you find my flaske."])
    quest_giver.dialogue["Find lost Flaske"] = find_ye_flaske


class FetchYeflaske(Quest):
    def __init__(self, quest_giver):
        super().__init__(quest_giver, 100, None, [HasYeflaske])
        self.name = "Find lost Flaske"
        self.on_completion = end_quest


quests = {"Find lost Flaske": FetchYeflaske}