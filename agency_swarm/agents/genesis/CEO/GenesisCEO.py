from agency_swarm import Agent
from agency_swarm.tools.genesis import CreateManifesto, CreateAgencyFolder


class GenesisCEO(Agent):

    def __init__(self, **kwargs):
        # Initialize tools in kwargs if not present
        if 'tools' not in kwargs:
            kwargs['tools'] = []
        # Add required tools
        kwargs['tools'].extend([CreateManifesto, CreateAgencyFolder])

        # Set instructions
        kwargs['instructions'] = "./instructions.md"

        # Initialize the parent class
        super().__init__(**kwargs)

