from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class BlogPostWriter():
    """BlogPostWriter crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    # Learn more about YAML configuration files here:
    # Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
    # Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended

    # If you would like to add tools to your agents, you can learn more about it here:
    # https://docs.crewai.com/concepts/agents#agent-tools
    @agent
    def outliner(self) -> Agent:
        return Agent(
            config=self.agents_config['outliner'], # type: ignore[index]
            verbose=True,
        )

    @agent
    def writer(self) -> Agent:
        return Agent(
            config=self.agents_config['writer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def markdown_expert(self) -> Agent:
        return Agent(
            config=self.agents_config['markdown_expert'], # type: ignore[index]
            verbose=True
        )

    # To learn more about structured task outputs,
    # task dependencies, and task callbacks, check out the documentation:
    # https://docs.crewai.com/concepts/tasks#overview-of-a-task
    @task
    def outlining_task(self) -> Task:
        return Task(
            config=self.tasks_config['outlining_task'], # type: ignore[index]
            human_input=True,
        )

    @task
    def drafting_task(self) -> Task:
        return Task(
            config=self.tasks_config['drafting_task'], # type: ignore[index]
        )

    @task
    def refinement_task(self) -> Task:
        return Task(
            config=self.tasks_config['refinement_task'], # type: ignore[index]
            human_input=True,
        )

    @task
    def convert_to_markdown_task(self) -> Task:
        return Task(
            config=self.tasks_config['convert_to_markdown_task'], # type: ignore[index]
            output_file='blog_post.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the BlogPostWriter crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
