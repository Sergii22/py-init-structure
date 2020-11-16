from py_init_structure.common_components.trees.test_project_sample import\
    TestProjectSampleTree
from py_init_structure.common_components.trees.test_project_tree import\
    TestProjectTree
from py_init_structure.common_components.project_trees import\
    ProjectTree

from py_init_structure.common_components.trees.env_and_deploy_files import \
    EnvDeployCIFiles


class ProjectCollection:

    def __init__(self, directory, project_type):
        self.project_type = project_type
        self.directory = directory

    def get_project_structure(self):
        """
        This method to store objects of projects trees
        :return: object of tree for particular project
        """
        projects = {"general-purpose-tests-project":
                    TestProjectSampleTree(self.directory),
                    "pytest-tests-project":
                        TestProjectTree(self.directory),
                    "env_and_deploy_files": EnvDeployCIFiles(self.directory)}
        return projects.get(self.project_type)

    def build_project(self):
        project = self.get_project_structure()
        return ProjectTree(project).create_project_tree(project.tree,
                                                        project.root_dir_name)
