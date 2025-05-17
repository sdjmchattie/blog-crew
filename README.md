# Blog Crew

Welcome to the Blog Crew project, powered by [crewAI](https://crewai.com).
This crew is designed to help write a blog post in my preferred style, but could be easily adapted to different styles for other people.

## Installation

Ensure you have Python >=3.10 <3.13 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:

```bash
crewai install
```

### Customizing

Create a `.env` file in the root of the repo and provide two values:

```text
MODEL=gpt-4.1-nano-2025-04-14
OPENAI_API_KEY=sk-proj-
```

You can use Ollama if you wish, but I have used OpenAI's API which you need to pay for.

- Modify `src/blog_post_writer/config/agents.yaml` to define your agents.
- Modify `src/blog_post_writer/config/tasks.yaml` to define your tasks.
- Modify `src/blog_post_writer/crew.py` to add your own logic, tools and specific args.
- Modify `src/blog_post_writer/main.py` to add custom inputs for your agents and tasks.

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
crewai run
```

This command initializes the Crew, assembling the agents and assigning them tasks as defined in your configuration.

As provided, the Crew generates a blog post, stopping for human feedback at key points in the process.
Once the blog post is complete, it will be output to `blog_post.md`.
