import os
from crewai import LLM
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task






@CrewBase
class AutonomousSupportTicketSystemCrew:
    """AutonomousSupportTicketSystem crew"""

    
    @agent
    def ticket_router_agent(self) -> Agent:
        
        return Agent(
            config=self.agents_config["ticket_router_agent"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def password_reset_agent(self) -> Agent:
        
        return Agent(
            config=self.agents_config["password_reset_agent"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    
    @agent
    def leave_balance_agent(self) -> Agent:
        
        return Agent(
            config=self.agents_config["leave_balance_agent"],
            
            
            tools=[

            ],
            reasoning=False,
            max_reasoning_attempts=None,
            inject_date=True,
            allow_delegation=False,
            max_iter=25,
            max_rpm=None,
            max_execution_time=None,
            llm=LLM(
                model="gpt-4o-mini",
                temperature=0.7,
            ),
        )
    

    
    @task
    def analyze_and_route_support_ticket(self) -> Task:
        return Task(
            config=self.tasks_config["analyze_and_route_support_ticket"],
            markdown=False,
        )
    
    @task
    def handle_password_reset_request(self) -> Task:
        return Task(
            config=self.tasks_config["handle_password_reset_request"],
            markdown=False,
        )
    
    @task
    def retrieve_and_report_leave_balance(self) -> Task:
        return Task(
            config=self.tasks_config["retrieve_and_report_leave_balance"],
            markdown=False,
        )
    
    @task
    def generate_final_support_response(self) -> Task:
        return Task(
            config=self.tasks_config["generate_final_support_response"],
            markdown=False,
        )
    

    @crew
    def crew(self) -> Crew:
        """Creates the AutonomousSupportTicketSystem crew"""
        return Crew(
            agents=self.agents,  # Automatically created by the @agent decorator
            tasks=self.tasks,  # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
        )
