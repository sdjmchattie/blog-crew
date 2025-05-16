#!/usr/bin/env python
import warnings

from blog_post_writer.crew import BlogPostWriter

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    topic = input("Enter the topic for the blog post: ")
    if not topic:
        raise ValueError("Topic cannot be empty.")

    inputs = {
        'topic': topic,
    }

    try:
        BlogPostWriter().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
