from crewai import Crew, Process
from task import write_task, research_task
from agents import Researcher,new_writer

crew = Crew(
    agents=[
        Researcher,new_writer
    ],
    tasks=[
        research_task,write_task
    ],
    process=Process.sequential  # or Process.parallel
)

# Starting the task execution 
#result =crew.kickoff(topic='AI in healthcare')
inputs_array = [{'topic': 'Growth Of GEN AI engineers in future'}]
results = crew.kickoff_for_each(inputs=inputs_array)
for result in results:
    print(result)
print(result)