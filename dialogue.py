

rumors = ["I saw a mudcrab the other day"]
directions = ["The church is to the North",
              "The market is to the South",
              "The castle is to the East"]
quest_topic_1 = ["I hear the blacksmith is having a rat problem.",
                 "You should go see him."]


class DialogueTree(object):
    def __init__(self):
        self.topics = {"Rumors": rumors,
                       "Directions": directions,
                       "Quest Topic 1": quest_topic_1}

