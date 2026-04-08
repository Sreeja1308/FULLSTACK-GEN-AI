# ✅ Install required packages if not already installed
# !pip install wikipedia transformers

import wikipedia
import textwrap
from transformers import pipeline

# ✅ LLM Summarizer
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# ✅ Memory Module
class Memory:
    def __init__(self):
        self.logs = []

    def store(self, data):
        self.logs.append(data)

    def recall(self, n=10):
        return "\n".join(self.logs[-n:])

# ✅ Human Review
def human_review(summary):
    print("\n✅ Agentic AI Final Summary:\n")
    print(textwrap.fill(summary, width=80))
    feedback = input("\nApprove summary? (yes/edit): ").strip().lower()
    if feedback == "edit":
        return input("\nPlease enter your revised summary:\n").strip()
    return summary

# ✅ Smart Agent for multiple references
class MultiRefAgent:
    def __init__(self, topic):
        self.topic = topic
        self.memory = Memory()

    def run(self):
        print(f"✅ Searching Wikipedia for topic: '{self.topic}'")
        related_titles = wikipedia.search(self.topic, results=5)
        print(f"✅ Found {len(related_titles)} references:\n{related_titles}\n")
        all_summaries = []

        for idx, title in enumerate(related_titles):
            try:
                print(f"🔍 Reading Reference {idx+1}: {title}")
                page = wikipedia.page(title)
                content = page.content[:2000]  # Limit for summarizer
                summary = summarizer(content, max_length=150, min_length=50, do_sample=False)
                summary_text = summary[0]['summary_text']
                print(f"✅ Summary for '{title}':\n{textwrap.fill(summary_text, width=80)}\n")
                self.memory.store(f"[{title}] {summary_text}")
                all_summaries.append(f"{title}: {summary_text}")
            except Exception as e:
                print(f"❌ Error fetching '{title}': {e}")

        combined = "\n\n".join(all_summaries)
        final_summary = summarizer(combined, max_length=200, min_length=80, do_sample=False)[0]['summary_text']
        self.memory.store(f"Combined Final Summary: {final_summary}")

        # Human Review
        reviewed = human_review(final_summary)
        self.memory.store(f"Final Approved Summary: {reviewed}")

        # Save
        filename = f"{self.topic.replace(' ','_')}_agentic_summary.txt"
        with open(filename, "w") as f:
            f.write(f"Topic: {self.topic}\n\n")
            f.write("References Used:\n")
            for t in related_titles:
                f.write(f"- {t}\n")
            f.write("\nFinal Summary:\n")
            f.write(reviewed)
            f.write("\n\nMemory Logs:\n")
            f.write(self.memory.recall())

        print(f"\n✅ Saved agentic summary & logs to '{filename}'")

# ✅ Run the Agent
if __name__ == "__main__":
    topic = input("Enter your research topic: ").strip()
    agent = MultiRefAgent(topic)
    agent.run()
