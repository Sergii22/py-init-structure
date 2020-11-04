from py_init_structure.common_components.base_files_dir import BasePythonFileDir as Base
from py_init_structure.common_components.pytest import PytestFiles as PF
from py_init_structure.common_components.descriptions import Descriptions as DC


class EnvDeployCIFiles:

    @property
    def dir_name(self):
        return self.root_dir_name

    def __init__(self, root_dir_name=None):
        self.root_dir_name = root_dir_name

    @property
    def tree(self):
        return self.tree_dict()

    def tree_dict(self):
        return {
            "name": self.root_dir_name,
            "type": "directory",
            "children": [
                {
                    "name": Base.REQUIREMENTS_FILE.value,
                    "type": "file",
                    "content": DC.REQUIREMENTS_FILE.value
                },
                {
                    "name":  Base.DOCKER_COMPOSE_FILE.value,
                    "type": "file",
                    "content": DC.DOCKER_COMPOSE_FILE.value
                },
                {
                    "name": Base.DOCKER_FILE.value,
                    "type": "file",
                    "content": DC.DOCKER_FILE.value
                },
                {
                    "name": PF.CONFTEST.value,
                    "type": "file",
                    "content": DC.CONFTEST_FILE.value
                },
                {
                    "name": PF.PYTEST_INI_FILE.value,
                    "type": "file",
                    "content": DC.PYTEST_INI_FILE.value
                },

            ]
        }
