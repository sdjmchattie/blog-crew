#!/usr/bin/env python
from datetime import datetime
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
    description = input("Describe the blog post you'd like to have written: ")
    if not description:
        raise ValueError("Description cannot be empty.")

    inputs = {
        'description': description,
        'current_year': str(datetime.now().year),
    }

    try:
        BlogPostWriter().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
