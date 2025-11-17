# weakness_detector_agent.py

class WeaknessDetectorAgent:
    def __init__(self, memory_tool):
        self.memory = memory_tool

    def update_weakness(self, topic, result):
        """
        Adds to weak list if student performed poorly.
        """
        history = self.memory.read_history()
        weak = history.get("weak_topics", [])

        if result == "wrong" and topic not in weak:
            weak.append(topic)

        history["weak_topics"] = weak
        self.memory.save_history(history)
        return weak
