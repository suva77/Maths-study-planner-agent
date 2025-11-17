# planner_agent.py

class PlannerAgent:
    def __init__(self, memory_tool):
        self.memory = memory_tool

    def generate_plan(self, topics):
        """
        Creates a study plan based on topics + past performance.
        """
        past_data = self.memory.read_history()

        # If no past data → simple plan
        if not past_data:
            return self.create_basic_plan(topics)

        # If past weakness exists → reorder topics
        weak = past_data.get("weak_topics", [])

        ordered = weak + [t for t in topics if t not in weak]
        return self.create_basic_plan(ordered)

    def create_basic_plan(self, topics):
        """
        Creates a simple structured plan.
        """
        plan = []
        for i, topic in enumerate(topics, start=1):
            plan.append({
                "day": i,
                "topic": topic,
                "task": "Study theory + practice 5 problems"
            })
        return plan

    def update_plan_after_feedback(self, topic, performance):
        """
        Adjusts plan using learner feedback.
        """
        history = self.memory.read_history()

        weak_list = history.get("weak_topics", [])

        if performance == "weak" and topic not in weak_list:
            weak_list.append(topic)

        history["weak_topics"] = weak_list
        self.memory.save_history(history)
        return True
